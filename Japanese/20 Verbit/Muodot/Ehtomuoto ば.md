---
type: form
ja: 仮定形（ば形）
name: Ehtomuoto ば
base: 仮定形
func: [ehto, yleinen-totuus]
jlpt: N4
sources: ["[[Minna no Nihongo II#Luku 35]]"]
status: learning
confidence: 3
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Yleinen ja looginen ehto: "jos A, niin B". Painottaa ehtoa, ei aikajärjestystä.

## Muodostussäännöt
| Sanaluokka | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → え-rivi + ば | 書く → 書けば |
| 一段 | る → れば | 食べる → 食べれば |
| 不規則 | する → すれば、来る → 来れば（くれば） | |
| い-adjektiivi | い → ければ | 安い → 安ければ |
| な-adjektiivi / subst. | + なら(ば) | 静か → 静かなら |
| Kielto | ない → なければ | 行かない → 行かなければ |

## Rajoitus
Jälkilauseessa ei yleensä voi olla käsky, pyyntö tai kutsu, jos etulause on toimintaverbi. Silloin käytä [[～たら (jos, kun)]].
- ○ 時間があれば、いいですね。
- × 京都に行けば、写真を撮ってください。→ ○ 京都に行ったら、…

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
