# 8x-buttons — Carte 8 boutons poussoirs (DIN)

## Description
Module boutons poussoirs (8 canaux) pour l'envoi d'événements MIDI numériques (Note On/Off, CC, etc.). Interface DIN (Digital Input) du contrôleur MIDIbox NG.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/8x-buttons/BP.png)

## Spécifications techniques
- 8 boutons poussoirs tactiles ou mécano
- Interface DIN (Digital Input) — 8 canaux
- Pull-up interne ou externe configurable
- Alimentation : +5V

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Bouton poussoir tactile | 6x6mm | 8 |
| Résistance pull-up | 10 kΩ | 8 |
| Connecteur | D-Sub 24 broches | 1 |
| LED | Vert 5 mm | 8 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DIN-1 → DIN-8 | Boutons B1..B8 |
| GND | Masse |
| +5V (pull-up) | Activé |

## Documentation de fabrication
- `hardware/` : sources KiCad (`BP.*`)
- `hardware/3D/` : modèle 3D du boîtier (`BP V3.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archives de fabrication

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
