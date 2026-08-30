---
type: set
theme: "<% tp.file.title %>"
jlpt: 
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [set]
---

> [!abstract] Tilanne
> Missä tätä sanastoa oikeasti tarvitaan.

## Sanat
```base
filters:
  and:
    - 'sets.contains(this)'
views:
  - type: table
    name: Sanat
    order:
      - file.name
      - note.reading
      - note.jlpt
      - note.status
    sort:
      - property: note.jlpt
        direction: ASC
```

## Valmiit fraasit
- 
