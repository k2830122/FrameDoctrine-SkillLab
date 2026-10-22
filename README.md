# FRAME DOCTRINE — PILOT SKILL LAB

A standalone browser-based simulator for experimental pilot skill builds in FRAME DOCTRINE: LAST RESORT.

**Status:** Research prototype v0.5. The game project itself is separate and is not included in this public repository. None of the proposed skills or balance numbers are official game specifications.

## Features

- 25 experimental pilot skills (original research ideas and Option-inspired candidates)
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

When a Skill says it grants an effective Ability bonus (SHOOTING, MELEE, SENSOR or REFLEX), the intended *research direction* is to use the resulting effective Ability in all relevant calculations, rather than granting narrow +Hit% / +Evasion% substitutions. This still requires explicit combat-design review before any change to the private Core.

This app currently simulates **training-point allocation only**, not on-map kill events, HP reductions, Action outcomes, or chance rolls.

## Ability cap removal and limited guaranteed outcomes (2026-10-23)

**New accepted research direction (not yet canonical Core):**
- Remove the numeric ceiling on both *base* and *effective* Pilot Abilities (SHOOTING, MELEE, SENSOR, REFLEX). A player may continue investing Training Points into a base Ability past 20, subject to their finite Training Point budget.
- Conditional Skill boosts stack into the effective Ability and use that full value consistently in all relevant Ability-dependent calculations.
- Extreme accuracy and evasion are allowed to become correspondingly strong. Probability quantities, however, are still bounded by 0–100%; removing an Ability ceiling is **not** removing probability bounds.
- Balance through finite growth points, real activation conditions, opportunity costs and build tradeoffs, not a universal ability ceiling. Do not silently migrate this rule into the private game Core or master specs.

**New speculative Skills (not approved effects):**
- **必中の一撃 / Decisive Shot:** a limited number of eligible attacks per Mission become guaranteed hits; draft ranks allow 1/2/3 uses. Prefer an understandable passive/conditional trigger over another active command. What counts as an eligible attack, how a use is spent and whether a 100% base hit consumes it remain unresolved.
- **完全回避 / Certain Evasion:** evade exactly one qualifying incoming attack after a preparation cost. Working non-active version is to use existing WAIT as its trigger, with 1/2/3 prepared guaranteed evades per Mission by rank. This is a proposal, not approval of specific timing or effect.
- In interactions between guaranteed hit and guaranteed dodge, the governing priority is **undecided**. Direct Fire vs Missile vs Area/multi-hit and interactions with critical penetration need explicit rules. Do not infer priorities from the labels alone.

The skill-list page models **purchase allocation**, not true combat resolution or activation charges. These new entries are deliberately labeled exploratory.

## 2026-10-23 — effective Ability rework of the original 19 skills

The Skill Lab now shows the research redesign on all 19 original candidates, retaining all 6 later rough ideas (25 total) and stable IDs for saved builds. **No Core changes are authorized.** Existing Option mechanics remain untouched.

**Research principle:** When a Skill grants conditional Ability +N or −N, use that *effective* Ability consistently in **all otherwise eligible formulas** that use SHOOTING, MELEE, SENSOR, or REFLEX, instead of one-off Hit/Evasion percentage exceptions. Conditional skills do not mutate the underlying base value. Base and effective Ability caps are removed *in the research design*; probability outputs still use ordinary 0–100% rules.

New compare-only Lv1/2/3 values:

- Frame Proficiency L/S/H: SHOOTING and MELEE +1/+2/+3 (not REFLEX).
- Early Starter, Solo Operator: SHOOTING and REFLEX +1/+2/+3.
- Precision Shooting, Mobile Evasion, Momentum Melee: relevant SHOOTING/REFLEX/MELEE +2/+4/+6 respectively, with existing stationary or 3-Hex movement trigger.
- Ordinary INTERCEPT specialist: SHOOTING +2/+4/+6 only during qualifying ordinary INTERCEPT.
- Burst Focus: selected Ability +2/+4/+6 (activation economics unresolved).
- Night/Adverse Weather, Stationary Observation, Active Scan Interpretation: SENSOR +4/+8/+12 under their respective conditions (strong provisional values; Active Scan Skill remains unapproved).
- Suppressive Fire: target effective REFLEX −1/−2/−3 for rest of firing Faction Phase; full applicable REFLEX semantics, not a special +Hit% buff.
- Guardian Reaction: REFLEX +1/+2/+3 when protecting an ally (Skill migration on hold).
- Stationary penetration, Lance charge penetration, BRACE Armor, CONCEAL Signature: remain special-effect skills; not all effects should be expressed as Ability gains.

The app is only a **point-allocation simulator**. Conditional skills are not automatically added to the base-Ability numbers in the pilot panel, because no battlefield conditions have been simulated; see each skill's trigger and effect instead. All new numeric proposals are marked provisional.
