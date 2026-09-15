---
type: set
theme: "Adverbit: tapa"
created: 2026-08-30
tags: [set, adverbi]
---

> [!abstract] Tilanne
> Miten jokin tehdään. Täydentää sanoja [[ゆっくり]]・[[しっかり]]・[[ちゃんと]]・[[はっきり]]・[[わざと]].

| JA | Lukutapa | FI |
|---|---|---|
| [[きちんと]] | きちんと | siististi, kunnolla |
| [[ぴったり]] | ぴったり | täsmälleen, juuri sopivasti |
| [[こっそり]] | こっそり | salaa, hiljaa |
| [[なんとなく]] | なんとなく | jotenkin, ilman erityistä syytä |
| [[なんとか]] | なんとか | jotenkuten, saada jotenkin hoidettua |
| [[たまたま]] | たまたま | sattumalta |

> [!note] きちんと vs ちゃんと
> Sama merkitys, eri rekisteri: [[ちゃんと]] on arkisempi, [[きちんと]] hieman huolitellumpi. Molemmat käyvät useimmissa tilanteissa.

> [!note] なんとか ja なんとなく
> Näyttävät samalta mutta eivät ole: なんとか = "sain jotenkin hoidettua" (lopputulos), なんとなく = "jotenkin vain, en osaa sanoa miksi" (syy puuttuu). なんとなく 悲しい = "olen jotenkin surullinen".

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
