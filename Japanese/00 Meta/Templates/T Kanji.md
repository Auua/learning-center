<%* const j = await tp.system.suggester(["N5","N4","N3","N2","N1"], ["N5","N4","N3","N2","N1"], false, "JLPT-taso"); -%>
---
type: kanji
kanji: <% tp.file.title %>
strokes:
grade:
jlpt: <% j %>
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
  - jlpt/<% j.toLowerCase() %>
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
#flashcards/kanji/<% j.toLowerCase() %>

<% tp.file.title %> (merkitys) ::: merkitys
<% tp.file.title %> (on'yomi) :: lukutapa (esimerkkisana lukutapa – käännös)
<% tp.file.title %> (kun'yomi) :: lukutapa (esimerkkisana lukutapa – käännös)
muistisääntö :: <% tp.file.title %>

#flashcards/kanji/<% j.toLowerCase() %>/sanat

<% tp.file.title %> - sana ::: (lukutapa) – käännös

#flashcards/kanji/<% j.toLowerCase() %>/nakoisserkut

<% tp.file.title %> (näköisserkut) :: toinen kanji (merkitys), toinen kanji (merkitys)

<% tp.file.title %> — mitkä kanjit muistuttavat tätä ja miten ne erotetaan?
?
ero
