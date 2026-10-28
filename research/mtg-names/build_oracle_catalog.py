#!/usr/bin/env python3
"""Build an independent, minimally filtered English MTG name catalog from Scryfall.

The checked-in expansion TSV files are a reproducible *snapshot* from mtg-setlists.
This script is a separate way to rebuild from the fuller Scryfall Oracle Cards bulk export,
including non-expansion and digital-only cards. Requires Python 3.9+ and network access.

Usage:
    python research/mtg-names/build_oracle_catalog.py --output /tmp/mtg-oracle-eligible.tsv
    python research/mtg-names/build_oracle_catalog.py --output /tmp/mtg-oracle-text.tsv --with-text

Only the optional local --with-text export contains Oracle card text. Please do not
commit the full Oracle-text export to this repo; retain it only for research.
"""
import argparse
import csv
import gzip
import io
import json
import re
import sys
from urllib.request import Request, urlopen

API = "https://api.scryfall.com/bulk-data/oracle-cards"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "FrameDoctrineSkillNameResearch/1.0 (personal research; respect Scryfall API limits)",
}
FORBIDDEN = re.compile(
    r"\b(?:you|your|yours|they|them|their|theirs|we|us|our|ours|"
    r"i|me|my|mine|he|him|his|she|her|hers|it|its)\b|['’]s\b|\b[a-z-]*ing\b",
    re.I,
)


def is_eligible(name):
    """Remove only previously agreed lexical bans, not aesthetic judgments."""
    return bool(name and not FORBIDDEN.search(name))


def read_bulk_cards(url):
    """Prefer the smaller JSONL GZip format; support legacy JSON exports too."""
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=180) as res:
        if url.endswith(".gz"):
            with gzip.GzipFile(fileobj=res) as gz:
                for line in gz:
                    if line.strip():
                        yield json.loads(line)
        elif ".jsonl" in url:
            for line in res:
                if line.strip():
                    yield json.loads(line)
        else:
            # Legacy Scryfall .json files are large and use JSON arrays.
            # This fallback requires sufficient local memory.
            for card in json.load(res):
                yield card


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="mtg-oracle-eligible.tsv")
    ap.add_argument("--with-text", action="store_true", help="Include original Oracle text (local research only)")
    args = ap.parse_args()

    request = Request(API, headers=HEADERS)
    with urlopen(request, timeout=30) as res:
        meta = json.load(res)
    url = meta.get("jsonl_download_uri") or meta.get("download_uri")
    if not url or not url.startswith("https://data.scryfall.io/"):
        raise RuntimeError(f"Unexpected Scryfall bulk URL: {url}")
    print("Bulk updated:", meta.get("updated_at"), file=sys.stderr)

    names = {}
    scanned = 0
    for card in read_bulk_cards(url):
        scanned += 1
        name = card.get("name", "").strip()
        if card.get("lang", "en") != "en" or not is_eligible(name):
            continue
        # Exclude pure token / emblem / art card objects, not actual cards.
        if card.get("layout") in {"token", "double_faced_token", "emblem", "art_series"}:
            continue
        key = name.casefold()
        if key in names:
            continue
        text = card.get("oracle_text") or " // ".join(
            face.get("oracle_text", "") for face in card.get("card_faces", [])
        )
        names[key] = {
            "name": name,
            "type_line": card.get("type_line", ""),
            "set": card.get("set", ""),
            "scryfall_url": card.get("scryfall_uri", ""),
            "oracle_text": text.replace("\r", "").replace("\n", " / "),
        }

    fields = ["name", "type_line", "set", "scryfall_url"]
    if args.with_text:
        fields.append("oracle_text")
    with open(args.output, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(sorted(names.values(), key=lambda c: c["name"].casefold()))
    print(f"Scanned {scanned:,} Oracle objects; wrote {len(names):,} names to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
