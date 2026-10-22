# encoders-led-rgb — Carte encodeurs avec anneau LED RGB (DIN + WS2812 sur Core J4B.SC)

## Description
Carte de front-end intégrant des encodeurs rotatifs avec anneau LED RGB pour le contrôle de paramètres MIDI avec retour visuel (position, valeur, mode, etc.). Chaque encodeur génère des événements MIDI sur le bus DIN, et l'anneau LED RGB adressable est piloté en **1 fil de données** directement sur le port **J4B.SC (PB6 / TIM4)** du Core STM32F4 (Core32F4), conformément au driver WS2812 de MIOS32.

📖 **Article de référence :** [4X2 ENC-SW-16-LED-RING-RGB (PEC16)](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — modèles PEC16 et P el12T. ⚠️ Marqué « non terminé, ne fonctionne pas » sur le blog.

> ⚠️ **Erreur corrigée :** L'anneau LED WS2812 ne se connecte **PAS** sur le bus DOUT (74HC595). Il se connecte directement sur **J4B.SC (pin PB6)** du Core32F4. L'alimentation 5V des LEDs doit être fournie séparément (pas via J4B).

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
- Anneau LED RGB adressable (WS2812/Neopixel) — **1 fil de données**
- Pilotage LED : directement sur **J4B.SC (PB6 / TIM4)** du Core STM32F4 (driver WS2812 MIOS32)
- Interface bus DIN (entrée encodeur) via module DIN (74HC165) sur J8/J9 du Core
- Alimentation 5V dédiée pour les LEDs (consommation élevée, jusqu'à 20 mA/LED) — **ne pas alimenter via J4B**

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Encodeur rotatif | PEC16R (ou équivalent) | 1 |
| Bouton-poussoir (intégré) | — | 1 |
| LED RGB adressable | WS2812 | 1 anneau |
| Connecteur DIN | Header mâle 2x05 (10 broches) vers module DIN | 1 |
| Connecteur WS2812 | 3 broches (Data, +5V, GND) vers J4B.SC du Core32 | 1 |

## Brochage / Mapping MIDIbox NG

### Bus DIN (encodeur) — via module DIN sur J8/J9 du Core32
| Broche | Signal |
|--------|--------|
| DIN-1 | Phase A de l'encodeur (74HC165) |
| DIN-2 | Phase B de l'encodeur (74HC165) |
| DIN-3 | Bouton-poussoir de l'encodeur (74HC165) |
| GND | Masse commune |
| +5V | Alimentation (pull-up) |

### Pilote WS2812 — directement sur J4B.SC du Core32F4 (PB6 / TIM4)
| Broche | Signal | Destination |
|--------|--------|-------------|
| DATA | Donnée WS2812 (1 fil) | **J4B.SC / PB6** du Core STM32F4 |
| +5V | Alimentation LEDs | Alimentation 5V externe (séparée du Core) |
| GND | Masse commune | Masse commune Core + LEDs |

> Configuration .NGC : `WS2812_SUPPORTED 1`, sortie sur `GPIOB, GPIO_Pin_6 (TIM4)`, pilote PWM + DMA. Voir [spécifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).

## Documentation de fabrication
- `hardware/` : sources KiCad (`PEC_16_V0.2.*`)
- `hardware/3D/` : modèle 3D de l'encodeur (`.wrl`, `.step`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archives de fabrication
- `libs/` : symboles et empreintes spécifiques si non partagés

---

## Conception & Compatibilité

Carte d'interface originale conçue pour le système **MB MODULBOX NG**, compatible avec les bus et modules du système MIDIbox NG.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial.

**Rétro-ingénierie par l'équipe — GPL-3.0**
