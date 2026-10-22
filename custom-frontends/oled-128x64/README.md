# oled-128x64 — Carte afficheur OLED 128x64 SSD1309 (SPI)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

## Description
Carte de front-end integrant un afficheur OLED 128x64 pixels pour l'affichage d'informations MIDI (nom de piste, valeur de parametre, menu, etc.). L'afficheur est un **SSD1309** commande en **SPI** (4 fils + reset), et **non** en I2C.

> ⚠️ **Correction majeure : les versions anterieures de cette page indiquaient un bus I2C (SSD1306 / SH1106, adresses 0x3C / 0x3D).** Le schema KiCad `Oled_1309_x1_V0.0.kicad_sch` montre un **SSD1309 en SPI** avec les broches `D0` (SCLK), `D1` (SDATA), `DC`, `CS` et `RES`. Il n'y a **aucune broche SDA/SCL ni adresse I2C** sur cette carte.
>
> ⚠️ Cet afficheur ne se connecte **pas** sur le bus DIN/DOUT du MIDIbox NG : il se branche sur une interface **SPI** du microcontroleur (SPI du Core ou SPI dedie).
>
> Le fait que le **nom du projet** soit `Oled_1309_x1_V0.0` (1309 = SSD1309, x1 = une voie SPI) confirme ce cablage.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](assets/Oled_1309_x1_V0.0.png)

## Spécifications techniques
- Afficheur OLED **128 x 64**, controleur **SSD1309**, communication **SPI 4 fils**
- Reset materiel : **R1 = 1 kΩ** (pull-up vers +5V) et **C1 = 10 µF** sur la ligne `RES`
- **8 cavaliers de selection** `JP1`..`JP8` : la ligne `CS` commune peut etre routee individuellement vers l'un des 8 connecteurs du bus, ce qui permet de **chainer plusieurs afficheurs** sur un meme bus SPI
- Connecteur de sortie `J1` = **IDC 2x08** (16 broches)
- Alimentation : **+5V**

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Afficheur OLED | SSD1309 128x64 (`ksir 2022:SSD_1309`) | 1 |
| Resistance | R 1 kΩ (pull-up `RES`) | 1 |
| Condensateur | C 10 µF (reset `RES`) | 1 |
| Cavalier de selection CS | Jumper 2 contacts (`JP1`..`JP8`) | 8 |
| Connecteur | IDC Header 2x08 P2.54mm (`J1`) | 1 |
| Vis de fixation | MountingHole 2.2mm M2 | 8 |

## Brochage / Mapping MIDIbox NG

### `J1` — connecteur de sortie (IDC 2x08)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | — | Non connectee |
| 2 | `CS6` | Ligne `CS` du cavalier `JP7` |
| 3 | `CS4` | Ligne `CS` du cavalier `JP5` |
| 4 | `CS2` | Ligne `CS` du cavalier `JP3` |
| 5 | `CS0` | Ligne `CS` du cavalier `JP1`/`JP2` |
| 6 | `D1` | **SDATA** (donnees SPI) |
| 7 | — | Non connectee |
| 8 | GND | Masse |
| 9 | — | Non connectee |
| 10 | `CS7` | Ligne `CS` du cavalier `JP8` |
| 11 | `CS6` | Ligne `CS` du cavalier `JP7` |
| 12 | `CS3` | Ligne `CS` du cavalier `JP4` |
| 13 | `CS1` | Ligne `CS` du cavalier `JP1`/`JP2` |
| 14 | `D0` | **SCLK** (horloge SPI) |
| 15 | `DC` | **Data/Command** |
| 16 | +5V | Alimentation |

### Signaux de l'afficheur `OLED1`
| Broche SSD1309 | Signal | Role |
|----------------|--------|------|
| `D0` | `D01` | **SCLK** — horloge SPI (vers `J1` broche 14) |
| `D1` | `D11` | **SDATA** — donnees SPI (vers `J1` broche 6) |
| `DC` | `DC1` | **Data/Command** (vers `J1` broche 15) |
| `CS` | `CS` | **Chip Select** — commun aux 8 cavaliers `JP1`..`JP8` |
| `RES` | `RES1` | **Reset** — tire vers +5V par R1 (1 kΩ), decouple par C1 (10 µF) |
| `VCC` | +5V | Alimentation |
| `GND` | GND | Masse |

### Cavaliers `JP1`..`JP8` — selection du chip select
Chaque cavalier relie la ligne `CS` commune de l'afficheur a une des 8 lignes `CS0`..`CS7` disponibles sur `J1`. Par defaut **aucun cavalier n'est pose** : il faut **poser au moins un cavalier** pour que l'afficheur reponde.

> Pour un afficheur unique : poser **un seul** cavalier (par exemple `JP1`), et cabler la ligne `CS` correspondante (`J1` broche 5 ou 13) sur la ligne `CS` du controleur.
>
> Pour plusieurs afficheurs en serie sur un bus SPI : poser un cavalier different sur chaque carte (`JP1`, `JP2`, ... `JP8`) et relier les 8 lignes `CS0`..`CS7` aux 8 sorties de selection du controleur.

### Raccordement au bus SPI
La ligne `D0`/`D1` se branche sur une interface **SPI** du microcontroleur. Sur le **Core32F4**, le connecteur **`J19`** est un port SPI 5V (utilise par l'AINSER64) et **`J16`** est le port SPI 3,3 V (carte SD / ETH). Le protocole SPI (mode, CPOL/CPHA) doit correspondre au SSD1309.

## Documentation de fabrication
- `hardware/` : sources KiCad (`Oled_1309_x1_V0.0.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archive de fabrication

---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Rétro-ingénierie par l'équipe — GPL-3.0**

