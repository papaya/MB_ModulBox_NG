# encoders-led-rgb — Carte encodeurs avec anneau LED RGB (DIN + DOUT)

## Description
Carte de front-end intégrant des encodeurs rotatifs avec anneau LED RGB pour le contrôle de paramètres MIDI avec retour visuel (position, valeur, mode, etc.). Chaque encodeur génère des événements MIDI sur le bus DIN, et l'anneau LED est piloté via le bus DOUT.

📖 **Article de référence :** [4X2 ENC-SW-16-LED-RING-RGB (PEC16)](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — modèles PEC16 et P el12T. ⚠️ Marqué « non terminé, ne fonctionne pas » sur le blog.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |
| Screenshot | `Screenshot%202023-05-19%20175512.png` | Capture d'écran du design |

![3D top](assets/PEC_16_V0.2.png)
![Screenshot](assets/Screenshot%202023-05-19%20175512.png)

## Spécifications techniques
- Encodeurs rotatifs avec poussoir intégré (type PEC16R ou équivalent)
- Anneau LED RGB adressable (WS2812) piloté via DOUT
- Interface bus DIN (entrée encodeur) + DOUT (pilotage LEDs)
- Alimentation dédiée pour les LEDs (consommation élevée selon nombre de LEDs allumées)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Encodeur rotatif | PEC16R (ou équivalent) | 1 |
| Bouton-poussoir (intégré) | — | 1 |
| LED RGB adressable | WS2812 | 1 anneau |
| Connecteur | Header mâle DIN + DOUT | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DIN-1 | Phase A de l'encodeur |
| DIN-2 | Phase B de l'encodeur |
| DIN-3 | Bouton-poussoir de l'encodeur |
| DOUT-1 | LED Rouge (anneau RGB) |
| DOUT-2 | LED Verte (anneau RGB) |
| DOUT-3 | LED Bleue (anneau RGB) |
| GND | Masse commune |
| +5V | Alimentation LEDs |

## Documentation de fabrication
- `hardware/` : sources KiCad (`PEC_16_V0.2.*`)
- `hardware/3D/` : modèle 3D de l'encodeur (`.wrl`, `.step`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archives de fabrication
- `libs/` : symboles et empreintes spécifiques si non partagés

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
