# 8x-pots — Carte 8 potentiomètres rotatifs (AIN)

## Description
Module potentiometres rotatifs (8 canaux) pour le controle de parametres continus MIDI (volume, filtre, effets, etc.). Chaque potentiometre est lu sur une voie analogique independante et connectee au bus AIN de l'ecosysteme MIDIbox NG.

Article de reference : [4X2-POTS-v0.2](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — utilise des potentiometres RK09D1130C1B ou RK09L1140A5L.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isometrique avec composants |

![3D top](assets/Pot.png)
![3D iso](assets/Pot-X2.png)

## Specifications techniques
- 8 potentiometres rotatifs (10 kOhm)
- Interface AIN (Analog Input) - 8 canaux
- Connecteur : header 24 broches D-Sub
- Alimentation : +5V ou +3V3 selon alimentation des pots

## Composants principaux
| Type | Denomination | Qte |
|------|-------------|-----|
| Potentiometre | RK09D1130C1B ou RK09L1140A5L (10 kOhm) | 8 |
| Connecteur | D-Sub 24 broches | 1 |
| Resistance pull-up | 4.7 kOhm | 8 |
| LED | Vert 5 mm | 8 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| AIN-1 a DIN-8 | Potentiometres P1..P8 |
| GND | Masse commune |
| +5V | Alimentation |

## Notes de montage et astuces DIY
- Verifier le cableage du curseur vers la broche AIN avant mise sous tension
- Deux variantes incluses : montage horizontal (1 pot et 2 pots) et montage vertical (1 pot)
- Fichiers 3D : Potars_V4.wrl (boitier), Potars_eurorack.step (montage Eurorack)

## Documentation de fabrication
- hardware/ : sources KiCad (Pot.kicad_pro, Pot-X2.kicad_pro, schematiques et PCB)
- hardware/3D/ : modeles 3D des potentiometres (.wrl, .step)
- production/ : Gerbers, BOM (Pot.csv), netlist (.xml), archives de fabrication
- Blog : [4X2-POTS-v0.2 sur ksir-diy.blogspot.com](https://ksir-diy.blogspot.com/)

---

Retro-ingenierie par l'equipe — GPL-3.0
