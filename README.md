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
- [ ] Datu saglabāšana JSON failā
- [ ] Datu ielāde no JSON faila

## Pašreizējā funkcionalitāte

Lietotnē iespējams:

- ievadīt jaunu uzdevumu teksta laukā;
- pievienot uzdevumu sarakstam ar pogu **Pievienot**;
- nepieļaut tukšu vai tikai atstarpēm sastāvošu uzdevumu pievienošanu;
- apskatīt pievienoto uzdevumu sarakstu;
- automātiski attīrīt ievades lauku pēc pievienošanas.

Pašreizējā versijā uzdevumi tiek glabāti tikai programmas darbības laikā.  
Pēc lietotnes aizvēršanas tie netiek saglabāti.

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
├── .gitignore
└── venv/ 
```

## Autors

Deniss Cvetkovs
