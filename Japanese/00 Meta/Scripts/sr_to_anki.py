#!/usr/bin/env python3
"""
Poimii Obsidian Spaced Repetition -syntaksilla kirjoitetut kortit vaultista
ja kirjoittaa Ankiin tuotavan TSV-tiedoston.

Tuetut muodot (sen jälkeen kun rivillä on esiintynyt #flashcards-tagi):
    Etu::Taka          yksisuuntainen inline-kortti
    Etu:::Taka         kaksisuuntainen inline-kortti (tuottaa kaksi korttia)
    Etu
    ?
    Taka               monirivinen kortti

Ajo:
    python3 "00 Meta/Scripts/sr_to_anki.py"
    python3 "00 Meta/Scripts/sr_to_anki.py" --out /polku/anki.tsv --deck "Japani"

UID-sarake on vakaa (sha1 tiedostopolusta + etupuolesta), joten sama kortti
päivittyy uudelleentuonnissa eikä monistu.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

SKIP_DIRS = {".obsidian", ".trash", ".git", "Templates"}
TAG_RE = re.compile(r"#flashcards(?:/[\w\-/åäöÅÄÖ]+)?")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
FM_TAG_LINE = re.compile(r"^\s*(jlpt|type)\s*:\s*(.+)$")


def clean(text: str) -> str:
    """Wikilinkit tekstiksi, rivinvaihdot <br>-tageiksi, tabit pois."""
    text = WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = text.replace("\t", " ").strip()
    return "<br>".join(line.strip() for line in text.split("\n") if line.strip())


def anki_tag(obsidian_tag: str) -> str:
    return obsidian_tag.lstrip("#").replace("/", "::")


def uid_for(relpath: str, front: str) -> str:
    return hashlib.sha1(f"{relpath}|{front}".encode("utf-8")).hexdigest()[:16]


def parse_file(path: Path, vault: Path):
    rel = str(path.relative_to(vault))
    lines = path.read_text(encoding="utf-8").split("\n")

    extra_tags = []
    in_fm = False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_fm = True
            continue
        if in_fm:
            if line.strip() == "---":
                break
            m = FM_TAG_LINE.match(line)
            if m and m.group(1) == "jlpt":
                val = m.group(2).strip().strip('"')
                if val:
                    extra_tags.append(f"jlpt::{val.lower()}")

    cards = []
    current_tag = None
    in_code = False
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code or stripped.startswith("|") or stripped.startswith(">"):
            i += 1
            continue

        tag_match = TAG_RE.search(line)
        if tag_match:
            current_tag = tag_match.group(0)
            rest = line.replace(current_tag, "").strip()
            if not rest:
                i += 1
                continue
            line, stripped = rest, rest

        if current_tag is None:
            i += 1
            continue

        tags = [anki_tag(current_tag)] + extra_tags

        if ":::" in stripped:
            front, back = stripped.split(":::", 1)
            cards.append((clean(front), clean(back), rel, tags))
            cards.append((clean(back), clean(front), rel, tags))
            i += 1
            continue

        if "::" in stripped and "://" not in stripped:
            front, back = stripped.split("::", 1)
            if front.strip() and back.strip():
                cards.append((clean(front), clean(back), rel, tags))
            i += 1
            continue

        if stripped == "?":
            front_lines = []
            j = i - 1
            while j >= 0 and lines[j].strip() and not lines[j].strip().startswith("#"):
                front_lines.insert(0, lines[j])
                j -= 1
            back_lines = []
            k = i + 1
            while k < len(lines) and lines[k].strip() and lines[k].strip() not in ("---",):
                if lines[k].strip().startswith("#") or lines[k].strip().startswith("```"):
                    break
                back_lines.append(lines[k])
                k += 1
            front, back = clean("\n".join(front_lines)), clean("\n".join(back_lines))
            if front and back:
                cards.append((front, back, rel, tags))
            i = k
            continue

        i += 1

    return cards


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=str(Path(__file__).resolve().parents[2]))
    ap.add_argument("--out", default=None)
    ap.add_argument("--deck", default="Japani")
    ap.add_argument("--notetype", default="Japani (Obsidian)")
    args = ap.parse_args()

    vault = Path(args.vault).resolve()
    out = Path(args.out) if args.out else vault / "00 Meta" / "Scripts" / "anki_export.tsv"

    all_cards, files = [], 0
    for path in sorted(vault.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        cards = parse_file(path, vault)
        if cards:
            files += 1
            all_cards.extend(cards)

    seen, rows = set(), []
    for front, back, rel, tags in all_cards:
        uid = uid_for(rel, front)
        if uid in seen:
            continue
        seen.add(uid)
        rows.append((uid, front, back, rel, " ".join(sorted(set(tags)))))

    with out.open("w", encoding="utf-8") as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write(f"#notetype:{args.notetype}\n")
        f.write(f"#deck:{args.deck}\n")
        f.write("#tags column:5\n")
        for row in rows:
            f.write("\t".join(row) + "\n")

    print(f"{len(rows)} korttia {files} tiedostosta -> {out}")


if __name__ == "__main__":
    sys.exit(main())
