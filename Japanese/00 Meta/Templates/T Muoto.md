<%* const j = await tp.system.suggester(["N5","N4","N3","N2","N1"], ["N5","N4","N3","N2","N1"], false, "JLPT-taso"); -%>
---
type: form
ja: 
name: "<% tp.file.title %>"
base: 
func: []
jlpt: <% j %>
sources: []
status: new
confidence: 1
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [form, jlpt/<% j.toLowerCase() %>]
---

> [!abstract] Mihin tätä tarvitaan
> 

## Merkitys
- **FI:** 
- **EN:** 

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 godan | | |
| 一段 ichidan | | |
| 不規則 epäsäännöllinen | する → 、来る → | |

## Poikkeukset
- 

## Puhekieli
- 

## Huomiot
- 

## Kieliopit jotka käyttävät tätä muotoa
```base
filters:
  and:
    - 'type == "grammar"'
    - 'attaches.contains(this)'
views:
  - type: table
    name: Kieliopit
    order:
      - file.name
      - note.jlpt
      - note.func
      - note.status
      - note.confidence
    sort:
      - property: note.jlpt
        direction: ASC
```

## Verbit joilla tämä on merkitty poikkeukselliseksi
```base
filters:
  and:
    - 'type == "verb"'
    - 'file.hasLink(this.file)'
views:
  - type: list
    name: Verbit
    order:
      - file.name
```

## Kortit
#flashcards/form/<% j.toLowerCase() %>

<% tp.file.title %>: mitä se tarkoittaa tai tekee?
?
merkitys

#flashcards/form/<% j.toLowerCase() %>/saanto

<% tp.file.title %> + 五段 う・つ・る :: sääntö (esimerkki)
<% tp.file.title %> + 五段 む・ぶ・ぬ :: sääntö (esimerkki)
<% tp.file.title %> + 一段 :: sääntö (esimerkki)
<% tp.file.title %> + 不規則 :: する → …、来る → …

#flashcards/form/<% j.toLowerCase() %>/taivutus

<% tp.file.title %>: 買う（かう, 五段 う） ::: taivutettu muoto（lukeminen）

#flashcards/form/<% j.toLowerCase() %>/poikkeus

poikkeuskysymys
?
vastaus

#flashcards/form/<% j.toLowerCase() %>/huomio

huomiokysymys
?
vastaus

#flashcards/form/<% j.toLowerCase() %>/puhekieli

kirjakielinen muoto
??
puhekielinen muoto

#flashcards/form/<% j.toLowerCase() %>/liittyy

kielioppi — mihin muotoon liittyy?
?
<% tp.file.title %>
