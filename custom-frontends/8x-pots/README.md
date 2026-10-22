# 8x-pots — Carte 8 potentiomètres rotatifs (AIN)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

## Description
Module potentiometres rotatifs (8 canaux) pour le controle de parametres continus MIDI (volume, filtre, effets, etc.). Chaque potentiometre est lu sur une voie analogique independante. La carte ne contient **aucun convertisseur analogique-numerique** : elle expose 8 curseurs sur un connecteur IDC, relies au module **AINSER64** (MCP3208 + CD4051) du bus AIN.

Article de reference : [4X2-POTS-v0.2](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — potentiometres RK09D1130C1B ou RK09L1140A5L.

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

## Specifications techniques
- 8 potentiometres rotatifs (10 kOhm), empreinte `RK09L and RK09D`
- **Tension de reference : +3V0** (et non +5V) — la borne `+3V0` alimente les deuxextremites de chaque potentiometre
- Sortie : 8 curseurs + GND + +3V0 sur un connecteur **IDC 2x05 P2.54mm** (`J1`)
- Lecture : via le module **AINSER64** du bus AIN (broche `J19` du Core32F4, SPI)
- Aucune resistance, aucun condensateur, aucun circuit actif sur la carte

## Composants principaux
| Type | Denomination | Qte |
|------|-------------|-----|
| Potentiometre rotatif | RK09D1130C1B / RK09L1140A5L (10 kOhm) | 8 |
| Connecteur | IDC Header 2x05 P2.54mm Vertical (`J1`) | 1 |
| Vis de fixation | MountingHole 3.2mm M3 | 6 |

> Il n'y a **pas de LED sur cette carte** (les versions antérieures de cette page en mentionnaient 8 : ce sont les voyants integres aux boutons/potentiometres, absents du schema KiCad).

## Brochage / Mapping MIDIbox NG

### Connecteur `J1` — vers module AINSER64 (bus AIN, `J19` du Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (reference 0 V) |
| 2 | +3V0 | Alimentation des potentiometres (borne haute) |
| 3 | `J1-A0` | Curseur du potentiometre **pot2** |
| 4 | `J1-A1` | Curseur du potentiometre **pot1** |
| 5 | `J1-A2` | Curseur du potentiometre **pot3** |
| 6 | `J1-A3` | Curseur du potentiometre **pot6** |
| 7 | `J1-A4` | Curseur du potentiometre **pot4** |
| 8 | `J1-A5` | Curseur du potentiometre **pot7** |
| 9 | `J1-A6` | Curseur du potentiometre **pot5** |
| 10 | `J1-A7` | Curseur du potentiometre **pot8** |

> **Cablage du potentiometre (verifie dans le schema KiCad)** : patte 1 -> GND, patte 2 -> **curseur** (-> broche `J1` correspondante), patte 3 -> **+3V0**.
>
> Le curseur etant relie a l'entree analogique de l'AINSER64, la plage de mesure est **0 .. 3,0 V** (et non 0 .. 5 V). L'AINSER64 (ADC MCP3208 12 bits) mesure donc 0..3 V avec une resolution effective d'environ 10 bits.
>
> **Les entrees analogiques non utilisees de l'AINSER64 doivent etre reliees a la masse**, sinon l'application emet des valeurs aleatoires.

### Module AINSER64 (rappel)
- Connecteur : **`J19`** du Core STM32F4 (SPI, 2 chip-selects `RC1`/`RC2`)
- Architecture : 1 × **MCP3208** (ADC 12 bits) + 8 × **CD4051** (multiplexeurs 8:1) + 1 × 74HC595
- Capacite : 64 entrees par module, jusqu'a 2 modules (128 voies) supportes par MIDIbox NG
- Les 8 entrees de chaque connecteur `J6`..`J13` de l'AINSER64 disposent de **+5V et GND** dedies ; si la tension de reference de 3,0 V est souhaitee, alimenter les potentiometres separement (c'est le cas ici : +3V0 local a la carte)

## Variante `Pot-X2` (montage 4x2)
- `hardware/Pot-X2.kicad_pcb` : variante **2 plaques de 4 potentiometres** empilees (41 empreintes)
- ⚠️ **Cette variante n'a pas de schema KiCad associe** et contient des empreintes non annotees (`REF**`) ainsi que 10 pads non connectes : elle est fournie **pour reference**, a verifier avant fabrication
- Le schema `Pot.kicad_sch` correspond a la variante **verticale** (8 potentiometres sur une plaque)

## Notes de montage et astuces DIY
- Verifier le cablage du curseur vers la broche `J1` avant mise sous tension
- Les potentiometres sont sur la carte verticale ; l'empilement 4x2 (`Pot-X2`) est mecaniquement separe
- Fichiers 3D : Potars_V4.wrl (boitier), Potars_eurorack.step (montage Eurorack)

## Documentation de fabrication
- `hardware/` : sources KiCad (`Pot.kicad_pro`, `Pot.kicad_sch`, `Pot.kicad_pcb`, + variante `Pot-X2.kicad_pcb`)
- `hardware/3D/` : modeles 3D des potentiometres (.wrl, .step)
- `production/` : Gerbers, BOM (Pot.csv), netlist (.xml), archives de fabrication
- Blog : [4X2-POTS-v0.2 sur ksir-diy.blogspot.com](https://ksir-diy.blogspot.com/)

---

## Conception & Compatibilite

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du systeme MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Licence & Usage :** Ces fichiers hardware sont partages sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du cablage ou du routage.

Retro-ingenierie par l'equipe — GPL-3.0

