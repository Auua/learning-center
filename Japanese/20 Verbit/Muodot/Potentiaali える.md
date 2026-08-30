---
type: form
ja: 可能形
name: Potentiaali える
base: 可能形
func: [kyky, mahdollisuus]
jlpt: N4
sources: ["[[Minna no Nihongo II#Luku 27]]", "[[Minna no Nihongo Chuukyuu I#Luku 12]]"]
status: learning
confidence: 3
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> "Osata / pystyä / voida tehdä". Taipuu itse kuin ichidan-verbi.

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → え-rivi + る | 書く → 書ける、飲む → 飲める |
| 一段 | る → られる | 食べる → 食べられる |
| 不規則 | する → **できる**、来る → 来られる（こられる） | |

## Partikkeli vaihtuu
を → **が**: 日本語**を**話す → 日本語**が**話せる。（を on puhekielessä yleistymässä, mutta が on turvallinen.）

## ら抜き言葉
Puhekielessä 食べられる → 食べれる. Ymmärretään, mutta ei kirjoitettuun kieleen eikä JLPT-vastaukseksi.

## Huomio
- 見える/聞こえる = aisti toimii itsestään; 見られる/聞ける = tilaisuus tai kyky. Vertaa: [[Vertailu — Potentiaali vs. spontaani aisti]]
- Potentiaalilla ei ole tahtomuotoa eikä käskymuotoa.

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
