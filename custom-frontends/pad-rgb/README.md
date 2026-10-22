# pad-rgb — Carte pads rétroéclairés RGB (DIN + WS2812 sur Core J4B.SC)

## Description
Carte de front-end intégrant des pads (boutons sensibles) rétroéclairés RGB (WS2812B) pour le déclenchement d'événements MIDI avec retour visuel couleur. Chaque pad génère un événement MIDI sur le bus DIN, et l'éclairage RGB est piloté en **1 fil de données** directement sur le port **J4B.SC (PB6 / TIM4)** du Core STM32F4 (Core32F4), conformément au driver WS2812 de MIOS32.

📖 **Article de référence :** [4X2-PADS-RGB](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — modèle PAD4X2.

> ⚠️ **Erreur corrigée :** Les LEDs WS2812B ne se connectent **PAS** sur le bus DOUT (74HC595). Elles se connectent directement sur **J4B.SC (pin PB6)** du Core32F4. Le bus DOUT (74HC595) est réservé aux LEDs standards non adressables.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](assets/Pad.png)

## Spécifications techniques
- Pads tactiles (boutons sensibles) — 8 voies
- Éclairage RGB WS2812B (1 fil de données, adressable en chaîne)
- Pilotage LED : directement sur **J4B.SC (PB6 / TIM4)** du Core STM32F4 (driver WS2812 MIOS32)
- Interface bus DIN (entrée des pads) via module DIN (74HC165) sur J8/J9 du Core
- Alimentation 5V dédiée pour les LEDs (consommation élevée, jusqu'à 20 mA/LED) — **ne pas alimenter via J4B**

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Pads tactiles | — | 8 |
| LED RGB adressable | WS2812B | 8 |
| Connecteur DIN | Header mâle 2x05 (10 broches) vers module DIN | 1 |
| Connecteur WS2812B | 3 broches (Data, +5V, GND) vers J4B.SC du Core32 | 1 |
| Symbole WS2812-2020 | `libs/symbols/` | 1 |
| Empreinte LED_WS2812-2020 | `libs/footprints/` | 1 |

## Brochage / Mapping MIDIbox NG

### Bus DIN (pads) — via module DIN sur J8/J9 du Core32
| Broche | Signal |
|--------|--------|
| DIN-1 → DIN-8 | Pads P1..P8 |
| GND | Masse commune |
| +5V | Alimentation (pull-up) |

### Pilote WS2812B — directement sur J4B.SC du Core32F4 (PB6 / TIM4)
| Broche | Signal | Destination |
|--------|--------|-------------|
| DATA | Donnée WS2812B (1 fil) | **J4B.SC / PB6** du Core STM32F4 |
| +5V | Alimentation LEDs | Alimentation 5V externe (séparée du Core) |
| GND | Masse commune | Masse commune Core + LEDs |

> Configuration .NGC : `WS2812_SUPPORTED 1`, sortie sur `GPIOB, GPIO_Pin_6 (TIM4)`, pilote PWM + DMA. Voir [spécifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).

## Documentation de fabrication
- `hardware/` : sources KiCad (`Pad.*`)
- `hardware/3D/` : modèles 3D des pads (`.wrl`, `.STEP`)
- `libs/symbols/` : symbole `WS2812-2020.kicad_sym`
- `libs/footprints/` : empreinte `LED_WS2812-2020.kicad_mod`
- `production/` : fichiers de position (`.pos`), datasheet WS2812B

---

## Conception & Compatibilité

Carte d'interface originale conçue pour le système **MB MODULBOX NG**, compatible avec les bus et modules du système MIDIbox NG.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial.

**Rétro-ingénierie par l'équipe — GPL-3.0**
