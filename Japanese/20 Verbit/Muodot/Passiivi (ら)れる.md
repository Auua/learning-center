---
type: form
ja: 受身形
name: Passiivi (ら)れる
base: 未然形 + れる/られる
func: [passiivi, karsimyspassiivi, kohteliaisuus]
jlpt: N4
sources: ["[[Minna no Nihongo II#Luku 37]]", "[[Minna no Nihongo II#Luku 49]]", "[[Minna no Nihongo Chuukyuu I#Luku 12]]"]
status: shaky
confidence: 3
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Kolme eri käyttöä, jotka näyttävät samalta: tavallinen passiivi, kärsimyspassiivi (迷惑の受身) ja kohtelias passiivi (尊敬語).

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → あ-rivi + れる（う → わ） | 読む → 読まれる、言う → 言われる |
| 一段 | る → られる | 食べる → 食べられる |
| 不規則 | する → される、来る → 来られる（こられる） | |

Muoto on identtinen ichidan-verbien [[Potentiaali える]]-muodon kanssa — konteksti ratkaisee.

## Rakenne
A **は** B **に** ～(ら)れる。
- 先生に褒められた。 Opettaja kehui minua.

## Kärsimyspassiivi
Intransitiivinenkin verbi voi olla passiivissa, kun tapahtuma haittasi puhujaa:
- 雨に降られた。 Jouduin sateeseen.
- 友達に来られて、勉強できなかった。
- ラッシュの電車で足を踏まれました。（joku astui jalalleni — ikävä sivuvaikutus）
- だれかに傘をまちがえられたんです。（joku otti sateenvarjoni vahingossa toisen sijaan — haittaava vaikutus, vaikka tekijä ei ollut tahallinen）

Chuukyuu I Luku 12 vahvistaa kaavan kaksi alalajia:
- **Intransitiivinen verbi**: 家へ帰る途中、雨に**降られて**、風邪をひいてしまった。／自転車で犯人を追いかけたが、**逃げられて**しまった。／隣の人に**騒がれて**、全然勉強できませんでした。
- **Transitiivinen verbi, objekti säilyy を:llä**: 店員にスープを**こぼされて**、新しいズボンが汚れてしまった。／家の前に自転車やバイクを**止められて**、困っています。／店のシャッターにスプレーで**落書きされて**、困っています。

Molemmissa tapauksissa lauseen aihe (puhuja) on tekemisen **haitallinen sivullinen**, ei suoraan sen kohde — tämä erottaa kärsimyspassiivin tavallisesta passiivista.

## Tavallinen kohteliaisuutta vailla oleva passiivi
Passiivia käytetään myös neutraaleissa historiallisissa/kulttuurisissa faktoissa, usein [[〜によって (tekijan merkitseminen, luova teko)]]:n kanssa: 法隆寺は607年に建てられました。「げんじものがたり」は紫式部によって書かれました。

## Kohteliaisuuskäyttö
社長はもう帰られました。= 帰りました, mutta kunnioittavasti. Ks. [[Keigo — kartta]].

## Esimerkit
![[Lausepankki — Passiivi ja valmistus#^pas4]]
![[Lausepankki — Passiivi ja valmistus#^pas5]]

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
