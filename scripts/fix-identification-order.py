#!/usr/bin/env python3
"""修正 .mxl 内 `<identification>` 的子元素顺序，使其符合 MusicXML 4.0 模式。

背景（2026-10-17 XSD 校验发现）：4 份语料的 `<identification>` 把 `<rights>`
追加在 `<encoding>` / `<source>` 之后，而模式要求 creator*, rights*, encoding?,
source?, relation*, miscellaneous* —— 顺序错即整份不合法（xmllint 报
"element rights: This element is not expected. Expected is one of
( relation, miscellaneous )"）。

修法：把 `<rights>…</rights>` 移到该块内第一个 `<encoding>` 之前
（无 encoding 则移到 `</identification>` 之前），其余内容逐字节不动；
. mxl 重新打包（容器内其它条目原样带回）。

用法：
    python3 scripts/fix-identification-order.py <file.mxl> [...]   # 修指定文件
    python3 scripts/fix-identification-order.py --all              # 修 scores/ 下全部
脚本幂等：已合规的文件再次运行不会改动。
"""
import pathlib
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def fix_xml(text: str) -> tuple[str, bool]:
    m = re.search(r"<identification>.*?</identification>", text, re.S)
    if not m:
        return text, False
    block = m.group(0)
    rights = re.search(r"[ \t]*<rights>.*?</rights>[ \t]*\n?", block, re.S)
    if not rights:
        return text, False
    # rights 已在 encoding 之前即合规
    enc = re.search(r"[ \t]*<encoding[ >]", block)
    if enc and rights.start() < enc.start():
        return text, False
    new_block = block[: rights.start()] + block[rights.end():]
    if enc:
        pos = enc.start()
    else:
        close = new_block.rindex("</identification>")
        pos = close
    new_block = new_block[:pos] + rights.group(0).rstrip("\n") + "\n" + new_block[pos:]
    return text[: m.start()] + new_block + text[m.end():], True


def fix_mxl(path: pathlib.Path) -> bool:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            contents = {n: z.read(n) for n in names}
        target = None
        for n in names:
            if n.lower().endswith((".xml", ".musicxml")) and not n.startswith("META-INF"):
                if target is None or len(contents[n]) > len(contents[target]):
                    target = n
        if target is None:
            return False
        text = contents[target].decode("utf-8")
        fixed, changed = fix_xml(text)
        if not changed:
            return False
        contents[target] = fixed.encode("utf-8")
        backup = tmp / path.name
        shutil.copy2(path, backup)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for n in names:
                z.writestr(n, contents[n])
        return True


def main() -> int:
    args = sys.argv[1:]
    if args == ["--all"]:
        files = sorted(p for p in (ROOT / "scores").rglob("*.mxl"))
    else:
        files = [pathlib.Path(a) for a in args]
    fixed = 0
    for f in files:
        f = f.resolve()
        if fix_mxl(f):
            try:
                shown = f.relative_to(ROOT)
            except ValueError:
                shown = f
            print(f"  已修正：{shown}")
            fixed += 1
    print(f"✅ 处理 {len(files)} 个文件，修正 {fixed} 个")
    return 0


if __name__ == "__main__":
    sys.exit(main())
