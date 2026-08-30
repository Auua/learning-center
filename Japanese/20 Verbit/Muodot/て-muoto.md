---
type: form
ja: て形
name: て-muoto
base: 音便形
func: [lauseiden-yhdistys, pyyntö, jatkuva-tekeminen, lupa]
jlpt: N5
sources: ["[[Minna no Nihongo I#Luku 14]]"]
status: learning
confidence: 4
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Japanin tärkein liitosmuoto. Ilman tätä ei ole ～ている、～てください、～てもいい、～てから、～てみる、～ておく、～てしまう.

## Muodostussäännöt
| Verbityyppi | Pääte | Sääntö | Esimerkki |
|---|---|---|---|
| 五段 | う・つ・る | → って | 買う → 買って、待つ → 待って、取る → 取って |
| 五段 | む・ぶ・ぬ | → んで | 飲む → 飲んで、遊ぶ → 遊んで、死ぬ → 死んで |
| 五段 | く | → いて | 書く → 書いて |
| 五段 | ぐ | → いで | 泳ぐ → 泳いで |
| 五段 | す | → して | 話す → 話して |
| 一段 | る | → て | 食べる → 食べて |
| 不規則 | | する → して、来る → 来て（きて） | |

## Poikkeukset
- **行く → 行って** (ei ×行いて). Ainoa iso poikkeus.
- 問う → 問うて、請う → 請うて (harvinaisia).

## Muistisääntö
う・つ・る = "utsuru" → って. む・ぶ・ぬ = "mubunu" → んで. く/ぐ = いて/いで. す = して.

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
