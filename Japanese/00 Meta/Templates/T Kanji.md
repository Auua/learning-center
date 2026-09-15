---
type: kanji
kanji: <% tp.file.title %>
strokes:
grade:
jlpt:
onyomi: []
kunyomi: []
meaning:
components: []
lookalikes: []
status: new
confidence: 1
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - kanji
---

## Avainmerkitys
 

## Osat
 

## Muistisääntö
> 

## Lukutavat
| Tyyppi | Lukutapa | Esimerkkisana |
|---|---|---|
| 音 on | | |
| 訓 kun | | |

## Sanat joissa esiintyy
```base
filters:
  and:
    - kanji.contains(this.file.name)
views:
  - type: table
    name: Sanat
    order:
      - file.name
      - reading
      - jlpt
      - status
      - meaning
    sort:
      - property: jlpt
        direction: ASC

```

## Näköisserkut
 

## Kuvavihje
![[]]

## Kortit
#flashcards/kanji 
<% tp.file.title %> — merkitys::
