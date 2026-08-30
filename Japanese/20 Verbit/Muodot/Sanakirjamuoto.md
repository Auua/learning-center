---
type: form
ja: 辞書形
name: Sanakirjamuoto
base: perusmuoto
func: [perusmuoto, ei-kohtelias-preesens, nominalisointi]
jlpt: N5
sources: ["[[Minna no Nihongo I#Luku 18]]"]
status: known
confidence: 5
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Verbin hakumuoto ja kaikkien muiden muotojen lähtökohta. Toimii myös lauseen sisällä ei-kohteliaana preesensinä.

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 godan | päättyy う-riviin: う・く・ぐ・す・つ・ぬ・ぶ・む・る | 書く、飲む、話す |
| 一段 ichidan | päättyy いる/える + る | 食べる、見る |
| 不規則 | する、来る（くる） | する、来る |

## Miten tunnistan tyypin
- Päättyy muuhun kuin る → aina **godan**.
- Päättyy る ja edellä い/え-äänne → yleensä **ichidan**, mutta poikkeuksia: 帰る、入る、走る、切る、知る、要る ovat godan.

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
