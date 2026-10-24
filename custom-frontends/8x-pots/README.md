# 8x-pots — Module custom 8 potentiomètres rotatifs (AIN)
![Pot 4x2](assets/pot4x2.png)

## Description

Module potentiomètres rotatifs (8 canaux) pour le contrôle de paramètres continus MIDI (volume, filtre, effets, etc.). Chaque potentiomètre est lu sur une voie analogique indépendante. La carte ne contient **aucun convertisseur analogique-numérique** : elle expose 8 curseurs sur un connecteur IDC, reliés au module **AINSER64** (MCP3208 + CD4051) du bus AIN.


## Spécifications techniques

- 8 potentiomètres rotatifs (10 kΩ), empreinte `RK09L and RK09D`
- **Tension de référence : +3V0** (et non +5V) — la borne `+3V0` alimente les deux extrémités de chaque potentiomètre
- Sortie : 8 curseurs + GND + +3V0 sur un connecteur **IDC 2x05 P2.54mm** (`J1`)
- Lecture : via le module **AINSER64** du bus AIN (broche `J19` du Core32F4, SPI)
- Aucune résistance, aucun condensateur, aucun circuit actif sur la carte

![Screenshot](assets/Screenshot%202023-05-19%20153745.png)

## Composants principaux

| Type | Dénomination | Qté |
|------|-------------|-----|
| Potentiomètre rotatif | RK09D1130C1B / RK09L1140A5L (10 kΩ) | 8 |
| Connecteur | IDC Header 2x05 P2.54mm Vertical (`J1`) | 1 |
| Vis de fixation | MountingHole 3.2mm M3 | 6 |

> Il n'y a **pas de LED sur cette carte**
## Brochage / Mapping MIDIbox NG
![3D top](assets/Pot_Botoom.png)
### Connecteur `J1` — vers module AINSER64 (bus AIN, `J19` du Core)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (référence 0 V) |
| 2 | +3V0 | Alimentation des potentiomètres (borne haute) |
| 3 | `J1-A0` | Curseur du potentiomètre **pot2** |
| 4 | `J1-A1` | Curseur du potentiomètre **pot1** |
| 5 | `J1-A2` | Curseur du potentiomètre **pot3** |
| 6 | `J1-A3` | Curseur du potentiomètre **pot6** |
| 7 | `J1-A4` | Curseur du potentiomètre **pot4** |
| 8 | `J1-A5` | Curseur du potentiomètre **pot7** |
| 9 | `J1-A6` | Curseur du potentiomètre **pot5** |
| 10 | `J1-A7` | Curseur du potentiomètre **pot8** |

> **Câblage du potentiomètre (vérifié dans le schéma KiCad)** : patte 1 → GND, patte 2 → **curseur** (→ broche `J1` correspondante), patte 3 → **+3V0**.

> Le curseur étant relié à l'entrée analogique de l'AINSER64, la plage de mesure est **0 .. 3,0 V** (et non 0 .. 5 V). L'AINSER64 (ADC MCP3208 12 bits) mesure donc 0..3 V avec une résolution effective d'environ 10 bits.

> **Les entrées analogiques non utilisées de l'AINSER64 doivent être reliées à la masse**, sinon l'application émet des valeurs aléatoires.

### Module AINSER64 (rappel)

- Connecteur : **`J19`** du Core STM32F4 (SPI, 2 chip-selects `RC1`/`RC2`)
- Architecture : 1 × **MCP3208** (ADC 12 bits) + 8 × **CD4051** (multiplexeurs 8:1) + 1 × 74HC595
- Capacité : 64 entrées par module, jusqu'à 2 modules (128 voies) supportés par MIDIbox NG
- Les 8 entrées de chaque connecteur `J6`..`J13` de l'AINSER64 disposent de **+5V et GND** dédiés ; si la tension de référence de 3,0 V est souhaitée, alimenter les potentiomètres séparément (c'est le cas ici : +3V0 local à la carte)

## Variante `Pot-X2` (montage 4x2)

- `hardware/Pot-X2.kicad_pcb` : variante **2 plaques de 4 potentiomètres** empilées (41 empreintes)
- ⚠️ **Cette variante n'a pas de schéma KiCad associé** et contient des empreintes non annotées (`REF**`) ainsi que 10 pads non connectés : elle est fournie **pour référence**, à vérifier avant fabrication
- Le schéma `Pot.kicad_sch` correspond à la variante **verticale** (8 potentiomètres sur une plaque)

## Notes de montage et astuces DIY

- Vérifier le câblage du curseur vers la broche `J1` avant mise sous tension
- Les potentiomètres sont sur la carte verticale ; l'empilement 4x2 (`Pot-X2`) est mécaniquement séparé
- Fichiers 3D : Potars_V4.wrl (boîtier), Potars_eurorack.step (montage Eurorack)

## Documentation de fabrication

- `hardware/` : sources KiCad (`Pot.kicad_pro`, `Pot.kicad_sch`, `Pot.kicad_pcb`, + variante `Pot-X2.kicad_pcb`)
- `hardware/3D/` : modèles 3D des potentiomètres (`.wrl`, `.step`)
- `production/` : Gerbers, BOM (Pot.csv), netlist (`.xml`), archives de fabrication
- Blog : [4X2-POTS-v0.2 sur ksir-diy.blogspot.com](https://ksir-diy.blogspot.com/)
## Assets de visualisation

| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |
| Pot 4x2 | `pot4x2.png` | Vue du montage 4x2 pots |
| Screenshot | `Screenshot%202023-05-19%20153745.png` | Capture d'écran du design |


---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Origine et usage :** conception originale MB MODULBOX NG, prévue pour le DIY/personnel. Aucune licence formelle n'est publiée dans le dépôt ; voir le README racine. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
