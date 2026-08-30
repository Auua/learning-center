---
type: source
title: Bunpro
kind: site
url: https://bunpro.jp/grammar_points
level: [N5, N4, N3, N2, N1]
language: en
status: kaytossa
created: 2026-08-29
tags: [source, site, srs]
---

> [!info] Mihin käytän
> Kielioppipisteen tarkistus ja esimerkkilauseet. URL-kaava: `https://bunpro.jp/grammar_points/<kielioppi>` (japanilaiset merkit URL-koodattuna), esim. [たら](https://bunpro.jp/grammar_points/%E3%81%9F%E3%82%89), [と (conditional)](https://bunpro.jp/grammar_points/%E3%81%A8-conditional).

## Mitä tästä on käyty läpi
```base
filters:
  and:
    - 'sources.contains(this)'
views:
  - type: table
    name: Käyty läpi
    order:
      - file.name
      - note.type
      - note.jlpt
      - note.status
    sort:
      - property: note.type
        direction: ASC
```
