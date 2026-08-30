---
type: form
ja: た形
name: た-muoto
base: 音便形
func: [menneisyys, kokemus, ehto]
jlpt: N5
sources: ["[[Minna no Nihongo I#Luku 19]]"]
status: learning
confidence: 4
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Menneisyys ei-kohteliaasti, ja pohja rakenteille ～たら、～たことがある、～たり～たり、～たほうがいい、～たばかり.

## Muodostussäännöt
Täsmälleen sama sääntö kuin [[て-muoto]], mutta て → た ja で → だ.

| Verbityyppi | て-muoto | た-muoto |
|---|---|---|
| 買う | 買って | 買った |
| 飲む | 飲んで | 飲んだ |
| 書く | 書いて | 書いた |
| 泳ぐ | 泳いで | 泳いだ |
| 話す | 話して | 話した |
| 食べる | 食べて | 食べた |
| する / 来る | して / 来て | した / 来た |

## Poikkeukset
- **行く → 行った**

## Kieliopit jotka liittyvät tähän muotoon
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

## Verbit joissa tämä on harjoiteltu
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
