---
type: form
ja: 
name: "<% tp.file.title %>"
base: 
func: []
jlpt: 
sources: []
status: new
confidence: 1
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> 

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 godan | | |
| 一段 ichidan | | |
| 不規則 epäsäännöllinen | する → 、来る → | |

## Poikkeukset
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
#flashcards/form 
