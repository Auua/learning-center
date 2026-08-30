---
type: source
title: Satori Reader
kind: reading
url: https://www.satorireader.com
level: [N4, N3, N2]
language: ja
status: suositus
created: 2026-08-29
tags: [source, immersion]
---

> [!info] Mihin käytän
> Tasonmukaista luettavaa, jossa jokaiseen lauseeseen on kieliopin selitys ja ääni. Sopii juuri N3-vaiheeseen, jossa oppikirjan ja aidon tekstin väliin jää kuilu. Poimi lauseita [[T Immersio]]-pohjalla.

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
