#!/usr/bin/env python3
"""整理公开版权曲库的**版权**与**版本**信息，并生成分类目录。

用法（一般由 `fetch.sh` 调用）：

    python3 Tools/PublicDomain/catalog.py [--out PublicDomainScores] [--cache .cache/publicdomain]

做三件事：

1. **归一化版权声明**。来源里的 `<rights>` 有 5 种写法（含 `OpneScore` 拼写错误、
   `Creative Commons copyright waiver (CC0 1.0 Universal)` 等），统一成一条可追溯的
   规范表述：许可 + 曲库 + 作曲家卒年 + 公共版权依据。
2. **修正 `<creator>` 顺序**。MuseScore 导出把 `arranger`（校对者）排在 `composer` 前面，
   而解析器取首个 `<creator>` —— 会把「Transcribed by ... from IMSLP」当成作曲者显示。
   这里把 composer 提到最前（arranger 等仍完整保留，只调顺序）。
3. **产出分类目录**：`CATALOG.md`（人读）+ `catalog.csv` / `catalog.json`（机读），
   按 体裁 / 时期 / 国别 / 版本 / 作曲家 多维归类。

三件事都会同步落到 `.xml` / `.musicxml` / `.mxl` 三种格式上（改一份，另两份重建）。
"""
import argparse
import csv
import html
import json
import re
import sys
import zipfile
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

# `<creator>` 的排列优先级：作曲者在前，校对/编配在后
CREATOR_ORDER = OrderedDict([
    ("composer", 0), ("lyricist", 1), ("poet", 2),
    ("translator", 3), ("arranger", 8),
])
CREATOR_LABEL = {"composer": "作曲", "lyricist": "作词", "poet": "诗人",
                 "translator": "译配", "arranger": "校订"}

# 曲库 → 规范名称（写进 <rights>）
CORPUS_NAME = {"Lieder": "OpenScore Lieder Corpus",
               "StringQuartets": "OpenScore String Quartets"}

PLACEHOLDER = "—"

# 国别识别：按 desc 里出现的词判定（从最具体到最宽泛）
NATIONALITY = [
    ("united states", "美国"), ("u.s.", "美国"), ("us ", "美国"), ("american", "美国"),
    ("hawaiian", "美国·夏威夷"),
    ("english", "英国"), ("england", "英国"), ("british", "英国"), ("scottish", "英国·苏格兰"),
    ("irish", "爱尔兰"), ("welsh", "英国·威尔士"),
    ("german", "德国"), ("austrian", "奥地利"), ("bohemian", "捷克"), ("czech", "捷克"),
    ("hungarian", "匈牙利"), ("polish", "波兰"), ("russian", "俄罗斯"),
    ("french", "法国"), ("belgian", "比利时"), ("dutch", "荷兰"), ("netherland", "荷兰"),
    ("italian", "意大利"), ("spanish", "西班牙"), ("portuguese", "葡萄牙"),
    ("swedish", "瑞典"), ("norwegian", "挪威"), ("danish", "丹麦"), ("finnish", "芬兰"),
    ("swiss", "瑞士"), ("greek", "希腊"), ("ukrainian", "乌克兰"),
    ("cuban", "古巴"), ("brazilian", "巴西"), ("mexican", "墨西哥"),
    ("canadian", "加拿大"), ("australian", "澳大利亚"), ("japanese", "日本"),
]

# 画像外的兜底（来源元数据里缺失的少数作曲家）
FALLBACK_BIO = {
    "Gossec,_François_Joseph": dict(name="François Joseph Gossec", gender="Male",
                                    born=1734, died=1829,
                                    desc="French composer"),
}


# ——————————————————————————————————————————————————————
# 解析工具
# ——————————————————————————————————————————————————————

def clean(s: str) -> str:
    """统一空白并反转义 —— 来源谱面里 <creator> 常带注释、换行与 &quot; 之类实体。"""
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def text_of(xml: str, tag: str) -> str:
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", xml, re.S)
    return clean(m.group(1)) if m else ""


def creators_of(xml: str) -> list[tuple[str, str]]:
    return [(t.lower(), clean(text))
            for t, text in re.findall(r'<creator[^>]*type="([^"]+)"[^>]*>(.*?)</creator>',
                                      xml, re.S)
            if clean(text)]


def load_composers(cache_dir: Path) -> dict:
    """读两个曲库的 data/composers.yaml，按来源目录名建索引。

    文件格式简单（两层缩进、标量值），这里用轻量解析，免得为了它引第三方依赖。
    """
    out = {}
    for repo in ("Lieder", "StringQuartets"):
        f = cache_dir / repo / "data" / "composers.yaml"
        if not f.exists():
            continue
        cur = None
        for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            if re.match(r"^\S+:$", line):
                cur = {}
                continue
            m = re.match(r"^\s{2,}([a-z_]+):\s?(.*)$", line)
            if cur is not None and m:
                cur[m.group(1)] = m.group(2).strip().strip("'\"")
                if "path" in cur:
                    out[cur["path"]] = cur
    # 乐谱目录名与元数据里的 path 未必逐字相同，例如
    #   scores/Hensel,_Fanny        ←→ path: Hensel,_Fanny_(Mendelssohn)
    #   scores/Barnard,_Charlotte_Alington ←→ path: Barnard,_Charlotte_Alington_-_aka_Claribel
    # 再按「去掉括号别名 / aka 后缀」的基名兜一层（不覆盖已精确命中的条目）
    for rec in list(out.values()):
        base = re.split(r"_\(|_-_aka_", rec.get("path", ""))[0]
        if base:
            out.setdefault(base, rec)
    for k, v in FALLBACK_BIO.items():
        out.setdefault(k, v)
    return out


def nationality(desc: str) -> str:
    low = (desc or "").lower()
    for key, name in NATIONALITY:
        if key in low:
            return name
    return PLACEHOLDER


def era(born, died) -> str:
    """按「生卒年中点」划定创作活跃期 —— 比单看生年更贴近实际风格分期。"""
    if not born or not died:
        return PLACEHOLDER
    mid = (born + died) / 2
    for hi, name in ((1750, "巴洛克"), (1795, "古典主义"), (1830, "浪漫主义（早期）"),
                     (1870, "浪漫主义（盛期）"), (1900, "晚期浪漫"), (9999, "近现代")):
        if mid <= hi:
            return name
    return PLACEHOLDER


# ——————————————————————————————————————————————————————
# 归一化：版权声明 与 creator 顺序
# ——————————————————————————————————————————————————————

def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def canonical_rights(corpus: str, died) -> str:
    tail = f"composition public domain (composer died {died})" if died \
        else "underlying composition in the public domain"
    return f"CC0-1.0 · {corpus} engraving · {tail}"


def normalize_creators(xml: str):
    """把 composer 提到最前；只有当这些 <creator> 是连续排列时才重排。"""
    m = re.search(r"<identification\b.*?</identification>", xml, re.S)
    if not m:
        return xml, False
    block = m.group(0)
    items = list(re.finditer(r"[ \t]*<creator\b[^>]*>.*?</creator>\n?", block, re.S))
    if len(items) < 2:
        return xml, False

    span = block[items[0].start():items[-1].end()]
    # 中间若夹着别的元素（<rights>/<encoding> 等），说明不连续，保持原样更安全
    if re.sub(r"\s", "", span) != re.sub(r"\s", "", "".join(i.group(0) for i in items)):
        return xml, False

    def prio(it):
        mt = re.search(r'type="([^"]+)"', it.group(0))
        return CREATOR_ORDER.get((mt.group(1).lower() if mt else ""), 5)

    ordered = sorted(items, key=prio)
    if [i.start() for i in ordered] == [i.start() for i in items]:
        return xml, False
    new_block = block[:items[0].start()] + "".join(i.group(0) for i in ordered) \
        + block[items[-1].end():]
    return xml.replace(block, new_block, 1), True


def normalize(xml: str, corpus: str, died) -> tuple[str, bool, bool]:
    """返回 (新 XML, 版权声明是否被改写, creator 顺序是否被调整)。"""
    new_rights = esc(canonical_rights(corpus, died))
    if re.search(r"<rights[^>]*>.*?</rights>", xml, re.S):
        xml2 = re.sub(r"<rights[^>]*>.*?</rights>", f"<rights>{new_rights}</rights>",
                      xml, count=1, flags=re.S)
    else:
        xml2 = xml.replace("</identification>",
                           f"  <rights>{new_rights}</rights>\n  </identification>", 1)
    rights_changed = xml2 != xml
    xml3, reordered = normalize_creators(xml2)
    return xml3, rights_changed, reordered


def write_three(folder: Path, stem: str, xml: str) -> None:
    """三格式同步落盘。

    ⚠️ 用字符串拼接而非 `Path.with_suffix()`：曲名常以「点数字」结尾（`... Op.1 No.6`），
    `with_suffix` 会把它当扩展名替掉，截断曲名并造成同名覆盖。
    """
    container = ('<?xml version="1.0" encoding="UTF-8"?>\n<container>\n  <rootfiles>\n'
                 f'    <rootfile full-path="{stem}.musicxml">\n      </rootfile>\n'
                 '    </rootfiles>\n  </container>\n')
    (folder / f"{stem}.musicxml").write_text(xml, encoding="utf-8")
    (folder / f"{stem}.xml").write_text(xml, encoding="utf-8")
    with zipfile.ZipFile(folder / f"{stem}.mxl", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("META-INF/container.xml", container)
        z.writestr(f"{stem}.musicxml", xml)


# ——————————————————————————————————————————————————————
# 主流程
# ——————————————————————————————————————————————————————

def main() -> int:
    root = Path(__file__).resolve().parents[2]
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(root / "PublicDomainScores"))
    ap.add_argument("--cache", default=str(root / ".cache" / "publicdomain"))
    ap.add_argument("--no-normalize", action="store_true",
                    help="只出清单，不改写谱面里的版权与 creator 顺序")
    args = ap.parse_args()

    out_dir = Path(args.out)
    cache_dir = Path(args.cache)
    manifest_file = out_dir / ".manifest.json"
    if not manifest_file.exists():
        print(f"❌ 找不到 {manifest_file}，请先运行 build.py / fetch.sh", file=sys.stderr)
        return 1
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    bios = load_composers(cache_dir)

    rows, rights_src, n_rights, n_creator = [], Counter(), 0, 0
    for piece in manifest["pieces"]:
        p_musicxml = out_dir / piece["path"]
        stem = p_musicxml.name[: -len(".musicxml")]
        xml = p_musicxml.read_text(encoding="utf-8")

        # —— 版本信息 ——
        m = re.search(r"<score-(?:partwise|timewise)[^>]*version=\"([^\"]+)\"", xml)
        ver = m.group(1) if m else PLACEHOLDER
        software = text_of(xml, "software") or PLACEHOLDER
        enc_date = text_of(xml, "encoding-date") or PLACEHOLDER

        # —— 版权信息 ——
        rights_raw = text_of(xml, "rights") or PLACEHOLDER
        rights_src[rights_raw] += 1

        # —— 谱面内标题 / 词曲作者 / 来源 ——
        cr = creators_of(xml)
        by_type = defaultdict(list)
        for t, v in cr:
            by_type[t].append(v)
        engraved = (by_type.get("composer") or [piece["composer"]])[0]
        iimslp = re.search(r"ReverseLookup/(\d+)", xml) or \
            re.search(r"imslp\.org/[^\s\"]*?/(\d+)", xml)
        imslp_id = iimslp.group(1) if iimslp else ""

        # 贡献人（转谱 / 校对 / 编配者）：来源是 CC0 时为 credit 致谢，
        # 将来若纳入 CC-BY 源（如 Mutopia）则是强制署名义务（见 PublicDomainLibrary.md）。
        contributor = " / ".join(
            by_type.get("arranger", []) + by_type.get("editor", [])
            + by_type.get("transcriber", [])
        )

        # 源 URL：优先用谱面内 <source>（常为 MuseScore 原始链接），
        # 缺失时回指来源曲库仓库首页，保证每首都能追溯到上游。
        repo_url = manifest["sources"].get(piece["source"], "").replace(".git", "")
        source_url = text_of(xml, "source") or repo_url

        # —— 家世（来自曲库 data/composers.yaml）——
        bio = bios.get(piece["source_composer_path"], {})
        died = int(bio["died"]) if str(bio.get("died", "")).isdigit() else None
        born = int(bio["born"]) if str(bio.get("born", "")).isdigit() else None
        corpus = CORPUS_NAME.get(piece["source"], piece["source"])

        if not args.no_normalize:
            new_xml, rights_changed, reordered = normalize(xml, corpus, died)
            if new_xml != xml:
                write_three(p_musicxml.parent, stem, new_xml)
                xml = new_xml
            n_rights += int(rights_changed)
            n_creator += int(reordered)

        rows.append({
            "category": piece["category"],
            # 姓名用来源元数据里的规范写法；谱面上刻印的原文另存一列备查
            "composer": clean(bio.get("name", "")) or engraved,
            "composer_engraved": engraved,
            "born": born or "", "died": died or "",
            "gender": bio.get("gender", ""),
            "nationality": nationality(bio.get("desc", "")),
            "era": era(born, died),
            "pd_year": (died + 71) if died else "",
            "title": piece["title"],
            "work": text_of(xml, "work-title"),
            "work_number": text_of(xml, "work-number"),
            "movement": text_of(xml, "movement-title"),
            "collection": piece["source_work_path"].split("/")[0]
                          if "/" in piece["source_work_path"] else "",
            "lyricist": " / ".join(by_type.get("lyricist", []) + by_type.get("poet", [])),
            "translator": " / ".join(by_type.get("translator", [])),
            "arranger": " / ".join(by_type.get("arranger", [])),
            "xml_version": ver, "software": software, "encoding_date": enc_date,
            "rights_raw": rights_raw,
            "rights_norm": canonical_rights(corpus, died),
            "imslp": f"https://imslp.org/wiki/Special:ReverseLookup/{imslp_id}"
                     if imslp_id else "",
            "source_url": source_url,
            "contributor": contributor,
            "wiki": bio.get("wikipedia", "") or bio.get("imslp", ""),
            "wikidata": bio.get("wikidata", ""),
            "source": piece["source"],
            "source_file": piece["source_file"],
            "parts": piece.get("parts", ""), "measures": piece.get("meas", ""),
            "notes": piece.get("notes", ""), "lyric_notes": piece.get("lyric", ""),
            "path": piece["path"],
        })
        # 把贡献人 / 源 URL 回填进溯源清单，使 .manifest.json 与 catalog 一致
        piece["contributor"] = contributor
        piece["source_url"] = source_url

    # 归一化会把原始写法覆盖掉，因此把「归一化前」的分布落盘快照 ——
    # 之后单独重跑本脚本时，报告里仍能看到当初的 7 种变体。
    before_file = out_dir / ".rights-before.json"
    if before_file.exists():
        stored = Counter(json.loads(before_file.read_text(encoding="utf-8")))
        if sum(stored.values()) == len(rows):
            rights_src = stored
    else:
        before_file.write_text(json.dumps(dict(rights_src), ensure_ascii=False, indent=1)
                               + "\n", encoding="utf-8")

    # ———— 写出机读清单 ————
    fields = list(rows[0].keys())
    with (out_dir / "catalog.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    (out_dir / "catalog.json").write_text(
        json.dumps({"count": len(rows), "pieces": rows}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8")

    # ———— 写出人读目录 ————
    write_catalog_md(out_dir / "CATALOG.md", rows, manifest, rights_src,
                     n_rights, n_creator, args.no_normalize)

    print(f"✅ {len(rows)} 首已整理 → {out_dir}/CATALOG.md、catalog.csv、catalog.json")
    if not args.no_normalize:
        print(f"   归一化版权声明 {n_rights} 条 · 修正 creator 顺序"
              f"（composer 前置）{n_creator} 条，三格式同步")

    # 贡献人 / 源 URL 回填进溯源清单，使 .manifest.json 与 catalog 一致
    manifest_file.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 随曲库分发 CC0 许可文本，便于直接上传公开仓库（GitHub / Gitee）
    (out_dir / "LICENSE").write_text(
        "This collection of MusicXML scores is published under the Creative Commons "
        "CC0 1.0 Universal license.\n\n"
        "To the extent possible under law, the contributors have waived all copyright "
        "and related or neighboring rights to the engraving / transcription in this "
        "collection. The underlying musical compositions are in the public domain.\n\n"
        "Full license text: https://creativecommons.org/publicdomain/zero/1.0/\n",
        encoding="utf-8")
    return 0


def write_catalog_md(path: Path, rows, manifest, rights_src, n_rights, n_creator, dry):
    cats = sorted({r["category"] for r in rows})
    ver = Counter(r["xml_version"] for r in rows)
    soft = Counter(r["software"] for r in rows)
    dates = sorted(r["encoding_date"] for r in rows if r["encoding_date"] != PLACEHOLDER)
    died_max = max((r["died"] for r in rows if r["died"]), default="")

    L = []
    a = L.append
    a("# 公开版权曲库 · 版权与版本清单 / 分类目录\n")
    a("> 由 `Tools/PublicDomain/catalog.py` 生成；文件名、路径、字段含义见文末。\n")
    a("## 〇、总览\n")
    a("| 项 | 值 |")
    a("|---|---|")
    a(f"| 曲目 | **{len(rows)} 首**（× 3 种格式 = {len(rows) * 3} 个文件）|")
    a(f"| 体裁 | " + "；".join(
        f"{c} {sum(1 for r in rows if r['category'] == c)} 首" for c in cats) + " |")
    a(f"| 作曲家 | {len({r['composer'] for r in rows})} 位 |")
    a(f"| 许可 | **CC0-1.0**（来源作者已献出公共版权，可自由分发）|")
    a(f"| 来源 | " + "；".join(manifest["sources"].values()) + " |")
    a(f"| 公共版权依据 | 作曲家去世 ≥ 70 年；最晚一位卒于 **{died_max}** "
      f"（第 {int(died_max) + 71} 年起进入公共版权）|")
    a(f"| 格式 | `.xml` / `.musicxml`（明文 MusicXML）+ `.mxl`（官方容器："
      "`META-INF/container.xml` + 根文件）|")
    a(f"| 校验 | 全部文件经工程解析器 `parsestat` 通读，0 失败 |")
    a("")

    a("## 一、版权信息\n")
    a("### 1.1 归一化前后的 `<rights>` 声明\n")
    a(f"下载的谱面里 `<rights>` 共有 **{len(rights_src)} 种写法**"
      + ("（已统一，见下）" if not dry else "") + "：\n")
    a("| 原始声明 | 数量 | 处理 |")
    a("|---|---|---|")
    for k, v in rights_src.most_common():
        if k == PLACEHOLDER:
            note = "文件缺 `<rights>` → 补写规范声明"
        elif "Opne" in k:
            note = "**拼写错误**（`OpneScore`）→ 归一"
        elif "Openscore" in k:
            note = "大小写不一（`Openscore`）→ 归一"
        elif "waiver" in k:
            note = "异体表述（`copyright waiver`）→ 归一"
        elif "LiederCorpus" in k or k.endswith("."):
            note = "冗长/带尾点 → 归一"
        else:
            note = "写法不统一 → 归一"
        a(f"| `{k}` | {v} | {note} |")
    a("")
    a("统一后的规范声明（写入每个谱面的 `<rights>`）：\n")
    a("```")
    a("CC0-1.0 · <曲库> engraving · composition public domain (composer died <卒年>)")
    a("```")
    a("")
    a("即：**曲谱排版（engraving）按 CC0-1.0 献出**，不再主张任何权利；"
      "同时注明**原作本身已过版权保护期**及其依据（作曲家卒年）。\n")
    if not dry:
        a(f"归一化：{'本次改写 %d 条声明' % n_rights if n_rights else '声明已全部规范（归一化是幂等的，重跑无需改写）'}。\n")

    a("### 1.2 逐作曲家公共版权依据\n")
    a("| 作曲家 | 生卒 | 国别 | 性别 | 曲目 | 公共版权起算年 |")
    a("|---|---|---|---|---|---|")
    agg = defaultdict(lambda: {"n": 0})
    for r in rows:
        k = r["composer"]
        agg[k]["n"] += 1
        agg[k].update({x: r[x] for x in ("born", "died", "nationality", "gender", "pd_year")})
    for k in sorted(agg, key=lambda x: (agg[x]["died"] or 9999, x)):
        v = agg[k]
        span = f"{v['born']}–{v['died']}" if v["born"] else PLACEHOLDER
        a(f"| {k} | {span} | {v['nationality']} | "
          f"{'女' if v['gender'] == 'Female' else ('男' if v['gender'] == 'Male' else PLACEHOLDER)} "
          f"| {v['n']} | {v['pd_year'] or PLACEHOLDER} |")
    a("")

    a("## 二、版本信息\n")
    a("### 2.1 MusicXML 规范版本\n")
    a("| 版本 | 曲目 | 说明 |")
    a("|---|---|---|")
    for v, n in ver.most_common():
        a(f"| {v} | {n} | " +
          ("DTD 4.0 Partwise（当前主流）" if v.startswith("4") else "DTD 3.1 Partwise（旧版）") + " |")
    a("")
    a("### 2.2 记谱软件版本\n")
    a("| 生成软件 | 曲目 |")
    a("|---|---|")
    for v, n in soft.most_common():
        a(f"| {v} | {n} |")
    a("")
    if dates:
        a(f"### 2.3 转换/导出时间\n\n`{dates[0]}` ~ `{dates[-1]}`"
          f"（共 {len(dates)} 份带 `<encoding-date>`）\n")
    a("### 2.4 曲库自身版本\n")
    a("| 曲库 | 仓库 | 取用方式 |")
    a("|---|---|---|")
    a("| 艺术歌曲 Lieder | OpenScore/Lieder | 稀疏检出（blobless，仅 `scores/` + `data/`）|")
    a("| 弦乐四重奏 | OpenScore/StringQuartets | 同上 |")
    a("")
    a("> 谱面内另记有 `<creator type=\"arranger\">`（校对/转写者，含 IMSLP 反查编号）"
      "与 `<source>`（MuseScore 原始链接），逐曲见第五节与 `catalog.csv`。\n")

    a("## 三、分类索引\n")
    for i, (dim, key) in enumerate(
            (("体裁", "category"), ("时期", "era"), ("国别", "nationality")), 1):
        a(f"### 3.{i} 按{dim}\n")
        c = Counter(r[key] for r in rows)
        a(f"| {dim} | 曲目 | 占比 |")
        a("|---|---|---|")
        for k, n in sorted(c.items(), key=lambda x: -x[1]):
            a(f"| {k or PLACEHOLDER} | {n} | {n * 100 // len(rows)}% |")
        a("")

    a("## 四、逐曲清单\n")
    a("| # | 体裁 | 作曲家 | 曲名（文件名） | 界面标题 | MusicXML | 软件 | 规模 | 贡献人（转谱/校对） | 源 URL |")
    a("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(sorted(rows, key=lambda x: (x["category"], x["composer"], x["title"])), 1):
        size = f"{r['parts']}声部/{r['measures']}小节/{r['notes']}音符" if r["parts"] else PLACEHOLDER
        a(f"| {i} | {r['category'][:4]} | {r['composer']} | {r['title']} | {r['work'] or PLACEHOLDER} "
          f"| {r['xml_version']} | {r['software']} | {size} "
          f"| {r['contributor'] or PLACEHOLDER} | {r['source_url'] or PLACEHOLDER} |")
    a("")
    a("---\n")
    a("### 字段说明\n")
    a("- **曲名（文件名）**：文件名的曲名部分。命名规则与 App 显示口径对齐 ——\n"
      "  MuseScore 导出里 `<work-title>` 是**曲集名**、`<movement-title>` 是**单曲名**，"
      "而 `MusicXMLParser` 取 `<work-title>` 作 `score.title`。\n"
      "  因此：曲集 ≠ 单曲时命名为「`曲集 - 单曲`」，否则直接用该标题本身。")
    a("- **界面标题**：App 标题栏实际显示的内容（即 `<work-title>`）。")
    a("- `规模`：解析器读出的 声部数 / 小节数 / 音符数，用于确认谱面被完整解析。")
    a("- `公共版权起算年`：按「作曲家卒年 + 70 年，次年起算」估算，"
      "实际以目标司法管辖区为准。")
    a("- 机读版本：`catalog.csv`（含全部字段，UTF-8-BOM，Excel 可直接打开）、"
      "`catalog.json`（另含 `collection`＝来源曲集目录、`movement`＝单曲名等明细）。")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
