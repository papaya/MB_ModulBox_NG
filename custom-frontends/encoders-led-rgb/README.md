# encoders-led-rgb — Carte 8 encodeurs PEC16 + 128 LED WS2812 (DIN + WS2812)
![Screenshot](assets/Screenshot%202023-05-19%20175512.png)

## Description
Carte de front-end integrant **8 encodeurs rotatifs avec poussoir** (PEC16) et **128 LED RGB adressables WS2812** (anneaux lumineux). Chaque encodeur genere des evenements MIDI via le **bus DIN**, et l'eclairage est commande par **une ligne de donnees WS2812**, les 128 LED etant **cascadees en serie**.
Se compose de 3 PCB;
un pcb avec les leds
un pcb avec les encodeurs
un pcb pour les connecteurs
un front panel en aluminium 
des diffuseur de lumiere translucide imprimé en 3d
des masque de lumiere imprimé en 3d noir pour empecher la lumiére de se diffuser ailleur  
📖 **Article de référence :** [4X2 ENC-SW-16-LED-RING-RGB (PEC16)](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — modèles PEC16 fonctionne, déja testé!

> ⚠️ Attention a la consomation des leds , j'ai baissé la luminosité a entre 5 et 10 % pour garder une consomation limité (entre 0,5 et 1 A sur la consomation totale du controleur)
> ⚠️ **Les LED WS2812 ne se connectent PAS sur le bus DOUT (74HC595).** Elles recoivent une ligne de donnees specifique d'une sortie WS2812 du **Core32F4** (`J4A` / `J4B`). L'alimentation 5V des LED doit etre fournie **separement** (pas via `J4A`/`J4B`).
>
> **Les 128 LED WS2812 sont en cascade** au niveau du cablage physique (chaine de donnees),  **elles sont adressables individuellement**. Il est possible de commander chaque LED a une couleur differente.


![PcbConnexionBottom](assets/connect%20board%20bottom.png)

## Spécifications techniques
- **8 encodeurs rotatifs avec poussoir integre** — PEC16 (`PEC16-4XXXF-SXXXX`, empreinte `PEC164120FS0012`) : 2 sorties de phase (A, B) + 1 poussoir
- **24 entrees DIN** au total (8 × A, 8 × B, 8 × poussoir), reparties sur 3 connecteurs `J11`, `J12`, `J13`
- **128 × WS2812-2020** (PLCC4 2.0 × 2.0 mm) en **cascade serie** unique : `J4` -> D1 -> D2 -> ... -> D128 -> `J5`
- 128 × condensateur de decoupling 100 nF sur chaque LED
- **Aucune resistance de pull-up sur la carte** : le pull-up 10 kΩ est porte par le module **DIN** (74HC165)
- 2 alimentations distinctes : `+5VA` (analogique, `J44`) et `+5VD` (digitale, `J45`)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Encodeur rotatif a poussoir | PEC16 (`PEC164120FS0012`) | 8 |
| LED RGB adressable | WS2812B (`LED_WS2812B-2020_PLCC4_2.0x2.0mm`) | 128 |
| Condensateur | C 100 nF | 128 |
| Connecteur DIN | IDC Header 2x05 (`J11`, `J12`, `J13`) | 3 |
| Connecteur WS2812 | PinSocket 1x03 (`J4` entree, `J5` sortie) | 2 |
| Connecteur alimentation | IDC 2x05 (`J44` = +5VA, `J45` = +5VD) | 2 |
| Connecteurs de report | PinHeader / PinSocket 1x03 et 1x06 (`J14`, `J15`, `J20`-`J25`, `J30`-`J35`) | 18 |


## Brochage / Mapping MIDIbox NG

### `J11` — poussoirs des encodeurs (8 entrees DIN) Se connecte sur carte DIN 
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune |
| 2 | — | Non connectee |
| 3 | `C_SW8` | Poussoir de l'encodeur **8** |
| 4 | `C_SW7` | Poussoir de l'encodeur **7** |
| 5 | `C_SW6` | Poussoir de l'encodeur **6** |
| 6 | `C_SW5` | Poussoir de l'encodeur **5** |
| 7 | `C_SW4` | Poussoir de l'encodeur **4** |
| 8 | `C_SW3` | Poussoir de l'encodeur **3** |
| 9 | `C_SW2` | Poussoir de l'encodeur **2** |
| 10 | `C_SW1` | Poussoir de l'encodeur **1** |

### `J12` — phases B/A des encodeurs 5 a 8 Se connecte sur carte DIN 
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune |
| 2 | — | Non connectee |
| 3 | `C_ENC8B` | Phase B encodeur **8** |
| 4 | `C_ENC8A` | Phase A encodeur **8** |
| 5 | `C_ENC7B` | Phase B encodeur **7** |
| 6 | `C_ENC7A` | Phase A encodeur **7** |
| 7 | `C_ENC6B` | Phase B encodeur **6** |
| 8 | `C_ENC6A` | Phase A encodeur **6** |
| 9 | `C_ENC5B` | Phase B encodeur **5** |
| 10 | `C_ENC5A` | Phase A encodeur **5** |

### `J13` — phases B/A des encodeurs 1 a 4 Se connecte sur carte DIN 
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune |
| 2 | — | Non connectee |
| 3 | `C_ENC4B` | Phase B encodeur **4** |
| 4 | `C_ENC4A` | Phase A encodeur **4** |
| 5 | `C_ENC3B` | Phase B encodeur **3** |
| 6 | `C_ENC3A` | Phase A encodeur **3** |
| 7 | `C_ENC2B` | Phase B encodeur **2** |
| 8 | `C_ENC2A` | Phase A encodeur **2** |
| 9 | `C_ENC1B` | Phase B encodeur **1** |
| 10 | `C_ENC1A` | Phase A encodeur **1** |

> Les encodeurs sont raccordes aux connecteurs de report `J30`..`J35` (1x06), qui reprennent les memes signaux `C_SWx`, `C_ENCxA`, `C_ENCxB` pour le routage physique vers les encodeurs.
>
> Les phases A/B constituent les **entrees d'un compteur de quadrature** : elles sont branchees sur deux entrees consecutives d'un registre **74HC165** du module DIN. Les poussoirs, eux, sont des contacts **vers GND**.

### `J4` / `J5` — cascade WS2812 J4 Se connecte sur j4b du core32f4 ou sur J5 du module precedent
| Connecteur | Broche | Signal | Description |
|------------|--------|--------|-------------|
| `J4` | 1 | +5V | Alimentation des LED |
| `J4` | 2 | `D1-DI` | **DATA d'entree** de la cascade (vers `D1`) |
| `J4` | 3 | GND | Masse |
| `J5` | 1 | +5V | Alimentation des LED |
| `J5` | 2 | `D128-DO` | **DATA de sortie** de la cascade (depuis `D128`) |
| `J5` | 3 | GND | Masse |

```
Core (J4A/J4B, WS2812)  ->  J4 (broche 2)  ->  D1 -> D2 -> ... -> D128  ->  J5 (broche 2)
```

### `J44` / `J45` — alimentations
| Connecteur | Broche | Signal | Description |
|------------|--------|--------|-------------|
| `J44` | 1 | GND | Masse analogique (`GNDA`) |
| `J44` | 6 | `J34-Pin_2` | Report vers `J34` |
| `J44` | 10 | +5VA | Alimentation **analogique** |
| `J45` | 1 | GND | Masse analogique (`GNDA`) |
| `J45` | 6 | `J35-Pin_2` | Report vers `J35` |
| `J45` | 10 | +5VD | Alimentation **digitale** |

### Chaine WS2812 du Core
- Le Core STM32F4 dispose de **4 lignes WS2812** (`J4A` PB10 / PB11, `J4B` **PB6** = TIM4 (reference MIOS32) / `J4B` PB9), chacune avec un pull-up 2,2 kΩ et une sortie en open-drain.
- **L'alimentation +5V des LED doit etre fournie separement** (jusqu'a 20 mA par LED RGB, soit 2,5 A pour 128 LED a pleine luminosite). Voir [specifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).
- Avec 128 LED en cascade sur une seule ligne, la longueur de piste et le nombre de LED restent dans les limites du protocole WS2812, mais **le routage de la carte presente 315 violations DRC** : a verifier avant fabrication.

## Documentation de fabrication
- `hardware/` : schéma historique global et PCB restauré (`PEC_16_V0.2.*`)
- `control-board/`, `encoders-board/`, `led-ring/` : PCB distincts, chacun documenté dans son dossier
- `production/` : BOM, positions et netlist uniquement ; aucun Gerber de sous-carte n'est versionné
- `mechanical/` : emplacement documentaire des sources de façade, absentes de l'inventaire local
- `libs/` : symboles et empreintes spécifiques si non partagés

### État de la séparation en trois cartes

Les PCB de la Control Board, de l'Encoders Board et du LED Ring existent déjà dans trois sous-dossiers. En revanche, les sous-projets ne sont pas encore autonomes : aucun ne dispose d'un schéma indépendant vérifié, les exports de fabrication ne sont pas séparés par PCB, et des configurations KiCad orphelines subsistent. Le schéma `hardware/PEC_16_V0.2.kicad_sch` reste la référence historique de l'ensemble ; il n'a pas été dupliqué artificiellement en trois schémas qui ne correspondraient pas aux cartes.

Les modèles STEP/WRL locaux ne sont pas versionnés et certaines références de modèles dans les PCB sont des chemins absolus Windows. Voir [`docs/interconnect.md`](docs/interconnect.md) et [`mechanical/README.md`](mechanical/README.md) avant de s'appuyer sur les rendus 3D ou l'assemblage.

---

![facade](assets/facade%20edge%20cut.png)

![entretoise](assets/ENC-PLASTIQUE-noir-v2.png)

![diffuseur](assets/ENC-PLASTIQUE-transparent.png)

![leds3q](assets/leds_3Quart.png)

![enc3q](assets/En_3Quart.png)

![conect3Q](assets/connect%20board%203Quart.png)

![Photo](assets/IMG_20230708_111915.jpg)

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Origine et usage :** conception originale MB MODULBOX NG, prévue pour le DIY/personnel. Aucune licence formelle n'est publiée dans le dépôt ; voir le README racine. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

🔋 **Gestion de la puissance** : La gestion de la puissance des LED est indispensable, j'ai paramétré les LED à 10% de puissance.
Conception originale MB MODULBOX NG. > ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
