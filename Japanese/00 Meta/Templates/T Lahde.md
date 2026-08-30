---
type: source
title: "<% tp.file.title %>"
kind: textbook
author: 
url: 
level: []
language: 
status: kaytossa
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [source]
---

> [!info] Mihin käytän
> 

## Rakenne / ankkurit
Linkitä muistiinpanoista otsikkoon: `[[<% tp.file.title %>#Luku 1]]`

### Luku 1

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
