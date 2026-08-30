---
type: compare
topic: Ehtolauseet
members: ["[[～と (aina kun, väistämätön seuraus)]]", "[[～ば (jos, ehto)]]", "[[～たら (jos, kun)]]", "[[～なら (jos kerran)]]"]
axis: [tahdonilmaus-jalkilauseessa, aikajarjestys, kontekstisidonnaisuus, automaattisuus]
jlpt: N4
sources: ["[[Minna no Nihongo I#Luku 23]]", "[[Minna no Nihongo I#Luku 25]]", "[[Minna no Nihongo II#Luku 35]]", "[[Minna no Nihongo Chuukyuu I#Luku 9]]"]
status: learning
confidence: 3
created: 2026-08-29
tags: [compare, grammar/ehto, jlpt/n4]
---

> [!question] Milloin kumpi?
> Kysy ensin: **saako jälkilauseessa olla tahtoa?** と ei salli. ば sallii vain, jos etulause on tila. たら sallii aina. なら sallii ja lisäksi kääntää aikajärjestyksen.

## Päätöspuu
1. Onko seuraus **väistämätön** (kone, luonnonlaki, reittiohje)? → [[～と (aina kun, väistämätön seuraus)]]
2. Onko jälkilauseessa **käsky, pyyntö, kutsu tai toive**?
   → jos etulause on toiminta: [[～たら (jos, kun)]]
   → jos etulause on tila tai adjektiivi: [[～ば (jos, ehto)]] käy myös
3. Reagoitko siihen mitä **toinen juuri sanoi** tai mikä on tilanteesta selvää? → [[～なら (jos kerran)]]
4. Tapahtuuko jälkilauseen teko **ennen** etulauseen tekoa? → vain [[～なら (jos kerran)]]
5. Muuten: yleinen hypoteesi ja "mitä vaaditaan" → [[～ば (jos, ehto)]]; konkreettinen kertatapaus → [[～たら (jos, kun)]]

## Vertailutaulukko
| Rakenne | Ydinero | Tahdonilmaus jälkilauseessa | Mennyt jälkilause | Aikajärjestys | Tyyliväri |
|---|---|---|---|---|---|
| [[～と (aina kun, väistämätön seuraus)]] | automaattinen seuraus | ❌ ei koskaan | ✅ = löytö | A → B | neutraali, ohjeet |
| [[～ば (jos, ehto)]] | looginen ehto, "riittääkö tämä" | ⚠️ vain jos etulause on tila | harvoin | A → B | kirjallinen, sananlaskut |
| [[～たら (jos, kun)]] | konkreettinen kertatapaus | ✅ vapaasti | ✅ = löytö | A → B | puhekielinen, yleisin |
| [[～なら (jos kerran)]] | konteksti, "jos kerran" | ✅ vapaasti | ❌ | **B voi olla ennen A:ta** | keskusteleva |

## Minimiparit
| A | B | Ero |
|---|---|---|
| 日本に行く**なら**、ガイドブックを買う | 日本に行っ**たら**、ガイドブックを買う | Kirja ostetaan ennen matkaa / perillä |
| 春になる**と**、桜が咲く | 春になっ**たら**、花見をしよう | Luonnonlaki / oma suunnitelma |
| 時間が**あれば**、行きます | 時間が**あったら**、行きます | Molemmat käyvät; ば on muodollisempi |
| 押す**と**、開きます | 押し**たら**、開きました | Yleinen ohje / yksittäinen tapahtuma |

## Testilauseet itselle
1. ＿＿＿、電話してください。(着く) → 着いたら
2. このボタンを＿＿＿、水が出ます。(押す) → 押すと
3. 温泉＿＿＿、伊豆がいいですよ。→ なら
4. 練習＿＿＿するほど上手になる。(する) → すれば

## Jäsenet
```base
filters:
  and:
    - 'type == "grammar"'
    - 'compare == this'
views:
  - type: table
    name: Jäsenet
    order:
      - file.name
      - note.jlpt
      - note.func
      - note.status
      - note.confidence
    sort:
      - property: note.confidence
        direction: ASC
```

## Esimerkkipankki
![[Lausepankki — Ehtolauseet]]

## Kortit
#flashcards/compare

Ehtolauseet: kumpi sallii käskyn jälkilauseessa, と vai たら?
?
たら. と ei koskaan salli tahdonilmausta. ば vain jos etulause on tilaverbi tai adjektiivi.

Missä ehtolauseessa jälkilauseen teko voi tapahtua ennen etulauseen tekoa?
?
なら. 日本に行くなら、ガイドブックを買ったほうがいい — kirja ostetaan ennen matkaa.
