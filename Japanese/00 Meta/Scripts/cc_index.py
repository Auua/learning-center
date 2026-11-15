#!/usr/bin/env python3
"""
Rakentaa command-centerin lukuindeksin vaultista (ADR-040).

Lukee tyypitetyt muistiinpanot (vocab, verb, kanji, grammar) niiden omista
kansioista, ratkaisee esimerkkilauseiden upotukset (![[Lausepankki — X#^id]])
sekä "## Esimerkit" -luettelon omat rivit (- 日本語 — käännös ![[ääni]]),
poimii kanjien "## Muistisääntö" -osion tekstin (ADR-041: `mnemonic`)
ja kirjoittaa yhden JSON-rivin per muistiinpano tiedostoihin

    .cc/index/{vocab,verb,kanji,grammar}.jsonl      (tai .NNN.jsonl-shardit)
    .cc/index/manifest.json

Indeksi on johdettua dataa: se generoidaan aina kokonaan uudelleen eikä sitä
muokata käsin. Vaadittujen kenttien lista (REQUIRED) tulee check_vault.py:stä,
jotta molemmat skriptit pitävät saman totuuden.

Ajo (mistä tahansa hakemistosta):
    python3 "Japanese/00 Meta/Scripts/cc_index.py"
    python3 "Japanese/00 Meta/Scripts/cc_index.py" --repo /polku/learning-center

Paluuarvo 0 aina kun indeksi kirjoitettiin; ohitetut muistiinpanot listataan
manifestin errors-kentässä eivätkä kaada ajoa.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from check_vault import REQUIRED  # noqa: E402  (sama totuus kuin eheystarkistuksella)

SCHEMA_VERSION = 1
VAULT_DIR = "Japanese"
INDEX_DIR = Path(".cc") / "index"
SKIP_DIRS = {".obsidian", ".trash", ".git", "Templates"}
SHARD_BYTES = 1_000_000  # ADR-024: shard ~500 riviin kun tiedosto ylittää ~1 MB
SHARD_LINES = 500

# kind -> (type, kansio vaultin sisällä)
KINDS = {
    "vocab": ("vocab", "30 Sanasto/Sanat"),
    "verb": ("verb", "20 Verbit/Lekseemit"),
    "kanji": ("kanji", "40 Kanji/Merkit"),
    "grammar": ("grammar", "10 Kielioppi/Pisteet"),
}

# Kenttien nimet sellaisina kuin vault ne nimeää (ADR-040: ei uudelleennimeämistä).
COMMON_FIELDS = ["jlpt", "status", "confidence", "reviewed", "created", "sources", "tags"]
KIND_FIELDS = {
    "vocab": ["word", "reading", "romaji", "meaning", "pos", "pitch", "kanji", "sets", "similar", "opposite"],
    "verb": ["word", "reading", "romaji", "meaning", "verbclass", "transitivity", "pair", "kanji", "sets"],
    "kanji": ["kanji", "strokes", "grade", "onyomi", "kunyomi", "meaning", "components", "lookalikes"],
    "grammar": ["ja", "reading", "meaning", "func", "attaches", "formality", "register", "similar", "compare"],
}
LIST_FIELDS = {
    "sources", "tags", "kanji", "sets", "similar", "opposite", "pitch", "onyomi", "kunyomi",
    "components", "lookalikes", "func", "attaches", "register",
}
INT_FIELDS = {"confidence", "strokes"}
# Pakollinen kenttä, jonka tyhjä lista on silti pätevä arvo: kun-lukuisilla
# kanjeilla (匂, 峠, 畑 …) ei ole on-lukutapaa, ja `onyomi: []` sanoo juuri sen.
EMPTY_LIST_OK = {("kanji", "onyomi")}

EMBED_RE = re.compile(r"!\[\[([^\]|#]+)#\^([\w\-]+)(?:\|[^\]]*)?\]\]")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]*))?\]\]")
SOURCE_RE = re.compile(r"^\[\[([^\]#|]+)(?:#(?:Luku|Lesson|Chapter)?\s*(\d+))?[^\]]*\]\]$")
MEANING_LINE_RE = re.compile(r"^\s*-\s*\*\*(FI|EN)\s*:\*\*\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BLOCK_ID_RE = re.compile(r"^\^([\w\-]+)\s*$")
SENTENCE_LINE_RE = re.compile(r"^\*\*(JA|FI)\*\*\s+(.*)$")
BULLET_RE = re.compile(r"^\s*-\s+(.*\S)\s*$")
QUOTE_MARK_RE = re.compile(r"^\s*(?:>\s?)+")  # lainausmerkit, myös sisäkkäiset
CALLOUT_RE = re.compile(r"^\[![\w-]+\][+-]?\s*")  # > [!warning] Otsikko -> Otsikko
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ANY_EMBED_RE = re.compile(r"!\[\[[^\]]*\]\]")  # ääniupotukset ![[tts_x.m4a]], ![[anki_x.mp3]]
TRAILING_SOURCE_RE = re.compile(r"\s*\(\s*\[\[[^\]]*\]\]\s*\)\s*$")  # "… ([[Minna no Nihongo I#Luku 2]])"
JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")
SENTENCE_END_SPLIT_RE = re.compile(r"^(.*[。！？])\s+(\S.*)$")  # erotinta ei ole: katkaistaan viimeiseen japanin lauseenloppuun
FINNISH_HINT_RE = re.compile(r"[äöåÄÖÅ]")
# Englannin pikkusanat ja kliitit, joista yksikään ei ole suomen sana (ei "on", "he", "me", "no"…).
ENGLISH_HINT_RE = re.compile(
    r"\b(the|is|are|was|were|be|been|you|she|it|we|they|him|his|her|them|their|our|us|my|your|this|that"
    r"|these|those|not|a|an|to|of|in|at|on\b(?= the\b)|and|or|but|if|so|as|for|from|with|by|about|into"
    r"|do|does|did|have|has|had|will|would|can|could|should|get|got|go|went|please|very|just|than|then"
    r"|when|what|who|how|why|where|there|here|one|all|any|some|more|most|much|many|like|make|I)\b"
    r"|\w('s|n't|'m|'re|'ve|'ll|'d)\b"
    r"|\b[a-z]{3,}(ed|ing)\b"  # englannin -ed/-ing-päätteet, joita suomessa ei ole
)


# ---------------------------------------------------------------- front-matter

def split_frontmatter(text: str) -> tuple[list[str], str]:
    """Palauttaa (front-matter-rivit, runko). Tyhjä lista jos lohkoa ei ole."""
    if not text.startswith("---"):
        return [], text
    lines = text.split("\n")
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[1:index], "\n".join(lines[index + 1 :])
    return [], text


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def split_inline_list(inner: str) -> list[str]:
    """Jakaa `a, "b, c", [[d]]` pilkuista lainausmerkkien ja [[...]]-linkkien ulkopuolella."""
    items: list[str] = []
    current: list[str] = []
    quote: str | None = None
    depth = 0
    for char in inner:
        if quote:
            current.append(char)
            if char == quote:
                quote = None
            continue
        if char in "\"'":
            quote = char
            current.append(char)
            continue
        if char == "[":
            depth += 1
        elif char == "]":
            depth = max(0, depth - 1)
        if char == "," and depth == 0:
            items.append("".join(current))
            current = []
            continue
        current.append(char)
    items.append("".join(current))
    return [unquote(item) for item in items if item.strip()]


def parse_frontmatter(lines: list[str]) -> dict[str, object]:
    """Regex-pohjainen YAML-osajoukko: skalaari, [inline, lista], tai
    monirivinen `- item`-lista. Riittää vaultin pohjille (ks. check_vault.py)."""
    result: dict[str, object] = {}
    key: str | None = None
    for line in lines:
        item = re.match(r"^\s+-\s*(.*)$", line)
        if item and key is not None and isinstance(result.get(key), list):
            result[key].append(unquote(item.group(1)))  # type: ignore[union-attr]
            continue
        match = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
        if not match:
            continue
        key, raw = match.group(1), match.group(2).strip()
        if raw == "":
            # Joko tyhjä arvo tai monirivisen listan aloitus; päätetään seuraavilla riveillä.
            result[key] = [] if key in LIST_FIELDS else ""
        elif raw.startswith("[") and raw.endswith("]"):
            result[key] = split_inline_list(raw[1:-1])
        else:
            result[key] = unquote(raw)
    return result


def normalise(field: str, value: object) -> object:
    if field in LIST_FIELDS:
        if value in ("", None):
            return []
        if isinstance(value, list):
            return [str(item) for item in value if str(item).strip()]
        return [str(value)]
    if isinstance(value, list):
        value = ", ".join(value)
    if value in ("", None):
        return None
    if field in INT_FIELDS:
        try:
            return int(str(value))
        except ValueError:
            return None
    return str(value)


def normalise_scalar(value: object) -> object:
    if isinstance(value, list):
        value = ", ".join(str(item) for item in value)
    return None if value in ("", None) else str(value)


def source_key(sources: list[str]) -> dict[str, object] | None:
    """Ensimmäinen lähdelinkki -> {book, chapter} (ADR-040: kielioppijärjestys)."""
    if not sources:
        return None
    match = SOURCE_RE.match(sources[0].strip())
    if not match:
        return {"book": sources[0].strip(), "chapter": None}
    chapter = match.group(2)
    return {"book": match.group(1).strip(), "chapter": int(chapter) if chapter else None}


# ---------------------------------------------------------------------- body

def body_sections(body: str) -> dict[str, list[str]]:
    """Otsikko -> rivit otsikon alla (ensimmäinen esiintymä)."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.split("\n"):
        heading = HEADING_RE.match(line)
        if heading:
            current = heading.group(2)
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return sections


def meaning_lines(sections: dict[str, list[str]]) -> dict[str, str | None]:
    out: dict[str, str | None] = {"fi": None, "en": None}
    for line in sections.get("Merkitys", []):
        match = MEANING_LINE_RE.match(line)
        if match:
            lang = match.group(1).lower()
            if out[lang] is None and match.group(2).strip():
                out[lang] = match.group(2).strip()
    return out


def strip_wikilinks(text: str) -> str:
    return WIKILINK_RE.sub(lambda m: (m.group(2) or m.group(1)).strip(), text)


class SentenceBank:
    """Ratkaisee ![[Tiedosto#^id]]-upotukset: lohko = rivit tyhjästä rivistä ^id-riviin."""

    def __init__(self, vault: Path):
        self.vault = vault
        self.by_stem: dict[str, Path] = {}
        for path in vault.rglob("*.md"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            self.by_stem.setdefault(path.stem, path)
        self._blocks: dict[Path, dict[str, list[str]]] = {}

    def _blocks_of(self, path: Path) -> dict[str, list[str]]:
        cached = self._blocks.get(path)
        if cached is not None:
            return cached
        blocks: dict[str, list[str]] = {}
        pending: list[str] = []
        for line in path.read_text(encoding="utf-8").split("\n"):
            block_id = BLOCK_ID_RE.match(line.strip())
            if block_id:
                blocks[block_id.group(1)] = pending
                pending = []
                continue
            if line.strip() in ("", "---"):
                pending = []
                continue
            pending.append(line)
        self._blocks[path] = blocks
        return blocks

    def resolve(self, stem: str, block_id: str) -> dict[str, object] | None:
        path = self.by_stem.get(stem.strip())
        if path is None:
            return None
        lines = self._blocks_of(path).get(block_id)
        if lines is None:
            return None
        sentence: dict[str, object] = {"ja": None, "fi": None, "ref": f"{stem.strip()}#^{block_id}"}
        for line in lines:
            match = SENTENCE_LINE_RE.match(line.strip())
            if match and sentence[match.group(1).lower()] is None:
                sentence[match.group(1).lower()] = strip_wikilinks(match.group(2)).strip()
        if sentence["ja"] is None:
            return None
        return sentence


def translation_lang(text: str) -> str:
    """Käännöksen kieli: ääkköset → fi, englannin pikkusana → en, muuten fi (vaultin oletuskieli)."""
    if FINNISH_HINT_RE.search(text):
        return "fi"
    lowered = re.sub(r"\bI\b", "I", text.lower())
    if ENGLISH_HINT_RE.search(lowered) or re.search(r"\bI\b", text):
        return "en"
    return "fi"


def inline_example(line: str, ref: str) -> dict[str, object] | None:
    """Luettelorivi "- 日本語 — käännös ![[ääni]]" → esimerkki, tai None jos rivillä ei ole japania."""
    bullet = BULLET_RE.match(line)
    if not bullet:
        return None
    text = TRAILING_SOURCE_RE.sub("", ANY_EMBED_RE.sub("", bullet.group(1))).strip()
    text = strip_wikilinks(text).strip()
    if not text:
        return None
    if " — " in text:
        ja, translation = (part.strip() for part in text.split(" — ", 1))
    else:
        split = SENTENCE_END_SPLIT_RE.match(text)
        ja, translation = (split.group(1).strip(), split.group(2).strip()) if split else (text, "")
    if not JAPANESE_RE.search(ja):
        return None
    example: dict[str, object] = {"ja": ja, "fi": None, "en": None, "ref": ref}
    if translation:
        example[translation_lang(translation)] = translation
    return example


def examples_from(
    sections: dict[str, list[str]], bank: SentenceBank, errors: list[str], stem: str
) -> list[dict[str, object]]:
    """Esimerkit dokumenttijärjestyksessä: lausepankkiupotukset ratkaistuina, muut rivit sellaisinaan."""
    out: list[dict[str, object]] = []
    for line in sections.get("Esimerkit", []):
        embeds = EMBED_RE.findall(line)
        if embeds:
            for embed_stem, block_id in embeds:
                resolved = bank.resolve(embed_stem, block_id)
                if resolved is None:
                    errors.append(f"unresolved example {embed_stem}#^{block_id}")
                else:
                    out.append({**resolved, "en": None})
            continue
        inline = inline_example(line, f"{stem}#Esimerkit")
        if inline is not None:
            out.append(inline)
    return out


def mnemonic_from(sections: dict[str, list[str]]) -> str | None:
    """`## Muistisääntö` pelkkänä tekstinä; tyhjä osio (pelkkä `>`) -> None.

    Lainausmerkit ja callout-tunniste pois, wikilinkit näkyväksi tekstikseen,
    lihavoinnin tähdet pois (kortti näyttää tekstin sellaisenaan). Rivinvaihdot
    säilyvät kappaleen sisällä, kappaleiden välissä on yksi tyhjä rivi.
    """
    paragraphs: list[list[str]] = [[]]
    for raw in sections.get("Muistisääntö", []):
        line = CALLOUT_RE.sub("", QUOTE_MARK_RE.sub("", raw).strip())
        line = BOLD_RE.sub(r"\1", strip_wikilinks(ANY_EMBED_RE.sub("", line))).strip()
        if line:
            paragraphs[-1].append(line)
        elif paragraphs[-1]:
            paragraphs.append([])
    text = "\n\n".join("\n".join(lines) for lines in paragraphs if lines)
    return text or None


# --------------------------------------------------------------------- index

def is_missing(kind: str, field: str, value: object) -> bool:
    if (kind, field) in EMPTY_LIST_OK and value in ([], "[]"):
        return False  # kenttä on kirjoitettu, ja se on tarkoituksella tyhjä
    return value in ("", None, [], "[]", '""')


def index_note(kind: str, path: Path, repo: Path, bank: SentenceBank) -> tuple[dict[str, object] | None, list[str]]:
    rel = path.relative_to(repo).as_posix()
    text = path.read_text(encoding="utf-8")
    fm_lines, body = split_frontmatter(text)
    if not fm_lines:
        return None, [f"{rel}: no front-matter"]
    fm = parse_frontmatter(fm_lines)
    expected_type = KINDS[kind][0]
    note_type = str(fm.get("type", "")).strip('"')
    if note_type != expected_type:
        return None, [f"{rel}: type is '{note_type}', expected '{expected_type}'"]

    missing = [
        field
        for field in REQUIRED.get(expected_type, [])
        if is_missing(kind, field, fm.get(field))
    ]
    if missing:
        return None, [f"{rel}: missing {', '.join(missing)}"]

    note_errors: list[str] = []
    sections = body_sections(body)
    record: dict[str, object] = {"path": rel, "type": expected_type}
    for field in COMMON_FIELDS + KIND_FIELDS[kind]:
        # `kanji` on kanji-muistiinpanossa itse merkki (skalaari), sanoissa lista.
        as_list = field in LIST_FIELDS and not (kind == "kanji" and field == "kanji")
        value = fm.get(field, [] if as_list else "")
        record[field] = normalise_scalar(value) if (field in LIST_FIELDS and not as_list) else normalise(field, value)
    record["source"] = source_key(record["sources"])  # type: ignore[arg-type]
    meaning = meaning_lines(sections)
    record["meaning"] = {"fi": meaning["fi"] or record.get("meaning"), "en": meaning["en"]}
    record["examples"] = examples_from(sections, bank, note_errors, path.stem)
    if kind == "kanji":
        record["mnemonic"] = mnemonic_from(sections)
    record["cards"] = sum(1 for line in sections.get("Kortit", []) if "::" in line or line.strip() == "?")
    return record, [f"{rel}: {error}" for error in note_errors]


def git_sha(repo: Path) -> str | None:
    env_sha = os.environ.get("GITHUB_SHA")
    if env_sha:
        return env_sha
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def write_shards(index_dir: Path, kind: str, records: list[dict[str, object]]) -> list[str]:
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records]
    total = sum(len(line.encode("utf-8")) + 1 for line in lines)
    if total <= SHARD_BYTES:
        (index_dir / f"{kind}.jsonl").write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        return [f"{kind}.jsonl"]
    names: list[str] = []
    for start in range(0, len(lines), SHARD_LINES):
        name = f"{kind}.{start // SHARD_LINES:03d}.jsonl"
        (index_dir / name).write_text("\n".join(lines[start : start + SHARD_LINES]) + "\n", encoding="utf-8")
        names.append(name)
    return names


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", type=Path, default=SCRIPT_DIR.parents[2], help="repon juuri (oletus: skriptistä päätelty)")
    args = parser.parse_args()
    repo = args.repo.resolve()
    vault = repo / VAULT_DIR
    if not vault.is_dir():
        print(f"vault-kansiota ei löydy: {vault}", file=sys.stderr)
        return 2

    index_dir = repo / INDEX_DIR
    index_dir.mkdir(parents=True, exist_ok=True)
    for stale in index_dir.glob("*.jsonl"):
        stale.unlink()

    bank = SentenceBank(vault)
    counts: dict[str, int] = {}
    shards: dict[str, list[str]] = {}
    errors: list[str] = []
    skipped: dict[str, int] = {}

    for kind, (_, folder) in KINDS.items():
        records: list[dict[str, object]] = []
        skipped[kind] = 0
        for path in sorted((vault / folder).glob("*.md"), key=lambda p: p.relative_to(repo).as_posix()):
            record, note_errors = index_note(kind, path, repo, bank)
            errors.extend(note_errors)
            if record is None:
                skipped[kind] += 1
            else:
                records.append(record)
        counts[kind] = len(records)
        shards[kind] = write_shards(index_dir, kind, records)

    manifest = {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "sha": git_sha(repo),
        "counts": counts,
        "skipped": skipped,
        "shards": shards,
        "errors": sorted(errors),
    }
    (index_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(f"index -> {index_dir.relative_to(repo)}")
    for kind in KINDS:
        print(f"  {kind:8s} {counts[kind]:5d} indexed, {skipped[kind]:3d} skipped, {len(shards[kind])} file(s)")
    print(f"  errors   {len(errors)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
