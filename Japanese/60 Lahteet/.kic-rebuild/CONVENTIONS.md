# Rebuild: "Kanji in Context Workbook Vol.1" transcription from scanned PDF

## Why this lives in the repo
A previous run kept all output in /private/tmp; macOS purged it and ~178 pages were lost.
Everything durable now lives here and is committed to git. PNGs are gitignored (regenerable).

## Paths
- PDF: ../PDF/Kanji in the context workbook 1.pdf
- Old OCR (leave untouched until the rebuild is complete): ../Kanji in the context workbook 1.md
- Page PNGs (300dpi grey, gitignored): ./pages/pNNN.png   NNN = PDF index 000-219
- Per-page output: ./out/pNNN.md  -> concatenated at the end, then swapped in for the old OCR
- venv with pymupdf: session scratchpad (regenerate with `python3 -m venv venv && ./venv/bin/pip install pymupdf`)

## Re-render pages if missing
./venv/bin/python -c "
import pymupdf; d=pymupdf.open(PDF)
[d[i].get_pixmap(dpi=300, colorspace=pymupdf.csGRAY).save(f'pages/p{i:03d}.png') for i in range(d.page_count)]"

## Page mapping
PDF index = book page + 20.  Book p.1 = PDF 021 ... book p.199 = PDF 219.
PDF 000-020 = cover + front matter (roman i-xxi).

## Formatting conventions (agreed with user)
- Lesson heading: `## 第 N 回　(first-last)`
- Section headings bold, blank rendered as ＿＿＿. Level 1-2 word them "意味と読み方";
  Level 3 uses "読み方と意味". Some lessons use "次の表現を勉強し" for section II too.
  Copy exactly what the page shows.
- Each checkbox item = one `- ` bullet. Multiple expressions on a printed line separated by
  two ideographic spaces （　　）.
- **bold** = word is UNDERLINED in the book (i.e. reference-book vocabulary).
- {漢字|かな} = furigana printed in the book (vault's markdown-furigana plugin syntax).
- Section III answer column goes at the end of the bullet after ` → `, multiple answers
  separated by ／ :  `- ...**万一**うまく... → **十分**（じゅうぶん）／**万一**（まんいち）`
- Kanji strip at page bottom: `**学習漢字 14–26:**　円　人　日　…`
- Page marker at end of each page file: `*[p.3]*`   (front matter uses `*[xiv]*`)
- `---` starts a new lesson page (the page carrying a 第N回 heading) only.
- ▲ before a kanji = not a reference-book entry (keep it).
- Ignore the previous owner's pencil handwriting in the scans.

## Method
Read pages/pNNN.png, transcribe, write with `cat > out/pNNN.md <<'EOF'` (Bash heredoc).
Crop-zoom only when underline/furigana is genuinely ambiguous.
Output lives in the repo working tree, which is what survives a /tmp purge.
Not committing unless the user asks (they own the vault's commit history).

## Progress
- DONE front matter: 001-012 (pages i-xiv)
- DEFERRED: 013-020 (English Introduction, pages xv-xxi) - user said start from body p.1 instead
- DONE body: 021-046 = LEVEL 1 COMPLETE (第1回-第11回, book pp.1-26)
- DONE body: 047-062 = LEVEL 2 COMPLETE (第12回-第18回, book pp.27-42)
- DONE body: 063-137 = Level 3 divider + 第19回-第55回 (book pp.43-117)
- DONE body: 138-140 (第56回 cont., 第57回 start, book pp.118-120)
- DONE body: 141-183 (第57回 cont. through 第76回, book pp.121-163)
- DONE body: 184-219 = LEVEL 3 COMPLETE (第77回-第94回, book pp.164-199)
- ALL PAGES TRANSCRIBED. Assembled into assembled.md and installed as
  "60 Lahteet/Kanji in the context workbook 1.md" on 2026-09-15.
  Previous yomitoku OCR saved as .kic-rebuild/ORIGINAL-ocr-backup.md
- REMAINING (only if asked): PDF 013-020 = English Introduction, book pp.xv-xxi.
