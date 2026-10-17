#!/usr/bin/env python3
"""谱件合法性：scores/ 下每个 .musicxml / .xml / .mxl 都通过 MusicXML XSD 校验。

  · .mxl 是 ZIP 容器：取其中最大的非 META-INF XML 作为谱件本体；
  · XSD 用 schema/musicxml/ 下的 W3C MusicXML 模式（musicxml.xsd 引用 xlink/xml，
    三者须同目录；该模式为 W3C Software Copyright 许可，随仓分发并保留声明）。

依赖：xmllint（libxml2-utils；GitHub ubuntu runner 与 macOS 均自带）。

用法： python3 scripts/check-xml.py     # 退出码 0 = 全部合法
"""
import pathlib
import subprocess
import sys
import tempfile
import zipfile
from typing import Optional

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCORES = ROOT / "scores"
XSD = ROOT / "schema" / "musicxml" / "musicxml.xsd"


def extract_xml(path: pathlib.Path, tmp: pathlib.Path) -> Optional[pathlib.Path]:
    if path.suffix != ".mxl":
        return path
    try:
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist()
                     if n.lower().endswith((".xml", ".musicxml")) and not n.startswith("META-INF")]
            if not names:
                return None
            biggest = max(names, key=lambda n: z.getinfo(n).file_size)
            out = tmp / (path.stem + ".xml")
            out.write_bytes(z.read(biggest))
            return out
    except zipfile.BadZipFile:
        return None


def main() -> int:
    if not XSD.is_file():
        print(f"❌ 缺 XSD：{XSD}")
        return 1
    files = sorted(
        f for f in SCORES.rglob("*")
        if f.is_file() and f.suffix.lower() in {".xml", ".musicxml", ".mxl"}
        and f.name not in {"catalog.json", "CATALOG.md"}
    )
    fail: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        for f in files:
            target = extract_xml(f, tmp)
            if target is None:
                fail.append(f"{f.relative_to(ROOT)}: 无法取得谱件 XML（容器损坏或无 XML）")
                continue
            r = subprocess.run(
                ["xmllint", "--schema", str(XSD), "--noout", str(target)],
                capture_output=True, text=True,
            )
            if r.returncode != 0:
                first = next((l for l in r.stderr.splitlines() if "error" in l.lower()), r.stderr[:80])
                fail.append(f"{f.relative_to(ROOT)}: {first.strip()[:120]}")
    if fail:
        print(f"❌ XSD 校验未通过（{len(fail)}/{len(files)}）：")
        for f in fail[:10]:
            print("   ·", f)
        return 1
    print(f"✅ XSD 校验通过（{len(files)} 份谱件，MusicXML 模式）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
