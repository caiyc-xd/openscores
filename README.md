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
licenses/         开放依赖的许可全文（alphaTab MPL-2.0、Bravura SIL OFL 1.1、FluidR3 GM MIT）
```

## 许可

| 组件 | 许可 |
|---|---|
| 本仓库代码（HTML / JS / CSS） | MIT（见 [`LICENSE`](LICENSE)） |
| 乐谱排版与转谱（`scores/`） | CC0-1.0（见 [`scores/LICENSE`](scores/LICENSE)） |
| alphaTab 渲染引擎（`player/alphaTab.min.js`，官方发布构建，**未修改**） | **MPL-2.0**（见 [`licenses/alphaTab-MPL-2.0.txt`](licenses/alphaTab-MPL-2.0.txt)） |
| Bravura 制谱字体 | SIL Open Font License 1.1 |
| FluidR3 GM 音色（`player/FluidR3_GM.sf3`） | MIT |
| sonivox 音色（`player/sonivox.sf2`，仅作音色加载失败时的回退） | 来源与许可**待确认**，见下方「已知待办」 |

许可全文见 [`licenses/`](licenses/)（含各组件来源地址）。

### 为什么 alphaTab 是 MPL-2.0（更正）

早前本页与首页把 alphaTab 写成 MIT，**不准确**：alphaTab 采用
[Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/)（file-level copyleft，
另有商业授权选项）。本仓库分发的是**未修改的官方发布构建**，按 MPL-2.0 §3.2 的要求：
许可声明与全文随仓库分发（`licenses/alphaTab-MPL-2.0.txt`），源码形式可从上游取得 ——
<https://github.com/CoderLine/alphaTab>（版本见 `player/` 内构建文件）。

## 已知待办（许可）

- `player/sonivox.sf2`：来源与许可未能确认（Android Sonivox 派生音色库在网上广泛流传，但缺少明确的许可声明）。
  处置选项：① 补上确切来源与许可文件；② 直接移除，仅保留 MIT 的 FluidR3 GM 与在线回退提示。
- alphaTab 的 `LICENSE.header` 还列出了其内置子模块的许可，如需在分发物中附带，请一并从上游取得。

## 贡献

- **加曲谱**：请确保为公共领域 / CC0（作曲家去世 ≥ 70 年，或权利人已献出）。提交 `scores/` 下的 `.mxl`，并在 `catalog.json` / `CATALOG.md` 补充条目与溯源。
- **改进播放器**：fork 后提交 Pull Request。
