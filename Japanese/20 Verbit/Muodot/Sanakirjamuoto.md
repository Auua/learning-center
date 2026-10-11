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

## Merkitys
- **FI:** perusmuoto, verbin hakumuoto; ei-kohtelias preesens
- **EN:** dictionary form

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

<!-- verbityyppikortit:alku -->
## Kortit
#flashcards/form/n5/taivutus

辞書形: 買います（かいます） ::: 買う（かう） — 五段 う
辞書形: 言います（いいます） ::: 言う（いう） — 五段 う
辞書形: 待ちます（まちます） ::: 待つ（まつ） — 五段 つ
辞書形: 持ちます（もちます） ::: 持つ（もつ） — 五段 つ
辞書形: 取ります（とります） ::: 取る（とる） — 五段 る
辞書形: 帰ります（かえります） ::: 帰る（かえる） — 五段 る
辞書形: 飲みます（のみます） ::: 飲む（のむ） — 五段 む
辞書形: 読みます（よみます） ::: 読む（よむ） — 五段 む
辞書形: 遊びます（あそびます） ::: 遊ぶ（あそぶ） — 五段 ぶ
辞書形: 呼びます（よびます） ::: 呼ぶ（よぶ） — 五段 ぶ
辞書形: 死にます（しにます） ::: 死ぬ（しぬ） — 五段 ぬ
辞書形: 書きます（かきます） ::: 書く（かく） — 五段 く
辞書形: 歩きます（あるきます） ::: 歩く（あるく） — 五段 く
辞書形: 泳ぎます（およぎます） ::: 泳ぐ（およぐ） — 五段 ぐ
辞書形: 急ぎます（いそぎます） ::: 急ぐ（いそぐ） — 五段 ぐ
辞書形: 話します（はなします） ::: 話す（はなす） — 五段 す
辞書形: 貸します（かします） ::: 貸す（かす） — 五段 す
辞書形: 行きます（いきます） ::: 行く（いく） — 五段 く, poikkeus
辞書形: 見ます（みます） ::: 見る（みる） — 一段 (iる)
辞書形: 起きます（おきます） ::: 起きる（おきる） — 一段 (iる)
辞書形: 食べます（たべます） ::: 食べる（たべる） — 一段 (eる)
辞書形: 寝ます（ねます） ::: 寝る（ねる） — 一段 (eる)
辞書形: します ::: する — 不規則
辞書形: 勉強します（べんきょうします） ::: 勉強する（べんきょうする） — 不規則
辞書形: 来ます（きます） ::: 来る（くる） — 不規則
<!-- verbityyppikortit:loppu -->

#flashcards/form/n5

辞書形: mitä se tarkoittaa?
?
Verbin hakumuoto ja kaikkien muiden muotojen lähtökohta. Toimii myös lauseen sisällä ei-kohteliaana preesensinä.

#flashcards/form/n5/saanto

辞書形 + 五段 :: päättyy う-riviin: う・く・ぐ・す・つ・ぬ・ぶ・む・る (書く、飲む、話す)
辞書形 + 一段 :: päättyy いる/える + る (食べる、見る)
辞書形 + 不規則 :: する、来る（くる）

#flashcards/form/n5/huomio

Verbi ei pääty る: mikä tyyppi?
?
Aina godan

Verbi päättyy る ja edellä い/え-äänne: mikä tyyppi?
?
Yleensä ichidan; godan-poikkeuksia: 帰る、入る、走る、切る、知る、要る

#flashcards/form/n5/liittyy

Puhekielen kysymykset ja partikkelien pudottaminen — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vからには (koska kerran, paatoksen jalkeen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

Vこと (nominalisointi, abstrakti tekeminen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto), ない形 (ない-muoto)

Vことがある・こともある (satunnainen poikkeus) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vことができます (kyky) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vしかない (ei ole muuta vaihtoehtoa) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vたびに (aina kun) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vためには (jotta voisi) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vために・Nのために (tarkoitusta varten) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vつもりはない・つもりだった・たつもり (kiistetty ja toteutumaton aikomus) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

Vところです (kolme vaihetta) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

Vにつれて (sita mukaa kun) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vのに (kayttotarkoitus, kulutus) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vのは・Vのが・Vのを (nominalisointi) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

Vべきだ (pitaisi tehda, velvollisuus) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vまえに (ennen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vようにいう・注意する・伝える・頼む (epasuora kehotus) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto)

Vようにしています (tavakseen pyrkiminen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto)

Vるところだった (oli juuri vahalla tapahtua) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vるまでもない (ei tarvitse edes) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vる上で (ottaen huomioon, sen suhteen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vる恐れがある (on vaarana etta) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

Vわけにはいかない (sosiaalinen este, ei voi) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto)

V・adjとき (silloin kun) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto), ない形 (ない-muoto)

V辞書形+時間・約束・用事 (aika, sopimus, asia tehtäväksi) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

V辞書形まで・までに (verbilause aikarajana) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

〜とおりに (juuri niin kuin) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

ことにする・ことにしている (oma paatos) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto)

ことになる・ことになっている (ulkopuolinen paatos) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto)

普通形 (puhekielinen perusmuoto) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto), た形 (た-muoto)

普通形と思います (mielipide) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～ことは・が・を (yleistys ja arvottaminen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～たがる・～たがっている (toisen havaittu halu) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～だけだ・ただ～だけでいい (vain se riittää) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～と (aina kun, väistämätön seuraus) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), ない形 (ない-muoto)

～とともに (yhdessa, samalla) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～なら (jos kerran) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

～ほどのものじゃない (ei niin suuri asia) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～より～ほうが (tekojen vertailu) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto)

～際［に］ (silloin kun, muodollinen) — mihin verbimuotoon liittyy?
?
辞書形 (Sanakirjamuoto), た形 (た-muoto)

辞書形: mitä kielioppeja siihen liittyy?
?
40 kielioppia, esim. Puhekielen kysymykset ja partikkelien pudottaminen, Vからには (koska kerran, paatoksen jalkeen), Vこと (nominalisointi, abstrakti tekeminen), Vことがある・こともある (satunnainen poikkeus), Vことができます (kyky), Vしかない (ei ole muuta vaihtoehtoa), Vたびに (aina kun), Vためには (jotta voisi)
