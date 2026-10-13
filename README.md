# MiniTask

## Statuss

🚧 MVP izstrādē

---

## Apraksts

MiniTask ir vienkārša darbvirsmas lietotne personīgo uzdevumu pārvaldībai un uzskaitei. Lietotne tiek izstrādāta pakāpeniski, ievērojot profesionālu pieeju: skaidrs mērķis, definēts MVP, sakārtota projekta struktūra un notikumu vadīta programmēšana.

---

## MVP Funkcionalitāte

- [x] Lietotnes GUI palaišana
- [x] Uzdevumu pievienošana
- [x] Uzdevumu saraksta attēlošana
- [x] Uzdevumu pabeigšana
- [x] Uzdevumu rediģēšana
- [x] Uzdevumu dzēšana
- [x] Datu saglabāšana JSON failā
- [x] Datu ielāde no JSON faila

---

## Pašreizējā funkcionalitāte

Lietotnē iespējams:

- ievadīt jaunu uzdevumu teksta laukā;
- pievienot uzdevumu sarakstam ar pogu **Pievienot**;
- nepieļaut tukšu vai tikai atstarpēm sastāvošu uzdevumu pievienošanu;
- apskatīt pievienoto uzdevumu sarakstu;
- automātiski attīrīt ievades lauku pēc pievienošanas;
- automātiski saglabāt datus;
- apstiprināt uzdevuma pabeigšanu ar pogu un apskatīt statusu;
- rediģēt izvēlētā uzdevuma tekstu;
- dzēst izvēlēto uzdevumu.
- Kļūdu apstrāde

**Pašreizējā versijā:**  
MiniTask tagad spēj droši startēties arī situācijās, kad datu fails `tasks.json` nav derīgs vai neeksistē. Datu ielādes loģika ir papildināta ar paredzamu kļūdu apstrādi, kas nodrošina, ka lietotne neavārijas un lietotājs tiek informēts par problēmu.

---

## Konkrētika

### Datu saglabāšana

MiniTask saglabā uzdevumus starp programmas palaišanas reizēm.  
Programmas darbības laikā uzdevumi tiek glabāti Python sarakstā (`self.tasks`), kas ir galvenā datu glabātuve.  
`QListWidget` tikai attēlo datus lietotājam.

Uzdevumi tiek saglabāti datnē **tasks.json**, kas atrodas projekta saknes mapē.  
Dati tiek saglabāti UTF-8 kodējumā, izmantojot `ensure_ascii=False`, lai latviešu burti būtu salasāmi.

Programmas startēšanas laikā dati no `tasks.json` tiek automātiski ielādēti.  
Ja datne vēl neeksistē, MiniTask sāk darbu ar tukšu sarakstu un datne tiek izveidota pēc pirmā uzdevuma pievienošanas.

---

### Uzdevumu pabeigšanas stāvoklis

MiniTask atbalsta uzdevumu izpildes stāvokli.  
Katrs uzdevums tiek glabāts kā strukturēts datu objekts ar divām īpašībām:

- `text` — uzdevuma teksts;
- `done` — vai uzdevums ir pabeigts.

Jauns uzdevums vienmēr tiek izveidots nepabeigts (`done = False`) un saskarnē tiek attēlots ar `[ ]`.

Lietotājs var izvēlēties uzdevumu sarakstā un nospiest pogu **Pabeigt uzdevumu**, lai mainītu tā stāvokli uz pabeigtu (`done = True`).  
Pabeigts uzdevums tiek attēlots ar `[x]`.

Uzdevumu teksts un izpildes stāvoklis tiek saglabāts failā `tasks.json`, tāpēc statuss saglabājas arī pēc programmas restartēšanas.

---

### Uzdevumu rediģēšana

MiniTask tagad ļauj lietotājam **rediģēt izvēlētā uzdevuma tekstu**.

- Lietotājs izvēlas uzdevumu sarakstā.
- Nospiež pogu **Rediģēt uzdevumu**.
- Atveras dialoga logs ar pašreizējo tekstu.
- Lietotājs var ievadīt jaunu tekstu vai nospiest *Cancel*.

Rediģēšana tiek veikta datu modelī `self.tasks`, nevis tikai saskarnē.  
Izmaiņas tiek saglabātas `tasks.json`, un pēc restartēšanas rediģētais teksts saglabājas.

Tiek nodrošināta validācija:

- tukšs teksts netiek saglabāts;
- Cancel nemaina datus;
- ja nekas nav izvēlēts, programma neizmaina citus uzdevumus.

---

### Uzdevumu dzēšana

MiniTask tagad atbalsta arī **uzdevumu dzēšanu**.

- Lietotājs izvēlas uzdevumu sarakstā.
- Nospiež pogu **Dzēst uzdevumu**.
- Programma izdzēš tieši izvēlēto uzdevumu no `self.tasks`.

Dzēšana tiek veikta datu modelī, izmantojot `self.tasks.pop(row)`.  
Pēc tam dati tiek saglabāti un saskarne atjaunota.

Ja nekas nav izvēlēts:

- programma neizdzēš pēdējo uzdevumu,
- neizmet kļūdas,
- neizmaina datus.

Pēc programmas restartēšanas dzēstais uzdevums neatgriežas.

---

### Kļūdu apstrāde

#### Neeksistējošs datu fails
Ja `tasks.json` neeksistē (piemēram, programmas pirmajā palaišanas reizē), MiniTask:
- neavārijas,
- izveido tukšu uzdevumu sarakstu (`self.tasks = []`),
- turpina darbu normāli.

Šī situācija tiek uzskatīta par normālu un lietotājam netiek rādīts brīdinājums.

#### Bojāts vai tukšs JSON fails
Ja `tasks.json` eksistē, bet tā saturs nav derīgs JSON (bojāts fails, nepilnīgs fails, tukšs fails), MiniTask:
- neavārijas,
- izveido tukšu uzdevumu sarakstu,
- parāda lietotājam brīdinājumu ar `QMessageBox.warning`.

**Brīdinājuma teksts:**
*Neizdevās nolasīt saglabātos uzdevumus, jo datu fails ir bojāts.
Lietotne turpinās darbu ar tukšu uzdevumu sarakstu.*

#### Apstrādātie izņēmumi
Datu ielādes laikā tiek apstrādāti divi paredzami izņēmumi:

- `FileNotFoundError` — datu fails neeksistē;
- `json.JSONDecodeError` — datu fails satur nederīgu JSON.

Abos gadījumos tiek nodrošināts drošs sākuma stāvoklis (`self.tasks = []`), lai pārējā programma varētu turpināt darbu bez kļūdām.

#### Drošs sākuma stāvoklis
Kļūmes gadījumā `self.tasks` vienmēr tiek iestatīts kā tukšs saraksts. Tas nodrošina, ka:
- saskarne var droši iterēt pa uzdevumiem,
- CRUD funkcijas turpina strādāt,
- programma neavārijas un saglabā paredzamu uzvedību.

MiniTask tagad ir ne tikai strādājoša, bet arī uzticama lietotne, kas korekti reaģē uz datu ielādes problēmām.

---

## CRUD darbības

MiniTask tagad demonstrē pilnu CRUD datu pārvaldības ciklu:

- **Create** — jauna uzdevuma pievienošana;
- **Read** — uzdevumu ielāde un attēlošana;
- **Update** — uzdevuma teksta maiņa vai `done` stāvokļa maiņa;
- **Delete** — uzdevuma dzēšana.

Visas izmaiņas tiek veiktas datu modelī `self.tasks`, un tikai pēc tam saskarne tiek atjaunota.

---

## Tehnoloģijas

- Python 3.14  
- PySide6 (Qt for Python)  
- Git

---

## Projekta struktūra

```
MiniTask/
│
├── main.py
├── README.md
├── requirements.txt
├── tasks.json
├── .gitignore
└── venv/ 
```

## Autors

Deniss Cvetkovs
