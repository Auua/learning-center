---
type: source
title: WaniKani
kind: srs
url: https://www.wanikani.com
level: [N5, N4, N3, N2]
language: en
status: harkinnassa
created: 2026-08-29
tags: [source, kanji, srs]
---

> [!info] Mihin käytän
> Kanjien radikaali- ja mnemoniikkajärjestelmä. Jos käytät, kopioi radikaalin nimi `40 Kanji/Osat`-muistiinpanoon, niin muistisäännöt pysyvät yhtenäisinä.

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
