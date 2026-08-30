---
type: form
ja: 命令形
name: Käskymuoto ろ
base: 命令形
func: [käsky, kielto]
jlpt: N4
sources: ["[[Minna no Nihongo II#Luku 33]]"]
status: learning
confidence: 3
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Suora käsky. Töykeä arjessa, mutta tavallinen kylteissä, urheilussa, mangassa ja epäsuorassa kerronnassa (～と言われた).

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → え-rivi | 書く → 書け、飲む → 飲め |
| 一段 | る → ろ（kirjakielessä よ） | 食べる → 食べろ / 食べよ |
| 不規則 | する → しろ／せよ、来る → 来い（こい） | |

## Kieltokäsky
Sanakirjamuoto + **な**: 行くな。 見るな。

## Pehmeämmät vaihtoehdot
～てください ＞ ～て ＞ ～なさい ＞ 命令形

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
