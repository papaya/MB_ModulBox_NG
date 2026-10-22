# DIN — Module Entrées Digitales DIN4_R5_KS (MIDIbox NG)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

## Description
Module de base **DIN** (Digital Input) de l'ecosysteme MIDIbox NG, equivalent du **MBHP_DINX4_R5**. Il fournit **32 entrees digitales** (4 registres a decalage **74HC165** en cascade) pour boutons, switchs et encodeurs. Se connecte aux front-ends DIN (`8x-buttons`, `keysw-4x2`, `encoders-led-rgb`, `pad-rgb`).

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](assets/DIN-DIN4_R5_KS.png)

## Spécifications techniques
- **4 × 74HC165** en cascade = **32 entrees digitales**
- **36 pull-up de 10 kΩ** : 28 (`R1`..`R28`) sur les entrees + 4 (`R33`..`R36`) pour definir un niveau quand un IC n'est pas pose
- **8 reseaux de resistances** `RN1`..`RN8` (`R_Array_SIP6`) pour les pull-up supplementaires
- 4 × condensateur de decoupling 100 nF (`C1`..`C4`), a poser **cote verso**, au plus pres de l'alimentation du 74HC165
- 6 connecteurs **IDC 2x05** : `J1`/`J2` (chainage / Core `J8J9`), `J3`..`J6` (entrees)
- **Sockets DIL 16 broches** pour les 74HC165 (obligatoires)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Décaleur | 74HC165 (DIP-16) | 4 |
| Résistance de pull-up | 10 kΩ (`R1`..`R36`) | 36 |
| Réseau de résistances | `R_Array_SIP6` (`RN1`..`RN8`) | 8 |
| Condensateur de decoupling | 100 nF (`C1`..`C4`) | 4 |
| Connecteur | IDC Header 2x05 P2.54mm (`J1`..`J6`) | 6 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 4 |

## Brochage / Mapping MIDIbox NG

### `J1` — interface vers le Core (`J8J9`) et chainage
| Broche | Signal | Description |
|--------|--------|-------------|
| 1, 2 | GND | Masse |
| 3, 4 | +5V | Alimentation 5 V |
| 5 | `IC1-Q7` | Sortie serie du premier 74HC165 (`Q7`) |
| 6 | — | Non connectee |
| 7, 8 | `SC` | **Horloge serie** (partagee par les 4 registres) |
| 9, 10 | `RC` | **Latch enable** (partage par les 4 registres) |

### `J2` — chainage vers un module DIN suivant
| Broche | Signal | Description |
|--------|--------|-------------|
| 1, 2 | GND | Masse |
| 3, 4 | +5V | Alimentation 5 V |
| 5 | `IC4-DS` | Entree serie du 4e registre (`DS`) — permet de chainer un module supplementaire |
| 6 | — | Non connectee |
| 7, 8 | `SC` | Horloge serie |
| 9, 10 | `RC` | Latch enable |

> Conformement a [ucapps.de/mbhp_din](https://www.ucapps.de/mbhp_din.html) : `J1` se branche sur le **Core (`J9`)** ou sur `J2` du module precedent ; `J2` permet de **chainer** les modules (le `DS` du dernier registre alimente le suivant).

### `J3`..`J6` — 8 entrees digitales chacun (avec GND)
Brochage type (identique pour `J3`, `J4`, `J5`, `J6`) :
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (contact du bouton) |
| 2 | — | Non connectee |
| 3 | `IC1-D7` | Entree digitale 7 |
| 4 | `IC1-D6` | Entree digitale 6 |
| 5 | `IC1-D5` | Entree digitale 5 |
| 6 | `IC1-D4` | Entree digitale 4 |
| 7 | `IC1-D3` | Entree digitale 3 |
| 8 | `IC1-D2` | Entree digitale 2 |
| 9 | `IC1-D1` | Entree digitale 1 |
| 10 | `IC1-D0` | Entree digitale 0 |

> Chaque entree `Dx` du 74HC165 est tiree vers **+5 V par une resistance de pull-up de 10 kΩ** : c'est ce qui definit un niveau logique quand le bouton n'est pas presse.
>
> **Pour un fonctionnement « high-active »** (5 V = actif), la doc officielle indique de **souder les deux cables isoles rouges sur 0 V (Vss) au lieu de 5 V**, ce qui transforme les pull-up en pull-down. Voir [ucapps.de/mbhp_din](https://www.ucapps.de/mbhp_din.html).
>
> **Les boutons se connectent entre l'entree `Dx` et GND** (broche 1 du connecteur).

## Documentation de fabrication
- `hardware/` : sources KiCad (`DIN4_R5_KS.*`)
- `hardware/3D/` : modèles 3D (`.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** — layout **DINX4_R5** (revised PCB, SmashTV) — conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Référence MIDIbox NG — GPL-3.0**
