---
type: form
ja: 使役形
name: Kausatiivi (さ)せる
base: 未然形 + せる/させる
func: [teettäminen, salliminen]
jlpt: N4
sources: ["[[Minna no Nihongo II#Luku 48]]", "[[Minna no Nihongo Chuukyuu I#Luku 3]]", "[[Minna no Nihongo Chuukyuu I#Luku 7]]"]
status: shaky
confidence: 2
tags: [form]
---

> [!abstract] Mihin tätä tarvitaan
> "Panna tekemään" tai "antaa tehdä". Kumpi merkitys, ratkeaa partikkelista ja kontekstista.

## Muodostussäännöt
| Verbityyppi | Sääntö | Esimerkki |
|---|---|---|
| 五段 | う-rivi → あ-rivi + せる（う → わ） | 書く → 書かせる、買う → 買わせる |
| 一段 | る → させる | 食べる → 食べさせる |
| 不規則 | する → させる、来る → 来させる（こさせる） | |

## Partikkelit
| Verbi | Rakenne | Sävy |
|---|---|---|
| Intransitiivinen | X **を** V-せる | pakotus |
| Intransitiivinen | X **に** V-せる | salliminen |
| Transitiivinen | X **に** Y **を** V-せる | kumpi tahansa |

- 母は弟**を**買い物に行かせた。 Äiti käski veljen mennä.
- 母は弟**に**買い物に行かせた。 Äiti antoi veljen mennä.

## Lisäesimerkkejä (Luku 48)
- 息子をイギリスへ留学させます。（pakotus/salliminen, vanhempi päättää）
- 娘にピアノを習わせます。
- ハンス君は外で遊ぶのが好きですね。……ええ。体にいいし、友達もできるし、できるだけ外で遊ばせています。（salliminen, myönteinen）
- ワット先生の授業はどうですか。……厳しいですよ。学生に絶対に日本語を使わせませんから。でも、言いたいことは自由に言わせます。（kielto + lupa vierekkäin, sama kausatiivimuoto kahdessa eri sävyssä）

## Kohtelias pyyntö
～させてください = "anna minun tehdä". 説明させてください。
Laajempi kokonaisuus kohteliaista lupapyynnöistä: ks. [[させてください・させていただけませんか (lupa itselle)]].

## Tunteen aiheuttaminen (Chuukyuu I Luku 7)
Erittäin yleinen kausatiivikäyttö: joku/jokin saa toisen **tuntemaan** jotain (泣かせる, 安心させる, 喜ばせる, 怖がらせる, 心配させる) — tekijä on tunteen aiheuttaja, ei kokija:
- 子どものとき、よく兄弟げんかをして弟を**泣かせました**。
- 早く就職して、両親を**安心させたい**と思っています。
- おいしいケーキを作って、子どもたちを**喜ばせた**。
- お化けの話をして、妹を**怖がらせてしまいました**。（ks. [[～たがる・～たがっている (toisen havaittu halu)]]:n がる-vartalo + kausatiivi: 怖がる→怖がらせる）

## Esimerkit
![[Lausepankki — Kausatiivi ja luvat#^kaus3]]
![[Lausepankki — Kausatiivi ja luvat#^kaus4]]

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
