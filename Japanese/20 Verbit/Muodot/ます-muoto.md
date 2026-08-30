---
type: form
ja: ます形
name: ます-muoto
base: 連用形（い段）
func: [kohteliaisuus, teonsana-vartalo]
jlpt: N5
sources: ["[[Minna no Nihongo I#Luku 4]]"]
status: known
confidence: 5
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Kohtelias taso. Vartalo (ます-runko ilman ますia) on myös lähtökohta monelle päätteelle: ～たい、～ながら、～やすい、～すぎる、～方.

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → い-rivi + ます | 書く → 書きます、飲む → 飲みます |
| 一段 | る pois + ます | 食べる → 食べます |
| 不規則 | する → します、来る → 来ます（きます） | |

## Aikamuodot
| | Myönteinen | Kielteinen |
|---|---|---|
| Preesens | 書きます | 書きません |
| Menneisyys | 書きました | 書きませんでした |

## Vartaloon liittyvät päätteet
～たい、～ながら、～やすい／～にくい、～すぎる、～方（かた）、～に行く

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
