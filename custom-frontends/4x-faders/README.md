# 4x-faders — Carte faders / glissières (AIN)

## Description
Carte de front-end intégrant des faders (glissières) pour le contrôle continu de paramètres MIDI (volume, filtre, effets, etc.). Chaque fader est lu sur une voie analogique indépendante via le bus AIN de l'écosystème MIDIbox NG.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/4x-faders/Fad_1.png)
![3D iso](docs/assets/frontends/4x-faders/Fad_2.png)

## Spécifications techniques
- Faders (glissières) pour contrôle continu MIDI
- Interface AIN (Analog Input) — voies analogiques
- Une voie AIN par fader (curseur vers broche AINx)
- Alimentation : +5V ou +3V3 selon les faders

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Fader / glissière | ALPS RA6020F ou équivalent | 1 ou 2 |
| Bouton/pommeau de fader | `ALPS Fader Knob.wrl` | 1 ou 2 |
| Connecteur IDC 2x05 vertical | `IDC-Header_2x05_P2.54mm_Vertical.wrl` | 1 |
| Connecteur | Header mâle vers bus AIN | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| AIN-x | Curseur du fader x |
| GND | Masse commune |
| +5V / +3V3 | Alimentation des faders |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Fad_1.*`, `Fad_2.*`)
- `hardware/3D/` : modèles 3D des faders et boutons (`.wrl`)
- `production/` : Gerbers pour Fad_1 et Fad_2

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
