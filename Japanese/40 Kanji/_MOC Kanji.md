---
type: moc
created: 2026-08-29
tags: [moc]
---
# Kanji

[[_MOC Kielioppi]] · [[_MOC Verbit]] · [[_MOC Sanasto]] · [[_MOC JLPT]] · [[Kertaus]]

## Merkit
![[Kanji.base#Merkit]]

## Osat ja radikaalit
![[Kanji.base#Osat ja radikaalit]]

## Sekaannusriski
![[Kanji.base#Sekaannusriski]]

## Laatutarkistukset
### Ilman osia
```dataview
LIST
FROM "40 Kanji/Merkit"
WHERE !components OR length(components) = 0
```

### Ilman sanaesiintymää
```dataview
LIST
FROM "40 Kanji/Merkit"
WHERE length(file.inlinks) = 0
```
