# keysw-4x2 — Clavier 4x2 touches (DIN)

## Description
Carte de front-end intégrant un clavier matricé 4x2 (8 touches) pour l'envoi d'événements MIDI (notes, CC, etc.). Chaque touche est lue sur une entrée digitale du bus DIN de l'écosystème MIDIbox NG.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/keysw-4x2/MB-KeySW_4x2_V0.3.png)

## Spécifications techniques
- Clavier matricé 4x2 (8 touches)
- Interface DIN (Digital Input) — matricage 4x2
- Diodes de protection anti-ghosting sur chaque touche
- Alimentation : +5V (pull-up)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Switch mécanique | Cherry MX Low Profile / Kailh | 8 |
| Touches (keycaps) | `beschr. Kappe.wrl` | 8 |
| LED SK6812MINI-E | Rétroéclairage optionnel | 8 |
| Diode anti-ghosting | 1N4148 | 8 |
| Connecteur | Header mâle 2x5 vers DIN | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DIN-1 → DIN-4 | Lignes de scan (colonnes) |
| DIN-5 → DIN-6 | Lignes de retour (lignes) |
| GND | Masse commune |
| +5V | Pull-up |

## Documentation de fabrication
- `hardware/` : sources KiCad (`MB-KeySW_4x2_V0.3.*`)
- `hardware/3D/shapes3D/` : modèles 3D des touches et switchs (`.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), fichiers de position, archives de fabrication

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
