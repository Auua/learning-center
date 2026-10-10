---
type: source
title: Core 2k/6k
kind: srs
url: https://ankiweb.net/shared/decks
level: [N5, N4, N3, N2, N1]
language: en
status: kaytossa
created: 2026-10-10
tags: [source, vocab, srs, anki]
---

> [!info] Mihin käytän
> Frekvenssijärjestetty perussanasto (Core 2000 + Core 6000) Anki-pakoista. Sanat tuotiin vaultiin 2026-10-10 skriptillä `00 Meta/Scripts/anki_to_vault.py`; tuodut muistiinpanot tunnistaa tagista `lahde/anki-core`. Suomenkieliset merkitykset (`anki/fi-auto`) on käännetty englanninkielisestä glossasta ja kannattaa tarkistaa.

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
