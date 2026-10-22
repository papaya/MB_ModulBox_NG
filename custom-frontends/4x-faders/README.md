# 4x-faders — Carte faders / glissieres (AIN)
![3D quart](assets/3d%203quart.png)
## Description
Carte de front-end integrant des faders (glissieres) pour le controle continu de parametres MIDI (volume, filtre, effets, etc.). Chaque fader est lu sur une voie analogique independante via le bus AIN de l'ecosysteme MIDIbox NG.

Article de reference : [4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isometrique avec composants |
| 3D quart | `3d%203quart.png` | Vue 3D quart du PCB |

![3D top](assets/Fad_1.png)
![3D iso](assets/Fad_2.png)


## Spécifications techniques
- Faders (glissières) pour contrôle continu MIDI
- Interface AIN (Analog Input) — voies analogiques via AINSER64 sur J19 (SPI) du Core32F4
- Une voie AIN par fader (curseur vers broche AINx)
- Alimentation : +5V (fournie par le Core via J19)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Fader / glissière | ALPS RA6020F ou équivalent | 1 ou 2 |
| Bouton/pommeau de fader | `ALPS Fader Knob.wrl` | 1 ou 2 |
| Connecteur IDC 2x05 vertical | `IDC-Header_2x05_P2.54mm_Vertical.wrl` | 1 |
| Connecteur | Header mâle IDC 2x05 vers bus AIN | 1 |

## Brochage / Mapping MIDIbox NG

### Bus AIN — via module AINSER64 sur J19 (SPI) du Core32F4
| Broche | Signal | Description |
|--------|--------|-------------|
| AIN-x | Curseur du fader x | Lecture curseur (MCP3208 via CD4051) |
| GND | Masse commune | Référence 0V |
| +5V | Alimentation des faders | Alimentation (Vd) |

> Câblage des faders : les deux pattes externes se connectent à +5V (Vd) et GND (Vs). Le curseur (patte centrale) se connecte sur l'entrée AIN correspondante. Toutes les entrées AIN non utilisées doivent être reliées à la masse (GND).

## Documentation de fabrication
- hardware/ : sources KiCad (Fad_1.*, Fad_2.*)
- hardware/3D/ : modeles 3D des faders et boutons (.wrl)
- production/ : Gerbers pour Fad_1 et Fad_2
- Blog : [4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2 sur ksir-diy.blogspot.com](https://ksir-diy.blogspot.com/)

---

## Conception & Compatibilité

Carte d'interface originale conçue pour le système **MB MODULBOX NG**, compatible avec les bus et modules du système MIDIbox NG.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial.

Retro-ingenierie par l'equipe — GPL-3.0
