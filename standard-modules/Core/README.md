# Core — Cœur STM32F4 Core32F4 (MIDIbox NG)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

## Description
Cœur de contrôle du contrôleur MIDIbox NG. Basé sur le module **MBHP_CORE_STM32F4** de la plateforme MIDIbox (STM32F407G-DISC1), il gère le multiplexage des bus AIN, DIN et DOUT, ainsi que la communication USB/MIDI. Version de référence : **Core32f4_V0.1**.

📖 **Article de référence :** [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) sur le blog Ksir DIY'S.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](assets/Core-Core32F4.png)

## Spécifications techniques
- Microcontrôleur **STM32F407G-DISC1** (`IC4`, header de connexion) sur le connecteur `IC1` = **74HCT541** (buffer de niveau) et `IC2` = **74HC595**
- Gestion des bus **AIN** (SPI), **DIN** (74HC165), **DOUT** (74HC595)
- Communication **USB/MIDI**, slot **carte SD** (`J1`), interface **LCD** (`J15A`/`J15B`), **SPI 3,3 V** (`J16`), **CAN** (`J18`)
- **Ports WS2812 : 4 lignes** reparties sur `J4A` et `J4B` (voir ci-dessous)
- **Port AIN (SPI) : `J19`** — interface SPI 5 V vers les modules AINSER64/AINSER8 (MCP3208 + CD4051), 2 chip-selects

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| MCU | STM32F407G-DISC1 (header `IC4`) | 1 |
| Buffer de niveau | 74HCT541 (`ic1`) | 1 |
| Registre a decalage | 74HC595 (`IC2`) | 1 |
| Connecteur IDC | P2.54mm Vertical (`J4A`, `J4B`, `J5A`, `J5B`, `J8J9`, `J10A`, `J10B`, `J11E`, `J15A`, `J15B`, `J16`, `J19`) | 12 |
| Connecteur PinHeader | 2.54mm (`J2`, `J15S`, `J17`, `J18`) | 4 |
| Connecteur carte SD | `J1` | 1 |
| Résistance axiale | R7a/R7b/R8a/R8b (2,2 kΩ), R11/R13 (1 kΩ), R12 (10 kΩ), R33 (réseau 4×1 kΩ) | 8 |
| Capacité | C14, C15 (100 nF) | 2 |
| Trimpot | P1, P2 (10 kΩ — contraste et luminosité LCD) | 2 |
| Diode / transistor | D1 (1N4148), T1 (BC817-40) | 2 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 6 |

## Brochage / Mapping MIDIbox NG

### Connecteurs du Core STM32F4 (verifies dans le schema KiCad)
| Connecteur | Fonction | Destination |
|------------|----------|-------------|
| **`J8J9`** (IDC 2x05) | Bus **DIN** + bus **DOUT** | Modules DIN / DOUT en cascade (`SC`, `RC`, `/S0`) |
| **`J19`** (IDC 2x05) | Bus **AIN** (SPI 5 V) | Modules AINSER64 / AINSER8 (pots, faders) |
| **`J4A`** (IDC 2x05) | 2 lignes **WS2812** | LEDs RGB adressables |
| **`J4B`** (IDC 2x05) | 2 lignes **WS2812** | LEDs RGB adressables |
| **`J5A`** / **`J5B`** (IDC 2x05) | GPIO 3,3 V generalistes | Sorties RS232 / MIDI supplementaires |
| **`J10A`** / **`J10B`** (IDC 2x05) | GPIO 3,3 V generalistes | **Standard Control Surface (SCS)** — boutons et encodeurs |
| **`J15A`** / **`J15B`** (IDC 2x08) | Interface **LCD** | Afficheurs 2x20 / 2x40 (`J15S` selectionne 5 V ou 3,3 V) |
| **`J16`** (IDC 2x05) | **SPI 3,3 V** (DMA) | Carte SD, MBHP_ETH |
| **`J11E`** (IDC 2x05) | Entrees MIDI supplementaires | |
| **`J18`** (1x02) | **CAN** (TTL, MBNet) | |
| **`J17`** (1x02) | USB PWR | |
| **`J2`** (1x02) | USB PWR | |
| **`J1`** | Slot **carte SD** | |
| **`J15S`** (1x03) | Selection tension LCD | 5 V ou 3,3 V |

### `J8J9` — bus DIN + DOUT (IDC 2x05)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1, 2 | GND | Masse commune |
| 3, 4 | +5V | Alimentation 5 V des modules |
| 5 | `/PB14` | Signal (controle du buffer `ic1` = 74HCT541) |
| 6 | `J8J9-P6` | Sortie buffer (`ic1` pin 11) |
| 7, 8 | `J8J9-P7` | Horloge serie (`SC`) et latch — sortie et entree |
| 9, 10 | `J8J9-P9` / `J8J9-P10` | Latch (`RC`) et donnees (`/S0`) |

### `J19` — bus AIN / SPI (IDC 2x05)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1, 2 | GND | Masse |
| 3, 4 | +5V | Alimentation 5 V des modules AIN |
| 5 | `/PB4` | **SPI clock / selection** |
| 6 | `J19-P6` | Sortie buffer (`ic1` pin 15) |
| 7, 8 | `J19-P7` | SPI MOSI/MISO |
| 9, 10 | `J19-P9` / `J19-P10` | Chip-selects `RC1` / `RC2` |

> Conformement a [ucapps.de/mbhp_ainser64](https://www.ucapps.de/mbhp_ainser64.html), les modules AINSER64 se connectent **en parallele sur `J19`** et sont distingues par leurs **chip-selects** (`RC1`, `RC2`).

### `J4A` / `J4B` — les 4 lignes WS2812
Le Core32F4 expose **4 sorties WS2812** (et non une seule), chacune avec une resistance de pull-up de 2,2 kΩ vers +5 V (sortie en **open-drain**) :

| Connecteur | Broche | Signal GPIO | Resistance de pull-up | Usage MIOS32 |
|------------|--------|-------------|-----------------------|-------------|
| `J4A` | 6 | **PB10** | `R7a` (2,2 kΩ -> +5V) | ligne WS2812 libre |
| `J4A` | 8 | **PB11** | `R8a` (2,2 kΩ -> +5V) | ligne WS2812 libre |
| `J4B` | 6 | **PB6** | `R7b` (2,2 kΩ -> +5V) | **ligne de reference MIOS32** (`GPIOB, GPIO_Pin_6`, timer `TIM4`, PWM + DMA) |
| `J4B` | 8 | **PB9** | `R8b` (2,2 kΩ -> +5V) | ligne WS2812 libre |
| `J4A`/`J4B` | 1 a 5, 7, 9 | GND | — | Masse |
| `J4A`/`J4B` | 10 | +5V | — | Alimentation |

> La spec MIOS32 officielle ([midibox.org](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html)) utilise **PB6 sur `J4B`** comme sortie de reference (`WS2812_TIM_OUT_PORT GPIOB`, `WS2812_TIM_OUT_PIN GPIO_Pin_6`, `WS2812_TIM TIM4`), car « *ce pin a deja une resistance de pull-up de 2,2 kOhm sur la carte MBHP_CORE_STM32F4, necessaire pour tirer la sortie a 5 V (le pin est configure en open-drain)* ». Les 3 autres lignes existent sur le meme connecteur et sont utilisables de la meme facon.
>
> **Alimentation WS2812 :** le +5V des LED ne doit **PAS** etre pris sur `J4A`/`J4B` (jusqu'a 20 mA par LED RGB) : prevoir une **alimentation 5 V dediee** et une masse commune.

### `J10A` / `J10B` — GPIO generalistes (Standard Control Surface)
| Connecteur | Broche | Signal |
|------------|--------|--------|
| `J10A` | 1 | GND |
| `J10A` | 2 | +3V3 |
| `J10A` | 3 a 10 | PE8, PE9, PE10, PE11, PE12, PE13, PE14, PE15 |
| `J10B` | 1 | GND |
| `J10B` | 2 | +3V3 |
| `J10B` | 3 a 10 | PC13, PC14, PC15, PE2, PE4, PE5, PE6, PE7 |

> `J10A` est prevu pour la **Standard Control Surface (SCS)** : y brancher directement boutons et encodeurs, sans registre 74HC165. Voir `custom-frontends/surface-control/`.

## Documentation de fabrication
- `hardware/` : sources KiCad (`Core32F4.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions, zip

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Référence MIDIbox NG — GPL-3.0**
