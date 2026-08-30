#!/usr/bin/env python3
"""
Tarkistaa vaultin eheyden: puuttuvat frontmatter-kentät, ratkeamattomat
wikilinkit (myös .base-upotukset), orvot muistiinpanot ja korttien määrän.

Ajo:
    python3 "00 Meta/Scripts/check_vault.py"
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

SKIP_DIRS = {".obsidian", ".trash", ".git"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#^]+)")
FENCE_RE = re.compile(r"^```")

REQUIRED = {
    "grammar": ["jlpt", "attaches", "status"],
    "verb": ["reading", "verbclass", "jlpt"],
    "form": ["ja", "func"],
    "vocab": ["reading", "jlpt"],
    "kanji": ["strokes", "onyomi", "meaning"],
    "compare": ["members"],
    "source": ["kind"],
}


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def links_outside_code(text):
    out, in_code = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line.strip()):
            in_code = not in_code
            continue
        if in_code:
            continue
        out.extend(WIKILINK_RE.findall(line))
    return [l.strip() for l in out]


def main():
    vault = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2])
    files = [p for p in vault.rglob("*.md") if not any(x in SKIP_DIRS for x in p.parts)]
    bases = [p for p in vault.rglob("*.base") if not any(x in SKIP_DIRS for x in p.parts)]
    names = {p.stem for p in files} | {p.name for p in bases} | {p.stem for p in bases}

    missing = defaultdict(list)
    unresolved = defaultdict(list)
    inlinks = defaultdict(int)
    templates = 0
    cards = 0

    for p in files:
        text = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(vault))
        if "Templates" in p.parts:
            templates += 1
            continue
        cards += text.count("#flashcards")

        fm = frontmatter(text)
        t = fm.get("type", "").strip('"')
        for field in REQUIRED.get(t, []):
            val = fm.get(field, "")
            if not val or val in ("[]", '""'):
                missing[rel].append(field)

        for target in links_outside_code(text):
            if target not in names:
                unresolved[target].append(rel)
            else:
                inlinks[target] += 1

    orphans = sorted(
        p.stem for p in files
        if "Templates" not in p.parts and inlinks[p.stem] == 0
    )

    print(f"Tiedostoja: {len(files)} md + {len(bases)} base  (pohjia {templates})")
    print(f"Korttilohkoja: {cards}")

    print(f"\n--- Puuttuvia pakollisia kenttiä: {len(missing)} tiedostossa")
    for rel, fields in sorted(missing.items()):
        print(f"  {rel}: {', '.join(fields)}")

    print(f"\n--- Ratkeamattomia linkkejä: {len(unresolved)} kpl")
    print("    (nämä eivät ole virheitä — ne ovat seuraavat luotavat muistiinpanot)")
    for target, sources in sorted(unresolved.items(), key=lambda kv: -len(kv[1])):
        print(f"  [[{target}]]  <- {len(sources)} viittausta: {', '.join(sources[:3])}")

    print(f"\n--- Orpoja (ei sisääntulevia linkkejä): {len(orphans)} kpl")
    for name in orphans:
        print(f"  {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
