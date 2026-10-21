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


## Specifications techniques
- Faders (glissieres) pour controle continu MIDI
- Interface AIN (Analog Input) - voies analogiques
- Une voie AIN par fader (curseur vers broche AINx)
- Alimentation : +5V ou +3V3 selon les faders

## Composants principaux
| Type | Denomination | Qte |
|------|-------------|-----|
| Fader / glissiere | ALPS RA6020F ou equivalent | 1 ou 2 |
| Bouton/pommeau de fader | `ALPS Fader Knob.wrl` | 1 ou 2 |
| Connecteur IDC 2x05 vertical | `IDC-Header_2x05_P2.54mm_Vertical.wrl` | 1 |
| Connecteur | Header male vers bus AIN | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| AIN-x | Curseur du fader x |
| GND | Masse commune |
| +5V / +3V3 | Alimentation des faders |

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
