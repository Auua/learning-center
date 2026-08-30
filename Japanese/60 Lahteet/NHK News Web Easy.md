---
type: source
title: NHK News Web Easy
kind: reading
url: https://www3.nhk.or.jp/news/easy/
level: [N4, N3]
language: ja
status: suositus
created: 2026-08-29
tags: [source, immersion]
---

> [!info] Mihin käytän
> Päivittäinen lyhyt uutinen furiganalla ja äänellä. Ilmainen. Yksi artikkeli päivässä = säännöllinen lukurutiini ilman motivaatiokysymystä.

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
