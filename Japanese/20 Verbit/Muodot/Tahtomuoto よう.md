---
type: form
ja: 意向形
name: Tahtomuoto よう
base: 意向形
func: [ehdotus, aikomus]
jlpt: N4
sources: ["[[Minna no Nihongo II#Luku 31]]", "[[Minna no Nihongo Chuukyuu I#Luku 5]]", "[[Minna no Nihongo Chuukyuu I#Luku 7]]"]
status: learning
confidence: 3
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> "Tehdäänpä / aion tehdä". Kohtelias vastine on ～ましょう.

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → お-rivi + う | 書く → 書こう、飲む → 飲もう |
| 一段 | る → よう | 食べる → 食べよう |
| 不規則 | する → しよう、来る → 来よう（こよう） | |

## Jatkorakenteet
- ～ようと思う — aikomus, jonka olen juuri päättänyt (ks. [[Vようと思っています (harkittu aikomus)]])
- ～ようとする／としない — yrittää tehdä / olla tekemäisillään, kielteisenä kieltäytyä yrittämästä — täysi käsittely: [[Vようとする (yrittaa, olla tekemaisillaan)]]
- ～ようがない — ei ole mitään keinoa tehdä

## Kieliopit jotka liittyvät tähän muotoon
```base
filters:
  and:
    - type == "grammar"
    - attaches.contains(this)
views:
  - type: table
    name: Kieliopit
    order:
      - file.name
      - jlpt
      - func
      - status
      - confidence
    sort:
      - property: jlpt
        direction: ASC
    columnSize:
      file.name: 431
      note.func: 416
      note.confidence: 38

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
