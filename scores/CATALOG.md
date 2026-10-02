# 公开版权曲库 · 版权与版本清单 / 分类目录

> 由 `Tools/PublicDomain/catalog.py` 生成；文件名、路径、字段含义见文末。

## 〇、总览

| 项 | 值 |
|---|---|
| 曲目 | **205 首**（× 3 种格式 = 615 个文件）|
| 体裁 | 弦乐四重奏 String Quartets 5 首；艺术歌曲 Lieder 200 首 |
| 作曲家 | 127 位 |
| 许可 | **CC0-1.0**（来源作者已献出公共版权，可自由分发）|
| 来源 | https://github.com/OpenScore/Lieder.git；https://github.com/OpenScore/StringQuartets.git |
| 公共版权依据 | 作曲家去世 ≥ 70 年；最晚一位卒于 **1954** （第 2025 年起进入公共版权）|
| 格式 | `.xml` / `.musicxml`（明文 MusicXML）+ `.mxl`（官方容器：`META-INF/container.xml` + 根文件）|
| 校验 | 全部文件经工程解析器 `parsestat` 通读，0 失败 |

## 一、版权信息

### 1.1 归一化前后的 `<rights>` 声明

下载的谱面里 `<rights>` 共有 **7 种写法**（已统一，见下）：

| 原始声明 | 数量 | 处理 |
|---|---|---|
| `OpenScore (CC0)` | 194 | 写法不统一 → 归一 |
| `Creative Commons copyright waiver (CC0 1.0 Universal)` | 4 | 异体表述（`copyright waiver`）→ 归一 |
| `OpenScore LiederCorpus (CC0). https://musescore.com/openscore-lieder-corpus/sets` | 2 | 冗长/带尾点 → 归一 |
| `—` | 2 | 文件缺 `<rights>` → 补写规范声明 |
| `OpneScore (CC0)` | 1 | **拼写错误**（`OpneScore`）→ 归一 |
| `OpenScore (CC0).` | 1 | 冗长/带尾点 → 归一 |
| `Openscore (CC0)` | 1 | 大小写不一（`Openscore`）→ 归一 |

统一后的规范声明（写入每个谱面的 `<rights>`）：

```
CC0-1.0 · <曲库> engraving · composition public domain (composer died <卒年>)
```

即：**曲谱排版（engraving）按 CC0-1.0 献出**，不再主张任何权利；同时注明**原作本身已过版权保护期**及其依据（作曲家卒年）。

归一化：本次改写 205 条声明。

### 1.2 逐作曲家公共版权依据

| 作曲家 | 生卒 | 国别 | 性别 | 曲目 | 公共版权起算年 |
|---|---|---|---|---|---|
| Elisabetta de Gambarini | 1730–1765 | 英国 | 女 | 1 | 1836 |
| Thomas Arne | 1710–1778 | 英国 | 男 | 2 | 1849 |
| Corona Schröter | 1751–1802 | 德国 | 女 | 1 | 1873 |
| Joseph Haydn | 1732–1809 | 奥地利 | 男 | 5 | 1880 |
| Sophie Gail | 1775–1819 | 法国 | 女 | 2 | 1890 |
| Harriett Abrams | 1758–1821 | 英国 | 女 | 2 | 1892 |
| Maria Theresia von Paradis | 1759–1824 | 奥地利 | 女 | 1 | 1895 |
| Louise Reichardt | 1779–1826 | 德国 | 女 | 1 | 1897 |
| Ludwig van Beethoven | 1770–1827 | 德国 | 男 | 2 | 1898 |
| Franz Schubert | 1797–1828 | 奥地利 | 男 | 1 | 1899 |
| François Joseph Gossec | 1734–1829 | 法国 | 男 | 1 | 1900 |
| William Shield | 1748–1829 | 英国 | 男 | 1 | 1900 |
| Jane Mary Guest | 1762–1846 | 英国 | 女 | 2 | 1917 |
| Fanny (Mendelssohn) Hensel | 1805–1847 | 德国 | 女 | 2 | 1918 |
| Felix Mendelssohn | 1809–1847 | 德国 | 男 | 2 | 1918 |
| Frédéric Chopin | 1810–1849 | 波兰 | 男 | 2 | 1920 |
| Henry Bishop | 1787–1855 | 英国 | 男 | 2 | 1926 |
| Robert Schumann | 1810–1856 | 德国 | 男 | 1 | 1927 |
| Emilie Zumsteeg | 1796–1857 | 德国 | 女 | 1 | 1928 |
| Jane Bianchi | 1776–1858 | 英国 | 女 | 1 | 1929 |
| Johanna Kinkel | 1810–1858 | 德国 | 女 | 1 | 1929 |
| Pauline Duchambge | 1776–1858 | 法国 | 女 | 2 | 1929 |
| Gioachino Rossini | 1792–1868 | 意大利 | 男 | 1 | 1939 |
| Charlotte Alington Barnard | 1830–1869 | 英国 | 女 | 2 | 1940 |
| Hector Berlioz | 1803–1869 | 法国 | 男 | 2 | 1940 |
| Peter Cornelius | 1824–1874 | 德国 | 男 | 2 | 1945 |
| Georges Bizet | 1838–1875 | 法国 | 男 | 2 | 1946 |
| Louise Farrenc | 1804–1875 | 法国 | 女 | 1 | 1946 |
| Elizabeth Phillips | 1822–1876 | 英国 | 女 | 1 | 1947 |
| Virginia Gabriel | 1825–1877 | 英国 | 女 | 2 | 1948 |
| Ellen Dickson | 1819–1878 | 英国 | 女 | 2 | 1949 |
| Josephine Lang | 1815–1880 | 德国 | 女 | 1 | 1951 |
| Augusta Browne | 1820–1882 | 美国 | 女 | 2 | 1953 |
| Emilie Mayer | 1812–1883 | 德国 | 女 | 1 | 1954 |
| Richard Wagner | 1813–1883 | 德国 | 男 | 1 | 1954 |
| Elizabeth Philp | 1827–1885 | 英国 | 女 | 1 | 1956 |
| Franz Liszt | 1811–1886 | 匈牙利 | 男 | 1 | 1957 |
| Loïsa Puget | 1810–1889 | 法国 | 女 | 1 | 1960 |
| Alfred Cellier | 1844–1891 | 英国 | 男 | 1 | 1962 |
| Ann Mounsey | 1811–1891 | 英国 | 女 | 1 | 1962 |
| Robert Franz | 1815–1892 | 德国 | 男 | 2 | 1963 |
| Charles Gounod | 1818–1893 | 法国 | 男 | 2 | 1964 |
| Emmanuel Chabrier | 1841–1894 | 法国 | 男 | 2 | 1965 |
| Faustina Hasse Hodges | 1823–1895 | 美国 | 女 | 1 | 1966 |
| Clara Wieck | 1819–1896 | 德国 | 女 | 1 | 1967 |
| Joseph Barnby | 1838–1896 | 英国 | 男 | 2 | 1967 |
| Johannes Brahms | 1833–1897 | 德国 | 男 | 2 | 1968 |
| Maria Lindsay | 1827–1898 | 英国 | 女 | 1 | 1969 |
| Ernest Chausson | 1855–1899 | 法国 | 男 | 2 | 1970 |
| Arthur Sullivan | 1842–1900 | 英国 | 男 | 1 | 1971 |
| Giuseppe Verdi | 1813–1901 | 意大利 | 男 | 1 | 1972 |
| Amelia Lehmann | 1838–1903 | 英国 | 女 | 1 | 1974 |
| Augusta Holmès | 1847–1903 | 法国 | 女 | 5 | 1974 |
| Hugo Wolf | 1860–1903 | 奥地利 | 男 | 1 | 1974 |
| Antonín Dvořák | 1841–1904 | 捷克 | 男 | 1 | 1975 |
| Clémence de Grandval | 1828–1907 | 法国 | 女 | 2 | 1978 |
| Pauline-Marie-Elisa Thys | 1835–1909 | 法国 | 女 | 1 | 1980 |
| Pauline Viardot | 1821–1910 | 法国 | 女 | 1 | 1981 |
| Gustav Mahler | 1860–1911 | 奥地利 | 男 | 1 | 1982 |
| Louisa Gray | 1830–1911 | — | 女 | 2 | 1982 |
| Jules Massenet | 1842–1912 | 法国 | 男 | 1 | 1983 |
| Samuel Coleridge-Taylor | 1875–1912 | 英国 | 男 | 3 | 1983 |
| Francesco Paolo Tosti | 1846–1916 | 意大利 | 男 | 1 | 1987 |
| George Butterworth | 1885–1916 | 英国 | 男 | 4 | 1987 |
| Liliʻuokalani | 1838–1917 | 美国·夏威夷 | 女 | 1 | 1988 |
| Scott Joplin | 1868–1917 | 美国 | 男 | 1 | 1988 |
| Claude Debussy | 1862–1918 | 法国 | 男 | 2 | 1989 |
| Hubert Parry | 1848–1918 | 英国 | 男 | 1 | 1989 |
| Lili Boulanger | 1893–1918 | 法国 | 女 | 2 | 1989 |
| Liza Lehmann | 1862–1918 | 英国 | 女 | 1 | 1989 |
| Helena Munktell | 1852–1919 | 瑞典 | 女 | 1 | 1990 |
| Ruggero Leoncavallo | 1857–1919 | 意大利 | 男 | 1 | 1990 |
| Amy Elsie Horrocks | 1867–1920 | 英国 | 女 | 2 | 1991 |
| Gabrielle Ferrari | 1851–1921 | 法国 | 女 | 2 | 1992 |
| Florence Ashton Marshall | 1843–1922 | 英国 | 女 | 1 | 1993 |
| Gabriel Fauré | 1845–1924 | 法国 | 男 | 2 | 1995 |
| Walter Parratt | 1841–1924 | 英国 | 男 | 4 | 1995 |
| Erik Satie | 1866–1925 | 法国 | 男 | 1 | 1996 |
| Marie Jaëll | 1846–1925 | 法国 | 女 | 1 | 1996 |
| Stefano Donaudy | 1879–1925 | 意大利 | 男 | 1 | 1996 |
| Charles Wood | 1866–1926 | 爱尔兰 | 男 | 1 | 1997 |
| Émile Paladilhe | 1844–1926 | 法国 | 男 | 1 | 1997 |
| Ange Flégier | 1846–1927 | 法国 | 男 | 1 | 1998 |
| Laura Netzel | 1839–1927 | 瑞典 | 女 | 1 | 1998 |
| Luise Adolpha Le Beau | 1850–1927 | 德国 | 女 | 1 | 1998 |
| Peter Warlock | 1894–1930 | 英国 | 男 | 1 | 2001 |
| Frederick Corder | 1852–1932 | 英国 | 男 | 1 | 2003 |
| Poldowski | 1880–1932 | 英国 | 女 | 1 | 2003 |
| Edward Elgar | 1857–1934 | 英国 | 男 | 2 | 2005 |
| Frederick Delius | 1862–1934 | 英国 | 男 | 2 | 2005 |
| Jane Bingham Abbott | 1851–1934 | 美国 | 女 | 2 | 2005 |
| Alban Berg | 1885–1935 | 奥地利 | 男 | 1 | 2006 |
| Alexander Mackenzie | 1847–1935 | 英国·苏格兰 | 男 | 3 | 2006 |
| Chiquinha Gonzaga | 1847–1935 | 巴西 | 女 | 2 | 2006 |
| Frederic Hymen Cowen | 1852–1935 | 英国 | 男 | 1 | 2006 |
| Sir Harold Boulton, 2nd Baronet | 1859–1935 | 英国 | 男 | 4 | 2006 |
| Edward German | 1862–1936 | 英国 | 男 | 2 | 2007 |
| Guy d'Hardelot | 1858–1936 | 英国 | 女 | 2 | 2007 |
| Arthur Somervell | 1863–1937 | 英国 | 男 | 1 | 2008 |
| Evelyn Faltis | 1887–1937 | 捷克 | 女 | 2 | 2008 |
| Ivor Gurney | 1890–1937 | 英国 | 男 | 2 | 2008 |
| Maude Valerie White | 1855–1937 | 英国 | 女 | 1 | 2008 |
| Mélanie Bonis | 1858–1937 | 法国 | 女 | 2 | 2008 |
| Cyril Rootham | 1875–1938 | 英国 | 男 | 1 | 2009 |
| Frank Bridge | 1879–1941 | 英国 | 男 | 2 | 2012 |
| Walford Davies | 1869–1941 | 英国 | 男 | 2 | 2012 |
| Eleanor Everest Freer | 1864–1942 | 美国 | 女 | 2 | 2013 |
| Alice Tegnér | 1864–1943 | 瑞典 | 女 | 1 | 2014 |
| Harold White | 1872–1943 | 爱尔兰 | 男 | 1 | 2014 |
| Amy Beach | 1867–1944 | 美国 | 女 | 4 | 2015 |
| Cécile Chaminade | 1857–1944 | 法国 | 女 | 2 | 2015 |
| Ethel Smyth | 1858–1944 | 英国 | 女 | 1 | 2015 |
| Luise Greger | 1862–1944 | 德国 | 女 | 2 | 2015 |
| Mathilde Kralik | 1857–1944 | 奥地利 | 女 | 1 | 2015 |
| Anton Webern | 1883–1945 | 奥地利 | 男 | 1 | 2016 |
| Fernando Obradors | 1897–1945 | 西班牙 | 男 | 2 | 2016 |
| Helen Hopekirk | 1856–1945 | 美国 | 女 | 1 | 2016 |
| Carrie Jacobs-Bond | 1862–1946 | 美国 | 女 | 2 | 2017 |
| Granville Bantock | 1868–1946 | 英国 | 男 | 2 | 2017 |
| Reynaldo Hahn | 1874–1947 | 法国 | 男 | 2 | 2018 |
| Clara Mathilda Faisst | 1872–1948 | 德国 | 女 | 4 | 2019 |
| Ethel Barns | 1874–1948 | 英国 | 女 | 1 | 2019 |
| Harry T. Burleigh | 1866–1949 | 美国 | 男 | 3 | 2020 |
| Richard Strauss | 1864–1949 | 德国 | 男 | 2 | 2020 |
| Arnold Schoenberg | 1874–1951 | 美国 | 男 | 1 | 2022 |
| Roger Quilter | 1877–1953 | 英国 | 男 | 1 | 2024 |
| Charles Ives | 1874–1954 | 美国 | 男 | 1 | 2025 |

## 二、版本信息

### 2.1 MusicXML 规范版本

| 版本 | 曲目 | 说明 |
|---|---|---|
| 4.0 | 202 | DTD 4.0 Partwise（当前主流） |
| 3.1 | 3 | DTD 3.1 Partwise（旧版） |

### 2.2 记谱软件版本

| 生成软件 | 曲目 |
|---|---|
| MuseScore 4.5.2 | 172 |
| MuseScore Studio 4.6.3 | 18 |
| MuseScore Studio 4.6.5 | 10 |
| MuseScore 3.6.2 | 3 |
| MuseScore Studio 4.7.4 | 2 |

### 2.3 转换/导出时间

`2025-07-09` ~ `2026-09-05`（共 205 份带 `<encoding-date>`）

### 2.4 曲库自身版本

| 曲库 | 仓库 | 取用方式 |
|---|---|---|
| 艺术歌曲 Lieder | OpenScore/Lieder | 稀疏检出（blobless，仅 `scores/` + `data/`）|
| 弦乐四重奏 | OpenScore/StringQuartets | 同上 |

> 谱面内另记有 `<creator type="arranger">`（校对/转写者，含 IMSLP 反查编号）与 `<source>`（MuseScore 原始链接），逐曲见第五节与 `catalog.csv`。

## 三、分类索引

### 3.1 按体裁

| 体裁 | 曲目 | 占比 |
|---|---|---|
| 艺术歌曲 Lieder | 200 | 97% |
| 弦乐四重奏 String Quartets | 5 | 2% |

### 3.2 按时期

| 时期 | 曲目 | 占比 |
|---|---|---|
| 晚期浪漫 | 71 | 34% |
| 近现代 | 56 | 27% |
| 浪漫主义（盛期） | 43 | 20% |
| 浪漫主义（早期） | 21 | 10% |
| 古典主义 | 11 | 5% |
| 巴洛克 | 3 | 1% |

### 3.3 按国别

| 国别 | 曲目 | 占比 |
|---|---|---|
| 英国 | 72 | 35% |
| 法国 | 45 | 21% |
| 德国 | 30 | 14% |
| 美国 | 20 | 9% |
| 奥地利 | 12 | 5% |
| 意大利 | 5 | 2% |
| 捷克 | 3 | 1% |
| 英国·苏格兰 | 3 | 1% |
| 瑞典 | 3 | 1% |
| 波兰 | 2 | 0% |
| 巴西 | 2 | 0% |
| — | 2 | 0% |
| 西班牙 | 2 | 0% |
| 爱尔兰 | 2 | 0% |
| 美国·夏威夷 | 1 | 0% |
| 匈牙利 | 1 | 0% |

## 四、逐曲清单

| # | 体裁 | 作曲家 | 曲名（文件名） | 界面标题 | MusicXML | 软件 | 规模 | 贡献人（转谱/校对） | 源 URL |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 弦乐四重 | Antonín Dvořák | Echo of Songs, B.152 | Echo of Songs, B.152 | 4.0 | MuseScore Studio 4.7.4 | — | Transcribed by flutemouse from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/13125367 | http://musescore.com/user/37221589/scores/24409123 |
| 2 | 弦乐四重 | François Joseph Gossec | String Quartet in C minor, RH 189 | String Quartet in C minor, RH 189 | 4.0 | MuseScore Studio 4.7.4 | — | Transcribed by flutemouse from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/355492 | http://musescore.com/user/37221589/scores/27571393 |
| 3 | 弦乐四重 | Joseph Haydn | String Quartet in B-flat major (“La Chasse”), Hob. III - 1, Op.1 No.1 | String Quartet in B-flat major (“La Chasse”), Hob. III:1, Op.1 No.1 | 3.1 | MuseScore 3.6.2 | — | Transcribed by Gijs Bikker from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/106785 | http://musescore.com/user/37221589/scores/8461409 |
| 4 | 弦乐四重 | Joseph Haydn | String Quartet in C major, Hob.III - 6, Op.1 No.6 | String Quartet in C major, Hob.III:6, Op.1 No.6 | 3.1 | MuseScore 3.6.2 | — | Transcribed by Controlledgoose and ashmoggs from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/106790 | http://musescore.com/user/37221589/scores/8806134 |
| 5 | 弦乐四重 | Joseph Haydn | String Quartet in E-flat major, Hob.III - 2, Op.1 No.2 | String Quartet in E-flat major, Hob.III:2, Op.1 No.2 | 3.1 | MuseScore 3.6.2 | — | Transcribed by Bernhard1964 from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/106786 | http://musescore.com/user/37221589/scores/8806881 |
| 6 | 艺术歌曲 | Alban Berg | 7 frühe Lieder - Nacht | 7 frühe Lieder | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/15386 | https://github.com/OpenScore/Lieder |
| 7 | 艺术歌曲 | Alexander Mackenzie | One who never turned his back | One who never turned his back | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #618722. Source: https://imslp.org/wiki/Special:ReverseLookup/618722 | http://musescore.com/user/27638568/scores/6499366 |
| 8 | 艺术歌曲 | Alexander Mackenzie | Spring Songs, Op.44 - Hope | Spring Songs, Op.44 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #241305. Source: https://imslp.org/wiki/Special:ReverseLookup/241305 | http://musescore.com/user/27638568/scores/6505088 |
| 9 | 艺术歌曲 | Alexander Mackenzie | Spring Songs, Op.44 - The First Rose | Spring Songs, Op.44 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #241305. Source: https://imslp.org/wiki/Special:ReverseLookup/241305 | http://musescore.com/user/27638568/scores/6505010 |
| 10 | 艺术歌曲 | Alfred Cellier | Oh! Woman, Sweet Woman | Oh! Woman, Sweet Woman | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #180626. Source: https://imslp.org/wiki/Special:ReverseLookup/180626 | http://musescore.com/user/27638568/scores/6480111 |
| 11 | 艺术歌曲 | Alice Tegnér | Betlehems stjärna | Betlehems stjärna | 4.0 | MuseScore 4.5.2 | — | Transcribed by mooing from IMSLP #436417. Source: https://imslp.org/wiki/Special:ReverseLookup/436417 | http://musescore.com/user/27638568/scores/6910499 |
| 12 | 艺术歌曲 | Amelia Lehmann | Bouton de Rose (To Rosa) | Bouton de Rose (To Rosa) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #285344. Source: https://imslp.org/wiki/Special:ReverseLookup/285344 | http://musescore.com/user/27638568/scores/6644591 |
| 13 | 艺术歌曲 | Amy Beach | 3 Browning Songs, Op. 44 - The Year's at the Spring | 3 Browning Songs, Op. 44 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #522898. Source: https://imslp.org/wiki/3_Browning_Songs,_Op.44_(Beach,_Amy_Marcy) | http://musescore.comhttps://musescore.com/user/27638568/scores/6212179 |
| 14 | 艺术歌曲 | Amy Beach | 3 Browning songs, Op. 44 - Ah, Love, but a Day! | 3 Browning songs, Op. 44 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #75959. Source: https://imslp.org/wiki/3_Browning_Songs,_Op.44_(Beach,_Amy_Marcy) | http://musescore.com/user/27638568/scores/6212193 |
| 15 | 艺术歌曲 | Amy Beach | 3 Shakespeare Songs, Op.37 - O Mistress Mine | 3 Shakespeare Songs, Op.37 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #637440. Source: https://imslp.org/wiki/Special:ReverseLookup/637440 | http://musescore.com/user/27638568/scores/6564424 |
| 16 | 艺术歌曲 | Amy Beach | 4 Songs, Op. 51 - Ich sagete nicht - Silent Love | 4 Songs, Op. 51 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #280033. Source: https://imslp.org/wiki/4_Songs,_Op.51_(Beach,_Amy_Marcy) | http://musescore.com/user/27638568/scores/6245971 |
| 17 | 艺术歌曲 | Amy Elsie Horrocks | Cottage Cradle Song | Cottage Cradle Song | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #592442. Source: https://imslp.org/wiki/Special:ReverseLookup/592442 | http://musescore.com/user/27638568/scores/6635580 |
| 18 | 艺术歌曲 | Amy Elsie Horrocks | The Bird and the Rose | The Bird and the Rose | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #237206. Source: https://imslp.org/wiki/Special:ReverseLookup/237206 | http://musescore.com/user/27638568/scores/6636096 |
| 19 | 艺术歌曲 | Ange Flégier | Le cor | — | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/756787 | https://musescore.com/user/27638568/scores/30346709 |
| 20 | 艺术歌曲 | Ann Mounsey | Songs of Remembrance - If love be life, I long to die | Songs of Remembrance | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #668562. Source: https://imslp.org/wiki/Special:ReverseLookup/ | http://musescore.com/user/27638568/scores/6646808 |
| 21 | 艺术歌曲 | Anton Webern | 5 Lieder aus “Der siebente Ring”, Op.3 - Dies ist ein Lied für dich allein | 5 Lieder aus “Der siebente Ring”, Op.3 | 4.0 | MuseScore 4.5.2 | — | Transcribed by joshuaballance from IMSLP #09951. Source: https://imslp.org/wiki/Special:ReverseLookup/09951 | http://musescore.com/user/27638568/scores/6715306 |
| 22 | 艺术歌曲 | Arnold Schoenberg | Das Buch der hängenden Gärten, Op.15 - Das schöne Beet betracht ich mir im Harren | Das Buch der hängenden Gärten, Op.15 | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/23662 | https://musescore.com/user/27638568/scores/30509480 |
| 23 | 艺术歌曲 | Arthur Somervell | A Shropshire Lad | A Shropshire Lad | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #529227. Source: https://imslp.org/wiki/A_Shropshire_Lad_(Somervell,_Arthur) | http://musescore.com/user/27638568/scores/6210838 |
| 24 | 艺术歌曲 | Arthur Sullivan | The Long Day Closes | The Long Day Closes | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #179565 (for voices ATBB or TTBB). Source: https://imslp.org/wiki/The_Long_Day_Closes_(Sullivan,_Arthur) | http://musescore.com/user/27638568/scores/6205297 |
| 25 | 艺术歌曲 | Augusta Browne | Forever Thine | Forever Thine | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #191749. Source: https://imslp.org/wiki/Special:ReverseLookup/191749 | http://musescore.com/user/27638568/scores/6588872 |
| 26 | 艺术歌曲 | Augusta Browne | The Reply of the Messenger Bird | The Reply of the Messenger Bird | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #253076. Source: https://imslp.org/wiki/Special:ReverseLookup/253076 | http://musescore.com/user/27638568/scores/6588799 |
| 27 | 艺术歌曲 | Augusta Holmès | 20 Mélodies - Chanson Lointaine | 20 Mélodies | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #295514. Source: http://imslp.org/wiki/20_Mélodies_(Holmès,_Augusta_Mary_Anne) | http://musescore.com/user/27638568/scores/5001716 |
| 28 | 艺术歌曲 | Augusta Holmès | Contes divins - L'Aubépine de St. Patrick | Contes divins | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #588987. Source: https://imslp.org/wiki/Contes_divins_(Holmès,_Augusta_Mary_Anne) | http://musescore.com/user/27638568/scores/5903060 |
| 29 | 艺术歌曲 | Augusta Holmès | Les Heures - L'Heure Rose | Les Heures | 4.0 | MuseScore 4.5.2 | — | Transcribed from Transcribed by Eloge from IMSLP #545236. Source: https://imslp.org/wiki/Les_heures_(Holm%C3%A8s%2C_Augusta_Mary_Anne) | http://musescore.com/user/27638568/scores/5712131 |
| 30 | 艺术歌曲 | Augusta Holmès | Les Sept Ivresses - L'Amour | Les Sept Ivresses | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #236513. Source: http://imslp.org/wiki/Les_sept_ivresses_(Holm%C3%A8s%2C_Augusta_Mary_Anne) | http://musescore.com/user/27638568/scores/5646201 |
| 31 | 艺术歌曲 | Augusta Holmès | Les Sérénades - Sérénade Printanière | Les Sérénades | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #112763 by Eloge. Source: https://imslp.org/wiki/Les_sérénades_(Holmès,_Augusta_Mary_Anne) | http://musescore.com/user/27638568/scores/5001684 |
| 32 | 艺术歌曲 | Carrie Jacobs-Bond | 3 Songs as Unpretentious as the Wild Rose - Nothing But a Wild Rose | 3 Songs as Unpretentious as the Wild Rose | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #196066. Source: https://imslp.org/wiki/Special:ReverseLookup/196066 | http://musescore.com/user/27638568/scores/6586980 |
| 33 | 艺术歌曲 | Carrie Jacobs-Bond | Because I Am Your Friend | Because I Am Your Friend | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #660145. Source: https://imslp.org/wiki/Special:ReverseLookup/660145 | http://musescore.com/user/27638568/scores/6586916 |
| 34 | 艺术歌曲 | Charles Gounod | 6 Mélodies - Le Premier Jour de Mai | 6 Mélodies | 4.0 | MuseScore 4.5.2 | — | — | https://musescore.com/openscore-lieder-corpus/scores/5079368 |
| 35 | 艺术歌曲 | Charles Gounod | Le soir, CG 441 | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/258735 | https://github.com/OpenScore/Lieder |
| 36 | 艺术歌曲 | Charles Ives | 114 Songs - Songs My Mother Taught Me | 114 Songs | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/29684 | https://github.com/OpenScore/Lieder |
| 37 | 艺术歌曲 | Charles Wood | Ethiopia Saluting the Colours | Ethiopia Saluting the Colours | 4.0 | MuseScore 4.5.2 | — | — | http://musescore.com/user/27638568/scores/6568070 |
| 38 | 艺术歌曲 | Charlotte Alington Barnard | Five o’clock in the morning | Five o’clock in the morning | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #397171. Source: https://imslp.org/wiki/Special:ReverseLookup/397171 | http://musescore.com/user/27638568/scores/6623145 |
| 39 | 艺术歌曲 | Charlotte Alington Barnard | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the - Farewell to Erin | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #286538. Source: https://imslp.org/wiki/Special:ReverseLookup/286538 | http://musescore.com/user/27638568/scores/6623221 |
| 40 | 艺术歌曲 | Chiquinha Gonzaga | A mulatinha | A mulatinha | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #612574. Source: https://imslp.org/wiki/Special:ReverseLookup/612574 | http://musescore.com/user/27638568/scores/6608395 |
| 41 | 艺术歌曲 | Chiquinha Gonzaga | A sereia | A sereia | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #625250. Source: https://imslp.org/wiki/Special:ReverseLookup/625250 | http://musescore.com/user/27638568/scores/6609884 |
| 42 | 艺术歌曲 | Clara Mathilda Faisst | 2 Kriegslieder - Unsern Getreuen | 2 Kriegslieder | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #623002. Source: https://imslp.org/wiki/Special:ReverseLookup/623002 | http://musescore.com/scores/faisst-clara/2-kriegslieder-856997919394677 |
| 43 | 艺术歌曲 | Clara Mathilda Faisst | 2 Lieder, Op.19 - Stimme eines seligen Geistes | 2 Lieder, Op.19 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #622488. Source: https://imslp.org/wiki/Special:ReverseLookup/622488 | http://musescore.com/user/27638568/scores/6575317 |
| 44 | 艺术歌曲 | Clara Mathilda Faisst | 2 Lieder, Op.8 - Die Insel der Vergessenheit | 2 Lieder, Op.8 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Ads20000 from IMSLP #621841. Source: https://imslp.org/wiki/2_Lieder,_Op.8_(Faisst,_Clara) | http://musescore.com/user/27638568/scores/6164267 |
| 45 | 艺术歌曲 | Clara Mathilda Faisst | 4 Lieder, Op.11 - Wanderlied | 4 Lieder, Op.11 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #622102. Source: https://imslp.org/wiki/4_Lieder%2C_Op.11_(Faisst%2C_Clara) | http://musescore.com/user/27638568/scores/6258870 |
| 46 | 艺术歌曲 | Clara Wieck | 6 Lieder, Op.13 - Ich stand in dunklen Träumen | 6 Lieder, Op.13 | 4.0 | MuseScore 4.5.2 | — | — | https://musescore.com/openscore-lieder-corpus/scores/5133602 |
| 47 | 艺术歌曲 | Claude Debussy | 2 Romances - L'âme évaporée | 2 Romances | 4.0 | MuseScore 4.5.2 | — | Originally transcribed by Keith Willams, then edited by DanielR toconform to the source edition IMSLP #14816. | http://musescore.com/user/27638568/scores/7163829 |
| 48 | 艺术歌曲 | Claude Debussy | 3 Chansons de France - Rondel - Le temps a laissé son manteau | 3 Chansons de France | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #09101. Source: https://imslp.org/wiki/Special:ReverseLookup/09101 | http://musescore.com/user/27638568/scores/8830536 |
| 49 | 艺术歌曲 | Clémence de Grandval | 6 Nouvelles mélodies - Les clochettes | 6 Nouvelles mélodies | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #578226. Source: https://imslp.org/wiki/6_Nouvelles_m%C3%A9lodies_(Grandval%2C_Cl%C3%A9mence_de) | http://musescore.com/user/27638568/scores/6613355 |
| 50 | 艺术歌曲 | Clémence de Grandval | Chanson de Barberine | Chanson de Barberine | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #578182. Source: https://imslp.org/wiki/Special:ReverseLookup/578182 | http://musescore.com/user/27638568/scores/6625925 |
| 51 | 艺术歌曲 | Corona Schröter | 25 Lieder - Lied der Morgenröte | 25 Lieder | 4.0 | MuseScore 4.5.2 | — | Transcribed by Ashmoggs from IMSLP #109659. Source: https://imslp.org/wiki/25_Lieder_(Schröter,_Corona) | http://musescore.com/user/27638568/scores/6017264 |
| 52 | 艺术歌曲 | Cyril Rootham | The Ballad of Kingslea Mere, Op.19 | The Ballad of Kingslea Mere, Op.19 | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #657998. Source: https://imslp.org/wiki/Special:ReverseLookup/657998 | http://musescore.com/user/27638568/scores/6449397 |
| 53 | 艺术歌曲 | Cécile Chaminade | Alleluia | Alleluia | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #154241. Source: https://imslp.org/wiki/Alleluia_(Chaminade%2C_C%C3%A9cile) | http://musescore.com/user/27638568/scores/6260992 |
| 54 | 艺术歌曲 | Cécile Chaminade | Amertume | Amertume | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #154299. Source: https://imslp.org/wiki/Amertume_(Chaminade%2C_C%C3%A9cile) | http://musescore.com/user/27638568/scores/6261036 |
| 55 | 艺术歌曲 | Edward Elgar | 2 Songs, Op.60 - The Torch | 2 Songs, Op.60 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #555775. Source: https://imslp.org/wiki/2_Songs,_Op.60_(Elgar,_Edward) | http://musescore.com/user/27638568/scores/6233544 |
| 56 | 艺术歌曲 | Edward Elgar | 7 Lieder - Like to the Damask Rose | 7 Lieder | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #556602. Source: https://imslp.org/wiki/7_Lieder_(Elgar%2C_Edward) | http://musescore.com/user/27638568/scores/6236149 |
| 57 | 艺术歌曲 | Edward German | 3 Spring Songs - All the World Awakes Today | 3 Spring Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #167819. Source: https://imslp.org/wiki/3_Spring_Songs_(German,_Edward) | http://musescore.com/user/27638568/scores/6243836 |
| 58 | 艺术歌曲 | Edward German | 3 Spring Songs - The Dew Upon the Lily | 3 Spring Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #167819. Source: https://imslp.org/wiki/3_Spring_Songs_(German,_Edward) | http://musescore.com/user/27638568/scores/6243838 |
| 59 | 艺术歌曲 | Eleanor Everest Freer | 2 Songs, Op.16 - Daughter of Egypt, veil thine eyes | 2 Songs, Op.16 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #33081. Source: https://imslp.org/wiki/Special:ReverseLookup/33081 | http://musescore.com/user/27638568/scores/6598677 |
| 60 | 艺术歌曲 | Eleanor Everest Freer | 2 Songs, Op.16 - The boat is chafing at our long delay | 2 Songs, Op.16 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #33081. Source: https://imslp.org/wiki/Special:ReverseLookup/33081 | http://musescore.com/user/27638568/scores/6598624 |
| 61 | 艺术歌曲 | Elisabetta de Gambarini | Lessons and Songs (Lessons for the Harpsichord, Intermix’d with - Behold, Behold and Listen | Lessons and Songs (Lessons for the Harpsichord, Intermix’d with Italian and English Songs) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #535387. Source: https://imslp.org/wiki/Special:ReverseLookup/535387 | http://musescore.com/user/27638568/scores/6604420 |
| 62 | 艺术歌曲 | Elizabeth Phillips | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the - Cushla Machree | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #286650. Source: https://imslp.org/wiki/Special:ReverseLookup/286650 | http://musescore.com/user/27638568/scores/6606200 |
| 63 | 艺术歌曲 | Elizabeth Philp | Modern Ballads - A Selection of 50 Favourite Songs and Ballads by the - Bye-and-Bye | Modern Ballads: A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers | 4.0 | MuseScore 4.5.2 | — | Transcribed by MusiPhil from IMSLP #286660. Source: https://imslp.org/wiki/Special:ReverseLookup/286660 | http://musescore.com/user/27638568/scores/6605890 |
| 64 | 艺术歌曲 | Ellen Dickson | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the - Destiny | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #286583. Source: https://imslp.org/wiki/Special:ReverseLookup/286583 | http://musescore.com/user/27638568/scores/6601006 |
| 65 | 艺术歌曲 | Ellen Dickson | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the - Drifting | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #286682. Source: https://imslp.org/wiki/Special:ReverseLookup/286682 | http://musescore.com/user/27638568/scores/6601058 |
| 66 | 艺术歌曲 | Emilie Mayer | 2 Gesänge - Abendglocken | 2 Gesänge | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #133706. Source: https://imslp.org/wiki/2_Gesänge_(Mayer,_Emilie) | http://musescore.com/user/27638568/scores/5823419 |
| 67 | 艺术歌曲 | Emilie Zumsteeg | 5 Lieder - Des Kaufmanns Liebeswerbung | 5 Lieder | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #192839. Source: https://imslp.org/wiki/5_Lieder_(Zumsteeg,_Emilie) | http://musescore.com/user/27638568/scores/6158642 |
| 68 | 艺术歌曲 | Emmanuel Chabrier | Ballade des gros dindons, IEC 5 - Ballade des gros dindons (1889) | Ballade des gros dindons, IEC 5 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Vinckenbosch from IMSLP #22635. https://imslp.org/wiki/Ballade_des_gros_dindons_(Chabrier%2C_Emmanuel) | http://musescore.com/user/27638568/scores/6587611 |
| 69 | 艺术歌曲 | Emmanuel Chabrier | Chanson pour Jeanne (1886), IEC 10 | Chanson pour Jeanne (1886), IEC 10 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Vinckenbosch from IMSLP #22637. https://imslp.org/wiki/Chanson_pour_Jeanne_(Chabrier,_Emmanuel) | http://musescore.com/user/27638568/scores/6497657 |
| 70 | 艺术歌曲 | Erik Satie | 4 Petites mélodies - Elégies | 4 Petites mélodies | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #16886. Source: https://imslp.org/wiki/Special:ReverseLookup/16886 | http://musescore.com/user/27638568/scores/6988229 |
| 71 | 艺术歌曲 | Ernest Chausson | 7 Mélodies, Op.2 - Nanny | 7 Mélodies, Op.2 | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #16897. Source: https://imslp.org/wiki/Special:ReverseLookup/154241 | http://musescore.com/user/27638568/scores/5077645 |
| 72 | 艺术歌曲 | Ernest Chausson | Serres chaudes, Op.24 - Serre chaude | Serres chaudes, Op.24 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #26882. Source: https://imslp.org/wiki/Serres_chaudes,_Op.24_(Chausson,_Ernest) | http://musescore.com/user/27638568/scores/5057840 |
| 73 | 艺术歌曲 | Ethel Barns | Sleep, Weary Heart | Sleep, Weary Heart | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #642301. Source: https://imslp.org/wiki/Special:ReverseLookup/642301 | http://musescore.com/user/27638568/scores/6586696 |
| 74 | 艺术歌曲 | Ethel Smyth | 3 Songs - The Clown | 3 Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #394162. Source: https://imslp.org/wiki/Special:ReverseLookup/394162 | http://musescore.com/user/27638568/scores/6665104 |
| 75 | 艺术歌曲 | Evelyn Faltis | Lieder fernen Gedenkens, Op. posth - Unklarheit | Lieder fernen Gedenkens, Op. posth. | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #86859. Source: https://imslp.org/wiki/Special:ReverseLookup/86859 | http://musescore.com/scores/faltis-evelyn/lieder-fernen-gedenkens-op-posth-364660142797621 |
| 76 | 艺术歌曲 | Evelyn Faltis | Lieder fernen Gedenkens, Op. posth - Zeig mir dein wahres Bild | Lieder fernen Gedenkens, Op. posth. | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #86859. Source: https://imslp.org/wiki/Special:ReverseLookup/86859 | http://musescore.com/scores/faltis-evelyn/lieder-fernen-gedenkens-op-posth-169951772618794 |
| 77 | 艺术歌曲 | Fanny (Mendelssohn) Hensel | 3 Lieder - Sehnsucht | 3 Lieder | 4.0 | MuseScore 4.5.2 | — | Transcribed by Justin M. Bornais from IMSLP #29138. Source: https://imslp.org/wiki/3_Lieder_(Hensel,_Fanny) | http://musescore.com/user/27638568/scores/6012947 |
| 78 | 艺术歌曲 | Fanny (Mendelssohn) Hensel | 3 Songs - Das Heimweh | 3 Songs | 4.0 | MuseScore 4.5.2 | — | Originally published as Felix Mendelssohn Op.8, No.2. Transcribed by Justin M. Bornais from IMSLP #28641. Source: https://imslp.org/wiki/3_Songs_(Hensel,_Fanny) | http://musescore.com/user/27638568/scores/6022316 |
| 79 | 艺术歌曲 | Faustina Hasse Hodges | Dreams | Dreams | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #453689. Source: https://imslp.org/wiki/Special:ReverseLookup/453689 | http://musescore.com/scores/faustina-hasse-hodges/dreams-758051027354335 |
| 80 | 艺术歌曲 | Felix Mendelssohn | 6 Duets (6 Lieder für zwei Singstimmen) - Ich wollt' meine Lieb' ergösse sich, MWV J 5. (1836) | 6 Duets (6 Lieder für zwei Singstimmen) | 4.0 | MuseScore 4.5.2 | — | Transcribed by Mélisande from IMSLP #41097, edited by Vinckenbosch, reviewed by DanielR. Source: https://imslp.org/wiki/Special:ReverseLookup/41097 | http://musescore.com/scores/felix-mendelssohn/6-duets-op63-191829826432365 |
| 81 | 艺术歌曲 | Felix Mendelssohn | 6 Gesänge, Op. 86 - Das Fenster, MWV K 29 | 6 Gesänge, Op. 86 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Vinckenbosch | http://musescore.com/scores/felix-mendelssohn/6-gesange-op86-339996791256601 |
| 82 | 艺术歌曲 | Fernando Obradors | Canciones Clásicas Españolas, Vol.1 - Del cabello más sutil | Canciones Clásicas Españolas, Vol.1 | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/875548 | https://github.com/OpenScore/Lieder |
| 83 | 艺术歌曲 | Fernando Obradors | Walzer-Gesänge, Op.6 - Liebe Schwalbe | Walzer-Gesänge, Op.6 | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/02082 | https://github.com/OpenScore/Lieder |
| 84 | 艺术歌曲 | Florence Ashton Marshall | Ask Me No More | Ask Me No More | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #184203. Source: https://imslp.org/wiki/Special:ReverseLookup/184203 | http://musescore.com/scores/florence-marshall/ask-me-no-more-393404191945123 |
| 85 | 艺术歌曲 | Francesco Paolo Tosti | Ideale | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/252752 | https://github.com/OpenScore/Lieder |
| 86 | 艺术歌曲 | Frank Bridge | 3 Tagore Songs, H.164 - Day after day | 3 Tagore Songs, H.164 | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/ | https://github.com/OpenScore/Lieder |
| 87 | 艺术歌曲 | Frank Bridge | H.40 - Lament | H.40 | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/895949 | https://github.com/OpenScore/Lieder |
| 88 | 艺术歌曲 | Franz Liszt | 3 sonetti di Petrarca, S.270b - Pace non trovo | 3 sonetti di Petrarca, S.270b | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/60386 | https://github.com/OpenScore/Lieder |
| 89 | 艺术歌曲 | Franz Schubert | Vier Gesänge aus 'Wilhelm Meister' (D.877), Op.62 - Mignon und der Harfner | Vier Gesänge aus 'Wilhelm Meister' (D.877), Op.62 | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #62399. Source: https://imslp.org/wiki/Special:ReverseLookup/62399 | http://musescore.com/scores/franz-schubert/4-gesange-aus-wilhelm-meister-d877-340326606902616 |
| 90 | 艺术歌曲 | Frederic Hymen Cowen | Hail! | Hail! | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #625663. Source: https://imslp.org/wiki/Special:ReverseLookup/625663 | http://musescore.com/user/27638568/scores/6482928 |
| 91 | 艺术歌曲 | Frederick Corder | O Sun, That Wakenest | O Sun, That Wakenest | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #183806. Source: https://imslp.org/wiki/Special:ReverseLookup/183806 | http://musescore.comhttps://musescore.com/user/27638568/scores/6480349 |
| 92 | 艺术歌曲 | Frederick Delius | 2 Songs, RT V - 16 - Il pleure dans mon cœur | 2 Songs, RT V/16 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #148197. Source: https://imslp.org/wiki/Special:ReverseLookup/148197 | http://musescore.com/user/27638568/scores/6510449 |
| 93 | 艺术歌曲 | Frederick Delius | 4 Old English Lyrics - It was a Lover and His Lass | 4 Old English Lyrics | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #435041. Source:https://imslp.org/wiki/Category:Shakespeare,_William | http://musescore.com/user/27638568/scores/6230256 |
| 94 | 艺术歌曲 | Frédéric Chopin | Op.74 - Wiosna | Op.74 | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/140312 | https://github.com/OpenScore/Lieder |
| 95 | 艺术歌曲 | Frédéric Chopin | Op.74 - Życzenie | Op.74 | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/140312 | https://musescore.com/user/27638568/scores/30707789 |
| 96 | 艺术歌曲 | Gabriel Fauré | 4 Mélodies, Op. 51 - Larmes | 4 Mélodies, Op. 51 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #291524 by Vinckenbosch. Source: https://imslp.org/wiki/M%C3%A9lodies_(Faur%C3%A9%2C_Gabriel) | http://musescore.com/user/27638568/scores/6135958 |
| 97 | 艺术歌曲 | Gabriel Fauré | Trois mélodies, Op.7 - Après un rêve | Trois mélodies, Op.7 | 4.0 | MuseScore 4.5.2 | — | Transcribed by ashmoggs from IMSLP #24047 Source: https://imslp.org/wiki/Special:ReverseLookup/24047 | http://musescore.com/user/27638568/scores/6810863 |
| 98 | 艺术歌曲 | Gabrielle Ferrari | Le Sommeil | Le Sommeil | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #575893. Source: https://imslp.org/wiki/Special:ReverseLookup/575893 | http://musescore.com/user/27638568/scores/6567603 |
| 99 | 艺术歌曲 | Gabrielle Ferrari | Lontan dagli occhi, lontan dal cuore, Op.17 | Lontan dagli occhi, lontan dal cuore, Op.17 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #507203. Source: https://imslp.org/wiki/Special:ReverseLookup/507203 | http://musescore.com/scores/ferrari-gabrielle/lontan-dagli-occhi-lontan-dal-cuore-op17-744768355530792 |
| 100 | 艺术歌曲 | George Butterworth | A Shropshire Lad - Loveliest of trees | A Shropshire Lad | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #239744. Source: https://imslp.org/wiki/6_Songs_from_A_Shropshire_Lad_(Butterworth,_George) | http://musescore.com/user/27638568/scores/6214840 |
| 101 | 艺术歌曲 | George Butterworth | A Shropshire Lad - When I was One-and-Twenty | A Shropshire Lad | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #239744. Source: https://imslp.org/wiki/6_Songs_from_A_Shropshire_Lad_(Butterworth,_George) | http://musescore.com/user/27638568/scores/6214844 |
| 102 | 艺术歌曲 | George Butterworth | Bredon Hill and Other Songs - Bredon Hill | Bredon Hill and Other Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #239744. Source: https://imslp.org/wiki/Bredon_Hill_and_Other_Songs_(Butterworth,_George) | http://musescore.com/user/27638568/scores/6377942 |
| 103 | 艺术歌曲 | George Butterworth | Love blows as the wind blows | Love blows as the wind blows | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #405017. Source: https://imslp.org/wiki/Love_Blows_as_the_Wind_Blows_(Butterworth,_George) | http://musescore.com/user/27638568/scores/6469541 |
| 104 | 艺术歌曲 | Georges Bizet | 20 Mélodies, Op.21 - Chanson d'avril | 20 Mélodies, Op.21 | 4.0 | MuseScore 4.5.2 | — | Transcribed by mooing from IMSLP #342985. Source: http://imslp.org/wiki/20_M%C3%A9lodies%2C_Op.21_(Bizet%2C_Georges) | http://musescore.com/user/27638568/scores/6877413 |
| 105 | 艺术歌曲 | Georges Bizet | Feuilles d'album - À une Fleur | Feuilles d'album | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #83314 | http://musescore.com/user/27638568/scores/5079494 |
| 106 | 艺术歌曲 | Gioachino Rossini | Soirées musicales - L’invito | Soirées musicales | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/106535 | https://github.com/OpenScore/Lieder |
| 107 | 艺术歌曲 | Giuseppe Verdi | In solitaria stanza | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/04701 | https://github.com/OpenScore/Lieder |
| 108 | 艺术歌曲 | Granville Bantock | 5 Songs from the Chinese Poets, 1st Series - The Ghost Road | 5 Songs from the Chinese Poets, 1st Series | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #236270. Source: https://imslp.org/wiki/5_Songs_from_the_Chinese_Poets,_1st_Series_(Bantock,_Granville) | http://musescore.com/user/27638568/scores/6211549 |
| 109 | 艺术歌曲 | Granville Bantock | 5 Songs from the Chinese Poets, 1st Series - The Old Fisherman of the Mists and Waters | 5 Songs from the Chinese Poets, 1st Series | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #236270. Source: https://imslp.org/wiki/5_Songs_from_the_Chinese_Poets,_1st_Series_(Bantock,_Granville) | http://musescore.com/user/27638568/scores/6211535 |
| 110 | 艺术歌曲 | Gustav Mahler | Des Knaben Wunderhorn - Rheinlegendchen | Des Knaben Wunderhorn | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/46767 | https://github.com/OpenScore/Lieder |
| 111 | 艺术歌曲 | Guy d'Hardelot | Afterwards, Love! | Afterwards, Love! | 4.0 | MuseScore 4.5.2 | — | Transcribed bydeadbeat-s from IMSLP #558603. Source: https://imslp.org/wiki/Special:ReverseLookup/558603 | http://musescore.com/user/27638568/scores/6627929 |
| 112 | 艺术歌曲 | Guy d'Hardelot | Bouquet de violettes | Bouquet de violettes | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #600385. Source: https://imslp.org/wiki/Special:ReverseLookup/600385 | http://musescore.com/user/27638568/scores/6627964 |
| 113 | 艺术歌曲 | Harold White | Macushla | — | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/329500 | https://github.com/OpenScore/Lieder |
| 114 | 艺术歌曲 | Harriett Abrams | Crazy Jane | Crazy Jane | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #396671. Source: https://imslp.org/wiki/Special:ReverseLookup/396671 | http://musescore.com/user/27638568/scores/6583907 |
| 115 | 艺术歌曲 | Harriett Abrams | The Orphan’s Prayer | The Orphan’s Prayer | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #436708. Source: https://imslp.org/wiki/Special:ReverseLookup/436708 | http://musescore.com/user/27638568/scores/6583966 |
| 116 | 艺术歌曲 | Harry T. Burleigh | 5 Songs of Laurence Hope - The Jungle Flower | 5 Songs of Laurence Hope | 4.0 | MuseScore 4.5.2 | — | Transcribed by Brian Alegant and Mark Gotham from IMSLP #238246. Source: https://imslp.org/wiki/5_Songs_of_Laurence_Hope_(Burleigh,_Harry_Thacker) | http://musescore.comhttps://musescore.com/user/27638568/scores/6518134 |
| 117 | 艺术歌曲 | Harry T. Burleigh | 5 Songs of Laurence Hope - Worth While | 5 Songs of Laurence Hope | 4.0 | MuseScore 4.5.2 | — | Transcribed by Brian Alegant and Mark Gotham from IMSLP #238246. Source: https://imslp.org/wiki/5_Songs_of_Laurence_Hope_(Burleigh,_Harry_Thacker) | http://musescore.comhttps://musescore.com/user/27638568/scores/6518082 |
| 118 | 艺术歌曲 | Harry T. Burleigh | Ethiopia Saluting the Colors | Ethiopia Saluting the Colors | 4.0 | MuseScore 4.5.2 | — | — | http://musescore.com/user/27638568/scores/6565727 |
| 119 | 艺术歌曲 | Hector Berlioz | Les nuits d’été, Op.7 - Le spectre de la rose | Les nuits d’été, Op.7 | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/421429 | https://musescore.com/user/27638568/scores/29062082 |
| 120 | 艺术歌曲 | Hector Berlioz | Les nuits d’été, Op.7 - Villanelle | Les nuits d’été, Op.7 | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/421429 | https://github.com/OpenScore/Lieder |
| 121 | 艺术歌曲 | Helen Hopekirk | My Lady of Sleep | My Lady of Sleep | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #204253. Source: https://imslp.org/wiki/Special:ReverseLookup/204253 | http://musescore.com/user/27638568/scores/6632270 |
| 122 | 艺术歌曲 | Helena Munktell | 10 Songs - 10 Mélodies - Sérénade | 10 Songs / 10 Mélodies | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #434307. Source: https://imslp.org/wiki/Special:ReverseLookup/434307 | http://musescore.com/user/27638568/scores/6654094 |
| 123 | 艺术歌曲 | Henry Bishop | (from - ) - Clari - or - The Maid of Milan - - Home. Sweet Home | (from:) "Clari" or "The Maid of Milan" | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #119287. Source: https://imslp.org/wiki/Home,_Sweet_Home_(Bishop,_Henry_Rowley) | http://musescore.comhttps://musescore.com/user/27638568/scores/6486038 |
| 124 | 艺术歌曲 | Henry Bishop | (from - ) - Evenings in Greece - - Sappho at her Loom | (from:) "Evenings in Greece" | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #572445. Source: https://imslp.org/wiki/Sappho_at_her_Loom_(Bishop,_Henry_Rowley) | http://musescore.com/openscore-lieder-corpus/bishop-henry-sappho-at-her-loom |
| 125 | 艺术歌曲 | Hubert Parry | 3 Songs, Op.12 - The Poet's Song | 3 Songs, Op.12 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #184205. Source: https://imslp.org/wiki/3_Songs,_Op.12_(Parry,_Charles_Hubert_Hastings) | http://musescore.comhttps://musescore.com/user/27638568/scores/6434272 |
| 126 | 艺术歌曲 | Hugo Wolf | Eichendorff-Lieder - Der Freund | Eichendorff-Lieder | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #23172. Source: https://imslp.org/wiki/Special:ReverseLookup/23172 | http://musescore.com/user/27638568/scores/5016637 |
| 127 | 艺术歌曲 | Ivor Gurney | 5 Elizabethan Songs - Orpheus | 5 Elizabethan Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #281985. Public Domain source: https://imslp.org/wiki/5_Elizabethan_Songs_(Gurney,_Ivor) | http://musescore.com/user/27638568/scores/6170065 |
| 128 | 艺术歌曲 | Ivor Gurney | I will go with my father a-ploughing | I will go with my father a-ploughing | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #89026. Source: https://imslp.org/wiki/I_Will_Go_with_My_Father_a-Ploughing_(Gurney,_Ivor) | http://musescore.com/user/27638568/scores/6466145 |
| 129 | 艺术歌曲 | Jane Bianchi | Helen | Helen | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #662011. Source: https://imslp.org/wiki/Special:ReverseLookup/662011 | http://musescore.com/user/27638568/scores/6592481 |
| 130 | 艺术歌曲 | Jane Bingham Abbott | Just for Today | Just for Today | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #412044. Source: https://imslp.org/wiki/Special:ReverseLookup/12044 | http://musescore.com/user/27638568/scores/6583477 |
| 131 | 艺术歌曲 | Jane Bingham Abbott | Think of Today | Think of Today | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #530500. Source: https://imslp.org/wiki/Special:ReverseLookup/530500 | http://musescore.com/user/27638568/scores/6583512 |
| 132 | 艺术歌曲 | Jane Mary Guest | Marion, or Will ye gang to the burn side - | Marion, or Will ye gang to the burn side? | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #436436. Source: https://imslp.org/wiki/Special:ReverseLookup/436436 | http://musescore.com/user/27638568/scores/6622431 |
| 133 | 艺术歌曲 | Jane Mary Guest | The Bonnie Wee Wife | The Bonnie Wee Wife | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #661154. Source: https://imslp.org/wiki/Special:ReverseLookup/661154 | http://musescore.com/user/27638568/scores/6621051 |
| 134 | 艺术歌曲 | Johanna Kinkel | 3 Duetten, Op.11 - Das Lied der Nachtigall | 3 Duetten, Op.11 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #618115. Source: https://imslp.org/wiki/3_Duetten,_Op.11_(Kinkel,_Johanna) | http://musescore.com/user/27638568/scores/6128281 |
| 135 | 艺术歌曲 | Johannes Brahms | 2 Gesänge, Op.91 - Gestillte Sehnsucht | 2 Gesänge, Op.91 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Vinckenbosch from IMSLP #92962. Source: https://imslp.org/wiki/2_Ges%C3%A4nge%2C_Op.91_(Brahms%2C_Johannes) | http://musescore.com/user/27638568/scores/6302395 |
| 136 | 艺术歌曲 | Johannes Brahms | 4 Gesänge, Op.46 - Die Kränze | 4 Gesänge, Op.46 | 4.0 | MuseScore 4.5.2 | — | — | http://musescore.com/openscore-lieder-corpus/scores/5084888 |
| 137 | 艺术歌曲 | Joseph Barnby | The Beggar Maid | The Beggar Maid | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #183800. Source: https://imslp.org/wiki/Special:ReverseLookup/183800 | http://musescore.com/user/27638568/scores/6478624 |
| 138 | 艺术歌曲 | Joseph Barnby | To England | To England | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #542017. Source: https://imslp.org/wiki/Special:ReverseLookup/542017 | http://musescore.com/user/27638568/scores/6479829 |
| 139 | 艺术歌曲 | Joseph Haydn | 10 Canzonets - Despair, Hob.XXVIa - 28 | 10 Canzonets | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #292750. Source: https://imslp.org/wiki/Special:ReverseLookup/292750 | http://musescore.comhttps://musescore.com/user/27638568/scores/6454673 |
| 140 | 艺术歌曲 | Joseph Haydn | 10 Canzonets - Fidelity, Hob.XXVIa - 30 | 10 Canzonets | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #292750. Source: https://imslp.org/wiki/Special:ReverseLookup/292750 | http://musescore.com/user/27638568/scores/6454809 |
| 141 | 艺术歌曲 | Josephine Lang | 2 Lieder, Op.28 - Traumbild | 2 Lieder, Op.28 | 4.0 | MuseScore 4.5.2 | — | Transcribed by ashmoggs from IMSLP #616432 & #616434. Source: https://imslp.org/wiki/2_Lieder,_Op.28_(Lang,_Josephine) | http://musescore.com/user/27638568/scores/6012375 |
| 142 | 艺术歌曲 | Jules Massenet | Poème pastoral - Chœur des Pastorale, DO.287 | Poème pastoral | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/78128 | https://github.com/OpenScore/Lieder |
| 143 | 艺术歌曲 | Laura Netzel | 3 Lieder, Op.44 - Lied | 3 Lieder, Op.44 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #434411. Source: https://imslp.org/wiki/Special:ReverseLookup/434411 | http://musescore.com/user/27638568/scores/6660019 |
| 144 | 艺术歌曲 | Lili Boulanger | Attente | Attente | 4.0 | MuseScore 4.5.2 | — | Transcribed by MarkPearse from IMSLP #435483. Source: https://imslp.org/wiki/Attente_(Boulanger%2C_Lili) | https://github.com/OpenScore/Lieder |
| 145 | 艺术歌曲 | Lili Boulanger | Clairières dans le ciel - Elle était descendue au bas de la prairie | Clairières dans le ciel | 4.0 | MuseScore 4.5.2 | — | Transcribed by MarkPearse from IMSLP #25057. Source: https://imslp.org/wiki/Clairières_dans_le_ciel_(Boulanger,_Lili) | http://musescore.com/user/27638568/scores/5852737 |
| 146 | 艺术歌曲 | Liliʻuokalani | Aloha Oe | Aloha Oe | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #26121. Source: https://imslp.org/wiki/Special:ReverseLookup/26121 | http://musescore.com/user/27638568/scores/6650166 |
| 147 | 艺术歌曲 | Liza Lehmann | 2 Seal Songs - The Mother Seal’s Lullaby | 2 Seal Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #626778. Source: https://imslp.org/wiki/Special:ReverseLookup/626778 | http://musescore.com/user/27638568/scores/6573515 |
| 148 | 艺术歌曲 | Louisa Gray | After so long | After so long | 4.0 | MuseScore 4.5.2 | — | Transcribed by deadbeat-s from IMSLP #676303. Source: https://imslp.org/wiki/Special:ReverseLookup/676303 | http://musescore.com/user/27638568/scores/6617407 |
| 149 | 艺术歌曲 | Louisa Gray | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the - He doesn’t love me | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #286659. Source: https://imslp.org/wiki/Special:ReverseLookup/286659 | http://musescore.com/user/27638568/scores/6617779 |
| 150 | 艺术歌曲 | Louise Farrenc | Le berger fidèle | Le berger fidèle | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #511756. Source: https://imslp.org/wiki/Special:ReverseLookup/511756 | http://musescore.com/scores/farrenc-louise/le-berger-fidele-660500950805874 |
| 151 | 艺术歌曲 | Louise Reichardt | 12 Deutsche und Italiänische Romantische Gesänge - Frühlingslied | 12 Deutsche und Italiänische Romantische Gesänge | 4.0 | MuseScore 4.5.2 | — | — | https://musescore.com/openscore-lieder-corpus/scores/5067312 |
| 152 | 艺术歌曲 | Loïsa Puget | Adieu, cousine | Adieu, cousine | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #602409. Source: https://imslp.org/wiki/Special:ReverseLookup/602409 | http://musescore.com/user/27638568/scores/6666995 |
| 153 | 艺术歌曲 | Ludwig van Beethoven | 6 Lieder, Op.48 - Bitten | 6 Lieder, Op.48 | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #26415. | http://musescore.com/user/27638568/scores/5115311 |
| 154 | 艺术歌曲 | Ludwig van Beethoven | 8 Lieder, Op.52 - Urians Reise um die Welt | 8 Lieder, Op.52 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #47274. Source: https://imslp.org/wiki/Special:ReverseLookup/47274 | http://musescore.comhttps://musescore.com/user/27638568/scores/6488630 |
| 155 | 艺术歌曲 | Luise Adolpha Le Beau | 2 Duette, Op.6 - Frühlingsanfang | 2 Duette, Op.6 | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #581957. Source: https://imslp.org/wiki/2_Duette,_Op.6_(Le_Beau,_Luise_Adolpha) | http://musescore.com/user/27638568/scores/5883528 |
| 156 | 艺术歌曲 | Luise Greger | 3 Lieder, Opp.122-124 - Dein, Op.122 | 3 Lieder, Opp.122-124 | 4.0 | MuseScore 4.5.2 | — | Transcribed by Ads20000 from IMSLP #625109. Source: https://imslp.org/wiki/3_Lieder,_Opp.122-124_(Greger,_Luise) | http://musescore.com/user/27638568/scores/6173951 |
| 157 | 艺术歌曲 | Luise Greger | Lieder, Op.125 - Auf den Schwingen der Nacht | Lieder, Op.125 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #625315. Source: https://imslp.org/wiki/Lieder,_Op.125_(Greger,_Luise) | http://musescore.com/user/27638568/scores/6171447 |
| 158 | 艺术歌曲 | Maria Lindsay | Far Away | Far Away | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #661318. Source: https://imslp.org/wiki/Special:ReverseLookup/661318 | http://musescore.com/user/27638568/scores/6609408 |
| 159 | 艺术歌曲 | Maria Theresia von Paradis | 12 Lieder, 1786 (alternative title - Zwölf Lieder auf ihrer Reise in - An das Klavier | 12 Lieder, 1786 (alternative title: Zwölf Lieder auf ihrer Reise in Musik gesetzt) | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #256073. Source: https://imslp.org/wiki/12_Lieder_auf_ihrer_Reise_in_Musik_gesetzt_(Paradis%2C_Maria_Theresia_von) | http://musescore.com/user/27638568/scores/5842033 |
| 160 | 艺术歌曲 | Marie Jaëll | 4 Mélodies - A toi | 4 Mélodies | 4.0 | MuseScore 4.5.2 | — | Transcribed by Eloge from IMSLP #511349. Source: https://imslp.org/wiki/4_M%C3%A9lodies_(Ja%C3%ABll,_Marie) | http://musescore.com/user/27638568/scores/5834392 |
| 161 | 艺术歌曲 | Mathilde Kralik | Blumenlieder - Maiglöckchen | Blumenlieder | 4.0 | MuseScore 4.5.2 | — | Transcribed by DanielR from IMSLP #621212. Source: https://imslp.org/wiki/Blumenlieder_(Kralik,_Mathilde) | http://musescore.com/user/27638568/scores/6165152 |
| 162 | 艺术歌曲 | Maude Valerie White | 3 Little Songs - When the Swallows Homeward Fly | 3 Little Songs | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #629930. Source:https://imslp.org/wiki/3_Little_Songs_(White,_Maude_Valérie) | http://musescore.com/user/27638568/scores/6202466 |
| 163 | 艺术歌曲 | Mélanie Bonis | Allons prier! - Allons prier! Hymne à Marie | Allons prier! | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #654022 : https://imslp.org/wiki/Allons_prier_(Bonis%2C_Mel) | http://musescore.com/user/27638568/scores/6635424 |
| 164 | 艺术歌曲 | Mélanie Bonis | Le chat sur le toit - Le chat sur le toit, 1912 | Le chat sur le toit | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #262191. Source: https://imslp.org/wiki/Special:ReverseLookup/262191 | http://musescore.com/user/27638568/scores/6635391 |
| 165 | 艺术歌曲 | Pauline Duchambge | Guitare | Guitare | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #515921. Source: https://imslp.org/wiki/Special:ReverseLookup/515921 | http://musescore.com/user/27638568/scores/6592539 |
| 166 | 艺术歌曲 | Pauline Duchambge | Le matelot | Le matelot | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #510573. Source: https://imslp.org/wiki/Special:ReverseLookup/510573 | http://musescore.com/user/27638568/scores/6592662 |
| 167 | 艺术歌曲 | Pauline Viardot | 6 Mélodies, VWV 1133-1137 - 1176 - À la Fontaine, VWV 1133 | 6 Mélodies, VWV 1133-1137/1176 | 4.0 | MuseScore 4.5.2 | — | Transcribed by fredipi from IMSLP #580246. Source: https://imslp.org/wiki/6_M%C3%A9lodies%2C_VWV_1133-1137%2F1176_(Viardot%2C_Pauline) | http://musescore.com/user/27638568/scores/5978033 |
| 168 | 艺术歌曲 | Pauline-Marie-Elisa Thys | Petit nègre | Petit nègre | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #517100. Source: https://imslp.org/wiki/Special:ReverseLookup/517100 | http://musescore.com/user/27638568/scores/6670960 |
| 169 | 艺术歌曲 | Peter Cornelius | 6 Lieder, Op.1 - Untreu | 6 Lieder, Op.1 | 4.0 | MuseScore 4.5.2 | — | — | https://musescore.com/score/5054931 |
| 170 | 艺术歌曲 | Peter Cornelius | 6 Lieder, Op.5 - Botschaft | 6 Lieder, Op.5 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #24063. Source: http://imslp.org/wiki/6_Lieder%2C_Op.5_(Cornelius%2C_Peter) | https://github.com/OpenScore/Lieder |
| 171 | 艺术歌曲 | Peter Warlock | Peterisms, Set 1 - Chopcherry | Peterisms, Set 1 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #272293. Source: https://imslp.org/wiki/Peterisms,_Set_1_(Warlock,_Peter) | http://musescore.comhttps://musescore.com/user/27638568/scores/6447286 |
| 172 | 艺术歌曲 | Poldowski | Dans une musette | Dans une musette | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #122258. Source: https://imslp.org/wiki/Special:ReverseLookup/122258 | http://musescore.com/user/27638568/scores/6663305 |
| 173 | 艺术歌曲 | Reynaldo Hahn | 7 Chansons grises - L’Heure exquise | 7 Chansons grises | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/91215 | https://github.com/OpenScore/Lieder |
| 174 | 艺术歌曲 | Reynaldo Hahn | À Chloris | — | 4.0 | MuseScore Studio 4.6.5 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/92334 | https://github.com/OpenScore/Lieder |
| 175 | 艺术歌曲 | Richard Strauss | 4 Lieder, Op. 27 - Morgen | 4 Lieder, Op. 27 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP# 135548. Source: https://imslp.org/wiki/4_Lieder,_Op.27_(Strauss,_Richard) | http://musescore.com/user/27638568/scores/6199578 |
| 176 | 艺术歌曲 | Richard Strauss | 4 Lieder, Op. 27 - Ruhe, meine Seele! | 4 Lieder, Op. 27 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP# 135548. Source: https://imslp.org/wiki/4_Lieder,_Op.27_(Strauss,_Richard) | http://musescore.com/user/27638568/scores/6183554 |
| 177 | 艺术歌曲 | Richard Wagner | 5 Gedichte für eine Frauenstimme (Wesendonck-Lieder) - Der Engel | 5 Gedichte für eine Frauenstimme (Wesendonck-Lieder) | 4.0 | MuseScore 4.5.2 | — | — | http://musescore.com/user/27638568/scores/5026068 |
| 178 | 艺术歌曲 | Robert Franz | 12 Gesänge, Op.1 - Ihr Auge | 12 Gesänge, Op.1 | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #88709. Source: https://imslp.org/wiki/12_Ges%C3%A4nge%2C_Op.1_(Franz%2C_Robert) | http://musescore.com/user/27638568/scores/5660573 |
| 179 | 艺术歌曲 | Robert Franz | 6 Gesänge, Op.10 - Für Musik | 6 Gesänge, Op.10 | 4.0 | MuseScore 4.5.2 | — | Transcribed by mooing from IMSLP #96278. Source: https://imslp.org/wiki/Special:ReverseLookup/96278 | http://musescore.com/user/27638568/scores/6806626 |
| 180 | 艺术歌曲 | Robert Schumann | 5 Lieder und Gesänge, Op.127 - Sängers Trost | 5 Lieder und Gesänge, Op.127 | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #271937. Source: https://imslp.org/wiki/Special:ReverseLookup/271937 | http://musescore.com/user/27638568/scores/6826352 |
| 181 | 艺术歌曲 | Roger Quilter | 3 Shakespeare Songs, Op.6 - Come Away, Death | 3 Shakespeare Songs, Op.6 | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/444590 | https://github.com/OpenScore/Lieder |
| 182 | 艺术歌曲 | Ruggero Leoncavallo | Mattinata | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/482691 | https://github.com/OpenScore/Lieder |
| 183 | 艺术歌曲 | Samuel Coleridge-Taylor | 6 Sorrow Songs, Op.57 - Oh what comes over the Sea | 6 Sorrow Songs, Op.57 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #26882. Source: https://imslp.org/wiki/Serres_chaudes,_Op.24_(Chausson,_Ernest) | http://musescore.com/user/27638568/scores/6189652 |
| 184 | 艺术歌曲 | Samuel Coleridge-Taylor | 6 Sorrow Songs, Op.57 - When I am dead, my dearest | 6 Sorrow Songs, Op.57 | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #26882. Source: https://imslp.org/wiki/Serres_chaudes,_Op.24_(Chausson,_Ernest) | http://musescore.com/user/27638568/scores/6189644 |
| 185 | 艺术歌曲 | Samuel Coleridge-Taylor | Oh, the Summer | Oh, the Summer | 4.0 | MuseScore 4.5.2 | — | Transcribed by pental from IMSLP #606188 Source: https://imslp.org/wiki/Oh,_the_Summer_(Coleridge-Taylor,_Samuel) | http://musescore.com/user/27638568/scores/6232117 |
| 186 | 艺术歌曲 | Scott Joplin | Please Say You Will | — | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #14477. Source: https://imslp.org/wiki/Please_Say_You_Will_(Joplin%2C_Scott) | http://musescore.com/user/27638568/scores/6304288 |
| 187 | 艺术歌曲 | Sir Harold Boulton, 2nd Baronet | 12 New Songs by some of the best and best-known British composers - Cradle Song | 12 New Songs by some of the best and best-known British composers | 4.0 | MuseScore 4.5.2 | — | Transcribed by markp earse from IMSLP #285334. Source: https://imslp.org/wiki/12_New_Songs_(Boulton,_Harold) | http://musescore.com/user/27638568/scores/6403758 |
| 188 | 艺术歌曲 | Sir Harold Boulton, 2nd Baronet | 12 New Songs by some of the best and best-known British composers - In Summer Weather | 12 New Songs by some of the best and best-known British composers | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #285334. Source: https://imslp.org/wiki/12_New_Songs_(Boulton,_Harold) | http://musescore.com/user/27638568/scores/6405467 |
| 189 | 艺术歌曲 | Sir Harold Boulton, 2nd Baronet | 12 New Songs by some of the best and best-known British composers - Love's Journey | 12 New Songs by some of the best and best-known British composers | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #285334. Source: https://imslp.org/wiki/12_New_Songs_(Boulton,_Harold) | http://musescore.com/user/27638568/scores/6404150 |
| 190 | 艺术歌曲 | Sir Harold Boulton, 2nd Baronet | 12 New Songs by some of the best and best-known British composers - Truant Wings | 12 New Songs by some of the best and best-known British composers | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #285334. Source: https://imslp.org/wiki/12_New_Songs_(Boulton,_Harold) | http://musescore.com/user/27638568/scores/6404394 |
| 191 | 艺术歌曲 | Sophie Gail | Le serment | Le serment | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #173063. Source: https://imslp.org/wiki/Special:ReverseLookup/173063 | http://musescore.com/user/27638568/scores/6604249 |
| 192 | 艺术歌曲 | Sophie Gail | Les langueurs | Les langueurs | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #173062. Source: https://imslp.org/wiki/Special:ReverseLookup/173062 | http://musescore.com/user/27638568/scores/6604179 |
| 193 | 艺术歌曲 | Stefano Donaudy | 36 Arie di Stile Antico - Spirate pur, spirate | 36 Arie di Stile Antico | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/857572 | https://github.com/OpenScore/Lieder |
| 194 | 艺术歌曲 | Thomas Arne | A Favorite Glee | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/26747 | https://github.com/OpenScore/Lieder |
| 195 | 艺术歌曲 | Thomas Arne | Blow, Blow, Thou Winter Wind | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/184189 | https://musescore.com/user/27638568/scores/8835588 |
| 196 | 艺术歌曲 | Virginia Gabriel | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the - Alone | Modern Ballads (A Selection of 50 Favourite Songs and Ballads by the Most Eminent Composers) | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #286579. Source: https://imslp.org/wiki/Special:ReverseLookup/286579 | http://musescore.com/user/27638568/scores/6601231 |
| 197 | 艺术歌曲 | Virginia Gabriel | Only | Only | 4.0 | MuseScore 4.5.2 | — | Transcribed from IMSLP #300723. Source: https://imslp.org/wiki/Special:ReverseLookup/300723 | http://musescore.com/user/27638568/scores/6603244 |
| 198 | 艺术歌曲 | Walford Davies | 8 New Nursery Rhymes, Op.23 - Old Woman | 8 New Nursery Rhymes, Op.23 | 4.0 | MuseScore 4.5.2 | — | Transcribed by ashmoggs from IMSLP #333826. Source: https://imslp.org/wiki/8_New_Nursery_Rhymes,_Op.23_(Davies,_Walford) | http://musescore.com/user/27638568/scores/6218722 |
| 199 | 艺术歌曲 | Walford Davies | 8 New Nursery Rhymes, Op.23 - The Apology | 8 New Nursery Rhymes, Op.23 | 4.0 | MuseScore 4.5.2 | — | Transcribed by ashmoggs from IMSLP #333826. Source: https://imslp.org/wiki/8_New_Nursery_Rhymes,_Op.23_(Davies,_Walford) | http://musescore.com/user/27638568/scores/6215563 |
| 200 | 艺术歌曲 | Walter Parratt | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 - For all the wonder of thy regal day | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 | 4.0 | MuseScore 4.5.2 | — | Series editor of original edition: Sir Walter Parratt. Transcribed from IMSLP #584347. Source: https://imslp.org/wiki/Special:ReverseLookup/584347 | http://musescore.com/user/27638568/scores/6683117 |
| 201 | 艺术歌曲 | Walter Parratt | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 - Hark! The world is full of thy praise | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 | 4.0 | MuseScore 4.5.2 | — | Series editor of original edition: Sir Walter Parratt. Transcribed from IMSLP #584347. Source: https://imslp.org/wiki/Special:ReverseLookup/584347 | http://musescore.com/user/27638568/scores/6682890 |
| 202 | 艺术歌曲 | Walter Parratt | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 - Out in the windy West | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 | 4.0 | MuseScore 4.5.2 | — | Series editor of original edition: Sir Walter Parratt. Transcribed from IMSLP #584347. Source: https://imslp.org/wiki/Special:ReverseLookup/584347 | http://musescore.com/user/27638568/scores/6681689 |
| 203 | 艺术歌曲 | Walter Parratt | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 - The seaboards are her mantle’s hem | “Choral Songs in honour of Her Majesty Queen Victoria”, 1899 | 4.0 | MuseScore 4.5.2 | — | Series editor of original edition: Sir Walter Parratt. Transcribed from IMSLP #584347. Source: https://imslp.org/wiki/Special:ReverseLookup/584347 | http://musescore.com/user/27638568/scores/6683352 |
| 204 | 艺术歌曲 | William Shield | The Maid of Lodi | The Maid of Lodi | 4.0 | MuseScore 4.5.2 | — | Transcribed by markpearse from IMSLP #516852. Source: https://imslp.org/wiki/The_Maid_of_Lodi_(Shield,_William) | http://musescore.com/user/27638568/scores/6445119 |
| 205 | 艺术歌曲 | Émile Paladilhe | Les roses d’Ispahan | — | 4.0 | MuseScore Studio 4.6.3 | — | Transcribed from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/371934 | https://github.com/OpenScore/Lieder |

---

### 字段说明

- **曲名（文件名）**：文件名的曲名部分。命名规则与 App 显示口径对齐 ——
  MuseScore 导出里 `<work-title>` 是**曲集名**、`<movement-title>` 是**单曲名**，而 `MusicXMLParser` 取 `<work-title>` 作 `score.title`。
  因此：曲集 ≠ 单曲时命名为「`曲集 - 单曲`」，否则直接用该标题本身。
- **界面标题**：App 标题栏实际显示的内容（即 `<work-title>`）。
- `规模`：解析器读出的 声部数 / 小节数 / 音符数，用于确认谱面被完整解析。
- `公共版权起算年`：按「作曲家卒年 + 70 年，次年起算」估算，实际以目标司法管辖区为准。
- 机读版本：`catalog.csv`（含全部字段，UTF-8-BOM，Excel 可直接打开）、`catalog.json`（另含 `collection`＝来源曲集目录、`movement`＝单曲名等明细）。
