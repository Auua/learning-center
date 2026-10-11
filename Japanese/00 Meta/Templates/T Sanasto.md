<%* const j = await tp.system.suggester(["N5","N4","N3","N2","N1"], ["N5","N4","N3","N2","N1"], false, "JLPT-taso"); -%>
---
type: vocab
word: <% tp.file.title %>
reading:
romaji:
meaning:
pos:
jlpt: <% j %>
pitch:
opposite: []
similar: []
kanji: []
sets: []
sources: []
status: new
confidence: 1
reviewed:
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - vocab
  - jlpt/<% j.toLowerCase() %>
---

## Merkitys
- **FI:** 
- **EN:** 
- **Ääni:** 

## Kollokaatiot ja käyttö
- 

## Sekoitan tähän
- 

## Esimerkit
- 日本語の lause — suomi/englanti ![[lause-ääni.mp3]]
<!-- vaihtoehtoisesti upotus lausepankista: ![[Lausepankki — Aihe#^tunnus]] -->

## Kuvavihje
![[]]

## Kortit
#flashcards/vocab/<% j.toLowerCase() %>

<% tp.file.title %> :: reading - meaning
reading :: <% tp.file.title %> - meaning
meaning :: <% tp.file.title %> - reading
![[ääni.mp3]] ::: <% tp.file.title %> - meaning

<% tp.file.title %> (opposite) :: opposite
<% tp.file.title %> (similar) :: similar

日本語の lause ::: suomi/englanti
![[lause-ääni.mp3]] ::: suomi/englanti

#flashcards/vocab/<% j.toLowerCase() %>/kollokaatio

kollokaatio
??
suomi/englanti

#flashcards/vocab/<% j.toLowerCase() %>/sekoitan

kysymys
?
vastaus
