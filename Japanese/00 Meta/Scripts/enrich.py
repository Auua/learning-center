#!/usr/bin/env python3
"""
Sisällön rikastus (2026-10-11): ääni, esimerkkilauseet, käänteiskortit, JLPT-tagit.

Alikomennot (kaikki idempotentteja):
    sentences-audio   lisää TTS-ääni jokaiseen lausepankin lauseeseen
    sentence-cards    kirjoittaa lausepankkien loppuun  JA (kielioppi) ?? FI (kielioppi)  -kortit
    words-audio       lisää TTS-ääni sanoihin ja verbeihin joilta ääni puuttuu (--levels N5,N4,N3)
    reverse           vaihtaa sana- ja verbikorttien  ::  ->  :::  (kaksisuuntainen)
    retag             #flashcards/vocab -> #flashcards/vocab/n5 jne. (jlpt-kentän mukaan)
    forms             kirjoittaa taivutusmuotojen Kortit-osion verbityyppikorteilla
    todo              listaa muistiinpanot joilta esimerkki puuttuu  (--levels, --out)
    apply-examples    lukee  id|JA|FI -rivit ja kirjoittaa Esimerkit + ääni
    examples-audio    lisää TTS-äänen olemassa oleviin Esimerkit-riveihin "- JA — FI" (--levels)

Äänet: macOS `say -v Kyoko` -> m4a, tallennetaan kansioon 70 Visuaalinen/Audio/TTS/
(gitignoressa, luodaan tarvittaessa uudelleen). Tiedostonimi on tekstin tiiviste.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]            # .../Japanese
AUDIO = VAULT / "70 Visuaalinen" / "Audio" / "TTS"
BANKS = VAULT / "50 Lauseet"
VOCAB = VAULT / "30 Sanasto" / "Sanat"
VERBS = VAULT / "20 Verbit" / "Lekseemit"
FORMS = VAULT / "20 Verbit" / "Muodot"
VOICE = "Kyoko"

AUDIO_EMBED = re.compile(r"!\[\[[^\]]+\.(?:mp3|m4a|wav|ogg)\]\]", re.I)
FURIGANA = re.compile(r"\{([^|}]+)\|([^}]+)\}")
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def fm(text: str, key: str) -> str:
    m = re.search(rf"^{key}: *(.*)$", text, re.M)
    return m.group(1).strip().strip('"') if m else ""


# ------------------------------------------------------------------ TTS
def speakable(text: str) -> str:
    text = FURIGANA.sub(lambda m: m.group(2), text)
    text = WIKILINK.sub(lambda m: m.group(2) or m.group(1), text)
    text = re.sub(r"[*_`~～〜（）()＿\[\]]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def tts(text: str) -> str | None:
    """Palauttaa tiedostonimen (luo tarvittaessa). None jos teksti on tyhjä tai synteesi epäonnistuu."""
    text = speakable(text)
    if not text:
        return None
    name = "tts_" + hashlib.sha1(f"{VOICE}|{text}".encode()).hexdigest()[:12] + ".m4a"
    out = AUDIO / name
    if out.exists():
        return name
    AUDIO.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        aiff = Path(td) / "a.aiff"
        r = subprocess.run(["say", "-v", VOICE, "-o", str(aiff), "--", text], capture_output=True)
        if r.returncode or not aiff.exists():
            return None
        r = subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "48000", str(aiff), str(out)],
                           capture_output=True)
        if r.returncode or not out.exists():
            return None
    return name


def tts_many(texts):
    texts = list(dict.fromkeys(texts))
    with ThreadPoolExecutor(6) as ex:
        return dict(zip(texts, ex.map(tts, texts)))


# ------------------------------------------------------------------ lausepankit
BLOCK = re.compile(
    r"(?P<head>\*\*JA\*\* (?P<ja>.+)\n\*\*FI\*\* (?P<fi>.+)\n\*\*Kielioppi\*\* (?P<gr>.+)\n)(?P<audio>\*\*Ääni\*\* .+\n)?(?P<id>\^\S+)$",
    re.M)


def sentences_audio():
    files = sorted(BANKS.glob("*.md"))
    texts = []
    for p in files:
        texts += [m.group("ja") for m in BLOCK.finditer(p.read_text(encoding="utf-8"))]
    audio = tts_many(texts)
    added = 0
    for p in files:
        t = p.read_text(encoding="utf-8")

        def sub(m):
            nonlocal added
            if m.group("audio") or not audio.get(m.group("ja")):
                return m.group(0)
            added += 1
            return f"{m.group('head')}**Ääni** ![[{audio[m.group('ja')]}]]\n{m.group('id')}"

        new = BLOCK.sub(sub, t)
        if new != t:
            p.write_text(new, encoding="utf-8")
    print(f"{added} lauseelle lisätty ääni ({len(audio)} uniikkia tekstiä)")


CARD_START, CARD_END = "<!-- lausekortit:alku -->", "<!-- lausekortit:loppu -->"


def grammar_links(gr: str) -> str:
    """Kielioppirivin wikilinkit (ennen ensimmäistä ·-merkkiä) kortin sivuille."""
    head = gr.split(" · ")[0]
    links = WIKILINK.findall(head) or WIKILINK.findall(gr)
    return " ".join(f"[[{a}]]" for a, _ in links)


def sentence_cards():
    total = 0
    for p in sorted(BANKS.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        t = re.sub(rf"\n*## Kortit\n{re.escape(CARD_START)}.*?{re.escape(CARD_END)}\n?", "\n", t, flags=re.S)
        cards = []
        for m in BLOCK.finditer(t):
            g = grammar_links(m.group("gr"))
            ja = FURIGANA.sub(lambda x: x.group(1), m.group("ja"))
            side = lambda s: f"{s}\n{g}" if g else s
            cards.append(f"{side(ja)}\n??\n{side(m.group('fi'))}")
        if not cards:
            continue
        total += len(cards)
        body = f"\n## Kortit\n{CARD_START}\n#flashcards/lauseet\n\n" + "\n\n".join(cards) + f"\n{CARD_END}\n"
        p.write_text(t.rstrip("\n") + "\n" + body, encoding="utf-8")
    print(f"{total} lausekorttia")


# ------------------------------------------------------------------ sanojen ääni
def split_section(text: str, heading: str):
    m = re.search(rf"^## {re.escape(heading)}\n", text, re.M)
    return m


def spoken_reading(text: str) -> str:
    r = fm(text, "reading") or fm(text, "word")
    r = re.split(r"[/、,;・]", r)[0]
    r = re.sub(r"[~～〜\s]", "", r)
    return r


def has_audio(text: str) -> bool:
    m = re.search(r"^## Merkitys\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return bool(m and AUDIO_EMBED.search(m.group(1)))


def level_notes(levels, with_example=None):
    for d in (VOCAB, VERBS):
        for p in sorted(d.glob("*.md")):
            t = p.read_text(encoding="utf-8")
            if fm(t, "jlpt") in levels:
                yield p, t


def words_audio(levels):
    todo = [(p, t) for p, t in level_notes(levels) if not has_audio(t) and "## Merkitys" in t]
    audio = tts_many([spoken_reading(t) for _, t in todo])
    added = 0
    for p, t in todo:
        name = audio.get(spoken_reading(t))
        if not name:
            continue
        m = re.search(r"^## Merkitys\n((?:- .*\n)+)", t, re.M)
        if not m:
            continue
        line = f"- **Ääni:** ![[{name}]]\n"
        t = t[:m.end()] + line + t[m.end():]
        p.write_text(t, encoding="utf-8")
        added += 1
    print(f"{added} sanalle/verbille lisätty ääni")


# ------------------------------------------------------------------ käänteiskortit
def kortit_split(t: str):
    i = t.find("\n## Kortit")
    return (t, "") if i < 0 else (t[:i], t[i:])


def reverse():
    n = 0
    for d in (VOCAB, VERBS):
        for p in d.glob("*.md"):
            t = p.read_text(encoding="utf-8")
            head, tail = kortit_split(t)
            if not tail:
                continue
            lines, changed = tail.split("\n"), False
            for i, l in enumerate(lines):
                if "::" in l and ":::" not in l and not l.startswith("#") and "://" not in l:
                    lines[i] = l.replace("::", ":::", 1)
                    changed = True
                    n += 1
            if changed:
                p.write_text(head + "\n".join(lines), encoding="utf-8")
    print(f"{n} korttia muutettu kaksisuuntaiseksi")


def retag():
    n = 0
    for d, tag in ((VOCAB, "vocab"), (VERBS, "verb")):
        for p in d.glob("*.md"):
            t = p.read_text(encoding="utf-8")
            lvl = fm(t, "jlpt").lower()
            if not re.fullmatch(r"n[1-5]", lvl):
                continue
            head, tail = kortit_split(t)
            new = re.sub(rf"^#flashcards/{tag}\s*$", f"#flashcards/{tag}/{lvl}", tail, flags=re.M)
            if new != tail:
                p.write_text(head + new, encoding="utf-8")
                n += 1
    print(f"{n} muistiinpanon korttitagi tasokohtainen")


# ------------------------------------------------------------------ taivutusmuotojen verbityyppikortit
GODAN_ROWS = {  # pääte -> (a, i, e, o)
    "う": ("わ", "い", "え", "お"), "つ": ("た", "ち", "て", "と"), "る": ("ら", "り", "れ", "ろ"),
    "む": ("ま", "み", "め", "も"), "ぶ": ("ば", "び", "べ", "ぼ"), "ぬ": ("な", "に", "ね", "の"),
    "く": ("か", "き", "け", "こ"), "ぐ": ("が", "ぎ", "げ", "ご"), "す": ("さ", "し", "せ", "そ"),
}
TE = {"う": "って", "つ": "って", "る": "って", "む": "んで", "ぶ": "んで", "ぬ": "んで", "く": "いて", "ぐ": "いで", "す": "して"}
TA = {k: v[:-1] + ("た" if v.endswith("て") else "だ") for k, v in TE.items()}

# (kanji, kana, tyyppi, selite)
VERBS_EX = [
    ("買う", "かう", "u", "五段 う"), ("言う", "いう", "u", "五段 う"),
    ("待つ", "まつ", "tsu", "五段 つ"), ("持つ", "もつ", "tsu", "五段 つ"),
    ("取る", "とる", "ru", "五段 る"), ("帰る", "かえる", "ru", "五段 る"),
    ("飲む", "のむ", "mu", "五段 む"), ("読む", "よむ", "mu", "五段 む"),
    ("遊ぶ", "あそぶ", "bu", "五段 ぶ"), ("呼ぶ", "よぶ", "bu", "五段 ぶ"),
    ("死ぬ", "しぬ", "nu", "五段 ぬ"),
    ("書く", "かく", "ku", "五段 く"), ("歩く", "あるく", "ku", "五段 く"),
    ("泳ぐ", "およぐ", "gu", "五段 ぐ"), ("急ぐ", "いそぐ", "gu", "五段 ぐ"),
    ("話す", "はなす", "su", "五段 す"), ("貸す", "かす", "su", "五段 す"),
    ("行く", "いく", "iku", "五段 く, poikkeus"),
    ("見る", "みる", "ichi", "一段 (iる)"), ("起きる", "おきる", "ichi", "一段 (iる)"),
    ("食べる", "たべる", "ichi", "一段 (eる)"), ("寝る", "ねる", "ichi", "一段 (eる)"),
    ("する", "する", "suru", "不規則"), ("勉強する", "べんきょうする", "suru", "不規則"),
    ("来る", "くる", "kuru", "不規則"),
]
KURU = {"nai": ("来ない", "こない"), "masu": ("来ます", "きます"), "te": ("来て", "きて"), "ta": ("来た", "きた"),
        "ba": ("来れば", "くれば"), "imp": ("来い", "こい"), "vol": ("来よう", "こよう"),
        "pass": ("来られる", "こられる"), "pot": ("来られる", "こられる"),
        "caus": ("来させる", "こさせる"), "cpass": ("来させられる", "こさせられる"), "dict": ("来る", "くる")}


def conj(kanji: str, kana: str, typ: str, form: str):
    """Palauttaa (kanji, kana) halutulle muodolle."""
    if typ == "kuru":
        return KURU[form]

    def tail(s, cut, add):
        return (s[:-cut] if cut else s) + add

    if typ == "suru":
        ends = {"nai": "しない", "masu": "します", "te": "して", "ta": "した", "ba": "すれば", "imp": "しろ",
                "vol": "しよう", "pass": "される", "pot": "できる", "caus": "させる", "cpass": "させられる", "dict": "する"}
        if form == "pot" and kanji != "する":
            return tail(kanji, 2, "できる"), tail(kana, 2, "できる")
        return tail(kanji, 2, ends[form]), tail(kana, 2, ends[form])
    if typ == "ichi":
        ends = {"nai": "ない", "masu": "ます", "te": "て", "ta": "た", "ba": "れば", "imp": "ろ", "vol": "よう",
                "pass": "られる", "pot": "られる", "caus": "させる", "cpass": "させられる", "dict": "る"}
        return tail(kanji, 1, ends[form]), tail(kana, 1, ends[form])
    last = kana[-1]
    a, i, e, o = GODAN_ROWS[last]
    if typ == "iku":
        te, ta = "って", "った"
    else:
        te, ta = TE[last], TA[last]
    ends = {"nai": a + "ない", "masu": i + "ます", "te": te, "ta": ta, "ba": e + "ば", "imp": e,
            "vol": o + "う", "pass": a + "れる", "pot": e + "る", "caus": a + "せる", "cpass": a + "せられる",
            "dict": last}
    return tail(kanji, 1, ends[form]), tail(kana, 1, ends[form])


FORM_NOTES = {  # tiedosto -> (koodi, otsikko kortin etupuolella)
    "ない-muoto.md": ("nai", "ない形"), "ます-muoto.md": ("masu", "ます形"), "て-muoto.md": ("te", "て形"),
    "た-muoto.md": ("ta", "た形"), "Ehtomuoto ば.md": ("ba", "ば形"), "Käskymuoto ろ.md": ("imp", "命令形"),
    "Tahtomuoto よう.md": ("vol", "意向形"), "Passiivi (ら)れる.md": ("pass", "受身形"),
    "Potentiaali える.md": ("pot", "可能形"), "Kausatiivi (さ)せる.md": ("caus", "使役形"),
    "Kausatiivipassiivi (さ)せられる.md": ("cpass", "使役受身形"), "Sanakirjamuoto.md": ("dict", "辞書形"),
}
FORMS_START, FORMS_END = "<!-- verbityyppikortit:alku -->", "<!-- verbityyppikortit:loppu -->"


def forms():
    total = 0
    for fn, (code, label) in FORM_NOTES.items():
        p = FORMS / fn
        if not p.exists():
            print("puuttuu:", fn)
            continue
        t = p.read_text(encoding="utf-8")
        t = re.sub(rf"\n*{re.escape(FORMS_START)}.*?{re.escape(FORMS_END)}\n?", "\n", t, flags=re.S)
        lvl = (fm(t, "jlpt") or "n5").lower()
        lines = []
        for kj, kn, typ, desc in VERBS_EX:
            both = lambda k, n: k if k == n else f"{k}（{n}）"
            if code == "dict":
                # käänteinen suunta: ます-muodosta sanakirjamuotoon (tunnista verbityyppi)
                mk, mn = conj(kj, kn, typ, "masu")
                front = f"{label}: {both(mk, mn)}"
                back = f"{both(kj, kn)} — {desc}"
            else:
                rk, rn = conj(kj, kn, typ, code)
                info = desc if kj == kn else f"{kn}, {desc}"
                front = f"{label}: {kj}（{info}）"
                back = both(rk, rn)
            lines.append(f"{front} ::: {back}")
            total += 1
        block = (f"\n{FORMS_START}\n## Kortit\n#flashcards/form/{lvl}/taivutus\n\n" + "\n".join(lines) + f"\n{FORMS_END}\n")
        p.write_text(t.rstrip("\n") + "\n" + block, encoding="utf-8")
    print(f"{total} verbityyppikorttia")


# ------------------------------------------------------------------ esimerkit
def todo(levels, out):
    rows = []
    for p, t in level_notes(levels):
        if re.search(r"^## Esimerkit", t, re.M):
            continue
        if re.search(r"[。？！]|ですか|ください", fm(t, "word") or p.stem):
            continue                                    # valmis fraasi, ei tarvitse esimerkkiä
        rows.append({"path": str(p.relative_to(VAULT)), "word": fm(t, "word") or p.stem,
                     "reading": fm(t, "reading"), "meaning": fm(t, "meaning"), "jlpt": fm(t, "jlpt")})
    Path(out).write_text(json.dumps(rows, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"{len(rows)} muistiinpanoa ilman esimerkkiä -> {out}")


def apply_examples(todo_json, lines_file):
    rows = json.loads(Path(todo_json).read_text(encoding="utf-8"))
    entries = {}
    for raw in Path(lines_file).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("|")
        if len(parts) != 3 or not parts[0].isdigit():
            print("ohitettu:", raw[:60])
            continue
        entries.setdefault(int(parts[0]), []).append((parts[1].strip(), parts[2].strip()))
    audio = tts_many([ja for v in entries.values() for ja, _ in v])
    done = 0
    for idx, sents in entries.items():
        p = VAULT / rows[idx]["path"]
        t = p.read_text(encoding="utf-8")
        if re.search(r"^## Esimerkit", t, re.M):
            continue
        body = "".join(f"- {ja} — {fi}" + (f" ![[{audio[ja]}]]" if audio.get(ja) else "") + "\n" for ja, fi in sents)
        sec = f"## Esimerkit\n{body}\n"
        if "\n## Kortit" in t:
            i = t.index("\n## Kortit") + 1
            t = t[:i] + sec + t[i:]
        else:
            t = t.rstrip("\n") + "\n\n" + sec
        p.write_text(t, encoding="utf-8")
        done += 1
    print(f"{done} muistiinpanoon lisätty esimerkit")


def examples_audio(levels):
    """Olemassa olevat esimerkkirivit (esim. Anki-tuonnista) ilman ääntä -> lisää ![[tts]] rivin loppuun."""
    line_re = re.compile(r"^- (?P<ja>.+?) — (?P<rest>.+)$")
    todo = []
    for p, t in level_notes(levels):
        m = re.search(r"^## Esimerkit\n(.*?)(?=^## |\Z)", t, re.M | re.S)
        if not m:
            continue
        rows = [l for l in m.group(1).split("\n") if line_re.match(l) and not AUDIO_EMBED.search(l)]
        if rows:
            todo.append((p, rows))
    audio = tts_many([line_re.match(l).group("ja") for _, rows in todo for l in rows])
    added = 0
    for p, rows in todo:
        t = p.read_text(encoding="utf-8")
        m = re.search(r"^## Esimerkit\n(.*?)(?=^## |\Z)", t, re.M | re.S)
        sec = m.group(1)
        for l in rows:
            name = audio.get(line_re.match(l).group("ja"))
            if name and l in sec:
                sec = sec.replace(l, f"{l} ![[{name}]]", 1)
                added += 1
        p.write_text(t[:m.start(1)] + sec + t[m.end(1):], encoding="utf-8")
    print(f"{added} esimerkkiriville lisätty ääni ({len(todo)} muistiinpanoa)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["sentences-audio", "sentence-cards", "words-audio", "examples-audio", "reverse", "retag",
                                    "forms", "todo", "apply-examples"])
    ap.add_argument("--levels", default="N5,N4,N3")
    ap.add_argument("--out", default="todo.json")
    ap.add_argument("--todo")
    ap.add_argument("--lines")
    a = ap.parse_args()
    simple = {"sentences-audio": sentences_audio, "sentence-cards": sentence_cards, "reverse": reverse,
              "retag": retag, "forms": forms}
    if a.cmd in simple:
        simple[a.cmd]()
    elif a.cmd == "words-audio":
        words_audio(set(a.levels.split(",")))
    elif a.cmd == "examples-audio":
        examples_audio(set(a.levels.split(",")))
    elif a.cmd == "todo":
        todo(set(a.levels.split(",")), a.out)
    else:
        apply_examples(a.todo, a.lines)
