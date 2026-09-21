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

**Pašreizējā versijā:**  
Lietotājs var izvēlēties uzdevumu no saraksta un ar pogu **Pabeigt uzdevumu**,  mainīt statusu uz `[x]`, kā arī rediģēt uzdevuma tekstu vai pilnībā izdzēst uzdevumu.

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
