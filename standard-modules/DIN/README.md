# DIN — Module Entrées Digitales DIN4_R5_KS (MIDIbox NG)

## Description
Module de base DIN (Digital Input) de l'écosystème MIDIbox NG. Fournit la lecture d'entrées digitales pour boutons, switchs, encodeurs. Se connecte aux front-ends DIN (8x-buttons, keysw-4x2, surface-control, etc.).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](docs/assets/standard-modules/DIN-DIN4_R5_KS.png)

## Spécifications techniques
- Entrées digitales pour boutons et switchs
- Interface DIN vers bus MIDIbox NG
- Multiplexage via 74HC165

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Décaleur | 74HC165 | 4 |
| Connecteur IDC 2x05 | P2.54mm Vertical | 1 |
| Résistance réseau | R_Array_SIP6 | 9 |
| Résistance axiale | R_Axial_DIN0204 | 36 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 4 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DIN-x | Entrée digitale x |
| GND | Masse commune |
| +5V | Alimentation |

## Documentation de fabrication
- `hardware/` : sources KiCad (`DIN4_R5_KS.*`, `DIN4_R5_KS_2024.*`)
- `hardware/3D/` : modèles 3D (`.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions

---

**Référence MIDIbox NG — GPL-3.0**