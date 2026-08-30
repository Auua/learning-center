---
type: home
created: 2026-08-29
tags: [moc]
---
# 日本語 — oppimisympäristö

> [!info] Taso nyt
> N3-työskentely käynnissä. N4:n aukot ([[Passiivi (ら)れる]], [[Kausatiivi (さ)せる]], [[Kausatiivipassiivi (さ)せられる]], ehtolauseet) kannattaa tukkia ensin.

## Aloita tästä
[[Kertaus]] — mitä pitää tehdä tänään
[[Vaultin käyttöohje]] — miten muistiinpanot linkittyvät

## Kartat
| | |
|---|---|
| [[_MOC Kielioppi]] | Kielioppipisteet ja vertailut |
| [[_MOC Verbit]] | Taivutusmuodot ja verbit |
| [[_MOC Sanasto]] | Sanat ja aihesetit |
| [[_MOC Kanji]] | Merkit ja radikaalit |
| [[_MOC JLPT]] | Tasokohtaiset näkymät |
| [[_MOC Lähteet]] | Oppikirjat ja sivustot |
| [[_MOC Päiväkirja]] | Opiskeluloki ja virheet |
| [[Keigo — kartta]] | N3 → N2 -kynnys |
| [[Kuvavihjeet — periaatteet]] | Miten muistisäännöt tehdään |

## Heikoimmat juuri nyt
![[Kertaus.base#Heikoimmat ensin]]

## Viimeksi muokatut
```base
filters:
  and:
    - 'type'
    - 'type != "moc"'
    - 'type != "home"'
views:
  - type: table
    name: Viimeksi muokatut
    order:
      - file.name
      - note.type
      - note.jlpt
      - note.status
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
    limit: 10
```

## Vaultin tila
```base
filters:
  and:
    - 'type'
views:
  - type: table
    name: Tyypeittäin
    groupBy:
      property: note.type
      direction: ASC
    order:
      - file.name
      - note.jlpt
      - note.status
```
