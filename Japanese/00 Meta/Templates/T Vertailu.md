---
type: compare
topic: "<% tp.file.title %>"
members: []
axis: []
jlpt: 
status: new
confidence: 1
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [compare]
---

> [!question] Milloin kumpi?
> Yhden lauseen sääntö, joka ratkaisee 80 % tapauksista.

## Päätöspuu
1. 
2. 

## Vertailutaulukko
| Rakenne | Ydinero | Menneisyys OK? | Tahdonilmaus jälkilauseessa OK? | Tyyliväri |
|---|---|---|---|---|

## Minimiparit
| A | B | Ero |
|---|---|---|

## Jäsenet
```base
filters:
  and:
    - 'type == "grammar"'
    - 'compare == this'
views:
  - type: table
    name: Jäsenet
    order:
      - file.name
      - note.jlpt
      - note.func
      - note.status
      - note.confidence
    sort:
      - property: note.confidence
        direction: ASC
```

## Kortit
#flashcards/compare 
