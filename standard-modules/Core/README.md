# Core — Cœur STM32F4 Core32F4 (MIDIbox NG)

## Description
Cœur de contrôle du contrôleur MIDIbox NG. Basé sur STM32F4, il gère le multiplexage des bus AIN, DIN et DOUT, ainsi que la communication USB/MIDI. Version de référence : Core32f4_V0.1.

📖 **Article de référence :** [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) sur le blog Ksir DIY'S.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](assets/Core-Core32F4.png)

## Spécifications techniques
- Microcontrôleur STM32F4 (Core32F4)
- Gestion des bus AIN, DIN, DOUT
- Communication USB/MIDI
- Connecteurs pour modules d'extension
- **Port WS2812 (LED strip adressable) :** J4B.SC = PB6 / TIM4 (GPIO_Pin_6) — 1 fil de données, pilote PWM + DMA via driver MIOS32
- **Port AIN (SPI) :** J19 — interface SPI vers modules AINSER64/AINSER8 (MCP3208 + CD4051), 2 chip selects (RC1, RC2)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| MCU | STM32F4 | 1 |
| Connecteur IDC | P2.54mm Vertical | 12 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 6 |
| Connecteur PinHeader | 2.54mm | 4 |
| Résistance axiale | R_Axial_DIN0204 | 8 |
| Capacité | Capacitor_THT | 2 |
| Boîtier DIP | DIP-16 / DIP-20 | plusieurs |
| Empreinte ksir | varie | 1 |

## Brochage / Mapping MIDIbox NG

### Connecteurs du Core STM32F4
| Connecteur | Signal | Destination |
|------------|--------|-------------|
| **J8 / J9** | Bus DIN (74HC165) + Bus DOUT (74HC595) | Modules DIN/DOUT en cascade |
| **J19** | Bus AIN (SPI) | Modules AINSER64 / AINSER8 (pots, faders) |
| **J4B.SC** | WS2812 data (PB6 / TIM4) | LEDs RGB adressables (1 fil de données) |
| **USB** | Communication MIDI vers hôte | Port USB Micro-B du Core |

> Alimentation WS2812 : le +5V des LEDs doit être fourni séparément (pas via J4B). Chaque RGB LED peut consommer jusqu'à 20 mA.

## Documentation de fabrication
- `hardware/` : sources KiCad (`Core32F4.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions, zip

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue.

**Référence MIDIbox NG — GPL-3.0**