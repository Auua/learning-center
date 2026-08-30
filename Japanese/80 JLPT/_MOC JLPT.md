---
type: moc
created: 2026-08-29
tags: [moc, jlpt]
---
# JLPT

[[N5]] · [[N4]] · [[N3]] · [[N2]] · [[N1]]

> [!info] Nykyinen taso
> Työskentelen N3-tasolla. N4 pitäisi olla selkärangassa — käytä [[Kertaus]]-näkymää löytääksesi N4-aukot ennen kuin lisäät N3-materiaalia.
>
> Tasomerkinnät ovat ohjeellisia: virallista JLPT-sanasto- tai kielioppilistaa ei ole julkaistu vuoden 2010 uudistuksen jälkeen.

## Kaikki tasoittain
![[JLPT.base#Kaikki tasot]]

## Status per taso
Ristiintaulukointi kahdella kentällä — Bases ryhmittelee vain yhdellä, joten tämä pysyy Dataview'na.

```dataview
TABLE length(rows) AS "Kpl"
FROM "10 Kielioppi" OR "20 Verbit" OR "30 Sanasto" OR "40 Kanji"
WHERE jlpt AND status
GROUP BY jlpt + " · " + status
```
