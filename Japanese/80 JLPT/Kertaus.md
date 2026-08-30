---
type: dashboard
created: 2026-08-29
tags: [dashboard]
---
# Kertaus

Mitä pitää ottaa työn alle. Päivitä `status`, `confidence` ja `reviewed` suoraan taulukon soluissa.

## 1. Heikoimmat ensin
![[Kertaus.base#Heikoimmat ensin]]

## 2. Ei kerrattu 30 päivään
Päivämäärälaskenta pysyy Dataview'na.

```dataview
TABLE type AS "Tyyppi", jlpt AS "JLPT", reviewed AS "Viimeksi", status AS "Status"
FROM "10 Kielioppi" OR "20 Verbit" OR "30 Sanasto" OR "40 Kanji"
WHERE reviewed AND date(reviewed) < date(today) - dur(30 days)
SORT reviewed ASC
LIMIT 30
```

## 3. Toistuvat virheet
![[Kertaus.base#Toistuvat virheet]]

## 4. Uudet, käsittelemättä
![[Kertaus.base#Uudet]]

## 5. Työn alla
![[Kertaus.base#Työn alla]]

## 6. Opiskeluaika
![[_MOC Päiväkirja]]
