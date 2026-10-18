# carte-puissance — Carte d'alimentation / distribution (standalone)

## Description
Carte de distribution d'alimentation pour l'écosystème MIDIbox NG. Elle fournit les tensions nécessaires aux modules AIN, DIN, DOUT et aux front-ends connectés sur les bus.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/carte-puissance/Carte_puissance.png)

## Spécifications techniques
- Distribution des rails +5V, +3.3V, GND
- Connecteurs d'entrée/sortie vers les bus AIN / DIN / DOUT
- Régulateurs de tension et condensateurs de découplage
- Protection contre les inversions de polarité

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Régulateur de tension | — | 1+ |
| Condensateur de découplage | — | plusieurs |
| Connecteur bus AIN/DIN/DOUT | Header mâle | plusieurs |
| Borne d'entrée secteur/alimentation | — | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| Entrée | Alimentation externe (à définir selon schéma) |
| Sortie AIN | +5V, GND vers bus AIN |
| Sortie DIN | +5V, GND vers bus DIN |
| Sortie DOUT | +5V, GND vers bus DOUT |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Carte_puissance.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, PDF du schéma

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
