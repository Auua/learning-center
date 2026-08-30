---
type: guide
created: 2026-08-29
tags: [meta]
---
# Vaultin käyttöohje

## Perusidea
Muistiinpano = **yksi asia**. Linkit tekevät rakenteen, Dataview kokoaa näkymät. Et kirjoita listoja käsin — merkitset kenttiä, ja listat syntyvät itsestään.

Kolme linkitystapaa, jotka kantavat koko vaultia:

| Kysymys | Miten se ratkeaa |
|---|---|
| "Mitkä kieliopit käyttävät て-muotoa?" | Kielioppimuistiinpanon kenttä `attaches: ["[[て-muoto]]"]` → [[て-muoto]]-sivun taulukko täyttyy itsestään |
| "Mitä eroa on たら:lla ja ば:lla?" | Molemmissa kenttä `compare:` osoittaa samaan [[Vertailu — Ehtolauseet と・ば・たら・なら]] -muistiinpanoon |
| "Missä kanji 食 esiintyy?" | Sana- ja verbimuistiinpanon kenttä `kanji: ["[[食]]"]` → [[食]]-sivu listaa sanat |

## Kansiot
| Kansio | Sisältö |
|---|---|
| `00 Meta` | Pohjat, skriptit, tämä ohje |
| `10 Kielioppi/Pisteet` | Yksi kielioppirakenne per muistiinpano |
| `10 Kielioppi/Vertailut` | "Samaa tarkoittavat" -muistiinpanot |
| `20 Verbit/Muodot` | Taivutusmuodot ja niiden säännöt |
| `20 Verbit/Lekseemit` | Yksittäiset verbit taivutustaulukoineen |
| `30 Sanasto/Sanat` · `Setit` | Sanat ja aihekokonaisuudet |
| `40 Kanji/Merkit` · `Osat` | Merkit ja radikaalit |
| `50 Lauseet` | Esimerkkilausepankit lohkotunnuksilla |
| `60 Lahteet` | Oppikirjat ja sivustot |
| `70 Visuaalinen` | Kuvavihjeet, Excalidraw-piirrokset, liitteet |
| `80 JLPT` | Tasokohtaiset näkymät ja [[Kertaus]] |
| `90 Paivakirja` | Opiskeluloki ja virhepäiväkirja |

## Kenttäsanasto
Kenttänimissä **ei väliviivoja eikä isoja kirjaimia** — Dataview tulkitsee väliviivan miinusmerkiksi.

| Kenttä | Arvot |
|---|---|
| `type` | grammar · compare · verb · form · vocab · kanji · component · source · sentences · set · log · mistake |
| `jlpt` | N5 · N4 · N3 · N2 · N1 |
| `status` | new · learning · shaky · known |
| `confidence` | 1–5 |
| `reviewed` | YYYY-MM-DD — päivitä kun kertaat |
| `attaches` | mihin verbimuotoon kielioppi liittyy |
| `compare` | linkki vertailumuistiinpanoon |
| `sources` | linkit `60 Lahteet`-muistiinpanoihin |

`status` ja `confidence` ovat ainoat kentät, joita sinun pitää muistaa päivittää. [[Kertaus]] näyttää heikoimmat ensin.

## Esimerkkilauseet
Lauseet asuvat **yhdessä paikassa** ja upotetaan muualle:
1. Kirjoita lause tiedostoon `50 Lauseet/…` ja anna sille lohkotunnus: `^tara1`
2. Upota se kielioppimuistiinpanoon: `![[Lausepankki — Ehtolauseet#^tara1]]`

Näin lauseen korjaus päivittyy joka paikkaan. Ks. [[Lausepankki — Ehtolauseet]].

## Kortit ja SRS
Kortit kirjoitetaan muistiinpanon `## Kortit` -osioon Obsidian Spaced Repetition -syntaksilla:

```
#flashcards/grammar/n4

Etupuoli::takapuoli
Kaksisuuntainen:::kortti

Pidempi kysymys?
?
Pidempi vastaus.
```

- **Obsidianissa:** SR-plugin kerää ne suoraan.
- **Ankiin:** `python3 "00 Meta/Scripts/sr_to_anki.py"` tuottaa tiedoston `00 Meta/Scripts/anki_export.tsv`.

Anki-tuonti kerran:
1. Tools → Manage Note Types → Add → Basic → nimeä **Japani (Obsidian)**, kentät: `UID`, `Front`, `Back`, `Source`
2. Kortin etupuoli `{{Front}}`, takapuoli `{{Back}}`
3. File → Import → valitse TSV → *Existing notes: Update* → ensimmäinen kenttä on UID

UID on vakaa tiiviste, joten sama kortti päivittyy eikä monistu. Jos muutat kortin etupuolta, syntyy uusi kortti — muuta mieluummin takapuolta.

## Ylläpito
```
python3 "00 Meta/Scripts/check_vault.py"
```
Listaa puuttuvat pakolliset kentät, ratkeamattomat linkit ja orvot muistiinpanot. Ratkeamaton linkki ei ole virhe — se on työjono: klikkaa sitä Obsidianissa ja muistiinpano syntyy.

## Uusi muistiinpano
`Ctrl/Cmd+P` → *Templater: Create new note from template* → valitse pohja kansiosta `00 Meta/Templates`.

Ilman Templateria: *Templates: Insert template* toimii samalla pohjakansiolla, mutta päivämääriä ei täytetä automaattisesti.

## Bases vai Dataview

Näkymät on rakennettu **Obsidian Bases** -ydintoiminnolla. Dataview on jäljellä vain siellä missä Bases ei taivu.

| | Bases | Dataview |
|---|---|---|
| Selaus- ja muokkaustaulukot | ✅ soluja voi muokata suoraan | ❌ vain luku |
| Itseviittaavat listat (`attaches.contains(this)`) | ✅ | ✅ |
| Ryhmittely | ✅ yhdellä kentällä | ✅ millä tahansa |
| Ristiintaulukointi (jlpt × status) | ❌ | ✅ |
| Päivämäärälaskenta ("ei kerrattu 30 pv") | ❌ | ✅ |
| Puuttuvan tiedon etsintä (`WHERE !sources`) | ❌ | ✅ |

Jäljellä olevat dataview-kyselyt ovat MOCien **Laatutarkistukset**-osioissa, [[Kertaus]]-sivun kohdassa 2, [[_MOC JLPT]]:n ristiintaulukossa ja [[_MOC Päiväkirja]]:n viikkosummassa. Jos poistat Dataviewin, menetät nuo ja muu toimii.

### Base-tiedostot
Kansiossa `00 Meta/Bases`. Yksi tiedosto sisältää useita näkymiä välilehtinä.

| Tiedosto | Näkymät |
|---|---|
| `Kielioppi.base` | Kaikki kieliopit · Heikoilla jäillä · Tasoittain · Vertailut |
| `Verbit.base` | Taivutusmuodot · Verbit · Tyypeittäin · Transitiiviparit · Epäsäännölliset |
| `Sanasto.base` | Kaikki sanat · Seteittäin · Setit |
| `Kanji.base` | Merkit · Vetomäärän mukaan · Osat ja radikaalit · Sekaannusriski |
| `JLPT.base` | Kaikki tasot · N5 · N4 · N3 · N2 · N1 |
| `Kertaus.base` | Heikoimmat ensin · Uudet · Työn alla · Toistuvat virheet |
| `Lähteet.base` | Kaikki lähteet · Tyypeittäin |
| `Päiväkirja.base` | Opiskeluloki · Virheet · Virheet syyn mukaan |

Upotus muistiinpanoon: `![[Kielioppi.base]]` tai yksi näkymä: `![[JLPT.base#N3]]`.

Muistiinpanokohtaiset listat (esim. "kieliopit jotka käyttävät tätä muotoa") ovat ```` ```base ````-lohkoja suoraan muistiinpanossa. Niissä `this` viittaa muistiinpanoon, jossa lohko on.

Näkymän lajittelun ja sarakkeet voi säätää Obsidianin käyttöliittymästä — muutokset tallentuvat takaisin `.base`-tiedostoon.

## Tarvittavat pluginit

| | Mihin | Pakollinen |
|---|---|---|
| Bases (ydintoiminto) | Kaikki taulukkonäkymät | Kyllä — vaatii Obsidian 1.9+, ryhmittely 1.10+ |
| Dataview | Laatutarkistukset, päivämäärälaskenta, ristiintaulukointi | Ei, mutta suositeltava |
| Templater | Pohjien päivämäärät ja otsikot | Ei |
| Spaced Repetition | Kertaus Obsidianissa | Ei |
| Excalidraw | Kuvavihjeet | Ei |

Dataviewin **Enable JavaScript Queries** -asetusta ei tarvita — jäljellä olevat kyselyt ovat perus-DQL:ää.

Ks. myös [[Kuvavihjeet — periaatteet]].
