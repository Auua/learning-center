import pymupdf, os
books = {
 "k2-kaito": "皆の日本語中級２本冊解答.pdf",
 "k2-bunpo": "皆の日本語中級２翻訳・文法解説英語版.pdf",
 "k2-honsatsu": "皆の日本語中級２本冊.pdf",
}
for key, fn in books.items():
    d = pymupdf.open(os.path.join("..", "PDF", fn))
    os.makedirs(f"{key}/pages", exist_ok=True); os.makedirs(f"{key}/out", exist_ok=True)
    for i in range(d.page_count):
        p = f"{key}/pages/p{i:03d}.png"
        if not os.path.exists(p):
            pix = d[i].get_pixmap(dpi=200, colorspace=pymupdf.csGRAY)
            pix.save(p)
    print(key, d.page_count, d[0].rect.width, d[0].rect.height)
