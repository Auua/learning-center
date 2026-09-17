# Rebuild: みんなの日本語 中級I — four books, vision transcription from scanned PDFs

Same method as ../.kic-rebuild (Kanji in Context Workbook 1). PDFs have no text layer.

## Books (key → PDF in ../PDF → target md in ..)
- mondai   → 皆の日本語中級１標準問題集.pdf (15 pp; answer section only)
- kaito    → 皆の日本語中級1本冊解答.pdf (72 pp)
- honsatsu → 皆の日本語中級１本冊.pdf (223 pp)
- bunpo    → 皆の日本語中級１翻訳・文法解説英語版.pdf (138 pp)

## Paths
- Page PNGs (200dpi grey, gitignored): <key>/pages/pNNN.png, NNN = PDF index. Regenerate: ./venv/bin/python render.py
- Per-page output: <key>/out/pNNN.md → assembled per book at the end, old OCR backed up to <key>/ORIGINAL-ocr-backup.md
- venv (gitignored): ./venv  (python3 -m venv venv && ./venv/bin/pip install pymupdf)

## Formatting conventions (shared)
- {漢字|かな} = furigana printed in the book (markdown-furigana plugin syntax).
- Lesson heading: `## 第N課`; printed section boxes (文法・練習 / 話す・聞く / 読む・書く / 問題 …): `### …`
- Page marker at end of each page file: `*[p.N]*` (printed page number; `*[PDF NNN]*` if unnumbered)
- Merge text flowing across columns/pages into the page where it starts.
- Ignore previous owner's handwriting.
- Crop-zoom (sips -c H W --cropOffset Y X, then sips -z) only when genuinely ambiguous.

## Answer-key books (mondai, kaito)
- Each numbered question is its own paragraph: `**1.**　1) 答え　2) 答え`
  (sub-answers separated by 　, one blank line between questions)
- Brackets and ／ exactly as printed ([ ] = omissible part, ／ = alternatives, 例： = example answer)

## kaito (本冊解答) layout — single column, long answers
- `# 1. 解答` / `# 2. 話す・聞く 会話スクリプト` / `# 3. CDの内容` = the book's three parts
- `## 第N課`, `### 文法・練習` etc. No ruby on recurring labels (第N課, 練習, 例, section names, 問題).
- Exercise: `**1.**　練習1` line, then each answer `- 1) …` (bullet, so markdown does not renumber);
  alternative answers printed on a 2nd line joined with `<br>`. Sub-exercise inside the same number: `**練習2**`.
- Dialogue scripts: `A：…<br>B：…` style, speaker names as printed.
- Part 2 会話スクリプト: `## 第N課　title`; scene note `*［…］*`; one utterance per paragraph `**タワポン**：　…`; underlined numbered phrases → `**①…**` (bold = underlined in book).
- Figures (maps, pictures needed for an answer): crop from pages/ PNG with sips into "70 Visuaalinen/liitteet/mnn-chukyu1-<key>-pNN-<name>.png" (vault attachment folder) and embed `![[file.png]]`. NB kaito/mondai/bunpo PNGs are 1433 px wide, honsatsu 1653.

## honsatsu (本冊) layout
- Furigana: printed on nearly every kanji → keep all ruby (as kic workbook). Compound ruby per word; split across okurigana.
- `## 第N課` lesson; `### 文法・練習` etc.; inner headings `#### 1.`; bold `**1）…**` for sub-parts.
- Numbered procedure lists as markdown `1. title<br>text`.

## Progress
- mondai: DONE p000-p014 (all 15 pp). Installed 2026-09-15; old OCR → mondai/ORIGINAL-ocr-backup.md
  Assemble any book: ./assemble.sh <key> "<target>.md" "<pages>" "<scope>"
- kaito: DONE p000-p071 (all 72 pp). Installed 2026-09-15; old OCR → kaito/ORIGINAL-ocr-backup.md. Map figure → 70 Visuaalinen/liitteet/mnn-chukyu1-kaito-p21-chizu.png
- honsatsu: next (223 pp, PNG 1653 px wide)

## honsatsu lesson-body details
- Grammar heading `#### 1．～…`; example sentences as `- 1) …`; `**練習1**` then `{例|れい}：` line and items.
- Exercise pictures: ./fig.sh honsatsu NNN name H W Y X (orig px = displayed px × 1.17), embed `![[mnn-chukyu1-honsatsu-pNNN-name.png]]`.
  Character portraits next to 聞いてみましょう are skipped (names are in text).
- Underlined text in examples → `<u>…</u>`. Answer blanks → ＿＿＿＿.
- Margin lesson tabs / margin page numbers ignored; page marker `*[p.N]*` = printed page.
- honsatsu: DONE p000-p186 (front matter + 第1課-第12課 complete, book pp.1-169; empty files = page merged into previous)
  REMAINING: p187-192 学習項目 (pp.170-175) → table per lesson; p193-207 新出語索引 (176-189) → `| 読み | 表記 | 課 | 頁 |`;
  p208-209 会話表現索引 (190-191; bold = 本冊 heading expressions); p210-220 漢字索引 (192-203) → `#### 漢字` + ▲音 △訓 + `| 語 | 読み | 課 |`;
  p221 = publisher ad (skip), p222 blank. Then assemble + install + kaito-like verification.
- bunpo: not started (138 pp)
- Correction: 新出語索引 = p193-206 (pp.176-189), 会話表現索引 = p207-208 (190-191), 漢字索引 = p209-220 (192-203).
  漢字索引 format: `### N課` then table `| 漢字 | 音読み／訓読み | 提出語（読み）提出課 |`; okurigana (bold in book) marked with "." (おこ.る);
  red-letter (特別な) readings cannot be distinguished in greyscale scan → not marked.
- honsatsu: DONE all 223 pp (p019-021 were lost to a failed && chain and rewritten). Installed 2026-09-15; old OCR → honsatsu/ORIGINAL-ocr-backup.md. 81 figures in 70 Visuaalinen/liitteet. 漢字索引 = 315 kanji (matches 凡例).

## bunpo (Translation & Grammatical Notes, English) layout
- English prose as-is; *italics*/**bold** for book titles/emphasis as printed. Japanese keeps printed furigana {漢字|かな}.
- Vocabulary lists: table `| 語 | 読み | English |` (読み column empty when the word is kana); sub-notes like ［バランスを～］ stay in the 語 cell.
- Conversation-expression entries: `| 表現 | | English |` plus shaded function note as a following row `| | | *note* |`.
- Lesson: `## Lesson N`; parts `### I. Vocabulary`, `### II. Grammatical Notes`; grammar headings `#### 1. …`.
- Page marker `*[p.N]*` printed page (front matter `*[PDF NNN]*`).
- Vocabulary: a new table header after each page break is fine; section labels **Conversational expressions** / **Proper nouns** (unlabelled in book, separated by dotted line). NB book p.3 is MISSING from the PDF scan.
- bunpo: DONE p000-p003 (cover, copyright, Foreword). p010 = "How to Use This Textbook Effectively" start. NEXT: p004.
- bunpo: DONE p000-p023 (front matter + contents). Vocabulary Part 1 starts p024 (book p.2). Book page = PDF - 22.
- bunpo: DONE p000-p066 (front matter + Part 1 Vocabulary, all 12 lessons). NEXT p067 = Part 2 Grammatical Notes.
- Grammar-notes format: `#### N．<boxed pattern>`; connection formula as `**Connection:** …` (brace alternatives joined with ／);
  numbered examples `①　日本語<br>English` (one paragraph each); **Ref:** boxes as `> **Ref:** 「…」：<br>例文　（☞『…』Lesson N）`; ※ notes kept.
- bunpo: DONE all 138 pp. Installed 2026-09-16; old OCR → bunpo/ORIGINAL-ocr-backup.md.
  Book's own alternative braces {a／b} are written with FULL-WIDTH ｛a／b｝ so they don't clash with {漢字|かな} ruby.
  Book p.3 (L1 vocab between 似合う and 使い分ける) is absent from the PDF itself (old OCR confirms).
- 中級Ⅰ: ALL FOUR BOOKS DONE.

# 中級Ⅱ (same conventions; keys k2-honsatsu, k2-kaito, k2-bunpo)
- k2-kaito: book prints NO furigana → plain Japanese, no ruby. Same answer layout as kaito. Book page = PDF - 2 (p002 = p.1).
- k2-kaito: PDF is MISSING book pages (76 PDF pp for a book that runs to p.81+). First confirmed gap: book pp.34-37
  (PDF p034 = book 33, PDF p035 = book 38). Gaps are flagged inline with a ⚠ blockquote.
  Second gap: book pp.44-47 (第24課 answers) — PDF p040 = book p.43, PDF p041 = book p.48 (script section start).
- k2-kaito: DONE all 76 pp. Installed 2026-09-16; old OCR → k2-kaito/ORIGINAL-ocr-backup.md.
  Gaps (missing from PDF itself): book pp.34-37, 44-47 — flagged inline with ⚠ blockquotes.
- k2-honsatsu: next (216 pp, PNG 1433 px wide). Book has furigana → keep {漢字|かな} as in 中級Ⅰ honsatsu.
- k2-honsatsu: page marker = printed page (PDF 024 = book p.1). Lesson opener box = blockquote like 中級Ⅰ honsatsu.
