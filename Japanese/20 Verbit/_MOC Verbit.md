---
type: moc
created: 2026-08-29
tags: [moc]
---
# Verbit

[[_MOC Kielioppi]] · [[_MOC Sanasto]] · [[_MOC Kanji]] · [[_MOC JLPT]] · [[Kertaus]]

## Taivutusmuodot
![[Verbit.base#Taivutusmuodot]]

## Verbit
![[Verbit.base#Verbit]]

## Transitiiviparit
![[Verbit.base#Transitiiviparit]]

## Laatutarkistukset
### Verbit joilta puuttuu taivutustaulukko
```dataview
LIST
FROM "20 Verbit/Lekseemit"
WHERE !contains(file.outlinks, link("て-muoto"))
```

### Verbit ilman kanjilinkkiä
```dataview
LIST
FROM "20 Verbit/Lekseemit"
WHERE !kanji OR length(kanji) = 0
```
