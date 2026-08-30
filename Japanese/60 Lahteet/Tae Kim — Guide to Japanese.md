---
type: source
title: Tae Kim — A Guide to Japanese Grammar
kind: site
author: Tae Kim
url: https://www.guidetojapanese.org/learn/grammar
level: [N5, N4, N3]
language: en
status: kaytossa
created: 2026-08-29
tags: [source, site]
---

> [!info] Mihin käytän
> Selittää rakenteet japanilaisen logiikan kautta, ei käännöskaavoina. Hyvä silloin kun oppikirjan sääntö tuntuu mielivaltaiselta. Myös [PDF-versio](https://www.guidetojapanese.org/grammar_guide.pdf).

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
