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

## Merkitys
- **FI:** liitosmuoto: yhdistää lauseita, pyynnöt, jatkuva tekeminen, lupa
- **EN:** te-form (connective form)

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

<!-- verbityyppikortit:alku -->
## Kortit
#flashcards/form/n5/taivutus

て形: 買う（かう, 五段 う） ::: 買って（かって）
て形: 言う（いう, 五段 う） ::: 言って（いって）
て形: 待つ（まつ, 五段 つ） ::: 待って（まって）
て形: 持つ（もつ, 五段 つ） ::: 持って（もって）
て形: 取る（とる, 五段 る） ::: 取って（とって）
て形: 帰る（かえる, 五段 る） ::: 帰って（かえって）
て形: 飲む（のむ, 五段 む） ::: 飲んで（のんで）
て形: 読む（よむ, 五段 む） ::: 読んで（よんで）
て形: 遊ぶ（あそぶ, 五段 ぶ） ::: 遊んで（あそんで）
て形: 呼ぶ（よぶ, 五段 ぶ） ::: 呼んで（よんで）
て形: 死ぬ（しぬ, 五段 ぬ） ::: 死んで（しんで）
て形: 書く（かく, 五段 く） ::: 書いて（かいて）
て形: 歩く（あるく, 五段 く） ::: 歩いて（あるいて）
て形: 泳ぐ（およぐ, 五段 ぐ） ::: 泳いで（およいで）
て形: 急ぐ（いそぐ, 五段 ぐ） ::: 急いで（いそいで）
て形: 話す（はなす, 五段 す） ::: 話して（はなして）
て形: 貸す（かす, 五段 す） ::: 貸して（かして）
て形: 行く（いく, 五段 く, poikkeus） ::: 行って（いって）
て形: 見る（みる, 一段 (iる)） ::: 見て（みて）
て形: 起きる（おきる, 一段 (iる)） ::: 起きて（おきて）
て形: 食べる（たべる, 一段 (eる)） ::: 食べて（たべて）
て形: 寝る（ねる, 一段 (eる)） ::: 寝て（ねて）
て形: する（不規則） ::: して
て形: 勉強する（べんきょうする, 不規則） ::: 勉強して（べんきょうして）
て形: 来る（くる, 不規則） ::: 来て（きて）
<!-- verbityyppikortit:loppu -->

#flashcards/form/n5

て形: mihin sitä tarvitaan?
?
Japanin tärkein liitosmuoto: ～ている、～てください、～てもいい、～てから、～てみる、～ておく、～てしまう.

#flashcards/form/n5/saanto

て形 + 五段 う・つ・る :: → って (買う → 買って、待つ → 待って、取る → 取って)
て形 + 五段 む・ぶ・ぬ :: → んで (飲む → 飲んで、遊ぶ → 遊んで、死ぬ → 死んで)
て形 + 五段 く :: → いて (書く → 書いて)
て形 + 五段 ぐ :: → いで (泳ぐ → 泳いで)
て形 + 五段 す :: → して (話す → 話して)
て形 + 一段 :: る → て (食べる → 食べて)
て形 + 不規則 :: する → して、来る → 来て（きて）

#flashcards/form/n5/poikkeus

行く: て形?
?
行って (ei ×行いて) — ainoa iso poikkeus

問う・請う: て形?
?
問うて、請うて (harvinaisia)

#flashcards/form/n5/huomio

て形: muistisääntö päätteille?
?
う・つ・る = "utsuru" → って; む・ぶ・ぬ = "mubunu" → んで; く/ぐ = いて/いで; す = して

#flashcards/form/n5/liittyy

Nこそ (juuri se, nimenomaan) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vて (tunnereaktion syy) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vて ください (pyyntö) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vて、Vて (peräkkäisyys) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてあげます・Vてもらいます・Vてくれます (teon antaminen) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてあります (tarkoituksella tehty tila) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vておきます (valmistelu etukateen) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてから、V2 (jälkeen) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてきます (kaynti ja paluu) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてしまいます (valitettavasti, loppuun asti) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてはじめて (vasta silloin kun) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてみます (kokeilla tehda) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vても (vaikka) — mihin verbimuotoon liittyy?
?
て形 (て-muoto), た形 (た-muoto)

Vても いいです・Vては いけません (lupa ja kielto) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vてやります (alaspain tehty teko) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

Vて・Vないで (tapa, keino) — mihin verbimuotoon liittyy?
?
て形 (て-muoto), ない形 (ない-muoto)

Vて以来 (siita lahtien kun) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

ご～いただく (kohtelias pyyntö, kiitollisuus) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

たとえ～ても (vaikka kuinka) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

てくださいます (kunnioittava anto) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

てほしい・ないでほしい (toive toiselle) — mihin verbimuotoon liittyy?
?
て形 (て-muoto), ない形 (ない-muoto)

てもらえませんか・ていただけないでしょうか (kohtelias pyyntoperhe) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

まだ～ていません (ei ole vielä tehty) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

よほど～でも (aika lailla, huomattava) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

自動詞＋ている (jaljelle jaanyt tila) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～ちゃう・～とく・～てる (puhekieliset supistumat) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～ている (elämänhistoria, saavutukset) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～ている (parhaillaan, tilan tulos) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～てくる・～ていく (liikkeen suunta) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～てくる・～ていく (muutos ajassa) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～てばかりいる・～ばかり～ている (liiallinen keskittyminen) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

～てもかまいません (saa tehdä, ei haittaa) — mihin verbimuotoon liittyy?
?
て形 (て-muoto)

て形: mitä kielioppeja siihen liittyy?
?
36 kielioppia, esim. Nこそ (juuri se, nimenomaan), Vさえ～ば (kunhan vain), Vて (tunnereaktion syy), Vて ください (pyyntö), Vて、Vて (peräkkäisyys), Vてあげます・Vてもらいます・Vてくれます (teon antaminen), Vてあります (tarkoituksella tehty tila), Vておきます (valmistelu etukateen)
