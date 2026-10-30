# Approved MTG Skill Names — v0.44 (2026-10-31)

**24 confirmed skills (22 distinct MTG names; the 3 Tempered Steel variants share one title).** Names are independent of original card mechanics. Decisive Denial (`brace-discipline`) now absorbs Shielded Passage's former protective role, while Shielded Passage (`guardian-reaction`) is archived and its previous acquisition points are refunded. All other confirmed IDs, including Figure of Destiny, Seize Opportunity and Iron Verdict, remain unchanged. Original cards are linked and card artwork can be viewed on Scryfall; the inline images below are referenced from the public Scryfall image endpoint, not copied into this repository.

| Skill ID | Current name / MTG card image | Skill effect | Source card's original effect (brief) |
| --- | --- | --- | --- |
| `frame-light` | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel)** (light)<br>![Tempered Steel MTG card](https://api.scryfall.com/cards/som/24?format=image&version=small) | Light搭乗時 SHOOTING・MELEE +1/+2/+3 | アーティファクト・クリーチャー全体+2/+2 |
| `frame-standard` | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel)** (standard)<br>![Tempered Steel MTG card](https://api.scryfall.com/cards/som/24?format=image&version=small) | Standard搭乗時 SHOOTING・MELEE +1/+2/+3 | 同上 |
| `frame-heavy` | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel)** (heavy)<br>![Tempered Steel MTG card](https://api.scryfall.com/cards/som/24?format=image&version=small) | Heavy搭乗時 SHOOTING・MELEE +1/+2/+3 | 同上 |
| `final-fortune` | **[Glimmer of Genius](https://scryfall.com/card/kld/49/glimmer-of-genius)**<br>![Glimmer of Genius MTG card](https://api.scryfall.com/cards/kld/49?format=image&version=small) | 各自軍Faction Phase開始時50%抽選。好調SHOOTING・MELEE +4/+5/+6、不調REFLEX −6/−5/−4（旧Final Fortuneと効果同一） | エネルギー2個を得てカードを2枚引く |
| `kill-momentum-growth` | **[Figure of Destiny](https://scryfall.com/card/eve/139/figure-of-destiny)**<br>![Figure of Destiny MTG card](https://api.scryfall.com/cards/eve/139?format=image&version=small) | 本人による敵撃破1体ごとにSHOOTING・MELEE各+2。最大累積2/4/6体（最大各+4/+8/+12）、Mission内限定 | 段階的に能力を強化できるクリーチャー。原カードの能力値やコストは移植しない |
| `avoid-fate` | **[Avoid Fate](https://scryfall.com/card/leg/175/avoid-fate)**<br>![Avoid Fate MTG card](https://api.scryfall.com/cards/leg/175?format=image&version=small) | 敵の適格な1Attackを全Hit回避するたびREFLEX +1、最大2/4/6回（最大+2/+4/+6）。Mission内限定、被弾しても維持 | 自分のパーマネントを対象とするインスタントまたはオーラ呪文を打ち消す |
| `marksmanship` | **[Seize Opportunity](https://scryfall.com/card/tdm/119/seize-opportunity)**<br>![Seize Opportunity MTG card](https://api.scryfall.com/cards/tdm/119?format=image&version=small) | 通常MOVE前の対Unit射撃で SHOOTING +2/+4/+6（旧Iron Verdict） | 上2枚を一時使用可能、または最大2体を+2/+1 |
| `sniper-rifle-proficiency` | **[Last Word](https://scryfall.com/card/dst/23/last-word)**<br>![Last Word MTG card](https://api.scryfall.com/cards/dst/23?format=image&version=small) | Sniper Rifleによる適格な射撃中のみ SHOOTING +2/+4/+6 | 打ち消されない呪文で対象の呪文を打ち消す |
| `heavy-rail-proficiency` | **[Iron Verdict](https://scryfall.com/card/khm/17/iron-verdict)**<br>![Iron Verdict MTG card](https://api.scryfall.com/cards/khm/17?format=image&version=small) | Heavy Railでの適格な射撃中だけSHOOTING +2/+4/+6 | タップ状態のクリーチャーへ5ダメージ、予顕あり |
| `mobile-evasion` | **[Escape Velocity](https://scryfall.com/card/thb/132/escape-velocity)**<br>![Escape Velocity MTG card](https://api.scryfall.com/cards/thb/132?format=image&version=small) | 通常MOVEで3Hex以上移動すると REFLEX +2/+4/+6 | 速攻と攻撃修整を付与、脱出可能 |
| `momentum-melee` | **[Collision Course](https://scryfall.com/card/dft/10/collision-course)**<br>![Collision Course MTG card](https://api.scryfall.com/cards/dft/10?format=image&version=small) | 3Hex以上通常MOVE後の白兵で MELEE +2/+4/+6（旧Through the Breach） | 自軍クリーチャー／機体数に応じて対象へダメージ、またはアーティファクト破壊 |
| `assault-lance-proficiency` | **[No Quarter](https://scryfall.com/card/tmp/193/no-quarter)**<br>![No Quarter MTG card](https://api.scryfall.com/cards/tmp/193?format=image&version=small) | Assault Lanceによる適格な白兵中のみ MELEE +2/+4/+6 | パワーの小さいクリーチャーとのブロック戦闘で破壊 |
| `brace-discipline` | **[Decisive Denial](https://scryfall.com/card/stx/382/decisive-denial)**<br>![Decisive Denial MTG card](https://api.scryfall.com/cards/stx/382?format=image&version=small) | 味方への合法なCOVERを実行したAttack中だけ自機Armor +2/+4/+6。REFLEX・Missile Intercept強化なし。Reaction保持だけでは無効 | クリーチャー間の格闘か、相手の呪文の打ち消しを選択 |
| `conceal-discipline` | **[Moment of Silence](https://scryfall.com/card/mmq/28/moment-of-silence)**<br>![Moment of Silence MTG card](https://api.scryfall.com/cards/mmq/28?format=image&version=small) | CONCEAL時Signature低下（暫定−2/−3/−4）、自機センサー停止 | 相手の次の戦闘フェイズを飛ばす |
| `fired-up` | **[Repercussion](https://scryfall.com/card/uds/95/repercussion)**<br>![Repercussion MTG card](https://api.scryfall.com/cards/uds/95?format=image&version=small) | 敵の攻撃でHitを受けた次のActivation、SHOOTING・MELEE +6/+9/+12 | クリーチャーが受けたダメージをそのコントローラーにも与える |
| `scan-interpretation` | **[Confront the Unknown](https://scryfall.com/card/soi/198/confront-the-unknown)**<br>![Confront the Unknown MTG card](https://api.scryfall.com/cards/soi/198?format=image&version=small) | ACTIVE SCAN中だけ INSIGHT +4/+8/+12、scanner Signature合計 +3/+4/+5 | 調査を行い、手掛かり数に応じてクリーチャーを強化 |
| `anti-air-recon` | **[Sight Beyond Sight](https://scryfall.com/card/dtk/75/sight-beyond-sight)**<br>![Sight Beyond Sight MTG card](https://api.scryfall.com/cards/dtk/75?format=image&version=small) | 飛行型敵への自機索敵判定で対象Signature項+1/+2/+3（実値変更なし） | 名前だけを採用。原カードのゲーム効果は移植しない |
| `solo-operator` | **[Audacity](https://scryfall.com/card/bro/169/audacity)**<br>![Audacity MTG card](https://api.scryfall.com/cards/bro/169?format=image&version=small) | 味方が4Hex以内にいないとき基礎INSIGHT依存でSHOOTING上昇 | クリーチャーに+2/+0とトランプル、死亡時ドロー |
| `pick-your-ground` | **[Dead of Winter](https://scryfall.com/card/mh1/85/dead-of-winter)**<br>![Dead of Winter MTG card](https://api.scryfall.com/cards/mh1/85?format=image&version=small) | 森林・瓦礫・掩体などの地形防御を追加−5/−10/−15pt | 氷雪パーマネント数に応じて非氷雪クリーチャー全体を弱体化 |
| `fault-line` | **[Fault Line](https://scryfall.com/card/usg/185/fault-line)**<br>![Fault Line MTG card](https://api.scryfall.com/cards/usg/185?format=image&version=small) | CritPen成功直後から対象Armor −2/−4/−6（同Attack後続Hitにも適用） | 地上クリーチャーと各プレイヤーへXダメージ |
| `survival-cache` | **[Survival Cache](https://scryfall.com/card/roe/44/survival-cache)**<br>![Survival Cache MTG card](https://api.scryfall.com/cards/roe/44?format=image&version=small) | Repair Kitの回復量8HPを12/16/20HPへ強化 | 2点回復、条件付きドロー、反復 |
| `suppressive-fire` | **[Shadow of Doubt](https://scryfall.com/card/rav/253/shadow-of-doubt)**<br>![Shadow of Doubt MTG card](https://api.scryfall.com/cards/rav/253?format=image&version=small) | 通常Direct FIREで全Hit外すと敵REFLEX −2/−4/−6（当該Faction Phaseまで） | プレイヤーのライブラリー探索を禁止しカードを引く |
| `last-stand-ability` | **[Brink of Disaster](https://scryfall.com/card/wwk/52/brink-of-disaster)**<br>![Brink of Disaster MTG card](https://api.scryfall.com/cards/wwk/52?format=image&version=small) | HP50%以下でREFLEX = +1 + floor(基礎INSIGHT×Lv/6)（低HP中持続） | エンチャントされたクリーチャー／土地がタップされるとそれを破壊 |
| `lethal-endurance` | **[Against All Odds](https://scryfall.com/card/one/1/against-all-odds)**<br>![Against All Odds MTG card](https://api.scryfall.com/cards/one/1?format=image&version=small) | Lv別Attack開始HP条件で致命的AttackをHP1で耐える（回数制限なし、同一Attack全Hit保証） | 小型のアーティファクト／クリーチャーを墓地から復帰、またはパーマネントを一時追放して戻す |

## v0.44 — Decisive Denial becomes COVER-only Armor (2026-10-31)

- Keep the approved title and ID `brace-discipline`. Only when a legal COVER Reaction actually redirects an enemy Attack from a nearby ally does this Skill grant its user's Armor **+2/+4/+6** at Lv1/2/3 for the entirety of that Attack. CritPen still ignores Armor; standard minimum 1 Damage remains.
- No REFLEX bonus, no ordinary self-defense bonus from an AVAILABLE Reaction, and no bonus to Missile Intercept, BRACE or ordinary INTERCEPT. Existing legal single-target missile Attacks may still be COVERed, which is distinct from intercepting the missile.
- Historic v0.42 and Shielded Passage records stay intact. 24 confirmed / 8 provisional / 12 archived, with unchanged storage ID, purchased levels and Core.

## v0.43 — New Avoid Fate; rename Glimmer of Genius (2026-10-31)

- **Avoid Fate** [LEG #175](https://scryfall.com/card/leg/175/avoid-fate), new confirmed ID `avoid-fate`: after an eligible enemy Attack aimed at this pilot ends with every Hit Attempt missing, add +1 effective REFLEX (one per Attack, not per Hit). Lv1/2/3 caps +2/+4/+6; persists despite damage until Mission end, then resets. Avoid Fate is conceptually paired with Figure of Destiny but has an independent stable ID.
- Existing Final Fortune is renamed **Glimmer of Genius** [KLD #49](https://scryfall.com/card/kld/49/glimmer-of-genius). Keep the established `final-fortune` ID, each friendly Faction Phase's 50/50 good/bad roll, and all Lv stats unchanged. Historical v0.38 records retain their original name.
- **24 confirmed skills, 22 distinct MTG titles** (3 Tempered Steel variants share a title). 8 provisional, 12 archived. No production Core changes or saved-build migration.

## v0.42 — Decisive Denial replaces two defensive skill roles (2026-10-31)

- Keep the confirmed MTG title **Decisive Denial** ([STX #382](https://scryfall.com/card/stx/382/decisive-denial)) and existing Skill ID `brace-discipline`; repurpose from BRACE-specific mitigation to defensive readiness while a WAIT-derived Reaction is AVAILABLE. Self or COVER defense gains REFLEX +1/+2/+3 and Armor +2/+4/+6. Self/ally Missile Intercept gains REFLEX +3/+6/+9. Skill no longer has the special 1-Damage→0 rule.
- Archive former confirmed **Shielded Passage** (`guardian-reaction`), preserving its complete historical entry in `ARCHIVED_SKILLS` and returning previously spent points via `retiredSkillLevels`. This skill is not a second active buff and its old levels are not automatically merged into `brace-discipline`.
- **Current totals: 23 confirmed, 8 provisional, 12 archived.** Core and original physical Options unchanged. Previously versioned sections below remain historical snapshots.

### Archived approved name — Shielded Passage (original v0.41)

| Skill ID | Historical name / MTG card image | Historical Skill effect | Source card's original effect |
| --- | --- | --- | --- |
| `guardian-reaction` | **[Shielded Passage](https://scryfall.com/card/gtc/24/shielded-passage)**<br>![Shielded Passage MTG card](https://api.scryfall.com/cards/gtc/24?format=image&version=small) | 味方のCOVER／ミサイル迎撃時 REFLEX +3/+6/+9 | クリーチャーへの次のダメージを軽減 |

## v0.41 — Figure of Destiny (2026-10-30)

- `kill-momentum-growth`: former provisional "撃破成長（仮）" is confirmed and renamed **Figure of Destiny**, [EVE #139](https://scryfall.com/card/eve/139/figure-of-destiny). One enemy Unit kill grows effective SHOOTING and MELEE by +2 each, capped at 2/4/6 kills for Lv1/2/3, within the current Mission only. No additional player-facing choice or experience system.
- Stable Skill ID remains unchanged. Main Core unaffected. **24 confirmed / 8 provisional / 11 archived**; older release histories remain historical snapshots.

## v0.40 — newly approved names and reused historical title

- **Sight Beyond Sight** (DTK #75) is approved for flying-target detection (`anti-air-recon`). Applies an additional +1/+2/+3 to TargetSignature in **this observer's** flying-enemy detection check only.
- **Iron Verdict** (KHM #17) is approved for Heavy Rail proficiency (`heavy-rail-proficiency`), effective SHOOTING +2/+4/+6 during eligible Heavy Rail shooting. **Iron Verdict was previously the name of `marksmanship`**, which was renamed **Seize Opportunity** in v0.37. The two skills must not share a stable ID or cause older saved skills to be relabeled.
- Current totals: **23 confirmed**, **9 provisional**, **11 archived**. Earlier release/history sections below retain their historically correct labels and figures. Core unchanged.

## Unassigned / candidate names

- **Last Word**: formerly used for stationary-fire skill in v0.28; reassigned to Sniper Rifle proficiency in v0.37.
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

## v0.36 — generic favorite-weapon proposal archived (2026-10-29)

- Provisional `charlene-favorite-weapon` / **Charlene** was moved to the archive. Existing 19 confirmed MTG skill names remain unchanged.
- Dedicated skills for Assault Lance and Sniper Rifle are under discussion; names and new entries will be added only after selection.

## v0.37 — approved MTG titles (2026-10-29)

| Stable ID | Previous title | Approved title | Source |
| --- | --- | --- | --- |
| `marksmanship` | Iron Verdict | **Seize Opportunity** | [TDM #119](https://scryfall.com/card/tdm/119/seize-opportunity) |
| `momentum-melee` | Through the Breach | **Collision Course** | [DFT #10](https://scryfall.com/card/dft/10/collision-course) |
| `assault-lance-proficiency` (new) | — | **No Quarter** | [TMP #193](https://scryfall.com/card/tmp/193/no-quarter) |
| `sniper-rifle-proficiency` (new) | — | **Last Word** | [DST #23](https://scryfall.com/card/dst/23/last-word) |

All four are real MTG card titles; source card mechanics are not ported. Current 21 confirmed skills, 9 provisional, 10 archived. Existing IDs and save compatibility are maintained. Production Core unchanged.

## v0.38 — Final Fortune (2026-10-29)

- Confirmed `final-fortune` from [Final Fortune](https://scryfall.com/card/mir/173/final-fortune). 50/50 good/bad roll at each friendly Faction Phase start, independent per pilot and phase. Good boosts SHOOTING/MELEE +4/+5/+6; bad reduces REFLEX −6/−5/−4. Effect lasts through the enemy phase until the next friendly phase. Source card mechanics are not ported. 22 confirmed, 9 provisional, 10 archived; Core unchanged.

## v0.39 — scan balance and archived MTG title (2026-10-29)

- **Confront the Unknown** (`scan-interpretation`): LIVE, unchanged INSIGHT +4/+8/+12 during ACTIVE SCAN; revised scanner Signature totals +3/+4/+5 (normal ACTIVE SCAN is +2), persisting until next own Activation start. [Original card](https://scryfall.com/card/soi/198/confront-the-unknown) remains the same.
- **Stillness in Motion** (`observation-discipline`): archived from confirmed skills. Prior name, source-card link and image, plus original effects retained for historical reference below. Existing skill ID and old saved rank history preserved.

### Archived approved title — original v0.38 row

| Skill ID | Original approved MTG title | Former Skill effect | Source card's original effect |
| --- | --- | --- | --- |
| `observation-discipline` | **[Stillness in Motion](https://scryfall.com/card/tdm/334/stillness-in-motion)**<br>![Stillness in Motion MTG card](https://api.scryfall.com/cards/tdm/334?format=image&version=small) | 通常MOVEせずActivation終了で次の自Activationまで INSIGHT +4/+8/+12 | クリーチャーに関わる能力を備えたエンチャント |

Current totals: **21 confirmed**, **9 provisional**, **11 archived**. Prior release notes below or above are historical and retain their original counts. Core unchanged.
