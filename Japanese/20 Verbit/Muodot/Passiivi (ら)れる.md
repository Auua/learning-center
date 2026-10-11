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

## Merkitys
- **FI:** passiivi: tavallinen, kärsimys- ja kohtelias passiivi
- **EN:** passive form

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

<!-- verbityyppikortit:alku -->
## Kortit
#flashcards/form/n4/taivutus

受身形: 買う（かう, 五段 う） ::: 買われる（かわれる）
受身形: 言う（いう, 五段 う） ::: 言われる（いわれる）
受身形: 待つ（まつ, 五段 つ） ::: 待たれる（またれる）
受身形: 持つ（もつ, 五段 つ） ::: 持たれる（もたれる）
受身形: 取る（とる, 五段 る） ::: 取られる（とられる）
受身形: 帰る（かえる, 五段 る） ::: 帰られる（かえられる）
受身形: 飲む（のむ, 五段 む） ::: 飲まれる（のまれる）
受身形: 読む（よむ, 五段 む） ::: 読まれる（よまれる）
受身形: 遊ぶ（あそぶ, 五段 ぶ） ::: 遊ばれる（あそばれる）
受身形: 呼ぶ（よぶ, 五段 ぶ） ::: 呼ばれる（よばれる）
受身形: 死ぬ（しぬ, 五段 ぬ） ::: 死なれる（しなれる）
受身形: 書く（かく, 五段 く） ::: 書かれる（かかれる）
受身形: 歩く（あるく, 五段 く） ::: 歩かれる（あるかれる）
受身形: 泳ぐ（およぐ, 五段 ぐ） ::: 泳がれる（およがれる）
受身形: 急ぐ（いそぐ, 五段 ぐ） ::: 急がれる（いそがれる）
受身形: 話す（はなす, 五段 す） ::: 話される（はなされる）
受身形: 貸す（かす, 五段 す） ::: 貸される（かされる）
受身形: 行く（いく, 五段 く, poikkeus） ::: 行かれる（いかれる）
受身形: 見る（みる, 一段 (iる)） ::: 見られる（みられる）
受身形: 起きる（おきる, 一段 (iる)） ::: 起きられる（おきられる）
受身形: 食べる（たべる, 一段 (eる)） ::: 食べられる（たべられる）
受身形: 寝る（ねる, 一段 (eる)） ::: 寝られる（ねられる）
受身形: する（不規則） ::: される
受身形: 勉強する（べんきょうする, 不規則） ::: 勉強される（べんきょうされる）
受身形: 来る（くる, 不規則） ::: 来られる（こられる）
<!-- verbityyppikortit:loppu -->

#flashcards/form/n4

受身形: mitkä kolme käyttöä?
?
Tavallinen passiivi, kärsimyspassiivi (迷惑の受身) ja kohtelias passiivi (尊敬語).

#flashcards/form/n4/saanto

受身形 + 五段 :: う-rivi → あ-rivi + れる（う → わ） (読む → 読まれる、言う → 言われる)
受身形 + 一段 :: る → られる (食べる → 食べられる)
受身形 + 不規則 :: する → される、来る → 来られる（こられる）

#flashcards/form/n4/huomio

Passiivi: perusrakenne?
?
A は B に ～(ら)れる (先生に褒められた)

Passiivi vs. ichidan-potentiaali: ero?
?
Muoto on identtinen; konteksti ratkaisee.

Kärsimyspassiivi: mitä se tarkoittaa?
?
Tapahtuma haittasi puhujaa; myös intransitiivinen verbi voi olla passiivissa (雨に降られた "jouduin sateeseen")

Kärsimyspassiivi, transitiivinen verbi: mikä pysyy?
?
Objekti säilyy を:lla (店員にスープをこぼされて…)

Passiivi neutraalissa tosiasiassa: miten tekijä merkitään?
?
によって (「げんじものがたり」は紫式部によって書かれました)

受身形 kohteliaisuutena?
?
社長はもう帰られました = 帰りました kunnioittavasti

#flashcards/form/n4/liittyy

Nから作られます (raaka-aine) — mihin verbimuotoon liittyy?
?
受身形 (Passiivi (ら)れる)

〜によって (tekijan merkitseminen, luova teko) — mihin verbimuotoon liittyy?
?
受身形 (Passiivi (ら)れる)

受身形: mitä kielioppeja siihen liittyy?
?
2 kielioppia, esim. Nから作られます (raaka-aine), 〜によって (tekijan merkitseminen, luova teko)
