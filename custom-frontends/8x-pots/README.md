# 8x-pots — Carte 8 potentiomètres rotatifs (AIN)

## Description
Module potentiometres rotatifs (8 canaux) pour le controle de parametres continus MIDI (volume, filtre, effets, etc.). Chaque potentiometre est lu sur une voie analogique independante et connectee au bus AIN de l'ecosysteme MIDIbox NG.

Article de reference : [4X2-POTS-v0.2](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — utilise des potentiometres RK09D1130C1B ou RK09L1140A5L.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isometrique avec composants |
| Pot 4x2 | `pot4x2.png` | Vue du montage 4x2 pots |
| Screenshot | `Screenshot%202023-05-19%20153745.png` | Capture d'ecran du design |

![3D top](assets/Pot.png)
![3D iso](assets/Pot-X2.png)
![Pot 4x2](assets/pot4x2.png)
![Screenshot](assets/Screenshot%202023-05-19%20153745.png)

## Spécifications techniques
- 8 potentiomètres rotatifs (10 kOhm)
- Interface AIN (Analog Input) — 8 canaux via AINSER64 sur J19 (SPI) du Core32F4
- Connecteur : header IDC 2x05 P2.54mm (10 broches)
- Alimentation : +5V (fournie par le Core via J19)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Potentiomètre | RK09D1130C1B ou RK09L1140A5L (10 kOhm) | 8 |
| Connecteur | IDC Header 2x05 P2.54mm Vertical | 1 |
| LED | Vert 5 mm | 8 |

## Brochage / Mapping MIDIbox NG

### Bus AIN — via module AINSER64 sur J19 (SPI) du Core32F4
| Broche | Signal | Description |
|--------|--------|-------------|
| AIN-1 → AIN-8 | Potentiomètres P1..P8 | Lecture curseur (MCP3208 via CD4051) |
| GND | Masse commune | Référence 0V |
| +5V | Alimentation | Alimentation des pots (Vd) |

> Câblage des pots : les deux pattes externes du potentiomètre se connectent à +5V (Vd) et GND (Vs). Le curseur (patte centrale) se connecte sur l'entrée AIN correspondante (A0..A7). Tous les entrées AIN non utilisées doivent être reliées à la masse (GND) pour éviter des valeurs aléatoires.

> Configuration : jusqu'à 64 voies analogiques par module AINSER64, jusqu'à 2 modules (128 pots) supportés par MIDIbox NG.

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

## Conception & Compatibilité

Carte d'interface originale conçue pour le système **MB MODULBOX NG**, compatible avec les bus et modules du système MIDIbox NG.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial.

Retro-ingenierie par l'equipe — GPL-3.0
