---
type: source
title: A Dictionary of Basic / Intermediate Japanese Grammar
kind: reference
author: Makino & Tsutsui
url: 
level: [N5, N4, N3, N2]
language: en
status: kaytossa
created: 2026-08-29
tags: [source, reference]
---

> [!info] Mihin käytän
> Nyanssierojen ratkaiseva lähde. Jokaisessa hakusanassa on "Related Expressions" -osio, joka on suoraan vertailumuistiinpanojen raaka-ainetta.

Merkintätapa muistiinpanossa: `[[Dictionary of Japanese Grammar]]` s. 123 (DBJG) / (DIJG).

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
