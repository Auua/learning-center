---
type: form
ja: ない形
name: ない-muoto
base: 未然形（あ段）
func: [kielto, kielteinen-ehto, kielteinen-pyyntö]
jlpt: N5
sources: ["[[Minna no Nihongo I#Luku 17]]", "[[Minna no Nihongo Chuukyuu I#Luku 7]]"]
status: learning
confidence: 4
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Kielto ei-kohteliaasti sekä pohja rakenteille ～なければならない、～ないでください、～なくてもいい、～ないほうがいい.

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → あ-rivi + ない | 書く → 書かない、飲む → 飲まない |
| 五段, päättyy う | う → **わ** + ない | 買う → 買わない (ei ×買あない) |
| 一段 | る pois + ない | 食べる → 食べない |
| 不規則 | する → しない、来る → 来ない（こない） | |

## Poikkeukset
- **ある → ない** (ei ×あらない).

## Johdannaiset
- ない → なくて (syy) / ないで (tapa)
- ない → なかった (mennyt kielto)

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
      file.name: 488
      note.func: 408
      note.confidence: 51

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
