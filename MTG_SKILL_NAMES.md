# Approved MTG Skill Names — v0.34 (2026-10-29)

**19 confirmed skills (17 distinct MTG names; the 3 Tempered Steel variants share one title).** Names are independent of original card mechanics. Stable Skill IDs, existing costs and levels are unchanged, except `suppressive-fire` whose previously provisional effect was explicitly finalized in this version. Original cards are linked and card artwork can be viewed on Scryfall; the inline images below are referenced from the public Scryfall image endpoint, not copied into this repository.

| Skill ID | Current name / MTG card image | Skill effect | Source card's original effect (brief) |
| --- | --- | --- | --- |
| `frame-light` | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel)** (light)<br>![Tempered Steel MTG card](https://api.scryfall.com/cards/som/24?format=image&version=small) | Light搭乗時 SHOOTING・MELEE +1/+2/+3 | アーティファクト・クリーチャー全体+2/+2 |
| `frame-standard` | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel)** (standard)<br>![Tempered Steel MTG card](https://api.scryfall.com/cards/som/24?format=image&version=small) | Standard搭乗時 SHOOTING・MELEE +1/+2/+3 | 同上 |
| `frame-heavy` | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel)** (heavy)<br>![Tempered Steel MTG card](https://api.scryfall.com/cards/som/24?format=image&version=small) | Heavy搭乗時 SHOOTING・MELEE +1/+2/+3 | 同上 |
| `marksmanship` | **[Iron Verdict](https://scryfall.com/card/khm/17/iron-verdict)**<br>![Iron Verdict MTG card](https://api.scryfall.com/cards/khm/17?format=image&version=small) | 通常MOVE前の対Unit射撃で SHOOTING +2/+4/+6 | タップ状態のクリーチャーに5ダメージ、予顕 |
| `mobile-evasion` | **[Escape Velocity](https://scryfall.com/card/thb/132/escape-velocity)**<br>![Escape Velocity MTG card](https://api.scryfall.com/cards/thb/132?format=image&version=small) | 通常MOVEで3Hex以上移動すると REFLEX +2/+4/+6 | 速攻と攻撃修整を付与、脱出可能 |
| `momentum-melee` | **[Through the Breach](https://scryfall.com/card/chk/193/through-the-breach)**<br>![Through the Breach MTG card](https://api.scryfall.com/cards/chk/193?format=image&version=small) | 3Hex以上通常MOVE後の白兵で MELEE +2/+4/+6 | 手札のクリーチャーを一時的に速攻で戦場へ出す |
| `guardian-reaction` | **[Shielded Passage](https://scryfall.com/card/gtc/24/shielded-passage)**<br>![Shielded Passage MTG card](https://api.scryfall.com/cards/gtc/24?format=image&version=small) | 味方のCOVER／ミサイル迎撃時 REFLEX +3/+6/+9 | クリーチャーへの次のダメージを軽減 |
| `brace-discipline` | **[Decisive Denial](https://scryfall.com/card/stx/382/decisive-denial)**<br>![Decisive Denial MTG card](https://api.scryfall.com/cards/stx/382?format=image&version=small) | BRACEのArmor追加+1/+2/+3、最終1ダメージを0に | クリーチャー間の格闘か、相手の呪文の打ち消しを選択 |
| `conceal-discipline` | **[Moment of Silence](https://scryfall.com/card/mmq/28/moment-of-silence)**<br>![Moment of Silence MTG card](https://api.scryfall.com/cards/mmq/28?format=image&version=small) | CONCEAL時Signature低下（暫定−2/−3/−4）、自機センサー停止 | 相手の次の戦闘フェイズを飛ばす |
| `fired-up` | **[Repercussion](https://scryfall.com/card/uds/95/repercussion)**<br>![Repercussion MTG card](https://api.scryfall.com/cards/uds/95?format=image&version=small) | 敵の攻撃でHitを受けた次のActivation、SHOOTING・MELEE +6/+9/+12 | クリーチャーが受けたダメージをそのコントローラーにも与える |
| `observation-discipline` | **[Stillness in Motion](https://scryfall.com/card/tdm/334/stillness-in-motion)**<br>![Stillness in Motion MTG card](https://api.scryfall.com/cards/tdm/334?format=image&version=small) | 通常MOVEせずActivation終了で次の自Activationまで INSIGHT +4/+8/+12 | クリーチャーに関わる能力を備えたエンチャント |
| `scan-interpretation` | **[Confront the Unknown](https://scryfall.com/card/soi/198/confront-the-unknown)**<br>![Confront the Unknown MTG card](https://api.scryfall.com/cards/soi/198?format=image&version=small) | ACTIVE SCAN中だけ INSIGHT +4/+8/+12 | 調査を行い、手掛かり数に応じてクリーチャーを強化 |
| `solo-operator` | **[Audacity](https://scryfall.com/card/bro/169/audacity)**<br>![Audacity MTG card](https://api.scryfall.com/cards/bro/169?format=image&version=small) | 味方が4Hex以内にいないとき基礎INSIGHT依存でSHOOTING上昇 | クリーチャーに+2/+0とトランプル、死亡時ドロー |
| `pick-your-ground` | **[Dead of Winter](https://scryfall.com/card/mh1/85/dead-of-winter)**<br>![Dead of Winter MTG card](https://api.scryfall.com/cards/mh1/85?format=image&version=small) | 森林・瓦礫・掩体などの地形防御を追加−5/−10/−15pt | 氷雪パーマネント数に応じて非氷雪クリーチャー全体を弱体化 |
| `fault-line` | **[Fault Line](https://scryfall.com/card/usg/185/fault-line)**<br>![Fault Line MTG card](https://api.scryfall.com/cards/usg/185?format=image&version=small) | CritPen成功直後から対象Armor −2/−4/−6（同Attack後続Hitにも適用） | 地上クリーチャーと各プレイヤーへXダメージ |
| `survival-cache` | **[Survival Cache](https://scryfall.com/card/roe/44/survival-cache)**<br>![Survival Cache MTG card](https://api.scryfall.com/cards/roe/44?format=image&version=small) | Repair Kitの回復量8HPを12/16/20HPへ強化 | 2点回復、条件付きドロー、反復 |
| `suppressive-fire` | **[Shadow of Doubt](https://scryfall.com/card/rav/253/shadow-of-doubt)**<br>![Shadow of Doubt MTG card](https://api.scryfall.com/cards/rav/253?format=image&version=small) | 通常Direct FIREで全Hit外すと敵REFLEX −2/−4/−6（当該Faction Phaseまで） | プレイヤーのライブラリー探索を禁止しカードを引く |
| `last-stand-ability` | **[Brink of Disaster](https://scryfall.com/card/wwk/52/brink-of-disaster)**<br>![Brink of Disaster MTG card](https://api.scryfall.com/cards/wwk/52?format=image&version=small) | HP50%以下でREFLEX = +1 + floor(基礎INSIGHT×Lv/6)（低HP中持続） | エンチャントされたクリーチャー／土地がタップされるとそれを破壊 |
| `lethal-endurance` | **[Against All Odds](https://scryfall.com/card/one/1/against-all-odds)**<br>![Against All Odds MTG card](https://api.scryfall.com/cards/one/1?format=image&version=small) | Lv別Attack開始HP条件で致命的AttackをHP1で耐える（回数制限なし、同一Attack全Hit保証） | 小型のアーティファクト／クリーチャーを墓地から復帰、またはパーマネントを一時追放して戻す |

## Unassigned / candidate names

- **Last Word**: formerly used for stationary-fire skill; not currently assigned.
- **Cost of Brilliance**: promising future title, deliberately unassigned.
- **Against All Odds**: reassigned from the former solo-skill use to the confirmed `lethal-endurance` survival skill (v0.34). The previously provisional **Against the Odds** (`against-the-odds`, low-accuracy CritPen) was **archived in v0.35**, resolving the near-duplicate names.

## v0.31 approved changes

| Stable ID | Previous title | Current title |
| --- | --- | --- |
| `guardian-reaction` | No One Left Behind | Shielded Passage |
| `brace-discipline` | Built to Last | Decisive Denial |
| `observation-discipline` | Standstill | Stillness in Motion |
| `solo-operator` | Against All Odds | Audacity |
| `scan-interpretation` | See Beyond | Confront the Unknown |
| `suppressive-fire` | 牽制射撃（仮） | Shadow of Doubt（設計確定） |

**Repercussion remains unchanged.** Labels: `コマンド強化` for COVER/BRACE/CONCEAL/ACTIVE SCAN skills, `位置・地形` for terrain and separation/position skills, and `装備・消耗品` for the Repair Kit skill. Historical documents retain prior names when describing past releases.

## v0.34 — survival skills and archive update (2026-10-29)

- Confirmed **Brink of Disaster** for `last-stand-ability`: HP≤50%, base INSIGHT–dependent REFLEX bonus.
- Confirmed **Against All Odds** for `lethal-endurance`: HP1 survival when Attack-start HP qualifies, without an artificial per-mission limit.
- No other confirmed skill names changed. The five archived candidates First Watch, Steady Nerves, Stay Frosty, Right on Cue and 据置精密貫徹 are no longer active. Main Core not modified.

## v0.35 — archived near-duplicate title (2026-10-29)

- Archived **Against the Odds** (`against-the-odds`) due to the undesired incentive to reduce hit chance. It is no longer an active skill.
- Confirmed **Against All Odds** (`lethal-endurance`) remains the sole active skill using this phrase. The 19 confirmed names and MTG card references did not change.
