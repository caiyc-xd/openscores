#!/usr/bin/env python3
"""权利审计：逐曲校验「公有领域判定 + 溯源」两条硬规则。

规则（2026-10-17 与用户确认后固化）：
  R1 pd_year == 作曲家卒年 + 71 —— 本库口径比通行「卒年 + 70」多留一年余量，
     以覆盖各法域（EU 70 年 / 中 50 年 / 美 95 年）的差异；全部条目均按此生成。
  R2 每条必须有溯源：arranger（转谱者）或 imslp 编号或 source_url 至少一项非空。
  R3 pd_year 不得晚于当前年份（不存在"未来才公有"的曲目）。
  R4 born / died 必须为整数且 died > born。

用法： python3 scripts/check-rights.py        # 退出码 0 = 全过
"""
import json
import pathlib
import sys
from datetime import date

PD_OFFSET = 71
ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "scores" / "catalog.json"


def main() -> int:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    pieces = data["pieces"]
    fail: list[str] = []

    if data.get("count") != len(pieces):
        fail.append(f"count 字段 {data.get('count')} != 实际 {len(pieces)}")

    for p in pieces:
        title = p.get("title", "<无题>")
        born, died, pd = p.get("born"), p.get("died"), p.get("pd_year")

        if not isinstance(born, int) or not isinstance(died, int):
            fail.append(f"[R4] {title}: born/died 非整数（{born!r}/{died!r}）")
            continue
        if died <= born:
            fail.append(f"[R4] {title}: died({died}) <= born({born})")
        if not isinstance(pd, int):
            fail.append(f"[R3] {title}: pd_year 非整数（{pd!r}）")
            continue
        if pd != died + PD_OFFSET:
            fail.append(f"[R1] {title}: pd_year={pd} != died({died})+{PD_OFFSET}")
        if pd > date.today().year:
            fail.append(f"[R3] {title}: pd_year={pd} 晚于 {date.today().year}")
        if not (p.get("arranger") or p.get("imslp") or p.get("source_url")):
            fail.append(f"[R2] {title}: 无溯源（arranger/imslp/source_url 全空）")

    if fail:
        print(f"❌ 权利审计未通过（{len(fail)} 项）：")
        for f in fail:
            print("   ·", f)
        return 1
    print(f"✅ 权利审计通过（{len(pieces)} 曲：pd_year=卒年+{PD_OFFSET}、溯源齐全、无未来条目）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
