# IO — Module Interface MIDI Midi_V0.1 (MIDIbox NG)

## Description
Module de base IO (Interface MIDI) de l'écosystème MIDIbox NG. Fournit les entrées/sorties MIDI physiques (IN/OUT) pour connecter le contrôleur à d'autres équipements MIDI.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](docs/assets/standard-modules/IO-Midi_V0.1.png)

## Spécifications techniques
- Entrées MIDI IN (x2)
- Sorties MIDI OUT (x2)
- Optocoupleurs 6N138 pour isolation
- Connecteurs DIN 5 broches (LEMO5)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Optocoupleur | 6N138 | 3 |
| Connecteur DIN-5 | LEMO5 | 5 |
| LED | D5.0mm | 5 |
| Résistance axiale | R_Axial_DIN0204 | 20 |
| Empreinte de fixation | MountingHole_3.2mm_M3_DIN965_Pad | 4 |
| Capacité | C_Disc | 6 |
| Diode | DO-35 | 2 |
| Circuit logique | SN74HC00N | 3 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| MIDI IN-1 / IN-2 | Entrées MIDI |
| MIDI OUT-1 / OUT-2 | Sorties MIDI |
| GND | Masse commune |
| +5V | Alimentation |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Midi_V0.1.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions

---

**Référence MIDIbox NG — GPL-3.0**