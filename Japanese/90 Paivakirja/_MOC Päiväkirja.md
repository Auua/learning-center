---
type: moc
created: 2026-08-29
tags: [moc]
---
# Päiväkirja

[[Kertaus]] · [[_MOC Kielioppi]]

> [!tip] Miksi virhepäiväkirja kannattaa
> Oma virhe on tehokkaampi kortti kuin oppikirjan esimerkki, koska se on jo kertaalleen epäonnistunut. Merkitse `recurring: true` kun sama virhe toistuu — [[Kertaus]] nostaa ne esiin.

## Opiskeluloki
Yhteenvetorivi laskee minuutit.

![[Päiväkirja.base#Opiskeluloki]]

## Virheet syyn mukaan
![[Päiväkirja.base#Virheet syyn mukaan]]

## Opiskeluaika viikoittain
```dataview
TABLE sum(rows.minutes) AS "Minuuttia", length(rows) AS "Kertaa"
FROM "90 Paivakirja/Loki"
WHERE date >= date(today) - dur(90 days)
GROUP BY dateformat(date, "yyyy-'W'WW") AS Viikko
SORT Viikko DESC
```
