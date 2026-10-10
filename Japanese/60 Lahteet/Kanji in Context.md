---
type: source
title: Kanji in Context (Revised Edition)
kind: textbook
url: 
level: [N3, N2, N1]
language: en
status: kaytossa
created: 2026-10-10
tags: [source, kanji, vocab, anki]
---

> [!info] Mihin käytän
> Kanji in Context -kirjan sanasto (Anki-pakka "Kanji in Context: Revised Edition"). Sanat tuotiin vaultiin 2026-10-10 skriptillä `00 Meta/Scripts/anki_to_vault.py`; tuodut muistiinpanot tunnistaa tagista `lahde/anki-kic`. Työkirja on erikseen: [[Kanji in the context workbook 1]].

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
