# 8x-buttons — Carte 8 boutons poussoirs (DIN)

## Description
Module boutons poussoirs (8 canaux) pour l'envoi d'evenements MIDI numeriques (Note On/Off, CC, etc.). Interface DIN (Digital Input) du controleur MIDIbox NG.

Article de reference : [4x2-BPL-v0.2](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S - modele BP4X2.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Screenshot 1 | `Screenshot%202023-05-19%20163416.png` | Capture d'écran du design |
| Screenshot 2 | `Screenshot%202023-05-19%20202624.png` | Capture d'écran du design |

![3D top](assets/BP.png)
![Screenshot 1](assets/Screenshot%202023-05-19%20163416.png)
![Screenshot 2](assets/Screenshot%202023-05-19%20202624.png)

## Specifications techniques
- 8 boutons poussoirs tactiles ou mecano
- Interface DIN (Digital Input) - 8 canaux
- Pull-up interne ou externe configurable
- Alimentation : +5V

## Composants principaux
| Type | Denomination | Qte |
|------|-------------|-----|
| Bouton poussoir tactile | 6x6mm | 8 |
| Resistance pull-up | 10 kOhm | 8 |
| Connecteur | D-Sub 24 broches | 1 |
| LED | Vert 5 mm | 8 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DIN-1 a DIN-8 | Boutons B1..B8 |
| GND | Masse |
| +5V (pull-up) | Active |

## Notes de montage et astuces DIY
- Verifier la configuration des entres (active haut / active bas) avant cableage
- Resistances de pull-up a prevoir selon le module DIN utilise

## Documentation de fabrication
- `hardware/` : sources KiCad (`BP.*`)
- `hardware/3D/` : modele 3D du boitier (`BP V3.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archives de fabrication

---

**Retro-ingenierie par l'equipe — GPL-3.0**
