#!/usr/bin/env python3
"""目录一致性：catalog.json ↔ scores/ 磁盘文件，双向零容差。

  F1 count 字段 == 实际条目数
  F2 每条 path 指向的文件存在（path 相对 scores/；**扩展名容差**——catalog 的 path
     历史上记 .musicxml，而磁盘实际为 .mxl，同 Stem 的 .mxl/.musicxml/.xml 均算命中）
  F3 磁盘上的谱件全部被 catalog 引用（无孤儿文件；catalog.json/CATALOG.md/LICENSE
     与已跟踪的工作文件 .manifest.json / .rights-before.json 除外）

用法： python3 scripts/check-catalog-files.py     # 退出码 0 = 全过
"""
import json
import pathlib
import sys
from typing import Optional

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "scores" / "catalog.json"
SCORES = ROOT / "scores"
EXCLUDE_NAMES = {"catalog.json", "CATALOG.md", "LICENSE", "catalog.csv",
                 ".manifest.json", ".rights-before.json"}
EXT_SWAPS = (".musicxml", ".mxl", ".xml")


def resolve(rel: str) -> Optional[pathlib.Path]:
    """按 path 原样找；找不到则换扩展名再找（返回 None 表示都没有）。

    ⚠️ 换扩展名必须用**字符串拼接**（`with_name(stem.name + ext)`）：文件名里大量存在
    `Op. 44` / `Hob. III` 这类内部点，`with_suffix(ext)` 会按「最后一个点」替换，
    把名字截成「…Op.mxl」（2026-10-17 实测踩中，72/205 条被误判缺失）。
    """
    direct = SCORES / rel
    if direct.is_file():
        return direct
    stem = direct.with_suffix("")
    for ext in EXT_SWAPS:
        cand = stem.with_name(stem.name + ext)
        if cand.is_file():
            return cand
    return None


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    pieces = data["pieces"]
    fail: list[str] = []

    if data.get("count") != len(pieces):
        fail.append(f"[F1] count={data.get('count')} != 实际 {len(pieces)}")

    referenced: set[pathlib.Path] = set()
    ext_stat: dict[str, int] = {}
    for p in pieces:
        rel = p.get("path")
        if not rel:
            fail.append(f"[F2] {p.get('title', '<无题>')}: 缺 path 字段")
            continue
        hit = resolve(rel)
        if hit is None:
            fail.append(f"[F2] {p.get('title', '<无题>')}: 文件不存在 → scores/{rel}"
                        f"（同 Stem 的 .mxl/.musicxml/.xml 也没有）")
            continue
        referenced.add(hit)
        ext_stat[hit.suffix] = ext_stat.get(hit.suffix, 0) + 1

    on_disk = {
        f for f in SCORES.rglob("*")
        if f.is_file() and f.name not in EXCLUDE_NAMES
        and f.suffix.lower() in {".xml", ".musicxml", ".mxl"}
    }
    orphans = sorted(on_disk - referenced)
    if orphans:
        fail.append(f"[F3] {len(orphans)} 个孤儿文件（磁盘有、catalog 无），"
                    f"例：{[str(o.relative_to(ROOT)) for o in orphans[:3]]}")

    if fail:
        print(f"❌ 目录一致性未通过（{len(fail)} 项）：")
        for f in fail:
            print("   ·", f)
        return 1
    detail = " ".join(f"{k}×{v}" for k, v in sorted(ext_stat.items()))
    print(f"✅ 目录一致性通过（{len(pieces)} 条 ↔ {len(on_disk)} 个文件，双向无差；{detail}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
