import pymupdf, os, sys
books = {
 "mondai": "皆の日本語中級１標準問題集.pdf",
 "kaito": "皆の日本語中級1本冊解答.pdf",
 "honsatsu": "皆の日本語中級１本冊.pdf",
 "bunpo": "皆の日本語中級１翻訳・文法解説英語版.pdf",
}
for key, fn in books.items():
    d = pymupdf.open(os.path.join("..", "PDF", fn))
    os.makedirs(f"{key}/pages", exist_ok=True); os.makedirs(f"{key}/out", exist_ok=True)
    for i in range(d.page_count):
        p = f"{key}/pages/p{i:03d}.png"
        if not os.path.exists(p):
            d[i].get_pixmap(dpi=200, colorspace=pymupdf.csGRAY).save(p)
    r = d[0].rect
    print(key, d.page_count, "pages", r.width, r.height)
