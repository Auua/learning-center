<%* const j = await tp.system.suggester(["N5","N4","N3","N2","N1"], ["N5","N4","N3","N2","N1"], false, "JLPT-taso"); -%>
---
type: grammar
ja: "<% tp.file.title %>"
reading: 
jlpt: <% j %>
func: []
attaches: []
formality: neutral
register: [puhuttu, kirjoitettu]
similar: []
compare: 
sources: []
status: new
confidence: 1
reviewed: 
created: <% tp.date.now("YYYY-MM-DD") %>
tags: [grammar, jlpt/<% j.toLowerCase() %>]
---

> [!abstract] Ydin
> Yhdellä lauseella: mitä tämä tekee.

## Merkitys
- **FI:** 
- **EN:** 

## Muodostus
| Mihin liittyy | Kaava | Esimerkki |
|---|---|---|
| Verbi | | |
| い-adjektiivi | | |
| な-adjektiivi | | |
| Substantiivi | | |

Käytetyt taivutusmuodot: 

## Nyanssi ja rajoitukset
- 
- Ei käy kun: 

## Esimerkit
- 

## Sekaannusvaara
Vertailu: 

## Kuvavihje
![[]]

## Kortit
#flashcards/grammar/<% j.toLowerCase() %>

<% tp.file.title %> — merkitys ja muodostus?
?
vastaus

#flashcards/grammar/<% j.toLowerCase() %>/muodostus

<% tp.file.title %> + verbi :: kaava — esimerkki
<% tp.file.title %> + い-adjektiivi :: kaava — esimerkki
<% tp.file.title %> + な-adjektiivi :: kaava — esimerkki
<% tp.file.title %> + substantiivi :: kaava — esimerkki

#flashcards/grammar/<% j.toLowerCase() %>/nyanssi

nyanssi- tai rajoituskysymys
?
vastaus

#flashcards/grammar/<% j.toLowerCase() %>/sekaannus

sekaannuskysymys
?
vastaus

#flashcards/grammar/<% j.toLowerCase() %>/vertailu

<% tp.file.title %> (similar) ::: toisen rakenteen otsikko (similar)
<% tp.file.title %> (compare) ::: toisen rakenteen otsikko (compare)
