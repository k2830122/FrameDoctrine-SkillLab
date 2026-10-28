# MTG card-name research for FRAME DOCTRINE: LAST RESORT

Status: **research only** (2026-10-29). No official skill names, balance values,
Skill Lab UI, or main-game code were changed.

## What is here

- `catalog/expansions-01.tsv` through `expansions-08.tsv`: a lightly filtered,
  linkable snapshot of names from **114 MTG expansion sets, 1994–2026**.
- `build_oracle_catalog.py`: an independent script for building a broader
  catalog from the Scryfall **Oracle Cards bulk download** (all card types and
  non-expansion products, including digital-only cards, rather than only
  expansion sets). It has NOT been run in this environment because the Scryfall
  download host cannot be reached from the local execution environment.
- `SHORTLIST.md`: aesthetic nominations, brief source-card effects, and a
  deliberately provisional 14-skill naming lineup, separately from the raw catalog.

## Snapshot methodology and scope

Source: [nwgarne/mtg-setlists](https://github.com/nwgarne/mtg-setlists), a public
set-by-set card index with [Scryfall](https://scryfall.com/) card links.

| Measure | Count |
| --- | ---: |
| Expansion sets examined | 114 |
| Card rows examined (includes reprints and versions) | 31,200 |
| Rows after lexical filtering and exact-name deduplication **within each batch** | 21,396 |
| Distinct names **across all eight batches** | 20,731 |

The TSV files have a comment preamble. The tabular columns are:
`name`, `set`, `type`, `scryfall_url`.
They intentionally contain creature, land, artifact, enchantment, instant,
and sorcery names alike.

**Only mechanical exclusions were applied:**
1. Explicit personal pronouns and possessives (you/your/them/their/our etc.).
2. Apostrophe-s (`'s` / `’s`) anywhere.
3. A word whose spelling ends in `-ing`.

No restrictions on word count, rigid military terminology, poetic imagery,
name-to-effect similarity, or particular part of speech were applied.
Terms rooted in MTG lore and other licensed properties remain in the raw
catalog **on purpose**; human curation must exclude inappropriate names.
A name in the catalog is not an endorsement or a design proposal.

**Coverage caveat:** The checked-in snapshot covers expansion-set cards, not
all unique MTG cards. It also excludes very small expansion entries and
non-expansion cards, even though excellent names may exist there. Duplicates
may recur between TSV batches; the global distinct-name count deduplicates
those records. The Oracle script is the recommended future path to improve
coverage.

## Refresh from the fuller Scryfall catalog

Scryfall's [bulk-data documentation](https://scryfall.com/docs/api/bulk-data)
describes the Oracle Cards export (one record per Oracle identity).
The script resolves the *current* download URI, handles modern JSONL/GZip
and older JSON exports, and uses the same lexical exclusions.

```bash
python3 research/mtg-names/build_oracle_catalog.py --output /tmp/mtg-oracle-eligible.tsv
```

For local design analysis only, optionally add `--with-text` to export Oracle
rules text. **Do not commit bulk copyrighted card text**. When proposing an
individual name, consult its Scryfall URL, summarize the original card effect
in Japanese, and evaluate how the name feels independently from the effect.

## Naming rules / design policy

The goal is a **coherent group of 14 appealing names**, not fourteen literal
translations of skill behavior. The original card's rules text is background,
not a constraint on which skill may receive that name.

- Prefer naturally memorable English names that fit military science fiction
  in combination. Length and grammatical structure can vary.
- Avoid proprietary character/place names, out-of-setting fantasy imagery,
  accidental comedy (e.g. `High Ground`), and repeated distinctive words
  across unrelated skills.
- Keep the shared chassis qualifier for the Light / Standard / Heavy series.
- Treat all assignments as provisional until the designer chooses them.
- Do not modify official Skill Lab skill definitions as part of this research.
