#!/usr/bin/env python3
"""
Yhdistää Anki-kokoelman japanin sanaston vaultiin.

Lähteet (Anki-muistiinpanotyypit):
    Core 6k Japanese, Japanese   -> Core 2k/6k        (lahde/anki-core)
    vocab Model                  -> WaniKani          (lahde/anki-wk)
    Japanese MNN ShoKyuu         -> Minna no Nihongo  (lahde/anki-mnn)
    Japanese KIC                 -> Kanji in Context  (lahde/anki-kic)

Vaiheet:
    extract   lukee Ankin kopion -> anki_merged.json (yksi rivi per sana)
    write     rikastaa olemassa olevat muistiinpanot ja luo puuttuvat
              (suomenkieliset merkitykset tiedostosta anki_fi.json)

Ajo:
    python3 "00 Meta/Scripts/anki_to_vault.py" extract --collection /polku/collection.anki2
    python3 "00 Meta/Scripts/anki_to_vault.py" write [--dry-run]

Turvallisuus: olemassa olevaan muistiinpanoon lisätään vain puuttuvaa
(tyhjä EN-rivi, Esimerkit-osio, ääni, lähde), mitään ei korvata.
Luodut muistiinpanot tunnistaa tagista lahde/anki-* ja päivämäärästä
created: 2026-10-10.
"""
import argparse
import json
import re
import shutil
import sqlite3
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]          # .../Japanese
SCRIPTS = Path(__file__).resolve().parent
MERGED = SCRIPTS / "anki_merged.json"
FI_FILE = SCRIPTS / "anki_fi.json"
AUDIO_DIR = VAULT / "70 Visuaalinen" / "Audio" / "Anki"   # gitignoressa
CREATED = "2026-10-10"

KANJI = r"一-鿿㐀-䶿々〆ヵヶ"
FURI_RE = re.compile(rf"[{KANJI}]+\[([^\]]+)\]")
TAG_RE = re.compile(r"<[^>]+>")
SOUND_RE = re.compile(r"\[sound:([^\]]+)\]")


# ---------------------------------------------------------------- helpers
def strip_html(s: str) -> str:
    s = SOUND_RE.sub("", s)
    s = TAG_RE.sub("", s)
    return s.replace("&nbsp;", " ").replace("　", " ").strip()


def furigana_to_kana(s: str) -> str:
    """'明[あ]かり' / '最[さい] 高[こう]' -> 'あかり' / 'さいこう'."""
    s = strip_html(s).replace(" ", "")
    return FURI_RE.sub(lambda m: m.group(1), s)


def norm_word(w: str) -> str:
    w = strip_html(w).replace("〜", "～").replace("~", "～")
    w = re.sub(r"「な」$", "", w)            # MNN: 変「な」 -> 変
    w = w.replace("「", "").replace("」", "")  # MNN: 「お」菓子 -> お菓子
    w = re.sub(r"\s+", "", w)
    return w


def sound(s: str):
    m = SOUND_RE.search(s or "")
    return m.group(1) if m else None


KANA_ROMA = {}
def _build_romaji():
    base = ("あa いi うu えe おo かka きki くku けke こko さsa しshi すsu せse そso "
            "たta ちchi つtsu てte とto なna にni ぬnu ねne のno はha ひhi ふfu へhe ほho "
            "まma みmi むmu めme もmo やya ゆyu よyo らra りri るru れre ろro わwa ゐi ゑe をo んn "
            "がga ぎgi ぐgu げge ごgo ざza じji ずzu ぜze ぞzo だda ぢji づzu でde どdo "
            "ばba びbi ぶbu べbe ぼbo ぱpa ぴpi ぷpu ぺpe ぽpo ぁa ぃi ぅu ぇe ぉo ゔvu")
    for tok in base.split():
        KANA_ROMA[tok[0]] = tok[1:]
    for k, r in [("き", "ky"), ("ぎ", "gy"), ("に", "ny"), ("ひ", "hy"), ("び", "by"),
                 ("ぴ", "py"), ("み", "my"), ("り", "ry")]:
        for s, v in [("ゃ", "a"), ("ゅ", "u"), ("ょ", "o")]:
            KANA_ROMA[k + s] = r + v
    for k, r in [("し", "sh"), ("ち", "ch"), ("じ", "j"), ("ぢ", "j")]:
        for s, v in [("ゃ", "a"), ("ゅ", "u"), ("ょ", "o")]:
            KANA_ROMA[k + s] = r + v
_build_romaji()


def romaji(kana: str) -> str:
    kana = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in kana)
    out, i = [], 0
    while i < len(kana):
        two, one = kana[i:i + 2], kana[i]
        if two in KANA_ROMA:
            out.append(KANA_ROMA[two]); i += 2; continue
        if one == "っ" and i + 1 < len(kana):
            nxt = KANA_ROMA.get(kana[i + 1:i + 3]) or KANA_ROMA.get(kana[i + 1], "")
            out.append("t" if nxt.startswith("ch") else nxt[:1]); i += 1; continue
        if one == "ー" and out:
            out.append(out[-1][-1:]); i += 1; continue
        if one in KANA_ROMA:
            r = KANA_ROMA[one]
            if one == "ん" and i + 1 < len(kana) and KANA_ROMA.get(kana[i + 1], "x")[:1] in "aiueoy":
                r = "n'"
            out.append(r)
        elif one in "～〜":
            pass
        else:
            out.append(one)
        i += 1
    return "".join(out)


POS_MAP = [  # (alaosa lähteen sanaluokasta, vaultin pos)
    ("suru", "noun-suru"), ("する verb", "noun-suru"), ("い adjective", "i-adjective"),
    ("i-adjective", "i-adjective"), ("な adjective", "na-adjective"), ("na-adjective", "na-adjective"),
    ("adverb", "adverb"), ("counter", "counter"), ("suffix", "suffix"), ("prefix", "prefix"),
    ("pronoun", "pronoun"), ("conjunction", "conjunction"), ("interjection", "interjection"),
    ("expression", "expression"), ("particle", "particle"), ("proper noun", "proper noun"),
    ("adjective", "i-adjective"), ("verb", "verb"), ("noun", "noun"),
]


def map_pos(src: str):
    s = (src or "").lower()
    if "verb" in s and ("する" in s or "suru" in s):
        return "noun-suru"
    for key, val in POS_MAP:
        if key in s:
            return val
    return None


# ---------------------------------------------------------------- vault
NOTE_DIRS = [VAULT / "30 Sanasto" / "Sanat", VAULT / "20 Verbit" / "Lekseemit"]
FM_WORD = re.compile(r'^word:\s*"?([^"\n]*)"?\s*$', re.M)


def vault_index():
    """word -> Path kaikille sanasto- ja verbimuistiinpanoille."""
    idx = {}
    for d in NOTE_DIRS:
        for p in d.glob("*.md"):
            idx.setdefault(p.stem.strip(), p)
            m = FM_WORD.search(p.read_text(encoding="utf-8")[:1500])
            if m and m.group(1).strip():
                idx.setdefault(m.group(1).strip(), p)
    return idx


# ---------------------------------------------------------------- ます -> sanakirjamuoto
I2U = dict(zip("いきぎしちにびみりじ", "うくぐすつぬぶむるず"))
E_ROW = set("えけげせてねべめれぜでへぺ")
# yleiset i-rivin ichidan-verbit (ます-muodosta ei voi päätellä luokkaa)
ICHIDAN_I = {"できる", "いる", "居る", "みる", "見る", "きる", "着る", "おきる", "起きる", "おりる", "降りる",
             "下りる", "かりる", "借りる", "あびる", "浴びる", "たりる", "足りる", "いきる", "生きる",
             "すぎる", "過ぎる", "のびる", "伸びる", "おちる", "落ちる", "とじる", "閉じる", "にる", "似る",
             "煮る", "しんじる", "信じる", "かんじる", "感じる", "おうじる", "応じる", "あきる", "飽きる"}


# yleiset godan-す-verbit: ennen する-sääntöjä (ごみを出します -> ごみを出す)
COMMON_SU = {"出す", "押す", "外す", "無くす", "なくす", "落とす", "消す", "話す", "貸す", "返す", "渡す",
             "回す", "起こす", "直す", "戻す", "探す", "残す", "降ろす", "下ろす", "動かす", "乾かす",
             "沸かす", "冷やす", "増やす", "減らす", "汚す", "壊す", "倒す", "治す", "足す", "指す",
             "刺す", "干す", "写す", "移す", "映す", "隠す", "許す", "示す", "表す", "現す", "越す",
             "通す", "鳴らす", "濡らす", "散らす", "飛ばす", "伸ばす", "延ばす", "急かす", "放す", "離す",
             "貼り出す", "思い出す", "引き出す", "取り出す", "差し出す", "呼び出す", "持ち出す", "連れ出す"}
# kaksiselitteiset tapaukset, joissa sääntö ei riitä
MASU_OVERRIDES = {"おります": ("おる", "おる"), "雨が降ります": ("雨が降る", "あめがふる"),
                  "雪が降ります": ("雪が降る", "ゆきがふる")}


def masu_to_dict(word, reading, known):
    """MNN: '壊します' -> ('壊す', 'こわす'). None, jos ei ole ます-verbi."""
    if word in MASU_OVERRIDES:
        return MASU_OVERRIDES[word]
    if not word.endswith("ます") or word in ("ございます",) or word.endswith("ございます"):
        return None
    w, r = word[:-2], (reading or "")[:-2]
    if not w:
        return None
    if w in ("来", "き") or w.endswith("来"):
        return w + "る" if w.endswith("来") else "来る", (r[:-1] if r else "") + "くる"
    if w.endswith("でき") and (len(w) == 2 or w[-3] in "がをにはもで"):   # 道ができます -> 道ができる
        return w + "る", r + "る"
    if w.endswith(("てき", "でき")) and len(w) > 2:          # 帰ってきます -> 帰ってくる
        return w[:-1] + "くる", r[:-1] + "くる"
    if w.endswith(("てい", "でい")):                       # ついています -> ついている
        return w + "る", r + "る"
    if w.endswith(("さい", "しゃい", "ざい")):              # くださる, なさる, いらっしゃる
        return w[:-1] + "る", r[:-1] + "る"
    if w == "し" or w.endswith("お願いし"):                 # します -> する
        return w[:-1] + "する", r[:-1] + "する"
    if w.endswith("し"):
        stem = w[:-1]
        su = stem + "す"
        if su in known or any(su == v or (su.endswith(v) and su[-len(v) - 1] in "をがにでもは")
                              for v in COMMON_SU):
            return stem + "す", r[:-1] + "す"
        if stem.endswith(("を", "が", "に", "く", "と")):                  # 就職をします -> 就職をする
            return stem + "する", r[:-1] + "する"
        if stem + "す" in known:
            return stem + "す", r[:-1] + "す"
        if stem and (stem + "する" in known or re.search(rf"([{KANJI}]{{2,}}|[ァ-ヶー]+)$", stem) or not re.search(rf"[{KANJI}]", stem)):
            return stem + "する", r[:-1] + "する"
        if len(stem) >= 2 and re.search(rf"[{KANJI}]$", stem):   # 買い物します -> 買い物する
            return stem + "する", r[:-1] + "する"
        return stem + "す", r[:-1] + "す"
    last = w[-1]
    if last in E_ROW:
        return w + "る", r + "る"
    if last in I2U:
        godan = (w[:-1] + I2U[last], r[:-1] + I2U[last])
        ichi = (w + "る", r + "る")
        if ichi[0] in ICHIDAN_I or any(
                ichi[0].endswith(("を" + v, "が" + v, "に" + v, "で" + v)) for v in ICHIDAN_I):   # シャワーを浴びる
            return ichi
        if godan[0] in known:
            return godan
        if ichi[0] in known:
            return ichi
        if last == "じ":
            return ichi
        return godan
    if re.fullmatch(rf"[{KANJI}]", last):                  # 見ます, 寝ます, 着ます
        return w + "る", r + "る"
    return None


# ---------------------------------------------------------------- extract
def open_collection(path: Path) -> sqlite3.Connection:
    c = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    c.create_collation("unicase", lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower()))
    return c


def notes_of(c, notetype):
    mid = c.execute("select id from notetypes where name=?", (notetype,)).fetchone()[0]
    names = [r[0] for r in c.execute("select name from fields where ntid=? order by ord", (mid,))]
    for flds, tags in c.execute("select flds, tags from notes where mid=?", (mid,)):
        yield dict(zip(names, flds.split("\x1f"))), tags.split()


def extract(collection: Path):
    c = open_collection(collection)
    entries = {}   # word -> entry

    def add(word, src, reading=None, en=None, pos=None, jlpt=None, examples=(),
            audio=None, source_link=None, verbinfo=None):
        word = norm_word(word)
        if not word:
            return
        e = entries.setdefault(word, {"word": word, "readings": [], "en": [], "pos": None,
                                      "jlpt": None, "examples": [], "audio": None,
                                      "sources": [], "tags": [], "verbinfo": None})
        if reading:
            reading = norm_word(reading).replace("～", "").rstrip("。")
            if reading not in e["readings"]:
                e["readings"].append(reading)
        if en and en.lower() not in [x.lower() for x in e["en"]]:
            e["en"].append(en)
        e["pos"] = e["pos"] or pos
        e["jlpt"] = e["jlpt"] or jlpt
        e["verbinfo"] = e["verbinfo"] or verbinfo
        for jp, tr in examples:
            if jp and len(e["examples"]) < 3 and jp not in [x[0] for x in e["examples"]]:
                e["examples"].append((jp, tr))
        e["audio"] = e["audio"] or audio
        if source_link and source_link not in e["sources"]:
            e["sources"].append(source_link)
        if src not in e["tags"]:
            e["tags"].append(src)

    # Core: 'Core 6k Japanese' (N-tagit) ennen 'Japanese'-tyyppiä
    for nt in ("Core 6k Japanese", "Japanese"):
        for f, tags in notes_of(c, nt):
            jl = next((t for t in tags if re.fullmatch(r"N[1-5]", t)), None)
            add(f["Vocabulary-Kanji"], "lahde/anki-core",
                reading=strip_html(f["Vocabulary-Kana"]),
                en=strip_html(f["Vocabulary-English"]),
                pos=map_pos(f["Vocabulary-Pos"]), jlpt=jl,
                examples=[(strip_html(f["Expression"]), strip_html(f["Sentence-English"]))],
                audio=sound(f["Vocabulary-Audio"]), source_link="[[Core 2k-6k]]")

    for f, tags in notes_of(c, "vocab Model"):
        st = f["Speech_Type"]
        vi = None
        if "verb" in st.lower() and "する" not in st and "suru" not in st.lower():
            vi = {"class": "godan" if "godan" in st.lower() else "ichidan" if "ichidan" in st.lower() else None,
                  "trans": "transitive" if "transitive" in st.lower() and "intransitive" not in st.lower()
                  else "intransitive" if "intransitive" in st.lower() else None}
        add(f["Vocab"], "lahde/anki-wk", reading=strip_html(f["Reading"]).split(",")[0].strip(),
            en=strip_html(f["Vocab_Meaning"]), pos=map_pos(st), verbinfo=vi,
            examples=[(strip_html(f[f"Context_jp{s}"]), strip_html(f[f"Context_en{s}"]))
                      for s in ("", "_2", "_3")],
            audio=sound(f["Audio_b"]), source_link="[[WaniKani]]")

    known = set(entries) | set(vault_index())
    for f, tags in notes_of(c, "Japanese MNN ShoKyuu"):
        lesson = next((int(m.group(1)) for t in tags if (m := re.fullmatch(r"L(\d+)\w*", t))), None)
        link = None
        if lesson:
            book = "Minna no Nihongo I" if lesson <= 25 else "Minna no Nihongo II"
            link = f"[[{book}#Luku {lesson}]]"
        en = strip_html(f["English"])
        word, reading = norm_word(f["Kanji"]), norm_word(furigana_to_kana(f["Furigana"])) or None
        pos = "verb" if en.startswith("to ") else None
        dict_form = masu_to_dict(word, reading, known)
        if dict_form:
            word, reading = dict_form
            pos = "verb"
        add(word, "lahde/anki-mnn", reading=reading,
            en=en, pos=pos,
            jlpt=("N5" if lesson <= 25 else "N4") if lesson else None,
            audio=None if "missing-media" in tags else sound(f["Audio"]), source_link=link)

    for f, tags in notes_of(c, "Japanese KIC"):
        en = strip_html(f["Meaning"])
        w = norm_word(f["Expression"])
        pos = "verb" if en.startswith("to ") and re.search(r"[うくぐすつぬぶむる]$", w) else None
        if re.match(r"^する[：:]", en):
            en, pos = re.sub(r"^する[：:]\s*", "", en), "noun-suru"
        elif pos is None and re.fullmatch(rf"[{KANJI}]+", w):
            pos = "noun"
        add(f["Expression"], "lahde/anki-kic", reading=furigana_to_kana(f["Reading"]) or None,
            en=en, pos=pos, source_link="[[Kanji in Context]]")

    for e in entries.values():
        if e["pos"] == "verb":
            if re.search(r"[をがにで]", e["word"][1:-1]) and re.search(r"[うくぐすつぬぶむる]$", e["word"]):
                e["pos"] = "expression"                     # 会社を休む, 風が吹く
            elif not re.search(r"[うくぐすつぬぶむる]$", e["word"]):
                e["pos"] = "noun-suru"                      # 乾杯, 教育
    data = sorted(entries.values(), key=lambda e: e["word"])
    MERGED.write_text(json.dumps(data, ensure_ascii=False, indent=0))
    print(f"{len(data)} sanaa -> {MERGED}")


# ---------------------------------------------------------------- write
VERB_POS = {"verb"}
BAD_FN = re.compile(r'[\\/:*?"<>|#^\[\]]')


def yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def canon(reading: str) -> str:
    """Lukutapojen vertailuun: katakana -> hiragana, ～。-merkit ja välit pois."""
    reading = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in reading)
    return re.sub(r"[～〜~。？?\s\-.]", "", reading)


def en_text(e) -> str:
    out, seen = [], set()
    for g in e["en"]:
        key = frozenset(x.strip().lower() for x in g.split(","))
        if key not in seen:
            seen.add(key)
            out.append(g)
    return "; ".join(out)


def example_lines(e) -> list:
    return [f"- {jp} — {en}" if en else f"- {jp}" for jp, en in e["examples"]]


def jlpt_tag(j):
    return f"jlpt/{j.lower()}" if j else None


def guess_verbclass(e) -> str:
    vi = e.get("verbinfo") or {}
    if vi.get("class"):
        return vi["class"]
    w, r = e["word"], (e["readings"] or [""])[0]
    if w.endswith("する"):
        return "suru"
    if w.endswith(("来る", "くる")) and r.endswith("くる") and len(r) <= 4:
        return "kuru"
    if r.endswith("る") and len(r) >= 2 and r[-2] in "いきぎしじちにひびみりえけげせぜてでねへべめれ":
        return "ichidan"   # arvio: osa i/e+る -verbeistä on godan (帰る, 入る, 走る ...)
    return "godan"


def new_note(e, fi: str) -> tuple:
    """Palauttaa (kansio, tiedostonimi, sisältö)."""
    verb = e["pos"] in VERB_POS
    reading = (e["readings"] or [""])[0]
    tags = ["verb" if verb else "vocab"]
    if jlpt_tag(e["jlpt"]):
        tags.append(jlpt_tag(e["jlpt"]))
    tags += sorted(e["tags"]) + ["anki/fi-auto"]
    srcs = ", ".join(yaml_str(s) for s in e["sources"])
    fm = ["---", f"type: {'verb' if verb else 'vocab'}", f"word: {yaml_str(e['word'])}",
          f"reading: {reading}", f"romaji: {romaji(reading)}", f"meaning: {yaml_str(fi)}"]
    if verb:
        vi = e.get("verbinfo") or {}
        fm += [f"verbclass: {guess_verbclass(e)}", f"transitivity: {vi.get('trans') or ''}", "pair: "]
    else:
        fm += [f"pos: {e['pos'] or ''}"]
    fm += [f"jlpt: {e['jlpt'] or ''}"]
    if not verb:
        fm += ["pitch: []"]
    fm += ["opposite: []", "similar: []", "kanji: []", "sets: []", f"sources: [{srcs}]",
           "status: new", "confidence: 1"]
    if not verb:
        fm += ["reviewed: "]
    fm += [f"created: {CREATED}", f"tags: [{', '.join(tags)}]", "---", ""]
    body = ["## Merkitys", f"- **FI:** {fi}", f"- **EN:** {en_text(e)}"]
    if len(e["readings"]) > 1:
        body.append(f"- **Muut lukutavat:** {'、'.join(e['readings'][1:])}")
    if e.get("audio_local"):
        body.append(f"- **Ääni:** ![[{e['audio_local']}]]")
    body += ["", "## Kollokaatiot ja käyttö", "- ", ""]
    if e["examples"]:
        body += ["## Esimerkit"] + example_lines(e) + [""]
    body += ["## Kortit", f"#flashcards/{'verb' if verb else 'vocab'}",
             f"{e['word']}::{reading} — {fi}", ""]
    folder = NOTE_DIRS[1] if verb else NOTE_DIRS[0]
    return folder, BAD_FN.sub("_", e["word"]) + ".md", "\n".join(fm + body)


def fm_field(text, key):
    m = re.search(rf"^{key}:[ \t]*(.*)$", text.split("\n---", 1)[0], re.M)
    return m


def set_empty_field(text, key, value):
    m = fm_field(text, key)
    if m and m.group(1).strip() in ("", '""'):
        return text[:m.start(1)] + value + text[m.end(1):], True
    return text, False


def add_to_inline_list(text, key, items):
    m = fm_field(text, key)
    if not m:
        return text, False
    cur = m.group(1).strip()
    if not (cur.startswith("[") and cur.endswith("]")):
        return text, False                       # lohkomuotoinen lista: ei kosketa
    inner = cur[1:-1].strip()
    add = [i for i in items if i not in inner]
    if not add:
        return text, False
    new = "[" + ", ".join(([inner] if inner else []) + add) + "]"
    return text[:m.start(1)] + new + text[m.end(1):], True


def enrich(path: Path, e) -> list:
    """Lisää puuttuvat tiedot olemassa olevaan muistiinpanoon. Palauttaa muutoslistan."""
    text = path.read_text(encoding="utf-8")
    orig, changes = text, []
    reading = (e["readings"] or [""])[0]
    for key, val in (("reading", reading), ("romaji", romaji(reading) if reading else ""),
                     ("pos", e["pos"] or ""), ("jlpt", e["jlpt"] or "")):
        if val:
            text, ch = set_empty_field(text, key, val)
            if ch:
                changes.append(key)
    text, ch = add_to_inline_list(text, "sources", [yaml_str(s) for s in e["sources"]])
    if ch:
        changes.append("sources")
    tags = [t for t in e["tags"] if t not in text]
    if e["jlpt"] and jlpt_tag(e["jlpt"]) not in text and "jlpt" in changes:
        tags.append(jlpt_tag(e["jlpt"]))
    text, ch = add_to_inline_list(text, "tags", tags)
    if ch:
        changes.append("tags")

    en = en_text(e)
    m = re.search(r"^- \*\*EN:\*\*[ \t]*$", text, re.M)
    if en and m:
        text = text[:m.end()].rstrip(" \t") + " " + en + text[m.end():]
        changes.append("EN")
    elif en and "**EN:**" not in text:
        m = re.search(r"^- \*\*FI:\*\*.*$", text, re.M)
        if m:
            text = text[:m.end()] + f"\n- **EN:** {en}" + text[m.end():]
            changes.append("EN")

    if e.get("audio_local") and e["audio_local"] not in text:
        m = re.search(r"^- \*\*EN:\*\*.*$", text, re.M) or re.search(r"^- \*\*FI:\*\*.*$", text, re.M)
        if m:
            text = text[:m.end()] + f"\n- **Ääni:** ![[{e['audio_local']}]]" + text[m.end():]
            changes.append("audio")

    ex = [l for l, (jp, _) in zip(example_lines(e), e["examples"]) if jp not in text]
    before = text
    if ex:
        m = re.search(r"^## Esimerkit[ \t]*\n((?:- [ \t]*\n)*)", text, re.M)
        if m:   # osio on olemassa: poista tyhjä luettelomerkki, lisää esimerkit alkuun
            text = text[:m.end(0) - len(m.group(1))] + "\n".join(ex) + "\n" + text[m.end(0):]
        else:
            k = re.search(r"^## Kortit", text, re.M)
            if k:
                text = text[:k.start()] + "## Esimerkit\n" + "\n".join(ex) + "\n\n" + text[k.start():]
        if text != before:
            changes.append("examples")

    if text != orig:
        path.write_text(text, encoding="utf-8")
    return changes


def write(dry_run: bool, media: Path):
    data = json.loads(MERGED.read_text())
    fi = json.loads(FI_FILE.read_text()) if FI_FILE.exists() else {}
    idx = vault_index()
    stats = {"enriched": 0, "unchanged": 0, "reading_conflict": 0, "created": 0,
             "no_fi": 0, "name_clash": 0, "audio": 0}
    conflicts, field_counts = [], {}
    if not dry_run:
        AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    for e in data:
        if e["audio"] and (media / e["audio"]).exists():
            e["audio_local"] = "anki_" + e["audio"]
            if not dry_run and not (AUDIO_DIR / e["audio_local"]).exists():
                shutil.copy2(media / e["audio"], AUDIO_DIR / e["audio_local"])
                stats["audio"] += 1
        path = idx.get(e["word"])
        if path:
            r = fm_field(path.read_text(encoding="utf-8"), "reading")
            vr = r.group(1).strip().strip('"') if r else ""
            if vr and e["readings"] and not ({canon(x) for x in re.split(r"[/／・、,]", vr)}
                                             & {canon(x) for x in e["readings"]}):
                stats["reading_conflict"] += 1
                conflicts.append(f"{e['word']}\tvault={vr}\tanki={'、'.join(e['readings'])}")
                continue
            if dry_run:
                stats["enriched"] += 1
                continue
            ch = enrich(path, e)
            stats["enriched" if ch else "unchanged"] += 1
            for c in ch:
                field_counts[c] = field_counts.get(c, 0) + 1
            continue
        if e["word"] not in fi:
            stats["no_fi"] += 1
            continue
        folder, name, content = new_note(e, fi[e["word"]])
        if (folder / name).exists():
            stats["name_clash"] += 1
            name = name[:-3] + f" ({(e['readings'] or ['?'])[0]}).md"
            if (folder / name).exists():
                continue
        if not dry_run:
            (folder / name).write_text(content, encoding="utf-8")
        stats["created"] += 1
    (SCRIPTS / "anki_reading_conflicts.tsv").write_text("\n".join(conflicts) + "\n")
    print(json.dumps(stats, indent=1), json.dumps(field_counts, ensure_ascii=False))


# ---------------------------------------------------------------- jlpt-arvio
# Kalibroitu Core 6k:n virallisia N-tageja vastaan (3077 sanaa): Core-järjestys
# 38 % osuu tasolleen, 80 % ±1 tason sisään; WaniKani+kanji 32 % / 80 %.
def _core_level(i):
    return 5 if i <= 700 else 4 if i <= 1800 else 3 if i <= 3000 else 2 if i <= 4500 else 1


def _wk_level(lv):
    return 5 if lv <= 8 else 4 if lv <= 16 else 3 if lv <= 26 else 2 if lv <= 38 else 1


def estimate_jlpt(collection: Path, dry_run: bool):
    c = open_collection(collection)
    core, wk, kj = {}, {}, {}
    for nt in ("Core 6k Japanese", "Japanese"):
        for f, _ in notes_of(c, nt):
            if f["Core-Index"].strip().isdigit():
                w = norm_word(f["Vocabulary-Kanji"])
                core[w] = min(core.get(w, 99999), int(f["Core-Index"]))
    for f, tags in notes_of(c, "vocab Model"):
        lv = next((t[5:] for t in tags if t.startswith("level")), None)
        if lv and lv.isdigit():
            wk[norm_word(f["Vocab"])] = int(lv)
    for f, _ in notes_of(c, "Japanese Kanji AnkiWeb"):
        v = f["Info_JLPT_Level"].strip()[:1]
        if v.isdigit():
            kj[strip_html(f["Kanji"])] = int(v) or 1      # 0 = JLPT-listan ulkopuolella -> N1

    def estimate(word):
        if word in core:
            return _core_level(core[word]), "core"
        ks = [kj[ch] for ch in word if ch in kj]
        if word in wk and ks:
            return round((_wk_level(wk[word]) + sum(ks) / len(ks)) / 2), "wk+kanji"
        if word in wk:
            return _wk_level(wk[word]), "wk"
        if ks:
            return round(sum(ks) / len(ks)), "kanji"
        return 3, "oletus"                              # pelkkä kana, ei muuta tietoa

    stats = {}
    for d in NOTE_DIRS:
        for p in d.glob("*.md"):
            text = p.read_text(encoding="utf-8")
            if "anki/fi-auto" not in text[:1200]:
                continue
            m = fm_field(text, "jlpt")
            if not m or m.group(1).strip():
                continue
            wm = FM_WORD.search(text[:1500])
            lvl, how = estimate(wm.group(1).strip() if wm else p.stem)
            stats[how] = stats.get(how, 0) + 1
            stats[f"N{lvl}"] = stats.get(f"N{lvl}", 0) + 1
            text = text[:m.start(1)] + f"N{lvl}" + text[m.end(1):]
            text, _ = add_to_inline_list(text, "tags", [f"jlpt/n{lvl}", "anki/jlpt-arvio"])
            if not dry_run:
                p.write_text(text, encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    ex = sub.add_parser("extract")
    ex.add_argument("--collection", type=Path, required=True)
    wr = sub.add_parser("write")
    wr.add_argument("--dry-run", action="store_true")
    wr.add_argument("--media", type=Path,
                    default=Path.home() / "Library/Application Support/Anki2/User 1/collection.media")
    jl = sub.add_parser("jlpt", help="arvioi puuttuvat JLPT-tasot tuoduille muistiinpanoille")
    jl.add_argument("--collection", type=Path, required=True)
    jl.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.cmd == "extract":
        extract(a.collection)
    elif a.cmd == "jlpt":
        estimate_jlpt(a.collection, a.dry_run)
    else:
        write(a.dry_run, a.media)
