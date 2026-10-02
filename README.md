# 公开领域乐谱 · Open Scores

公开版权（CC0 / 公共领域）乐谱的网页渲染与试听。基于 [alphaTab](https://www.alphatab.net/) 开源引擎，可在线看谱、听谱，无需账号、无需联网。

本仓库为开放项目，**欢迎通过 Issues / Pull Requests 完善曲库与播放器**。

## 内容

- 205 首公开版权乐谱（艺术歌曲、弦乐四重奏），均为作曲家去世 ≥ 70 年的作品。
- 乐谱排版（engraving / 转谱）按 **CC0-1.0** 献出；原作本身已过版权保护期。
- 逐曲溯源见 [`scores/CATALOG.md`](scores/CATALOG.md)，完整清单见 [`scores/catalog.json`](scores/catalog.json)。

## 本地运行

浏览器出于安全限制，不能直接 `file://` 双击打开（会禁止读取本地谱文件）。请用本地 http 服务器：

```bash
python3 -m http.server 8080
# 然后浏览器打开：
#   http://localhost:8080/player.html?score=scores/艺术歌曲/Jane%20Bingham%20Abbott/Jane%20Bingham%20Abbott%20-%20Just%20for%20Today.mxl
#   http://localhost:8080/library.html
```

## 目录结构

```
index.html        开放项目首页
player.html       曲谱渲染 + 试听播放器（布局切换 / 分页翻页 / 播放光标 / 总谱·分谱 / 分谱独奏）
library.html      曲库检索与下载
style.css         样式
player/           alphaTab 引擎 + Bravura 制谱字体 + FluidR3 / sonivox 合成音色
scores/           公开领域乐谱（CC0）与清单
licenses/         开放依赖的许可全文（alphaTab MIT、Bravura SIL OFL 1.1、FluidR3 GM MIT）
```

## 许可

| 组件 | 许可 |
|---|---|
| 本仓库代码（HTML / JS / CSS） | MIT（见 [`LICENSE`](LICENSE)） |
| 乐谱排版与转谱（`scores/`） | CC0-1.0（见 [`scores/LICENSE`](scores/LICENSE)） |
| alphaTab 渲染引擎 | MIT |
| Bravura 制谱字体 | SIL Open Font License 1.1 |
| FluidR3 GM / sonivox 音色 | MIT |

许可全文见 [`licenses/`](licenses/)。

## 贡献

- **加曲谱**：请确保为公共领域 / CC0（作曲家去世 ≥ 70 年，或权利人已献出）。提交 `scores/` 下的 `.mxl`，并在 `catalog.json` / `CATALOG.md` 补充条目与溯源。
- **改进播放器**：fork 后提交 Pull Request。
