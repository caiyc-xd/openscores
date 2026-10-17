#!/usr/bin/env python3
"""修掉 MuseScore 4.5.2 导出里的两处 MusicXML 4.0 模式违例（XSD 校验发现）。

背景（2026-10-17）：全量 XSD 校验 205 份中 2 份不合法，均为上游导出缺陷：

  Q1 `<accidental-mark cautionary="...">` —— cautionary 属性在 4.0 模式的
     accidental-mark 上不被允许（MuseScore 4.5.2 仍按旧写法输出）。
     处置：删掉该属性（4.0 无等价表达；影响仅限个别提示性变音的括注显示）。
  Q2 `<instrument-change>` 缺必填 `id` 属性（导出漏写）。
     处置：补一个唯一 id（`ic-<n>`）。

两处都是保守修法：不增删任何音乐内容。脚本幂等。

用法：
    python3 scripts/fix-schema-quirks.py <file.mxl> [...]
    python3 scripts/fix-schema-quirks.py --all
"""
import pathlib
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def fix_xml(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []

    def strip_cautionary(m: re.Match) -> str:
        tag = m.group(0)
        new = re.sub(r'\s+cautionary="[^"]*"', "", tag)
        if new != tag:                       # 只有真删掉了属性才记（否则空转重写 zip）
            notes.append("移除 accidental-mark 的 cautionary 属性")
        return new

    text = re.sub(r"<accidental-mark\b[^>]*>", strip_cautionary, text)

    counter = [0]

    def add_id(m: re.Match) -> str:
        tag = m.group(0)
        if "id=" in tag:
            return tag
        counter[0] += 1
        notes.append("为 instrument-change 补 id")
        return tag[: -1] + f' id="ic-{counter[0]}">'

    # Q3 instrument-change 里嵌套整块 score-instrument（MuseScore 4.5.2 错误导出）：
    #     instrument-change 的内容模型是 virtual-instrument-data，不含 score-instrument；
    #     且其 id 语义是「指向受影响的 score-instrument」（IDREF）。
    #     修法：摘掉嵌套的 score-instrument（score-part 里的定义仍在），
    #     把 instrument-change 的 id 设为被摘元素的 id。
    def fix_instrument_change(m: re.Match) -> str:
        block = m.group(0)
        nested = re.search(r"<score-instrument\s+id=\"([^\"]+)\"[^>]*>.*?</score-instrument>",
                           block, re.S)
        if not nested:
            return block
        sid = nested.group(1)
        notes.append(f"摘除 instrument-change 内嵌套的 score-instrument({sid})，id 改指该 instrument")
        block = block[: nested.start()] + block[nested.end():]
        block = re.sub(r'<instrument-change\b[^>]*>',
                       f'<instrument-change id="{sid}">', block, count=1)
        return block

    text = re.sub(r"<instrument-change\b[^>]*>.*?</instrument-change>",
                  fix_instrument_change, text, flags=re.S)

    text = re.sub(r"<instrument-change\b[^>]*>", add_id, text)
    return text, notes


def fix_mxl(path: pathlib.Path) -> list[str]:
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            contents = {n: z.read(n) for n in names}
        target = None
        for n in names:
            if n.lower().endswith((".xml", ".musicxml")) and not n.startswith("META-INF"):
                if target is None or len(contents[n]) > len(contents[target]):
                    target = n
        if target is None:
            return []
        fixed, notes = fix_xml(contents[target].decode("utf-8"))
        if not notes:
            return []
        contents[target] = fixed.encode("utf-8")
        backup = pathlib.Path(td) / path.name
        shutil.copy2(path, backup)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for n in names:
                z.writestr(n, contents[n])
        return notes


def main() -> int:
    args = sys.argv[1:]
    files = (sorted((ROOT / "scores").rglob("*.mxl")) if args == ["--all"]
             else [pathlib.Path(a).resolve() for a in args])
    total = 0
    for f in files:
        notes = fix_mxl(f)
        if notes:
            try:
                shown = f.relative_to(ROOT)
            except ValueError:
                shown = f
            print(f"  已修正 {shown}：{len(notes)} 处（{notes[0]} 等）")
            total += len(notes)
    print(f"✅ 处理 {len(files)} 个文件，修正 {total} 处")
    return 0


if __name__ == "__main__":
    sys.exit(main())
