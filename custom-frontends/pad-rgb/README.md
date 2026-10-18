# pad-rgb — Carte pads rétroéclairés RGB (DIN + DOUT)

## Description
Carte de front-end intégrant des pads (boutons sensibles) rétroéclairés RGB (WS2812) pour le déclenchement d'événements MIDI avec retour visuel couleur. Chaque pad génère un événement MIDI sur le bus DIN, et l'éclairage RGB est piloté via le bus DOUT.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/pad-rgb/Pad.png)

## Spécifications techniques
- Pads tactiles (boutons sensibles)
- Éclairage RGB WS2812 (1 fil de données)
- Interface DIN (entrée des pads) + DOUT (pilotage LEDs WS2812)
- Alimentation 5V dédiée pour les LEDs (consommation élevée)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Pads tactiles | — | 8 |
| LED RGB adressable | WS2812B | 8 |
| Connecteur | Header mâle DIN + DOUT | 1 |
| Symbole WS2812-2020 | `libs/symbols/` | 1 |
| Empreinte LED_WS2812-2020 | `libs/footprints/` | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DIN-1 → DIN-8 | Pads P1..P8 |
| DOUT-1 | Data WS2812 (LED RGB) |
| GND | Masse commune |
| +5V | Alimentation LEDs |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Pad.*`)
- `hardware/3D/` : modèles 3D des pads (`.wrl`, `.STEP`)
- `libs/symbols/` : symbole `WS2812-2020.kicad_sym`
- `libs/footprints/` : empreinte `LED_WS2812-2020.kicad_mod`
- `production/` : fichiers de position (`.pos`), datasheet WS2812B

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
