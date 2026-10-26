# FRAME DOCTRINE — PILOT SKILL LAB

**Current release: v0.23 (2026-10-26).** 33 active Skills: **6 confirmed**, 27 provisional; 1 retired Skill archived separately. Confirmed Skill names are English-only even in the Japanese interface. The Pilot Ability formerly labeled AWARENESS is now **INSIGHT**; private Core's Pilot Detection and Frame Sensor have not been renamed. Historical notes below may still use former names.


## Historical decision log: Frame Proficiency Skills (2026-10-23)

**確定（仕様確定）:** 機体習熟 Light / Standard / Heavy

| Level | Effective SHOOTING | Effective MELEE |
|---|---:|---:|
| Lv1 | +1 | +1 |
| Lv2 | +2 | +2 |
| Lv3 | +3 | +3 |

Passive automatic Skill: applies while operating the matching Frame class. The changes are effective Ability modifiers used by all eligible SHOOTING/MELEE calculations, including applicable Missile Intercept or Critical Penetration checks. REFLEX and AWARENESS are unaffected. No Action, Reaction, MP, cooldown or use count. One Training Point per rank.

This decision replaces the earlier provisional +2/+3/+5% accuracy/evasion proposal. **Confirmed for Skill Lab game design, not yet implemented into private Core or canonical specifications.** All other skills were not approved at the time of that decision; see the later Opening Advantage confirmation below.


A standalone browser-based simulator for experimental pilot skill builds in FRAME DOCTRINE: LAST RESORT.

**Status:** Research prototype v0.15. The game project itself is separate and is not included in this public repository. None of the proposed skills or balance numbers are official game specifications.

## Features

- 33 active experimental pilot skills (six confirmed, 27 provisional) and one retired Skill in the archive
- Ability development and Lv.1–3 skill purchases with a shared 1–12 point budget
- Undo, reset, filter and search
- Local browser auto-save and import/export of build JSON
- In-app classifications of 20 existing Options, for design study only

## Run

Open `index.html` directly in a modern browser or access the GitHub Pages site once Pages has been enabled.

## Publish with GitHub Pages

Repository **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save**.

All files in this repository (and its published Pages site) are intentionally public. Do not commit private project source, documents, character art, secrets or other non-public assets here.

## Source separation

This repository was initialized independently of the private game's Git history. Only the standalone application and this public README were copied. This skill lab does not modify the game's core, option implementations or canonical specifications.

## Disclaimer

Experimental results and numbers are design hypotheses; the simulator models **point allocation**, not full combat outcomes.

## New concept candidates (2026-10-23)

The following candidates are only rough exploratory ideas, not accepted implementation requirements. The initial Lv.1–3 values and caps in the app are illustrative placeholders.

- **Kill Momentum Growth / 撃破成長:** Each enemy defeated grants a bonus to a player-chosen Ability. Important unresolved questions: choice timing, per-mission versus persistent growth, stacking cap, and kill credit.
- **Reflex Follow-Up Move / 反射機動:** After acting, gain a chance to move again proportional to *effective REFLEX*. Illustrative Lv.1 formula: 1% × REFLEX (REFLEX 10 → 10%); higher-level scaling is provisional. The legality and interaction with existing mobility features are unresolved.
- **Lethal Endurance / 不屈:** Survive an otherwise lethal hit at HP 1. The current per-level initial-HP thresholds and once-per-mission limit are illustrative only.
- **Low-HP Ability Surge / 背水の陣:** Gain an effective Ability bonus when current HP falls below a chosen threshold. Ability selection, threshold and level bonus are not approved.

### Cross-cutting idea: Ability-value-based Skills

Besides ordinary Ability-boosting Skills, investigate Skills whose *magnitude or activation probability is calculated from the Pilot's current effective Ability*, such as `REFLEX × 1%` for a conditional follow-up move. This gives ordinary Ability increases additional strategic value.

When a Skill says it grants an effective Ability bonus (SHOOTING, MELEE, AWARENESS or REFLEX), the intended *research direction* is to use the resulting effective Ability in all relevant calculations, rather than granting narrow +Hit% / +Evasion% substitutions. This still requires explicit combat-design review before any change to the private Core.

This app currently simulates **training-point allocation only**, not on-map kill events, HP reductions, Action outcomes, or chance rolls.

## Ability cap removal and limited guaranteed outcomes (2026-10-23)

**New accepted research direction (not yet canonical Core):**
- Remove the numeric ceiling on both *base* and *effective* Pilot Abilities (SHOOTING, MELEE, AWARENESS, REFLEX). A player may continue investing Training Points into a base Ability past 20, subject to their finite Training Point budget.
- Conditional Skill boosts stack into the effective Ability and use that full value consistently in all relevant Ability-dependent calculations.
- Extreme accuracy and evasion are allowed to become correspondingly strong. Probability quantities, however, are still bounded by 0–100%; removing an Ability ceiling is **not** removing probability bounds.
- Balance through finite growth points, real activation conditions, opportunity costs and build tradeoffs, not a universal ability ceiling. Do not silently migrate this rule into the private game Core or master specs.

**New speculative Skills (not approved effects):**
- **必中の一撃 / Decisive Shot:** a limited number of eligible attacks per Mission become guaranteed hits; draft ranks allow 1/2/3 uses. Prefer an understandable passive/conditional trigger over another active command. What counts as an eligible attack, how a use is spent and whether a 100% base hit consumes it remain unresolved.
- **完全回避 / Certain Evasion:** evade exactly one qualifying incoming attack after a preparation cost. Working non-active version is to use existing WAIT as its trigger, with 1/2/3 prepared guaranteed evades per Mission by rank. This is a proposal, not approval of specific timing or effect.
- In interactions between guaranteed hit and guaranteed dodge, the governing priority is **undecided**. Direct Fire vs Missile vs Area/multi-hit and interactions with critical penetration need explicit rules. Do not infer priorities from the labels alone.

The skill-list page models **purchase allocation**, not true combat resolution or activation charges. These new entries are deliberately labeled exploratory.

## 2026-10-23 — effective Ability rework of the original 19 skills

The Skill Lab now shows the research redesign on all 19 original candidates, retaining all 6 later rough ideas (28 total) and stable IDs for saved builds. **No Core changes are authorized.** Existing Option mechanics remain untouched.

**Research principle:** When a Skill grants conditional Ability +N or −N, use that *effective* Ability consistently in **all otherwise eligible formulas** that use SHOOTING, MELEE, AWARENESS, or REFLEX, instead of one-off Hit/Evasion percentage exceptions. Conditional skills do not mutate the underlying base value. Base and effective Ability caps are removed *in the research design*; probability outputs still use ordinary 0–100% rules.

New compare-only Lv1/2/3 values:

- Frame Proficiency L/S/H: SHOOTING and MELEE +1/+2/+3 (not REFLEX).
- Opening Vigilance (formerly Opening Advantage; confirmed): AWARENESS and REFLEX +1/+2/+3. Solo Operator (provisional): SHOOTING and REFLEX +1/+2/+3.
- Precision Shooting, Mobile Evasion, Momentum Melee: relevant SHOOTING/REFLEX/MELEE +2/+4/+6 respectively, with existing stationary or 3-Hex movement trigger.
- Ordinary INTERCEPT specialist: SHOOTING +2/+4/+6 only during qualifying ordinary INTERCEPT.
- Burst Focus: selected Ability +2/+4/+6 (activation economics unresolved).
- Night/Adverse Weather, Stationary Observation, Active Scan Interpretation: AWARENESS +4/+8/+12 under their respective conditions (strong provisional values; Active Scan Skill remains unapproved).
- Suppressive Fire: target effective REFLEX −1/−2/−3 for rest of firing Faction Phase; full applicable REFLEX semantics, not a special +Hit% buff.
- Guardian Reaction: REFLEX +1/+2/+3 when protecting an ally (Skill migration on hold).
- Stationary penetration, Lance charge penetration, BRACE Armor, CONCEAL Signature: remain special-effect skills; not all effects should be expressed as Ability gains.

The app is only a **point-allocation simulator**. Conditional skills are not automatically added to the base-Ability numbers in the pilot panel, because no battlefield conditions have been simulated; see each skill's trigger and effect instead. Unconfirmed numerical proposals are marked provisional; the approved Frame Proficiency and Opening Vigilance Skills have fixed Skill Lab specifications.
\n## Passive-first Skill design (2026-10-23)\n\n[SKILL_DESIGN_NOTES.md](SKILL_DESIGN_NOTES.md) has the current cost catalogue and new Skill concepts: REFLEX-based second-chance dodge, SHOOTING-based movement-disabling hit, and additional-ammo multi-attempt FIRE. The design direction favors passive Skills and existing tactical resources, with active Skills as exceptions only. All three are exploratory.\n
## 2026-10-23 — Range and movement-triggered skill drafts

Two further exploratory candidates were added (30 total): a condition-based “Lucky Star” slot (example: firing from 7 Hexes, effect TBD) and a REFLEX-dependent movement firing penalty mitigation skill. Refer to [SKILL_DESIGN_NOTES.md](SKILL_DESIGN_NOTES.md) for candidate formulas and Core distinctions. Their conditions and numbers are not approved final mechanics.

## v0.9 — Pilot AWARENESS and saved-build migration (2026-10-23)

- Pilot Ability label: **AWARENESS（状況把握）**, formerly displayed as SENSOR in Skill Lab. This remains the current private game's internal **`PilotStats.Detection`**. Physical **`Frame.Sensor`** is a distinct Frame statistic; private Core and canonical game specs remain unchanged.
- Legacy browser saves and imported JSON with `abilityBonus.SENSOR` automatically map to `abilityBonus.AWARENESS`, preserving allocated Training Points. New exports use AWARENESS.
- The 「確定スキルを見る」 button toggles on/off; the second click restores previously selected search/category/origin/status filters (Issue #1).
- **Historical exploration (superseded by the confirmed v0.10 design below):** Early Starter duration was proposed as `max(1, floor(base AWARENESS at deployment / 2))` global Turns. The formula and Lv bonuses have since been approved for Opening Advantage. The general integer-rounding policy is still under discussion and is not an approved global Core change.

## v0.10 — Historical: Opening Advantage / 初動掌握 (superseded by v0.11)

**Status: 確定 (Skill Lab design, not implemented in private Core).** Existing Skill ID `early-starter` is retained for saved build compatibility. Rename from アーリースターター / Early Starter to **初動掌握 / Opening Advantage**.

| Rank | Effective SHOOTING | Effective REFLEX | Training cost |
|---|---:|---:|---:|
| Lv1 | +1 | +1 | 1P total |
| Lv2 | +2 | +2 | 2P total |
| Lv3 | +3 | +3 | 3P total |

Trigger: passive and automatic from global Turn 1. Duration: global Turns `1..max(1, floor(base AWARENESS measured at sortie deployment / 2))`, inclusive. It applies in **every Faction Phase** of each eligible global Turn; expires from the start of the next global Turn. The base AWARENESS snapshot is not recomputed on conditional temporary changes during the battle. Examples: AWARENESS 10 → Turns 1–5; 16 → Turns 1–8; 20 → Turns 1–10.

The modifiers affect all eligible uses of effective SHOOTING/REFLEX while active, including direct-attack accuracy, defensive evasion, qualifying missile-intercept formula, and relevant CritPen. No Frame-class restriction or extra Action/Reaction/ammunition/resource consumption. Baseline Ability is unchanged. The confirmed-vs-draft count becomes **4 confirmed / 26 under consideration** in the Skill Lab; use the confirmed filter to inspect them.

Design rationale: a time-limited, Frame-agnostic alternative to permanent single-Ability training and Frame Proficiency. Particularly useful for high-AWARENESS reconnaissance pilots who need early evasion; mission lengths and contact-turn distributions should still be tested. This decision **does not change `docs/IDEAS.md`, `docs/CORE_SPEC.md`, or any implementation in the private game**.

## v0.11 — Confirmed Opening Vigilance / 初動警戒 (2026-10-23)

**Current approved design** (supersedes the previous Opening Advantage confirmation): The public Skill Lab card `early-starter` is renamed **初動警戒 / Opening Vigilance**. Its underlying Skill ID is kept unchanged, preserving existing saved builds. The earlier SHOOTING/REFLEX bonus and subsequently discussed MELEE addition are not adopted.

| Rank | Effective AWARENESS | Effective REFLEX | Cumulative Training Points |
|---|---:|---:|---:|
| Lv1 | +1 | +1 | 1 |
| Lv2 | +2 | +2 | 2 |
| Lv3 | +3 | +3 | 3 |

Automatically active in **every faction Phase** of global Turn 1 through `max(1, floor(base AWARENESS at deployment / 2))` (inclusive), then expires. The duration uses **base AWARENESS at sortie deployment**, including permanently trained base points but **excluding the Skill's own conditional AWARENESS increase** and any other temporary buff. Skill rank changes the benefit, not its duration. Base AWARENESS10 = 5 Turns, 16 = 8 Turns, 20 = 10 Turns. While active, the effective AWARENESS bonus contributes to eligible detection checks and REFLEX to eligible enemy attacks/evasion/reaction formulas. Base Ability never changes. No Frame-class limit or extra active command.

The three formerly named **Frame Proficiency** Skills (Light/Standard/Heavy) retained their effects and have been renamed **Frame Combat Proficiency** in v0.12: effective SHOOTING and MELEE each +1/+2/+3 within the specified Frame class. No extra six-pair card variants have been adopted. **4 confirmed and 26 exploratory Skills** remain.

Scope: Skill Lab research design, not private game's Core or canonical gameplay documents. This simulator allocates points; it does not currently simulate live battlefield buffs or Turn counts.

## v0.12 — Released Skill Lab skill-spec consolidation (2026-10-23)

**Current state: 32 cards; 6 confirmed; 26 exploratory.** Confirmed:
1. 機体戦闘習熟：Light / Frame Combat Proficiency: Light
2. 機体戦闘習熟：Standard / Frame Combat Proficiency: Standard
3. 機体戦闘習熟：Heavy / Frame Combat Proficiency: Heavy
4. 初動警戒 / Opening Vigilance
5. 臨戦集中 / Combat Focus
6. 戦況適応 / Tactical Adaptation

The three Frame Combat Proficiency cards retain the exact previous effects and Skill IDs `frame-light`, `frame-standard`, `frame-heavy`. A matching Frame class gives effective **SHOOTING +1/2/3 and MELEE +1/2/3** by rank. **AWARENESS/REFLEX, scouting, mobility and defensive ability are not strengthened.** Only the displayed Skill name changes.

**戦況適応 / Tactical Adaptation** is a new confirmed passive Skill, Lv1/2/3 effective SHOOTING and MELEE **+1/+2/+3**. Activates at global Turn `max(3, 20 - base AWARENESS at sortie)`, inclusive and continues to end of Mission; phase-wide and Frame-agnostic. Example base AWARENESS 10 → Turn10, 14 → Turn6, 15 → Turn5, 16 → Turn4, 17+ → Turn3. Re-evaluating activation time against temporary effective-AWARENESS boosts is not allowed. No additional command. It complements the early defense/scouting role of Opening Vigilance.

**臨戦集中 / Combat Focus**, previously `集中バースト` / Temporary Burst, is confirmed on existing Skill ID `burst-focus`. Upon legal WAIT, the Pilot acquires the normal one binary Reaction. If no Reaction is spent before the following own Faction Phase, that Reaction expires as normal and the Skill activates automatically: for the Pilot's next Activation, effective **SHOOTING and MELEE +2/+4/+6** by Skill Lv1/2/3. Ends on Activation completion, does not stack, and no additional UI action is needed. An INTERCEPT/COVER/etc Reaction spent during the intervening phases disqualifies the bonus.

The following are **not confirmed**, with explicit provisional numerical effects shown solely to compare builds:
- **臨戦警戒 / Combat Vigilance** (reuse existing Skill ID `certain-evasion`, replacing the old guaranteed-evasion draft): while a WAIT-granted Reaction remains available, raise evasion by **floor(base AWARENESS/3), floor(2×base AWARENESS/3), base AWARENESS percentage points** for Lv1/2/3. It does **not** guarantee a dodge nor consume a Reaction simply for being attacked. Weapon/attack-family eligibility, exact base/effective AWARENESS source, combination with Combat Focus when an unspent Reaction earns both benefits, and balancing against enemy mass attacks remain unresolved.
- **Charlene / 愛用武器** (new Skill ID `charlene-favorite-weapon`): when attacking **with the one chosen weapon definition**, strengthen the attack's applicable SHOOTING/MELEE by provisional **+2/+4/+6** for Lv1/2/3. It is not an all-rifles category buff, not an always-on combat ability buff, and not an effect when attacking using another weapon. Weapon selection rules and exact effect strength are unapproved.

**The lab still simulates only Training Point allocation, not live battle conditions, Reaction lifecycle, weapon registration or attack probabilities.** Charlene's selected weapon is stated conceptually only; there is no weapon selection control yet. Existing saved builds retain the IDs for the three renamed Frame skills, `early-starter`, `burst-focus` and `certain-evasion`, preventing loss of owned ranks. No private Core, Godot or master specification files are modified by this release. Older sections above record historical design proposals; for the current Skill Lab state use this v0.12 section.

Related tracked work: GitHub Issues #4–#8.

## v0.13 — Activation-condition categories and opportunity-cost research UI (2026-10-23)

The Skill Lab now groups **all 32 cards by their primary activation/eligibility condition** rather than mixing the strengthened combat stat and trigger. The former broad `汎用`, `射撃`, `白兵` etc. category labels have been replaced with the following **ten research categories, in explicit display order**:

| Primary category | Cards | Purpose |
|---|---:|---|
| 機体・武器固定 | 4 | Match Frame class or a particular weapon; Frame Combat Proficiency remains the first baseline reference |
| 時間経過 | 2 | Opening-only or delayed Turn activation |
| WAIT・Reaction | 4 | WAIT, ordinary INTERCEPT/COVER, Reaction held or spent |
| 移動・静止 | 7 | MOVE, no-MOVE, route-length constraints |
| 距離・布陣 | 2 | Isolation, particular Hex range |
| 天候・環境 | 1 | Weather-dependent activation |
| 姿勢・走査 | 3 | BRACE, CONCEAL or ACTIVE SCAN Main Action |
| 攻撃・弾薬 | 4 | Direct attacks, Hit conditions, ammunition and special attack effect |
| 被弾・HP | 3 | HP thresholds, fatal damage, attacks received |
| 行動後・撃破 | 2 | End-of-action chance or kill-triggered effect |

Every card also includes independent `costTags` and a plain-language `tradeoffDetail` to describe **the resource, tradeoff or restrictive requirement**: Frame/weapon commitment, limited effective Turns, WAIT/Reaction opportunity, stationary/movement choice, separation and geometry, attack Signature exposure, Main Action, added ammunition, dangerous HP, special chance/uses, etc. A new **制約・対価** dropdown filters by these tags; keyword search also includes the new metadata. **Activation requirements, resource expenditure, opportunity costs and mere conditional limits are not identical**; the UI label explicitly warns against counting inherent Core action costs twice.

The category tab bar, `すべて` grouped sections and category dropdown use the same ordering, and the default page opens the **すべて** view with Frame/weapon specialists first. The `確定スキルを見る` toggle also retains the selected tradeoff filter when restoring previous selections.

No Skill's identifier, cost, numeric effect, approved status, or trigger text changed. It remains **6 confirmed / 26 exploratory**; existing local-storage/JSON build data stays compatible. All categories and tag assignments are **research UI taxonomy**, not an implementation of in-battle effects and not a change to private Core.

Related issue: #10.

## v0.14 — Pilot-aware Level previews (2026-10-23)

**The main Lv1 / Lv2 / Lv3 descriptions prioritize concrete sample-Pilot values over formulas.** Formula details are available in each relevant card's expandable **計算式・設計上の補足** section. The prototype still simulates Training Point allocation, not full battle resolution.

The research sample Pilot **PHANTOM-01** has base Abilities of 10 before the user's permanent point allocations. For the following existing draft Skills, visible Lv results are calculated using the sample's current base Abilities and update immediately when they are changed:

- **臨戦警戒 / Combat Vigilance** (`certain-evasion`): direct evasion bonus in **percentage points** from base AWARENESS; display Lv1/2/3 values using `floor(AWARENESS × Lv / 3)` (the Lv3 expression is equivalent to the full AWARENESS value).
- **反射機動** (`reflex-followup-move`), **見切り回避** (`reflex-second-chance`): probability `clamp(REFLEX × Lv,0,100)%`.
- **脚部制圧射撃** (`leg-disrupting-shot`): probability `clamp(SHOOTING × Lv,0,100)%`.
- **移動射撃術** (`moving-fire-discipline`): result of reducing weapon movement modifiers **−10 and −20** by up to `floor(REFLEX × Lv / 3)`, capped at zero penalty; show both practical examples for the same sample Pilot. Weapons with zero penalty do not acquire a bonus.

For the confirmed **初動警戒 / Opening Vigilance**, the shown expiry Turn is now the sample's computed `max(1,floor(base AWARENESS/2))`; for **戦況適応 / Tactical Adaptation**, the start Turn is `max(3,20-base AWARENESS)`. Their approved level bonuses and triggering rules have not changed.

**Disclosure and scope:** The pilot number is the current displayed *base* Ability after point allocation, not the entire battle-effective Ability after other conditional Skills. Dynamic drafts remain **未確定**, and values are illustrations, not guaranteed outcomes in a specific battle. Original detailed research formulas remain present in expanded notes; existing Skill IDs, level effects, training costs and confirmed-status count (**6**) are unchanged. Skill count stays **32**. Browser-stored and JSON builds remain backward compatible. No changes to private Core or master gameplay specs.

## v0.15 — INSIGHT, English-first naming and retirement archive (2026-10-23)

**The current five confirmed Skill IDs and their displayed names** are:

| Stable Skill ID | English name | Confirmed effect |
|---|---|---|
| `frame-light` | **Frame Combat Proficiency (Light)** | Matching class: effective SHOOTING & MELEE +1/+2/+3 |
| `frame-standard` | **Frame Combat Proficiency (Standard)** | Matching class: effective SHOOTING & MELEE +1/+2/+3 |
| `frame-heavy` | **Frame Combat Proficiency (Heavy)** | Matching class: effective SHOOTING & MELEE +1/+2/+3 |
| `early-starter` | **First Watch** | During global Turn 1 through `max(1,floor(base INSIGHT / 2))`: effective INSIGHT & REFLEX +1/+2/+3 |
| `burst-focus` | **Steady Nerves** | After WAIT with its Reaction unspent through the start of next friendly phase: next Activation effective SHOOTING & MELEE +2/+4/+6 |

**INSIGHT** is the English name for the pilot's cognitive awareness/detection stat previously called **AWARENESS**. This is a **Skill Lab presentation/data key change**, not a changed combat formula or a change to private C# `PilotStats.Detection` / `Frame.Sensor`. First Watch uses **base INSIGHT at sortie** as a duration snapshot; its temporary INSIGHT bonus never extends its duration.

**The formerly confirmed Tactical Adaptation, subsequently renamed Quick Study, has been retired.** Stable historical ID `tactical-adaptation` is **absent from the 31 active Skills**, no longer learnable or included in filters. It is listed in a separate collapsed **Archived Skills** section, with its former behavior and retirement rationale. Its former passive offense bonus could come online very early for high-INSIGHT pilots, remain indefinitely, and overlap with class-limited Frame Combat Proficiency. The suggestion to delay it until First Watch ends was also rejected because it would paradoxically activate later for higher-INSIGHT pilots. Do not implement or assume that rejected change.

**Legacy build migration:** same browser storage key `fd-skill-lab-v1` and unchanged schema version 1. On load/import, input `abilityBonus.INSIGHT` is preferred; older `abilityBonus.AWARENESS` and older `abilityBonus.SENSOR` are accepted and converted to INSIGHT. When `skillLevels["tactical-adaptation"]` is found, its historical Lv is stored under `retiredSkillLevels["tactical-adaptation"]` for archival display, but it **does not consume training points**. The abandoned rank's points are thus available for new training. New JSON exports retain the archival rank metadata and use INSIGHT. All other Skill IDs, acquisition ranks and costs remain intact. Reset preserves archived-history metadata.

This release changes public Skill Lab only; private game Core and canonical specifications remain unchanged. Candidate Skill names among the 26 unfinished concepts have **not** been wholesale renamed to English or approved. Historical sections in this README and the notes are preserved as design records; this v0.15 section supersedes conflicts in older names, counts and Skill decisions.

## v0.16 — Stay Frosty confirmed (2026-10-23)

**Current Skill Lab:** 31 active Skills (6 confirmed, 25 experimental), plus Quick Study in Archived Skills. Existing five approved Skill effects are unchanged.

The former experimental `certain-evasion` / 臨戦警戒 / Combat Vigilance is now the sixth confirmed Skill, **Stay Frosty**. Its unchanged stable identifier protects localStorage and exported build ranks. Only its **newly approved rules** are reflected:

- WAIT grants an ordinary binary Reaction. **While that Reaction is still AVAILABLE**, Stay Frosty decreases the attacker's **pre-clamp HitRaw** by a Skill-dependent flat number of HitRaw points. It does not directly increase REFLEX or guarantee the same numeric improvement to the final evasion probability.
- Apply `N=base INSIGHT at sortie` (permanent training included, temporary buffs excluded): **Lv1: −floor(N/2)**, **Lv2: −floor(3N/4)**, **Lv3: −N** HitRaw points.
- Sample N10 => −5/−7/−10; N12 => −6/−9/−12; N15 => −7/−11/−15; N20 => −10/−15/−20. The Skill Lab displays the computed sample pilot numbers on each Lv and recalculates when INSIGHT is trained.
- Resolve eligible attacks with the same rules on either faction: form HitRaw, subtract Stay Frosty, then clamp ordinary hit probability to 0..100 and calculate any excess-hit Critical Penetration conversion from that final HitRaw. For example with N15 and Lv3, incoming original HitRaw130 becomes 115; hit chance stays 100% but the *excess-accuracy addition* to CritPen changes from 15 percentage points to 7.5 percentage points under the proposed CritPen conversion.
- The effect is automatic and remains active for **multiple eligible attacks as long as the usual Reaction remains unused**. Evading or being hit does not itself consume Reaction. INTERCEPT/COVER/Missile Intercept spends Reaction and ends the bonus; unused Reaction expires normally at the next own Faction Phase.
- Compatible with **Steady Nerves**: if the Reaction was not spent, it can still trigger Steady Nerves in the next own Activation. Does not extend itself with temporary INSIGHT, including First Watch's effects.
- Ordinary unit-targeted Direct FIRE / MELEE and eligible guided-impact hit checks are in the intended scope; immunity to attacks that have no such hit/evasion roll is not created. Edge cases (special profiles, area attack, multi-hit and priority of other modifiers) still require private Core implementation design and combat tests, with hidden Faction information safeguarded.
- **Important:** The public simulator is still a *Skill point planner* displaying research-defined effects; it does not execute battles, CritPen rolls or a combat pipeline. `docs/IDEAS.md` in the private game repo holds the candidate 100% excess accuracy to CritPen conversion (50% of excess and no 8% artificial cap); `docs/CORE_SPEC.md` continues to describe legacy Core. Skill Lab v0.16 does not modify the private Core or canonical specifications.

Previous sections of this document are retained as historical snapshots; this v0.16 section supersedes their older Skill status and placeholder numeric descriptions.

## v0.17 — Right on Cue and Got Your Six confirmed (2026-10-23)

**31 active Skills: 8 confirmed and 23 exploratory, plus Quick Study archived separately.** Previous six confirmed Skills retain their effects.

**Right on Cue** (stable ID `reaction-shooter`, formerly 迎撃射撃術): legal ordinary Reaction INTERCEPT **and** Missile Intercept gain effective **SHOOTING +2/+4/+6** at Lv1/2/3. Ordinary INTERCEPT unit-targeted accuracy has SHOOTING coefficient 3, so gains HitRaw **+6/+12/+18**, contributing to over-100 hit accuracy/CritPen on eligible weapons under the design study. Missile Intercept instead has SHOOTING coefficient 2, so gains InterceptHitRaw **+4/+8/+12**. Missile Intercept has no CritPen. It works for eligible self- or allied-target Missile Intercept but not Main Action attacks or COVER. All normal Reaction, weapon/ammo and legality requirements remain.

**Got Your Six** (stable ID `guardian-reaction`, formerly 護衛反応 and DRS Option-inspired): the Pilot gains effective **REFLEX +3/+6/+9** at Lv1/2/3 **only while using COVER or Missile Intercept to protect another Friendly Unit**. COVER protects a different adjacent Friendly Unit from an eligible already committed single-target attack by substituting the coverer as the final defender, without physically moving; normal Direct FIRE, single-target Melee and guided missiles are in scope, while area/hex/direction-targeted attacks and attacks generated by Reaction are excluded. When COVERing an eligible Direct FIRE/Melee/guided Missile hit, REFLEX coefficient 3 yields enemy HitRaw **−9/−18/−27**. When performing Missile Intercept for an ally, REFLEX coefficient 2 yields InterceptHitRaw **+6/+12/+18**. Does not improve self-defense, self-target Missile Intercept or ordinary attacking INTERCEPT. No extra Reaction is granted.

**Core separation:** Defensive Response Suite is still a physical Option implemented in the private game's Core with a separate +2 qualifying REFLEX effect. Skill Lab confirmation is **not** equipment deletion, a decision to stack effects, or implementation of the skill into Core. Preserve the existing Skill IDs and browser/JSON saves. Gameplay formulas are notes in the simulator; it only allocates points, not actual battle resolution. Historical descriptions in this README are superseded by v0.17 where they conflict.

## v0.18 — Stay Frosty effective REFLEX rework (2026-10-23)

The confirmed **Stay Frosty** skill (ID `certain-evasion`) has been redesigned as a conditional **effective REFLEX boost** while the Pilot holds an AVAILABLE Reaction from WAIT. The former bespoke, direct negative incoming-HitRaw modifier is superseded. All other confirmed Skill effects and stable Skill IDs are preserved.

- On sortie snapshot **base INSIGHT** after permanent pilot training; exclude temporary INSIGHT Skill bonuses (including First Watch). Use the base to calculate Lv1 **effective REFLEX +ceil(INSIGHT/6)**, Lv2 **+ceil(INSIGHT/4)**, Lv3 **+ceil(INSIGHT/3)**.
- Sample INSIGHT 10 gives **REFLEX +2/+3/+4**; INSIGHT 15 gives **+3/+4/+5**; INSIGHT 18 gives **+3/+5/+6**; INSIGHT 20 gives **+4/+5/+7**. The main Lv1–3 card fields show these numerical sample-Pilot REFLEX gains, recalculated from the user's INSIGHT point allocation; expanded per-Skill details retain the exact formulas.
- This is **effective REFLEX, not an extra bonus only on being attacked**. Apply it consistently in any otherwise eligible REFLEX-derived computation while Reaction is held: ordinary target defense, qualified guided-Missile terminal hit defense, Missile Intercept accuracy, and a committed qualifying COVER. For ordinary single-unit Direct FIRE / Melee, REFLEX +1 lowers attacker's pre-clamp HitRaw by 3; for Missile Intercept, REFLEX +1 increases InterceptHitRaw by 2. If an eligible attack is already above 100 HitRaw, the reduced attacker HitRaw also decreases prospective excess-accuracy CritPen (candidate design) under the same normal formula.
- If the Pilot **starts a legal INTERCEPT / COVER / Missile Intercept while Reaction is available**, the skill bonus applies through **that Reaction's own resolution**, even though the Reaction is consumed by the action's commit. It is no longer available for subsequent attacks or checks after the consumed Reaction. Merely being attacked, hitting or dodging does not itself consume Reaction. Unspent Reaction expires at the next own Faction Phase as usual; this may trigger separately purchased Steady Nerves.
- No new button, Reaction stock, cooldown or uses. `Got Your Six` may strengthen REFLEX further in an eligible ally-protection Reaction when both skills are learned; the *private Core Option* Defensive Response Suite's equipment/stacking treatment is still unresolved.
- The public simulator only models **Training Point allocations and per-skill sample values**, not actual battles, Reaction timing, or CritPen rolls. The private game Core and canonical specifications are not modified.

## v0.19 — Against the Odds (2026-10-26)

**Against the Odds** (new stable Skill ID `against-the-odds`) is added as an active research candidate. **English name is selected; numerical coefficients are research baselines, not final balance approval.** This is **not** a ninth confirmed Skill. Active catalogue: **32 Skills (8 confirmed, 24 provisional)**; archived Quick Study remains separate.

- **Concept:** A passive mental/combat-instinct technique that makes an infrequent successful Hit more likely to find an armor weakness when normal Hit Chance is low. It neither increases ordinary Hit Chance nor multiplies weapon Power. Applies to **both shooting and melee**, but only to attacks whose weapon has **CritPen YES**, and only when normal Penetration leaves `EffectiveArmor > 0`. No extra command, Action, Reaction, charge or currency.
- **Research formula:** Set `H = clamp(floor(HitRaw), 0, 100)`, `C0 = min(100, max(2, 4 + 0.5*(EffectiveSHOOTING_or_MELEE - 10)) + 0.5*max(0, floor(HitRaw)-100))`. For Skill level `L` in 1..3, `BonusRaw = min(10*L, 60*L*((100-H)/100)^2)`, `Bonus = floor(2*BonusRaw)/2` in percentage points, and `CritPenWithSkill = min(100, C0 + Bonus)`. Use half-point precision, existing CritPen qualification and usual probability clamp; this remains a study design only.
- **Examples:** At H=70%, Skill Bonuses are +5/+10.5/+16pt at Lv1/2/3, and with C0=4% the resulting conditional CritPen rates are 9/14.5/20%. At H=60% bonuses are +9.5/+19/+28.5pt, resulting in 13.5/23/32.5% with C0=4%. Increasing low-H effects and preserving high-H excess-accuracy rewards are deliberate. The possibility that a lower-H attack yields greater expected armor-bypass damage against very heavy armor is accepted as a potential tactical specialization, not an automatic reason for rejection.
- **Eligible melee under the current weapon table:** Combat Knife (CritPen YES). BASH, Assault Lance and Explosive Axe currently have CritPen NO. Current ranged NO weapons, guided Missile, Missile Intercept and Area/Hex attacks gain no CritPen.
- **Existing resolution preserved:** In ordinary multi-hit Direct FIRE, each attempt has its own Hit roll but the whole Attack has at most one CritPen roll, and only the corresponding successful Hit ignores Armor. Combat Knife's six-Hex AreaMelee treats each affected target as its own Melee Attack for CritPen eligibility. Do not grant repeated CritPen rolls to SMG/GPMG bursts.
- **Scope:** Skill Lab is a Training Point allocation simulator, not a combat simulator. New card and formula help illustrate prospective outcomes; no RNG, attack resolution or change to the private Core. Preserve existing Skill IDs and saved builds. Old README design-log paragraphs are historical and are overridden by the current main-repository canonical specifications where inconsistent.

## v0.20 — Provisional simultaneous paired-weapon FIRE skill (2026-10-26)

**Provisional card:** `二丁同時射撃（仮）` (`paired-fire`). The name and Lv1–3 penalties are **not finalized**. The Skill Lab now shows 33 active Skills (8 confirmed, 25 provisional), plus archived Quick Study.

**Proposed player behavior:** Equip two copies of exactly the same standard `UnitTargetedDirectFire` Weapon Definition and select either one for an ordinary FIRE. If both are eligible for firing, the passive skill automatically fires **both** at the same original Unit target. No extra active ability button or second Main Action is added. The 1 Main Action contains two independent weapon Attacks; both equipped entries retain distinct runtime ammunition identities and spend their normal `AmmoCostPerAttack`. No automatic retargeting on destruction.

**Provisional level values:** Lv1: both weapon Attack HitRaw values **−40 points**; Lv2 **−30 points**; Lv3 **−20 points**. Apply each penalty within its weapon's normal accuracy calculation, along with the usual shooter SHOOTING, target REFLEX, movement/terrain and other permitted situational modifiers; clamp to 0–100% per Hit attempt. Example with SHOOTING10, REFLEX10, no other modifier: SMG or Assault Rifle (ACC95) gives per-Hit 55/65/75%, and Shotgun (ACC105) 65/75/85%, across Lv1/2/3. The build planner shows these examples dynamically as the sample pilot's base SHOOTING changes; it does not simulate combat.

**Ammo, capacity, hit attempts:** SMG×2 has 3+3 Hit attempts and spends 3+3 Ready rounds; GPMG-6×2 has 2+2 attempts and spends 2+2 rounds; Shotgun/Assault Rifle/Sniper Rifle×2 each produces two single-shot Attacks with one round spent from each copy. Weapon capacity is paid twice: SMG/Assault Rifle/Shotgun pairs cost 2 (any Frame class); GPMG-6/Sniper Rifle pairs cost 4 (Heavy only). Each weapon's own RELOAD rules remain.

**CritPen:** Two independent weapon Attacks mean that a **CritPen YES** pair can make up to one CritPen roll **per weapon Attack** (two total), contingent on qualifying Hits and remaining effective Armor. In each Attack, success ignores armor for only its own eligible Hit. A Shotgun is CritPen NO and gains no CritPen. Against the Odds can stack on the two qualifying Attack calculations, but the combined Skill investment at Lv3+Lv3 would be six Training Points.

**Open mechanics / scope:** Final naming, balance, auto-single fallback when the second weapon is not ready, Reaction-INTERCEPT scope, and exact COVER/Exposure/Signature once-per-composite-action orchestration still require separate design work. The preferred concept gives only one original targeting/COVER/Exposure opportunity despite two weapon Attacks. Fired ammunition is spent for both as part of the committed composite action, with unneeded Hit attempts skipped after destruction. Presentation may depict simultaneous fire while Core resolves outcomes deterministically. Do not automatically extend the skill to missiles, direction-/Hex-targeted Area weapons, Melee, Missile Intercept or other attack families. No edits to private game Core and no confirmed individual Skill migration. This is a Training Point build planner, not a tactical simulator.


## v0.21 — First Watch design status reopened (2026-10-26)

First Watch (stable ID `early-starter`) is now **under review**, not confirmed. Its old level effects and INSIGHT-dependent duration remain provisional reference values; the Skill Lab saved builds and skill IDs are preserved. 33 active entries: 7 confirmed and 26 provisional. This change does not modify the private game's Core.

## v0.22 — Plant Your Feet / Keep Moving; observation deferred (2026-10-26)

**Current Skill Lab status:** 33 active entries, 9 Skill Lab design-confirmed and 24 provisional/on hold; 1 archived Quick Study. Changes here concern **research design**, not canonical individual Core Skill implementation. Existing Skill IDs, storage key and saved builds are unchanged.

### Plant Your Feet — design-confirmed

- Stable Skill ID: `marksmanship` (renamed from the provisional Japanese label 精密射撃).
- Passive trigger: make a qualifying **ordinary Unit-targeted Direct FIRE** before performing one's own ordinary MOVE in the same Activation. This requires a legal target Track, Range and Direct-Fire LOS before moving; moving afterward via a valid MSU sequence does **not** disqualify the shot retroactively. A Light Frame's post-action DISPLACE similarly does not change an already-resolved FIRE.
- Effective SHOOTING is **+2 / +4 / +6** for Lv1 / Lv2 / Lv3. In normal unit-target accuracy, that contributes **+6 / +12 / +18 HitRaw points** before clamp. The approved effective-Ability/excess-HitRaw CritPen design uses the same applicable effective SHOOTING. No extra ammo, dedicated Action or Skill-charge system.
- This confirmation covers the normal own-Activation Unit-targeted FIRE use discussed. Reaction INTERCEPT and special attack families are **not automatically broadened** by this entry. Original Fire Control Stabilizer Option remains in private Core; its eventual migration/replacement and stacking are separately open.

### Keep Moving — design-confirmed

- Stable Skill ID: `mobile-evasion` (renamed from provisional 機動回避).
- Passive trigger: successfully enter **at least 3 actual Hexes** during the Pilot's own **ordinary MOVE**. The third successful Hex entry activates the effect, not a planned path length or 3 Movement-cost points. If movement is halted earlier, it never activates. REPOSITION and Light DISPLACE do not supply qualifying ordinary-MOVE entries.
- Effective REFLEX **+2 / +4 / +6** at Lv1 / Lv2 / Lv3; effect persists through intervening Faction Phases and expires at start of the Unit's next own Faction Phase. In normal direct-fire or Melee defense, attacker HitRaw is reduced by **6 / 12 / 18** points; other otherwise-eligible effective REFLEX uses (including guided missile terminal defense and Missile Intercept) also receive the bonus through their respective formulas. Missile Intercept's coefficient 2 yields **+4 / +8 / +12** accuracy points while this Skill is active.
- Movement can expose the Pilot to enemy sensors/INTERCEPT; eligible weapons may incur their ordinary self-movement firing modifiers. No separate gauge, penalty or command is invented. The existing Maneuver Assist System (MAS) Option remains in the private Core; eventual removal/stacking and full migration details are separately open.

### Reopened / deferred candidates

- **First Watch** (ID `early-starter`): remains *under review* following v0.21; former INSIGHT-based duration and Lv1–3 values are comparison material, not confirmed design.
- **定点観測** (ID `observation-discipline`): **on hold**. The former stationary Activation completion → INSIGHT +4/+8/+12 design is historical comparison data, not adopted. MOVE→WAIT or WAIT-only variants were explored but are not approved: WAIT is often the default when a moved unit has no legal attack, and passive extended detection risks displacing the distinct ACTIVE SCAN action. Do not add a complex second WAIT variant or suppress the normal Reaction as a forced cost.
- All other Skill Lab confirmed/provisional entries retain their prior state. The independent Skill Lab remains an allocation/suggestion tool, not a combat simulator.


## v0.23 — Reopen three WAIT / Reaction skill designs (2026-10-26)

The user requested that **every confirmed WAIT / Reaction Skill except Got Your Six** return to design review. These three Skill Lab cards now have status **under review**, without removing or archiving their prior effects and Lv1–3 research values:

- `reaction-shooter` — Right on Cue
- `burst-focus` — Steady Nerves
- `certain-evasion` — Stay Frosty

**Got Your Six** (`guardian-reaction`) remains **confirmed**. The other five confirmed entries are Frame Combat Proficiency (Light / Standard / Heavy), Plant Your Feet, and Keep Moving. First Watch remains under review and 定点観測 remains on hold. The total active catalogue is unchanged at **33**: **6 confirmed / 27 provisional or on hold**. Archived Quick Study remains 1.

These are status changes only, not automatic balance adjustments. The former formulas and effect details stay accessible for design comparisons; Skill IDs, point-allocation behavior, JSON imports/exports and existing browser saves stay intact. Historical README sections describing older confirmed counts and effects remain dated design history, superseded for current status by this v0.23 record. Nothing is migrated to, or changed in, the private production Core.
