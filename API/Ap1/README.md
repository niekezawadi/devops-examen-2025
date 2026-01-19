Ap1 – School Library API
In dit experiment testte ik de School Library API via de Swagger‑interface in de DEVASC‑VM. Het doel was om een volledige CRUD‑flow uit te voeren: een token ophalen, een boek toevoegen, controleren, verwijderen en opnieuw controleren.

Stappen die ik heb uitgevoerd

1. Token ophalen
Ik ben gestart met het ophalen van een token via POST /loginViaBasic.
Daarvoor gebruikte ik de credentials cisco en Cisco123!.
De API gaf een token terug in de JSON‑response, dat ik vervolgens invoerde via de “Authorize”-knop in Swagger.

2. Een boek toevoegen
Daarna heb ik een nieuw boek toegevoegd via POST /books.
Ik gebruikte deze body:

json
{
  "id": 4,
  "title": "IPV6 Fundamentals",
  "author": "Rick Graziani"
}
De API antwoordde met statuscode 200, wat betekent dat het boek correct werd toegevoegd.

3. Controleren of het boek bestaat
Met GET /books heb ik gecontroleerd of het boek effectief in de lijst stond.
Het boek met id 4 verscheen zoals verwacht.

4. Het boek verwijderen
Vervolgens heb ik het boek verwijderd via DELETE /books/4.
Ook hier kreeg ik een 200‑status terug.

5. Controleren of het boek weg is
Tot slot heb ik opnieuw GET /books uitgevoerd om te bevestigen dat het boek niet langer in de lijst stond.

Structuur in GitHub
Code
API/Ap1/
├── README.md
└── screenshots/
    ├── 01-post-book.png
    ├── 02-get-books-after-post.png
    ├── 03-delete-book.png
    ├── 04-get-books-after-delete.png
    ├── 05-authorize.png
    └── 06-token.png

Resultaat
De volledige CRUD‑flow werkt zoals verwacht.
De API‑key werd correct gebruikt, alle endpoints reageerden met de juiste statuscodes en de screenshots tonen elke stap van het experiment.
Ap1 is hiermee volledig afgerond.

Gebruikte tools
Swagger (OpenAPI)

Chromium in de DEVASC‑VM

Ubuntu Screenshot Tool

Git en GitHub via de terminal
