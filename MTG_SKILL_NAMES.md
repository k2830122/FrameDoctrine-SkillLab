# Approved Skill Names — v0.63 (2026-11-08)

**27 confirmed active skills (25 distinct names; the 3 Machine Over Matter variants share one title).** As of v0.63 the active roster also has 1 provisional skill and 21 archived/paused entries. Inevitable End and Full Bore were newly approved as verified actual MTG card names. New names are user-approved; exact MTG-card provenance is not asserted when unverified. Names are independent of original card mechanics. Decisive Denial (`brace-discipline`) and Antagonize (`brace-antagonize`) are archived after the retirement of COVER and BRACE; Shielded Passage (`guardian-reaction`) remains archived. All other confirmed IDs, including Figure of Destiny, Steady Aim and Iron Verdict, remain unchanged. Original cards are linked and card artwork can be viewed on Scryfall; the inline images below are referenced from the public Scryfall image endpoint, not copied into this repository.

**v0.63 archival note:** [Confront the Unknown](https://scryfall.com/card/soi/198/confront-the-unknown) (`scan-interpretation`) is now archived, not an active named Skill. Its former ACTIVE SCAN-only INSIGHT +4/+8/+12 and scanner Signature +3/+4/+5 are preserved in archived design history. This does not implement removal of ACTIVE SCAN in production Core. The new active name Anticipate was verified in the 20,731-name expansion snapshot.

Historical v0.60 mechanics note: Collision Course requires **5 or more actual entered Hexes in normal MOVE** (previously 3); Escape Velocity already required 5 and its descriptions now consistently say **5 or more**. All old entries below are historical unless explicitly revised. No MTG names, IDs, active/archive status or Core rules changed.

| Skill ID | Current name / MTG card image | Skill effect | Source card's original effect (brief) |
| --- | --- | --- | --- |
| `frame-light` | **[Machine Over Matter](https://scryfall.com/card/bro/57/machine-over-matter)** (light) | Light搭乗時 SHOOTING・MELEE +1/+2/+3 | アーティファクト・クリーチャーがいるとコスト減少、非土地パーマネントを手札へ戻す |
| `frame-standard` | **[Machine Over Matter](https://scryfall.com/card/bro/57/machine-over-matter)** (standard) | Standard搭乗時 SHOOTING・MELEE +1/+2/+3 | 同上 |
| `frame-heavy` | **[Machine Over Matter](https://scryfall.com/card/bro/57/machine-over-matter)** (heavy) | Heavy搭乗時 SHOOTING・MELEE +1/+2/+3 | 同上 |
| `final-fortune` | **[Wax and Wane](https://mtg.wtf/card/inv/296a/Wax)** | 全体Turn開始時50%抽選。好調SHOOTING・MELEE +4/+5/+6、不調REFLEX −6/−5/−4 | 原名Wax // Wane。片面でクリーチャーを強化、片面でエンチャントを破壊する分割カード |
| `kill-momentum-growth` | **[Figure of Destiny](https://scryfall.com/card/eve/139/figure-of-destiny)**<br>![Figure of Destiny MTG card](https://api.scryfall.com/cards/eve/139?format=image&version=small) | 本人による敵撃破1体ごとにSHOOTING・MELEE各+2。最大累積2/4/6体（最大各+4/+8/+12）、Mission内限定 | 段階的に能力を強化できるクリーチャー。原カードの能力値やコストは移植しない |
| `avoid-fate` | **[Avoid Fate](https://scryfall.com/card/leg/175/avoid-fate)**<br>![Avoid Fate MTG card](https://api.scryfall.com/cards/leg/175?format=image&version=small) | 敵の適格な1Attackを全Hit回避するたびREFLEX +1、最大2/4/6回（最大+2/+4/+6）。Mission内限定、被弾しても維持 | 自分のパーマネントを対象とするインスタントまたはオーラ呪文を打ち消す |
| `paired-fire` | **[Dual Strike](https://scryfall.com/card/khm/132/dual-strike)** | 同一のAssault Rifle／SMG／Shotgun2丁連動FIRE。各銃HitRaw−40/−30/−20pt、SHOOTING/REFLEX平均、片丁のみなら通常射撃 | インスタント／ソーサリーをコピーする能力を持つ呪文 |
| `marksmanship` | **[Steady Aim](https://scryfall.com/card/war/177/steady-aim)**<br>![Steady Aim MTG card](https://api.scryfall.com/cards/war/177?format=image&version=small) | 通常MOVE前の対Unit射撃で SHOOTING +2/+4/+6（旧Iron Verdict） | 実在するMTGカードから名称のみ採用。原カードの効果はゲームへ移植しない |
| `sniper-rifle-proficiency` | **[Last Word](https://scryfall.com/card/dst/23/last-word)**<br>![Last Word MTG card](https://api.scryfall.com/cards/dst/23?format=image&version=small) | Sniper Rifleによる適格な射撃中のみ SHOOTING +2/+4/+6 | 打ち消されない呪文で対象の呪文を打ち消す |
| `heavy-rail-proficiency` | **[Iron Verdict](https://scryfall.com/card/khm/17/iron-verdict)**<br>![Iron Verdict MTG card](https://api.scryfall.com/cards/khm/17?format=image&version=small) | Heavy Autocannon（武装容量3・Shots2）での適格な射撃中のみSHOOTING +2/+4/+6。旧IDは保存互換保持、Heavy Railには無効 | タップ状態クリーチャーへ5ダメージ、予顕あり |
| `pre-activation-reflex` | **[Anticipate](https://scryfall.com/card/dtk/45/anticipate)**<br>![Anticipate MTG card](https://api.scryfall.com/cards/dtk/45?format=image&version=small) | 各全体Turn開始から自身のActivation開始まで、未行動中の実効REFLEX +max(1, floor(出撃時の基礎INSIGHT×Lv/10))。INSIGHT10なら+1/+2/+3。 | 山札上3枚を見て1枚を手札に加え、残りを山札の下に置く |
| `mobile-evasion` | **[Escape Velocity](https://scryfall.com/card/thb/132/escape-velocity)**<br>![Escape Velocity MTG card](https://api.scryfall.com/cards/thb/132?format=image&version=small) | 通常MOVEで実際に5HEX以上進入すると次自身のActivation開始まで REFLEX +2/+4/+6 | 速攻と攻撃修整を付与、脱出可能 |
| `momentum-melee` | **[Collision Course](https://scryfall.com/card/dft/10/collision-course)**<br>![Collision Course MTG card](https://api.scryfall.com/cards/dft/10?format=image&version=small) | 通常MOVEで実際に5HEX以上進入後の白兵で MELEE +2/+4/+6（旧Through the Breach） | 自軍クリーチャー／機体数に応じて対象へダメージ、またはアーティファクト破壊 |
| `assault-lance-proficiency` | **[No Quarter](https://scryfall.com/card/tmp/193/no-quarter)**<br>![No Quarter MTG card](https://api.scryfall.com/cards/tmp/193?format=image&version=small) | Assault Lanceによる適格な白兵中のみ MELEE +2/+4/+6 | パワーの小さいクリーチャーとのブロック戦闘で破壊 |
| `finisher-half-hp` | **[Inevitable End](https://scryfall.com/card/thb/102/inevitable-end)** | 敵HP50%未満の対象へ適格な射撃・白兵でSHOOTING・MELEE +3/+5/+7。Attack開始時HPを固定 | 原カードは対象を継続的に追い詰めるエンチャント。ゲームへ効果自体は移植しない |
| `full-health-offense` | **[Full Bore](https://scryfall.com/card/eoe/135/full-bore)** | 自機HP満タンなら適格な射撃・白兵でSHOOTING・MELEE +2/+3/+4。全快で復帰 | 原カード効果をそのまま使わず、最大能力を発揮するという英語表現から命名 |
| `fired-up` | **[Repercussion](https://scryfall.com/card/uds/95/repercussion)**<br>![Repercussion MTG card](https://api.scryfall.com/cards/uds/95?format=image&version=small) | 敵の攻撃でHitを受けた次のActivation、SHOOTING・MELEE +6/+9/+12 | クリーチャーが受けたダメージをそのコントローラーにも与える |
| `anti-air-recon` | **[High Alert](https://scryfall.com/card/rna/182/high-alert)**<br>![High Alert MTG card](https://api.scryfall.com/cards/rna/182?format=image&version=small) | 飛行型敵への自機索敵判定で対象Signature項+1/+2/+3（実値変更なし） | 実在するMTGカードから名称のみ採用。原カードの効果はゲームへ移植しない |
| `leave-no-trace` | **[Leave No Trace](https://scryfall.com/card/rav/23/leave-no-trace)**<br>![Leave No Trace MTG card](https://api.scryfall.com/cards/rav/23?format=image&version=small) | 常時Signature −1/−2/−3とDetection Power −4/−8/−12の交換。基本索敵予算−1/−2/−3 | 指定色のエンチャントを全て破壊 |
| `solo-operator` | **[Audacity](https://scryfall.com/card/bro/169/audacity)**<br>![Audacity MTG card](https://api.scryfall.com/cards/bro/169?format=image&version=small) | 味方が4Hex以内にいないとき基礎INSIGHT依存でSHOOTING上昇 | クリーチャーに+2/+0とトランプル、死亡時ドロー |
| `pick-your-ground` | **[Familiar Ground](https://scryfall.com/card/wth/127/familiar-ground)**<br>![Familiar Ground MTG card](https://api.scryfall.com/cards/wth/127?format=image&version=small) | 敵の合法な通常Direct FIREが樹冠と交差し基本−10ptを受けるAttack中だけ実効REFLEX +2/+4/+6（HitRaw追加−6/−12/−18pt相当、合計−16/−22/−28pt）。全Hitに適用しAttack終了で失効。森林Hex滞在のみでは無効、建物遮断時は攻撃不成立 | 実在するMTGカードから名称のみ採用。原カードの効果はゲームへ移植しない |
| `leg-disrupting-shot` | **[Off Balance](https://scryfall.com/card/nem/15/off-balance)**<br>![Off Balance MTG card](https://api.scryfall.com/cards/nem/15?format=image&version=small) | 通常Direct FIREで未行動・未移動の敵Unitに1Hit以上命中した後、基礎INSIGHT×Lv÷2%で1Attackに1回抽選（0.5%保持）。当該TurnのMOVEだけ阻止、次Turnには持ち越さない。旧ID維持 | 実在するMTGカードから名称のみ採用。原カードの効果はゲームへ移植しない |
| `fault-line` | **[Fault Line](https://scryfall.com/card/usg/185/fault-line)**<br>![Fault Line MTG card](https://api.scryfall.com/cards/usg/185?format=image&version=small) | CritPen成功直後から対象Armor −2/−4/−6（同Attack後続Hitにも適用） | 地上クリーチャーと各プレイヤーへXダメージ |
| `survival-cache` | **[Emergency Weld](https://scryfall.com/card/bro/93/emergency-weld)** | Repair Kitの回復量8HPを12/16/20HPへ強化 | 墓地のアーティファクト・クリーチャーカードを手札に戻し、1/1アーティファクト・兵士トークンを作る |
| `suppressive-fire` | **[Shadow of Doubt](https://scryfall.com/card/rav/253/shadow-of-doubt)**<br>![Shadow of Doubt MTG card](https://api.scryfall.com/cards/rav/253?format=image&version=small) | 通常Direct FIREで全Hit外すと敵REFLEX −2/−4/−6（対象の次Activation開始まで） | プレイヤーのライブラリー探索を禁止しカードを引く |
| `last-stand-ability` | **[Brink of Disaster](https://scryfall.com/card/wwk/52/brink-of-disaster)**<br>![Brink of Disaster MTG card](https://api.scryfall.com/cards/wwk/52?format=image&version=small) | HP50%以下でREFLEX = +1 + floor(基礎INSIGHT×Lv/6)（低HP中持続） | エンチャントされたクリーチャー／土地がタップされるとそれを破壊 |
| `lethal-endurance` | **[Against All Odds](https://scryfall.com/card/one/1/against-all-odds)**<br>![Against All Odds MTG card](https://api.scryfall.com/cards/one/1?format=image&version=small) | Lv1: HP50%以下でArmor+2。Lv2: HP25%以下でさらにArmor+4（合計+6）。Lv3: そのArmor強化に加えAttack開始HP2以上ならHP1生存（同Attackの全Hit） | 小型のアーティファクト／クリーチャーを墓地から復帰、またはパーマネントを一時追放して戻す |

## v0.54 — Archived BRACE and COVER skills (2026-11-02)

- **[Decisive Denial](https://scryfall.com/card/stx/382/decisive-denial)** (`brace-discipline`) retired because COVER and its WAIT-granted Reaction are removed in the new design; historical Armor +2/+4/+6 remains only in archived metadata.
- **[Antagonize](https://scryfall.com/card/snc/100/antagonize)** (`brace-antagonize`) retired because BRACE is removed; historical AI target-attraction levels remain archived.
- Their entries are no longer present in the table of *active approved* titles. Older Git revisions preserve their complete original source-card register rows. Saved ranks and stable IDs are preserved. There are **25 confirmed active entries (23 distinct titles)**, 4 provisional, 17 archived.

## v0.53 — Four renamed approved skills (2026-11-02)

| Stable ID | Old name | New name (verified MTG card) |
| --- | --- | --- |
| `anti-air-recon` | Sight Beyond Sight | **[High Alert](https://scryfall.com/card/rna/182/high-alert)** |
| `marksmanship` | Seize Opportunity | **[Steady Aim](https://scryfall.com/card/war/177/steady-aim)** |
| `pick-your-ground` | Privileged Position | **[Familiar Ground](https://scryfall.com/card/wth/127/familiar-ground)** |
| `leg-disrupting-shot` | Impede Momentum | **[Off Balance](https://scryfall.com/card/nem/15/off-balance)** |

Only names and active-name references changed. Skill IDs, all ability bonuses and triggers, player save key, status counts, and main game Core remain unchanged. Prior entries are historical.

## v0.52 — Wax and Wane display name (2026-11-01)

- `final-fortune` adopts **Wax and Wane** as its final displayed English skill name. Earlier name: Wax + Wane; before that Mercurial Mind. Source and inspiration: MTG's existing split card **Wax // Wane** (Invasion #296), whose **exact** printed/Oracle card-name syntax differs from this intentional natural-language adaptation. Source link in the registry points to the original card, not to a card literally titled Wax and Wane.
- No gameplay, ID, rank, save or roster-count changes. Current 27 confirmed (25 distinct names), 4 provisional, 15 archived.

## v0.51 — Dual Strike / Wax + Wane (2026-11-01)

- `paired-fire` confirmed as **Dual Strike** (MTG Kaldheim #132), with simultaneous matched slot-1 weapons and SHOOTING/REFLEX mean replacing ordinary shooting skill, per-gun HitRaw penalty −40/−30/−20. Enemy initial snapshot shared, independent attacks, no cross-gun Fault Line benefit, ordinary one-gun fallback when unavailable.
- `final-fortune` **Mercurial Mind → Wax + Wane**, after the MTG split card **Wax // Wane** (Invasion #296); + is the display convention.
- Previously unverified source names **Machine Over Matter** and **Emergency Weld** are MTG cards from The Brothers' War (#57, #93); source links refreshed. Now **27 confirmed / 25 distinct titles**, four provisional, 15 archived. All stable IDs, save data and main-game Core unchanged.

## v0.50 — Approved renames / new growth category (2026-11-01)

- `pick-your-ground`: **Privileged Position** (formerly Dead of Winter; previous name reserved for future reuse).
- `survival-cache`: **Emergency Weld** (formerly Survival Cache).
- `frame-light`, `frame-standard`, `frame-heavy`: **Machine Over Matter** (formerly Tempered Steel, three variants).
- `final-fortune`: **Mercurial Mind** (formerly Glimmer of Genius).
- Both **Figure of Destiny** and **Avoid Fate** now belong to the **ミッション内成長** group; no changes to functionality.
- Confirmed **26 skills / 24 distinct titles**; 5 provisional and 15 archived. Names, UI group only; no core, effect, ID or save compatibility changes.
- Card links/pictures are provided only where an exact source card was verified. Unverified same-name MTG provenance is left blank rather than using the old card under a new skill name.

## v0.49 — Two provisional concepts retired (2026-11-01)

- Archived `lance-charge` (突撃貫徹) and `reflex-followup-move` (反射機動（仮）), while retaining their saved-build retired rank history and refunding Training Points. Neither had an approved MTG title, so the confirmed registry of **26 skills / 24 distinct MTG titles** is unchanged.
- Now **31 active (26 confirmed / 5 provisional), 15 archived**. Four already-confirmed titles (Dead of Winter, Survival Cache, Tempered Steel, Glimmer of Genius) are *only* under review; no renames yet.

## v0.48 — Impede Momentum officially named (2026-11-01)

- **[Impede Momentum](https://scryfall.com/card/dmu/54/impede-momentum)** is adopted for the former provisional movement suppression skill `leg-disrupting-shot`; stable ID, three level percentages and INSIGHT dependency are unchanged. The skill is now confirmed and grouped with enemy debuffs.
- **26 confirmed skills, 24 unique approved MTG titles, 7 provisional, 13 archived**. Audacity and Brink of Disaster remain unchanged. No other confirmed skill was renamed.
- Naming-family audit and tentative semantic mismatch suggestions are in the v0.48 README / design notes; these suggestions authorize no additional name changes.

## v0.47 — Movement suppression probability changed (2026-11-01)

- The existing provisional skill `leg-disrupting-shot` remains unnamed in English; new effect: **base INSIGHT × Lv / 2%**, without truncating half-percentage-point chances, on an eligible enemy Unit-targeted FIRE/INTERCEPT Attack with at least one Hit (once per Attack, never once per Hit). Its eventual MTG card title is still undecided.
- IR-9's innate Forced Halt is superseded in **future design**, but current production Core is not migrated. Audacity and Brink of Disaster's hidden base-INSIGHT floor breakpoints are flagged for future redesign; their mechanics remain unchanged. Final game UI should present actual Skill values and hypothetical +1 Ability deltas, rather than exposing internal formulas.
- Still **25 confirmed skills / 23 distinct MTG names**, 8 provisional, 13 archived.

## v0.46 — Antagonize / Leave No Trace and revisions (2026-11-01)

- **Against All Odds** (`lethal-endurance`) now upgrades through HP ≤50%: Armor+2 (Lv1), HP ≤25%: +4 more Armor (+6 total from Lv2), then at Lv3 survival of one lethal Attack down to HP1 if starting at HP≥2. Original Lv1/2 HP1-survival variants are superseded.
- **Iron Verdict** (`heavy-rail-proficiency`) now strengthens Heavy Autocannon (Armament Capacity 3, 2 Hit Attempts), **not** Heavy Rail. Its stable historical ID remains unchanged to avoid relabeling and breaking saved builds.
- New **[Antagonize](https://scryfall.com/card/snc/100/antagonize)** (`brace-antagonize`) is a BRACE-triggered enemy targeting-utility skill with Lv1–3 tiers but **unspecified numerical utility** pending real AI tuning. No automatic Track or forced targeting.
- New **[Leave No Trace](https://scryfall.com/card/rav/23/leave-no-trace)** (`leave-no-trace`) provides persistent Signature −1/−2/−3 and Detection Power −4/−8/−12, a deliberate Sensor-budget tradeoff.
- Previous **Moment of Silence** (`conceal-discipline`) is paused and moved to archived research pending redesign; existing skill purchases are migrated to `retiredSkillLevels` with rank points refunded. The historical card name and unchanged prior specification are documented below.
- **25 confirmed, 23 distinct MTG titles**, 8 provisional, 13 archived/paused. No Core changes, no new game action; the planned enemy interleaving remains a separate game implementation.

### Archived approved name — Moment of Silence (v0.45, paused v0.46)

| Skill ID | Historical name / MTG card | Archived v0.45 effect |
| --- | --- | --- |
| `conceal-discipline` | **[Moment of Silence](https://scryfall.com/card/mmq/28/moment-of-silence)**<br>![Moment of Silence MTG card](https://api.scryfall.com/cards/mmq/28?format=image&version=small) | CONCEAL時Signature低下（暫定−2/−3/−4）、自機センサー停止 | 相手の次の戦闘フェイズを飛ばす |

## v0.45 — COVER opportunity study (2026-10-31)

- Decisive Denial's approved name, ID and COVER-only Armor +2/+4/+6 effect are unchanged. The pilot cannot gain this bonus when personally targeted rather than protecting an adjacent ally. A non-battle, assumption-driven COVER opportunity and per-hit Armor comparison was added to Skill Lab.
- The weapon-mechanics descriptions for No Quarter, Collision Course, Fault Line and a provisional dual-fire idea were updated to match the **2026-10-29 canonical design** (Assault Lance Range 1 and CritPen YES; additional applicable CritPen-capable direct weapons and Explosive Axe). No skill naming, skill level or points changed; the game's current code still awaits the weapon design migration.

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
