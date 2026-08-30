---
type: moc
created: 2026-08-29
tags: [moc]
---
# Kielioppi

[[_MOC Verbit]] · [[_MOC Sanasto]] · [[_MOC Kanji]] · [[_MOC Lähteet]] · [[_MOC JLPT]] · [[Kertaus]]

## Selaa ja muokkaa
Taulukon soluja voi muokata suoraan — `status` ja `confidence` päivittyvät muistiinpanoon.

![[Kielioppi.base]]

## Laatutarkistukset
Nämä kyselyt etsivät *puuttuvaa* tietoa, mihin Bases ei taivu.

### Ilman lähdeviitettä
```dataview
LIST
FROM "10 Kielioppi/Pisteet"
WHERE !sources OR length(sources) = 0
```

### Ilman vertailumuistiinpanoa
```dataview
LIST
FROM "10 Kielioppi/Pisteet"
WHERE !compare
```

### Ilman esimerkkilausetta
```dataview
LIST
FROM "10 Kielioppi/Pisteet"
WHERE length(filter(file.outlinks, (l) => contains(meta(l).path, "50 Lauseet"))) = 0
```
