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

## Merkitys
- **FI:** ehtomuoto: yleinen ja looginen ehto, "jos A, niin B"
- **EN:** conditional ba-form

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

<!-- verbityyppikortit:alku -->
## Kortit
#flashcards/form/n4/taivutus

ば形: 買う（かう, 五段 う） ::: 買えば（かえば）
ば形: 言う（いう, 五段 う） ::: 言えば（いえば）
ば形: 待つ（まつ, 五段 つ） ::: 待てば（まてば）
ば形: 持つ（もつ, 五段 つ） ::: 持てば（もてば）
ば形: 取る（とる, 五段 る） ::: 取れば（とれば）
ば形: 帰る（かえる, 五段 る） ::: 帰れば（かえれば）
ば形: 飲む（のむ, 五段 む） ::: 飲めば（のめば）
ば形: 読む（よむ, 五段 む） ::: 読めば（よめば）
ば形: 遊ぶ（あそぶ, 五段 ぶ） ::: 遊べば（あそべば）
ば形: 呼ぶ（よぶ, 五段 ぶ） ::: 呼べば（よべば）
ば形: 死ぬ（しぬ, 五段 ぬ） ::: 死ねば（しねば）
ば形: 書く（かく, 五段 く） ::: 書けば（かけば）
ば形: 歩く（あるく, 五段 く） ::: 歩けば（あるけば）
ば形: 泳ぐ（およぐ, 五段 ぐ） ::: 泳げば（およげば）
ば形: 急ぐ（いそぐ, 五段 ぐ） ::: 急げば（いそげば）
ば形: 話す（はなす, 五段 す） ::: 話せば（はなせば）
ば形: 貸す（かす, 五段 す） ::: 貸せば（かせば）
ば形: 行く（いく, 五段 く, poikkeus） ::: 行けば（いけば）
ば形: 見る（みる, 一段 (iる)） ::: 見れば（みれば）
ば形: 起きる（おきる, 一段 (iる)） ::: 起きれば（おきれば）
ば形: 食べる（たべる, 一段 (eる)） ::: 食べれば（たべれば）
ば形: 寝る（ねる, 一段 (eる)） ::: 寝れば（ねれば）
ば形: する（不規則） ::: すれば
ば形: 勉強する（べんきょうする, 不規則） ::: 勉強すれば（べんきょうすれば）
ば形: 来る（くる, 不規則） ::: 来れば（くれば）
<!-- verbityyppikortit:loppu -->

#flashcards/form/n4

ば形: mitä se ilmaisee?
?
Yleinen ja looginen ehto "jos A, niin B". Painottaa ehtoa, ei aikajärjestystä.

#flashcards/form/n4/saanto

ば形 + 五段 :: う-rivi → え-rivi + ば (書く → 書けば)
ば形 + 一段 :: る → れば (食べる → 食べれば)
ば形 + 不規則 :: する → すれば、来る → 来れば（くれば）
ば形 + い-adjektiivi :: い → ければ (安い → 安ければ)
ば形 + な-adjektiivi / substantiivi :: + なら(ば) (静か → 静かなら)
ば形 + kielto :: ない → なければ (行かない → 行かなければ)

#flashcards/form/n4/huomio

ば形: mikä rajoitus jälkilauseessa?
?
Jos etulause on toimintaverbi, jälkilauseessa ei yleensä voi olla käskyä, pyyntöä tai kutsua — silloin käytä ～たら. ○ 時間があれば、いいですね。 × 京都に行けば、写真を撮ってください。 → ○ 京都に行ったら、…

#flashcards/form/n4/liittyy

Vさえ～ば (kunhan vain) — mihin verbimuotoon liittyy?
?
ば形 (Ehtomuoto ば), て形 (て-muoto)

Vば〜ほど (mita enemman, sita) — mihin verbimuotoon liittyy?
?
ば形 (Ehtomuoto ば)

Vば～だけ (mita enemman, sita enemman) — mihin verbimuotoon liittyy?
?
ば形 (Ehtomuoto ば), た形 (た-muoto)

～ば (jos, ehto) — mihin verbimuotoon liittyy?
?
ば形 (Ehtomuoto ば)

ば形: mitä kielioppeja siihen liittyy?
?
5 kielioppia, esim. Vさえ～ば (kunhan vain), Vなければ なりません (velvollisuus), Vば〜ほど (mita enemman, sita), Vば～だけ (mita enemman, sita enemman), ～ば (jos, ehto)
