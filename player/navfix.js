/*!
 * navfix.js —— 补全 alphaTab 1.9.0 从 MusicXML 导入时缺失的「跳转停在哪里」语义。
 *
 * 背景（MusicXML 规范）：
 *   <sound dalsegno="segno"/>  表示「从这里跳回 Segno」；
 *   <sound dacapo="yes"/>      表示「从这里跳回开头」；
 *   而「跳回去以后在哪儿收住」由**独立的**标记决定：
 *   <sound fine="yes"/> 是乐章最后一个音；<sound tocoda="coda"/> 是「去 Coda」点，<sound coda="coda"/> 是 Coda 段起点。
 *
 * 问题：alphaTab 1.9.0 的 MusicXML 导入器只按属性本身记录「裸跳转」
 *   （JumpDalSegno / JumpDaCapo / JumpDalSegnoSegno），不回看整谱是否存在 Fine / Coda 标记，
 *   于是播放时跳回去会一路播到曲末，而不是在 Fine（或 To Coda）处结束。
 *
 * 修法：scoreLoaded 之后按整谱标记把裸跳转升级为对应变体，再让 alphaTab 重新生成 MIDI。
 *   JumpDalSegno       (9)  -> JumpDalSegnoAlFine       (12) / JumpDalSegnoAlCoda       (10)
 *   JumpDaCapo         (5)  -> JumpDaCapoAlFine         (8)  / JumpDaCapoAlCoda         (6)
 *   JumpDalSegnoSegno  (13) -> JumpDalSegnoSegnoAlFine  (16) / JumpDalSegnoSegnoAlCoda  (14)
 * 括号里是 alphaTab 的 Direction 数值（TargetFine=0 / TargetSegno=1 / TargetCoda=3 /
 * JumpDaCoda=17 等）。
 *
 * 判定优先级：谱面存在 Fine 就按 al Fine（Fine 是「乐章收尾」语义，最明确）；
 * 否则若同时存在 To Coda(17) 与 Coda(3) 标记，按 al Coda。
 * 两者都没有时保持原样（裸跳转 = 跳回去一直播到曲末，符合规范）。
 */
(function () {
  "use strict";

  var TARGET_FINE = 0;
  var TARGET_CODA = 3;
  var JUMP_DA_CODA = 17;

  // [裸跳转, al Fine, al Coda]
  var UPGRADES = [
    [9, 12, 10],   // D.S.      -> D.S. al Fine / al Coda
    [5, 8, 6],     // D.C.      -> D.C. al Fine / al Coda
    [13, 16, 14]   // D.S.S.    -> D.S.S. al Fine / al Coda
  ];

  function hasDirection(score, value) {
    var bars = score.masterBars;
    for (var i = 0; i < bars.length; i++) {
      var d = bars[i].directions;
      if (d && d.size > 0 && d.has(value)) return true;
    }
    return false;
  }

  /** 就地把裸跳转升级为带停止点的变体，返回改动的条数（幂等：重复调用不会再次升级）。 */
  function upgrade(score) {
    if (!score || !score.masterBars || !score.masterBars.length) return 0;

    var hasFine = hasDirection(score, TARGET_FINE);
    var hasCoda = hasDirection(score, JUMP_DA_CODA) && hasDirection(score, TARGET_CODA);
    if (!hasFine && !hasCoda) return 0;

    var changed = 0;
    var bars = score.masterBars;
    for (var i = 0; i < bars.length; i++) {
      var d = bars[i].directions;
      if (!d || d.size === 0) continue;
      for (var k = 0; k < UPGRADES.length; k++) {
        var rule = UPGRADES[k];
        if (!d.has(rule[0])) continue;
        d["delete"](rule[0]);
        d.add(hasFine ? rule[1] : rule[2]);
        changed++;
      }
    }
    return changed;
  }

  /**
   * 对已载入的 api 应用修正。
   * @returns {number} 升级的跳转条数（0 = 无需修正）
   */
  function apply(api) {
    try {
      if (!api || !api.score) return 0;
      var changed = upgrade(api.score);
      // 谱面模型改了以后必须让 alphaTab 重新生成 MIDI 与 tick 缓存，跳转才会真正进入播放流。
      if (changed > 0 && typeof api.loadMidiForScore === "function") api.loadMidiForScore();
      return changed;
    } catch (e) {
      if (window.console && console.warn) console.warn("[navfix] 跳转修正失败：", e);
      return 0;
    }
  }

  window.ScoreNavFix = { apply: apply, upgrade: upgrade };
})();
