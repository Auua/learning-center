---
type: source
title: Jisho.org
kind: dictionary
url: https://jisho.org
level: [N5, N4, N3, N2, N1]
language: en
status: kaytossa
created: 2026-08-29
tags: [source, dictionary]
---

> [!info] Mihin käytän
> Sanahaku, lukutavat, kanjin piirrosjärjestys, JLPT-taso, esimerkkilauseet.

Suora hakulinkki muistiinpanoon: `[食べる](https://jisho.org/search/食べる)` · kanji: `[食](https://jisho.org/search/食%20%23kanji)`

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
