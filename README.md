# MB_ModulBox_NG — Contrôleur MIDI Modulaire (Écosystème MIDIbox NG)

Projet open-source hardware de contrôleur MIDI modulaire basé sur l'écosystème **MIDIbox NG**.  
Ce projet est développé et documenté sur le blog **[Ksir DIY'S](https://ksir-diy.blogspot.com/)** — article principal : *"ModulBox V2" (mai 2023)*.

Le projet est séparé en deux grands ensembles :

1. **Modules standards MIDIbox** (AIN, DIN, DOUT, Core, IO) — référence centrale dans `standard-modules/`
2. **Cartes additionnelles / front-ends spécifiques** — plaques de contrôle physiques dans `custom-frontends/`

---

## 📖 Articles et ressources du blog ksir-diy.blogspot.com

| Article du blog | Thème | Lien |
|-----------------|-------|------|
| [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) | Présentation globale du projet (mai 2023) | [Voir sur le blog](https://ksir-diy.blogspot.com/) |
| [ALL FILES — Archive complète](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing) | Tous les fichiers de fabrication, schémas, Gerbers | [Google Drive](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing) |

**Articles par carte :**
| Carte | Article du blog | Dossier |
|-------|----------------|---------|
| 4X2-POTS-v0.2 | Potentiomètres rotatifs | `custom-frontends/8x-pots/` |
| 4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2 | Faders / glissières | `custom-frontends/4x-faders/` |
| 4x2-BPL-v0.2 | Boutons poussoirs | `custom-frontends/8x-buttons/` |
| 4X2-PADS-RGB | Pads rétroéclairés RGB WS2812 | `custom-frontends/pad-rgb/` |
| 4X2 ENC-SW-16-LED-RING-RGB (PEC16) | Encodeurs avec anneau LED RGB | `custom-frontends/encoders-led-rgb/` |

> ⚠️ L'article *"4X2 ENC-SW-16-LED-RING-RGB (PEC16)"* est marqué comme **"non terminé, ne fonctionne pas"** sur le blog. Les sources sont néanmoins disponibles pour référence.

---

## Arborescence du projet

```
MB_ModulBox_NG/
├── README.md                 # Ce document
├── PLAN.md                   # Feuille de route d'organisation (phases 0-9)
├── .gitignore                # Exclusion des polluants KiCad et macOS
├── common-docs/              # Documentation générale et bus MIDIbox NG
│   ├── README.md
│   ├── bus-midibox-ng.md     # Schéma de principe des bus AIN / DIN / DOUT
│   ├── connecteurs/          # Brochage des connecteurs de bus communs
│   └── schémas-principe/     # Blocs logiques partagés
├── global-libs/              # Bibliothèques partagées (symboles + empreintes)
│   ├── symbols/              # *.kicad_sym partagés
│   └── footprints/           # *.pretty partagés
├── standard-modules/         # Modules de base MIDIbox (copie de référence)
│   ├── AIN/                  # Entrées analogiques
│   ├── DIN/                  # Entrées digitales
│   ├── DOUT/                 # Sorties digitales
│   ├── Core/                 # Cœur STM32F4 (Core32f4)
│   └── IO/                   # Interface MIDI / IO
├── custom-frontends/         # Cartes additionnelles de contrôle
│   ├── 4x-faders/            # Glissières / faders (AIN)
│   ├── 8x-pots/              # Potentiomètres rotatifs (AIN)
│   ├── 8x-buttons/           # Boutons poussoirs (DIN)
│   ├── encoders-led-rgb/     # Encodeurs avec anneau LED RGB (DIN+DOUT)
│   ├── pad-rgb/              # Pads rétroéclairés RGB WS2812 (DIN+DOUT)
│   ├── oled-128x64/          # Afficheur OLED 128x64 (I2C/SPI)
│   ├── keysw-4x2/            # Clavier matricé 4x2 touches (DIN)
│   ├── carte-puissance/      # Alimentation / distribution
│   └── surface-control/      # Surface de contrôle globale (prototype V0.1)
├── archive/                  # Versions figées (KICAD_6, doublons, tests)
│   ├── 2023-KICAD-6/
│   ├── 2023-KICAD-7-doublons/
│   └── experimental/
├── docs/                     # Documentation et assets visuels
│   ├── assets/system/        # Vues d'ensemble, schémas d'architecture
│   ├── assets/standard-modules/  # Rendus 3D des modules standards
│   ├── assets/frontends/     # Rendus 3D par front-end
│   └── guides/               # Guides de câblage et d'assemblage
└── tools/                    # Scripts de nettoyage / validation
```

---

## Table des matières des front-ends

| Front-end | Bus | Rôle | Dossier |
|-----------|-----|------|---------|
| 4x-faders | AIN | Glissières / faders | `custom-frontends/4x-faders/` |
| 8x-pots | AIN | 8 potentiomètres rotatifs | `custom-frontends/8x-pots/` |
| 8x-buttons | DIN | 8 boutons poussoirs | `custom-frontends/8x-buttons/` |
| encoders-led-rgb | DIN + DOUT | Encodeurs avec anneau LED RGB | `custom-frontends/encoders-led-rgb/` |
| pad-rgb | DIN + DOUT | Pads rétroéclairés RGB WS2812 | `custom-frontends/pad-rgb/` |
| oled-128x64 | I2C / SPI | Afficheur OLED 128x64 | `custom-frontends/oled-128x64/` |
| keysw-4x2 | DIN | Clavier matricé 4x2 touches | `custom-frontends/keysw-4x2/` |
| carte-puissance | — | Alimentation / distribution | `custom-frontends/carte-puissance/` |
| surface-control | DIN + DOUT + AIN | Surface de contrôle globale (V0.1) | `custom-frontends/surface-control/` |

---

## Modules standards MIDIbox

| Module | Bus | Rôle | Dossier |
|--------|-----|------|---------|
| AIN | AIN | Entrées analogiques (64 voies) | `standard-modules/AIN/` |
| DIN | DIN | Entrées digitales (DIN4_R5_KS) | `standard-modules/DIN/` |
| DOUT | DOUT | Sorties digitales | `standard-modules/DOUT/` |
| Core | — | Cœur STM32F4 (Core32F4) | `standard-modules/Core/` |
| IO | MIDI | Interface MIDI IN/OUT | `standard-modules/IO/` |

---

## Documentation

- `common-docs/bus-midibox-ng.md` — Schéma de principe des bus AIN, DIN et DOUT de MIDIbox NG
- `common-docs/connecteurs/` — Brochage détaillé des connecteurs de bus
- Chaque front-end possède son propre `README.md` avec son brochage et ses notes d'assemblage
- `docs/assets/` — Rendus 3D des PCB (vues top et isométrique)

---

## Contribuer

1. Consulter `PLAN.md` pour la feuille de route détaillée
2. Chaque modification de front-end doit être accompagnée de son `README.md`
3. Vérifier que les chemins KiCad restent relatifs avant tout commit
4. Les anciennes versions sont conservées dans `archive/` (ne pas supprimer sans validation)

---

**Licence :** GPL-3.0 — Open Source Hardware  
**Rétro-ingénierie et structuration :** Équipe MB_ModulBox_NG
