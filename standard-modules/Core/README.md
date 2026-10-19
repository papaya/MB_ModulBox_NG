# Core — Cœur STM32F4 Core32F4 (MIDIbox NG)

## Description
Cœur de contrôle du contrôleur MIDIbox NG. Basé sur STM32F4, il gère le multiplexage des bus AIN, DIN et DOUT, ainsi que la communication USB/MIDI. Version de référence : Core32f4_V0.1.

📖 **Article de référence :** [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) sur le blog Ksir DIY'S.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](docs/assets/standard-modules/Core-Core32F4.png)

## Spécifications techniques
- Microcontrôleur STM32F4 (Core32F4)
- Gestion des bus AIN, DIN, DOUT
- Communication USB/MIDI
- Connecteurs pour modules d'extension

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| MCU | STM32F4 | 1 |
| Connecteur IDC | P2.54mm Vertical | 12 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 6 |
| Connecteur PinHeader | 2.54mm | 4 |
| Résistance axiale | R_Axial_DIN0204 | 8 |
| Capacité | Capacitor_THT | 2 |
| Boîtier DIP | DIP-16 / DIP-20 | plusieurs |
| Empreinte ksir | varie | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| Bus AIN | Entrées analogiques multiplexées |
| Bus DIN | Entrées digitales |
| Bus DOUT | Sorties digitales |
| USB | Communication MIDI vers hôte |
| GND / +5V | Alimentation |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Core32F4.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions, zip

---

**Référence MIDIbox NG — GPL-3.0**