# MiniTask

## Statuss

🚧 MVP izstrādē

## Apraksts

MiniTask ir vienkārša darbvirsmas lietotne personīgo uzdevumu pārvaldībai un uzskaitei. Lietotne tiek izstrādāta pakāpeniski, ievērojot profesionālu pieeju: skaidrs mērķis, definēts MVP, sakārtota projekta struktūra un notikumu vadīta programmēšana.

## MVP Funkcionalitāte

- [x] Lietotnes GUI palaišana (PD01)
- [x] Uzdevumu pievienošana (PD02)
- [x] Uzdevumu saraksta attēlošana (PD02)
- [ ] Uzdevumu dzēšana
- [x] Datu saglabāšana JSON failā
- [x] Datu ielāde no JSON faila

## Pašreizējā funkcionalitāte

Lietotnē iespējams:

- ievadīt jaunu uzdevumu teksta laukā;
- pievienot uzdevumu sarakstam ar pogu **Pievienot**;
- nepieļaut tukšu vai tikai atstarpēm sastāvošu uzdevumu pievienošanu;
- apskatīt pievienoto uzdevumu sarakstu;
- automātiski attīrīt ievades lauku pēc pievienošanas.
- automātiski saglabāt datus.

Pašreizējā versijā dati jau tiek glabāti `tasks.json` failā.  
Pēc lietotnes aizvēršanas dati saglabājās. Palaižot programmu atkārtoti, tie parādīsies sarakstā!

## Datu saglabāšana

MiniTask saglabā uzdevumus starp programmas palaišanas reizēm.  
Programmas darbības laikā uzdevumi tiek glabāti Python sarakstā (`self.tasks`), kas ir galvenā datu glabātuve.  
`QListWidget` tikai attēlo datus lietotājam.

Uzdevumi tiek saglabāti datnē **tasks.json**, kas atrodas projekta saknes mapē.  
Dati tiek saglabāti UTF-8 kodējumā, izmantojot `ensure_ascii=False`, lai latviešu burti būtu salasāmi.

Programmas startēšanas laikā dati no `tasks.json` tiek automātiski ielādēti.  
Ja datne vēl neeksistē, MiniTask sāk darbu ar tukšu sarakstu un datne tiek izveidota pēc pirmā uzdevuma pievienošanas.


## Tehnoloģijas

- Python 3.14
- PySide6 (Qt for Python)
- Git

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
