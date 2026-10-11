<%* const j = await tp.system.suggester(["N5","N4","N3","N2","N1"], ["N5","N4","N3","N2","N1"], false, "JLPT-taso"); -%>
---
type: compare
topic: "<% tp.file.title %>"
members: []
axis: []
jlpt: <% j %>
status: new
confidence: 1
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [compare, jlpt/<% j.toLowerCase() %>]
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

## Testilauseet itselle
1. ＿＿＿、… → vastaus

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
#flashcards/compare/<% j.toLowerCase() %>

#flashcards/compare/<% j.toLowerCase() %>/saanto

Milloin kumpi? (yhden lauseen sääntö)
?
vastaus

#flashcards/compare/<% j.toLowerCase() %>/paatospuu

päätöspuun ehto (esim. seuraus on väistämätön)
?
valittava rakenne

#flashcards/compare/<% j.toLowerCase() %>/rakenne

rakenne ::: ydinero
rakenne (sarake) :: arvo

#flashcards/compare/<% j.toLowerCase() %>/minimipari

A-lause vs. B-lause: mikä ero?
?
ero

#flashcards/compare/<% j.toLowerCase() %>/testi

Täytä: ＿＿＿、…
?
oikea vastaus — perustelu
