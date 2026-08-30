---
type: moc
created: 2026-08-29
tags: [moc]
---
# Sanasto

[[_MOC Kielioppi]] · [[_MOC Verbit]] · [[_MOC Kanji]] · [[_MOC JLPT]] · [[Kertaus]]

## Setit
![[Sanasto.base#Setit]]

## Kaikki sanat
![[Sanasto.base#Kaikki sanat]]

## Laatutarkistukset
### Ilman settiä
```dataview
LIST
FROM "30 Sanasto/Sanat"
WHERE !sets OR length(sets) = 0
```

### Ilman kanjilinkkiä (ei koske kana-sanoja)
```dataview
LIST
FROM "30 Sanasto/Sanat"
WHERE (!kanji OR length(kanji) = 0) AND pos != "i-adjective"
```
