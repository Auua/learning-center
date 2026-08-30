---
type: set
theme: "Kirjoitusjärjestelmät"
jlpt: N5
created: 2026-08-29
tags: [set]
---

> [!abstract] Tilanne
> Japanin kirjoitusjärjestelmästä puhuminen — [[Minna no Nihongo I#Luku 9]].

## Sanat
| JA | FI |
|---|---|
| [[絵]] | kuva, piirros |
| [[字]] | kirjain, merkki |
| [[漢字]] | kanji |
| [[ひらがな]] | hiragana |
| [[かたかな]] | katakana |
| [[ローマ字]] | latinalaiset aakkoset |
| [[細かいお金]] | pikkuraha, vaihtoraha |
| [[チケット]] | lippu (esim. konsertti) |

## Muistiinpanot
[[書く]] · [[読む]]

## Sanat (omat muistiinpanot)
```base
filters:
  and:
    - 'sets.contains(this)'
views:
  - type: table
    name: Sanat
    order:
      - file.name
      - note.reading
      - note.jlpt
      - note.status
    sort:
      - property: note.jlpt
        direction: ASC
```
