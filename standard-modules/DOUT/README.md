# DOUT — Module Sorties Digitales DOUT (MIDIbox NG)


## Description
Module de base **DOUT** (Digital Output) de l'ecosysteme MIDIbox NG, equivalent du **MBHP_DOUTX4_R5**. Il fournit **32 sorties digitales** (4 registres a decalage **74HC595** en cascade) pour piloter des LEDs standards, des afficheurs 7 segments, des relais ou de la logique.

> ⚠️ **Le DOUT pilote des sorties NON adressables.** Les LED RGB WS2812/WS2812B ne passent **PAS** par ce module : elles recoivent une ligne de donnees d'une sortie WS2812 du **Core32F4** (`J4A` / `J4B`). Voir `standard-modules/Core/README.md`.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](assets/DOUT-DOUT.png)

## Spécifications techniques
- **4 × SN74HC595N** en cascade = **32 sorties digitales**
- **32 resistances de limitation de 220 Ω** : `R1` est un **reseau 8 × 220 Ω** (`DIP-16_R220_network`), `R2`/`R3`/`R4` sont des DIP-16 individuels
- 4 × condensateur de decoupling 100 nF (`C1`..`C4`), a poser **cote verso**, au plus pres de l'alimentation du 74HC595
- 6 connecteurs **IDC 2x05** : `J1`/`J2` (chainage / Core `J8J9`), `J3`..`J6` (sorties)
- **Sockets DIL 16 broches** pour les 74HC595

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Décaleur | SN74HC595N (DIP-16) | 4 |
| Résistance de limitation | 220 Ω (reseau DIP-16 ×1 + DIP-16 ×3) | 4 (32 valeurs) |
| Condensateur de decoupling | 100 nF (`C1`..`C4`) | 4 |
| Connecteur | IDC Header 2x05 P2.54mm (`J1`..`J6`) | 6 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 4 |

## Brochage / Mapping MIDIbox NG

### `J1` — interface vers le Core (`J8J9`) et chainage
| Broche | Signal | Description |
|--------|--------|-------------|
| 1, 2 | GND | Masse |
| 3, 4 | +5V | Alimentation 5 V |
| 5 | `J1-Pad5` | Donnees serie entrantes (`/S0`) — relie a `J2` du module precedent |
| 6 | `/S0` | **Donnees serie** (`SI`) |
| 7 | — | Non connectee |
| 8 | `/DOUT_SC` | **Horloge serie** (`SCLK`) |
| 9 | — | Non connectee |
| 10 | `/DOUT_RC` | **Latch enable** (`RCLK`) |

### `J2` — chainage vers un module DOUT suivant
| Broche | Signal | Description |
|--------|--------|-------------|
| 1, 2 | GND | Masse |
| 3, 4 | +5V | Alimentation 5 V |
| 5 | `J1-Pad5` | Donnees serie (relie a `J1`) |
| 6 | `IC4-QH_2` | **Sortie serie** (`Q7'`) du 4e registre — alimente le module suivant |
| 7, 8 | `/DOUT_SC` | Horloge serie |
| 9, 10 | `/DOUT_RC` | Latch enable |

> Conformement a [ucapps.de/mbhp_dout](https://www.ucapps.de/mbhp_dout.html) : `J1` se branche sur le **Core (`J8`)** ou sur `J2` du module precedent ; `J2` permet de **chainer** les modules (jusqu'a 8 modules / 32 registres / 256 sorties en MIOS32).

### `J3`..`J6` — 8 sorties digitales chacun (avec GND)
Brochage type (identique pour `J3`, `J4`, `J5`, `J6`) :
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (cathode des LED) |
| 2 | — | Non connectee |
| 3 a 10 | `R1-R8.1` .. `R1-R1.1` | Sorties digitales 7 a 0 (apres resistance 220 Ω) |

> **Attention a l'ordre des sorties** : conformement a la doc officielle, « *la premiere LED est generalement placee sur D7 d'un connecteur de sortie, alors que sur un module MBHP_DIN la premiere bouton est sur D0* ». Cet ordre heritage ne sera pas change.
>
> La **resistance de 220 Ω est sur ce module** (avant la LED), pas sur le front-end. Pour piloter de la logique plutot que des LED, les resistances peuvent etre remplacees par des straps (pontage).
>
> Les **afficheurs 7 segments**, **LEDs standard** et **relais** (via opto-coupleurs ou transistors) se connectent ici.

## Documentation de fabrication
- `hardware/` : sources KiCad (`DOUT.*`)
- `hardware/3D/` : modèles 3D (`.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions

> ℹ️ **Note de revision (2026-10-22)** : la version maintenue du dépôt (`hardware/DOUT.kicad_pcb` = **DOUT2024**, référence officielle MB Hardware 2024, cohérente avec `production/`) présente **21 pads non connectes** au niveau du +5V et **74 violations DRC** au total (outre 5 autres fichiers). Il n'existe pas de version alternative de meilleure qualité dans `archive/` (la version `superseded-dout` est une ancienne génération, 36038 lignes de différence) : elle est **retenue telle quelle** et signalée comme non fabriquable en l'état sans révision du routage du +5V.

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** — layout **DOUTX4_R5** (revised PCB, SmashTV) — conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Référence MIDIbox NG — GPL-3.0**> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
