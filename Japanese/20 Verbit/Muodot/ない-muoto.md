---
type: form
ja: ない形
name: ない-muoto
base: 未然形（あ段）
func: [kielto, kielteinen-ehto, kielteinen-pyyntö]
jlpt: N5
sources: ["[[Minna no Nihongo I#Luku 17]]", "[[Minna no Nihongo Chuukyuu I#Luku 7]]"]
status: learning
confidence: 4
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> Kielto ei-kohteliaasti sekä pohja rakenteille ～なければならない、～ないでください、～なくてもいい、～ないほうがいい.

## Merkitys
- **FI:** kielto ei-kohteliaasti; pohja kielteisille rakenteille
- **EN:** plain negative (nai-form)

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → あ-rivi + ない | 書く → 書かない、飲む → 飲まない |
| 五段, päättyy う | う → **わ** + ない | 買う → 買わない (ei ×買あない) |
| 一段 | る pois + ない | 食べる → 食べない |
| 不規則 | する → しない、来る → 来ない（こない） | |

## Poikkeukset
- **ある → ない** (ei ×あらない).

## Johdannaiset
- ない → なくて (syy) / ないで (tapa)
- ない → なかった (mennyt kielto)

## Kieliopit jotka liittyvät tähän muotoon
```base
filters:
  and:
    - type == "grammar"
    - attaches.contains(this)
views:
  - type: table
    name: Kieliopit
    order:
      - file.name
      - jlpt
      - func
      - status
      - confidence
    sort:
      - property: jlpt
        direction: ASC
    columnSize:
      file.name: 488
      note.func: 408
      note.confidence: 51

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

ない形: 買う（かう, 五段 う） ::: 買わない（かわない）
ない形: 言う（いう, 五段 う） ::: 言わない（いわない）
ない形: 待つ（まつ, 五段 つ） ::: 待たない（またない）
ない形: 持つ（もつ, 五段 つ） ::: 持たない（もたない）
ない形: 取る（とる, 五段 る） ::: 取らない（とらない）
ない形: 帰る（かえる, 五段 る） ::: 帰らない（かえらない）
ない形: 飲む（のむ, 五段 む） ::: 飲まない（のまない）
ない形: 読む（よむ, 五段 む） ::: 読まない（よまない）
ない形: 遊ぶ（あそぶ, 五段 ぶ） ::: 遊ばない（あそばない）
ない形: 呼ぶ（よぶ, 五段 ぶ） ::: 呼ばない（よばない）
ない形: 死ぬ（しぬ, 五段 ぬ） ::: 死なない（しなない）
ない形: 書く（かく, 五段 く） ::: 書かない（かかない）
ない形: 歩く（あるく, 五段 く） ::: 歩かない（あるかない）
ない形: 泳ぐ（およぐ, 五段 ぐ） ::: 泳がない（およがない）
ない形: 急ぐ（いそぐ, 五段 ぐ） ::: 急がない（いそがない）
ない形: 話す（はなす, 五段 す） ::: 話さない（はなさない）
ない形: 貸す（かす, 五段 す） ::: 貸さない（かさない）
ない形: 行く（いく, 五段 く, poikkeus） ::: 行かない（いかない）
ない形: 見る（みる, 一段 (iる)） ::: 見ない（みない）
ない形: 起きる（おきる, 一段 (iる)） ::: 起きない（おきない）
ない形: 食べる（たべる, 一段 (eる)） ::: 食べない（たべない）
ない形: 寝る（ねる, 一段 (eる)） ::: 寝ない（ねない）
ない形: する（不規則） ::: しない
ない形: 勉強する（べんきょうする, 不規則） ::: 勉強しない（べんきょうしない）
ない形: 来る（くる, 不規則） ::: 来ない（こない）
<!-- verbityyppikortit:loppu -->

#flashcards/form/n5

ない形: mihin sitä tarvitaan?
?
Kielto ei-kohteliaasti sekä pohja rakenteille ～なければならない、～ないでください、～なくてもいい、～ないほうがいい.

#flashcards/form/n5/saanto

ない形 + 五段 :: う-rivi → あ-rivi + ない (書く → 書かない、飲む → 飲まない)
ない形 + 五段 う-loppuinen :: う → わ + ない (買う → 買わない, ei ×買あない)
ない形 + 一段 :: る pois + ない (食べる → 食べない)
ない形 + 不規則 :: する → しない、来る → 来ない（こない）

#flashcards/form/n5/poikkeus

ある: ない形?
?
ない (ei ×あらない)

#flashcards/form/n5/huomio

ない → syy ja tapa?
?
なくて (syy) / ないで (tapa)

ない → mennyt kielto?
?
なかった

#flashcards/form/n5/liittyy

Vざるを得ない (on pakko) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

Vざる～ (kirjallinen kielteinen liite) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

Vないかぎり (ellei, niin kauan kuin ei) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

Vないで ください (kielteinen pyyntö) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

Vなくても いいです (ei tarvitse) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto), て形 (て-muoto)

Vなければ なりません (velvollisuus) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto), ば形 (Ehtomuoto ば)

決して～ない (ei missaan nimessa) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

～ず［に］・～ず (kirjallinen kielto) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

～なくちゃ・～なきゃ (puhekielinen pakko) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto)

～なくてはならない・～なくてはいけない (pakko, toinen muoto) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto), て形 (て-muoto)

～なくてもかまいません (ei tarvitse, ei haittaa) — mihin verbimuotoon liittyy?
?
ない形 (ない-muoto), て形 (て-muoto)

ない形: mitä kielioppeja siihen liittyy?
?
24 kielioppia, esim. Vこと (nominalisointi, abstrakti tekeminen), Vざるを得ない (on pakko), Vざる～ (kirjallinen kielteinen liite), Vて・Vないで (tapa, keino), Vないかぎり (ellei, niin kauan kuin ei), Vないで ください (kielteinen pyyntö), Vなくても いいです (ei tarvitse), Vなければ なりません (velvollisuus)
