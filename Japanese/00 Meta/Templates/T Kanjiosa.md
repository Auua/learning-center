---
type: component
glyph: "<% tp.file.title %>"
meaning: 
variants: []
strokes: 
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [kanji/component]
---

## Merkitys
 

## Muodot
 

## Kanjit jotka sisältävät tämän
```base
filters:
  and:
    - 'type == "kanji"'
    - 'components.contains(this)'
views:
  - type: table
    name: Kanjit
    order:
      - file.name
      - note.meaning
      - note.jlpt
      - note.strokes
    sort:
      - property: note.strokes
        direction: ASC
```
