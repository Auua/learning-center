---
type: source
title: Maggie Sensei
kind: site
url: https://maggiesensei.com
level: [N4, N3, N2]
language: en
status: kaytossa
created: 2026-08-29
tags: [source, site]
---

> [!info] Mihin käytän
> Puhekielen sävyt ja partikkelien nyanssit, joita oppikirjat eivät käsittele. Esim. [たら](https://maggiesensei.com/2011/02/17/conditional-%E3%80%9C%E3%81%9F%E3%82%89-tara-request-lesson/), [ば](https://maggiesensei.com/2018/03/28/how-to-use-%E3%81%B0-ba/).

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
