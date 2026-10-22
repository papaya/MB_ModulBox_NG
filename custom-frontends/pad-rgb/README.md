# pad-rgb — Carte pads retroeclaires RGB (DIN + WS2812 en cascade)


## Description
Carte de front-end integrant des pads (boutons sensibles) retroeclaires RGB (WS2812B) pour le declenchement d'evenements MIDI avec retour visuel couleur. Chaque pad genere un evenement MIDI sur le **bus DIN**, et l'eclairage RGB est commande par **une seule ligne de donnees WS2812** qui traverse la carte. Les **LED WS2812B sont adressables individuellement** : chaque pixel peut afficher sa propre couleur. La ligne de donnees traverse la chaine (câblage en serie) mais aucune limitation d'adressage.

📖 **Article de référence :** [4X2-PADS-RGB](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S — modèle PAD4X2.

> ⚠️ **Les LED WS2812B ne se connectent PAS sur le bus DOUT (74HC595).** Elles recoivent une ligne de donnees specifique d'une sortie WS2812 du **Core32F4** (`J4A` / `J4B`). Le bus DOUT (74HC595) est reserve aux LEDs standards non adressables.
>
> ⚠️ **Les 8 LED WS2812B sont en cascade** au niveau du cablage physique (chaine de donnees), mais **elles sont adressables individuellement**. Il est possible de commander chaque LED a une couleur differente.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](assets/Pad.png)

## Spécifications techniques
- 2 pads multi-contacts (`Pad x 4`) totalisant **8 contacts** -> 8 entrees DIN distinctes
- Éclairage RGB **WS2812-2020** (PLCC4 2.0 x 2.0 mm) : **8 LED en cascade série**
- Interface bus **DIN** (entrée des pads) via le module DIN (74HC165) sur `J8`/`J9` du Core
- 8 × condensateur de découplage 100 nF (0402) sur chaque LED
- Alimentation 5V dédiée pour les LED (consommation élevée, jusqu'à 20 mA/LED) — **ne pas alimenter via `J4A`/`J4B`**

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Pad multi-contacts | `Pad x 4` | 2 |
| LED RGB adressable | WS2812B (`LED_WS2812B-2020_PLCC4_2.0x2.0mm`) | 8 |
| Condensateur | C 100 nF 0402 | 8 |
| Connecteur | IDC Header 2x05 P2.54mm (`J1` = DIN, `J2` = entree LED, `J3` = sortie LED) | 3 |
| Vis de fixation | MountingHole 3 mm / 2.2 mm M2 | 18 |
| Symbole WS2812-2020 | `libs/symbols/` | 1 |
| Empreinte LED_WS2812-2020 | `libs/footprints/` | 1 |

## Brochage / Mapping MIDIbox NG

### `J1` — 8 entrees DIN (vers le module DIN 74HC165, chainage `J8`/`J9` du Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (contact du pad) |
| 2 | — | Non connectee |
| 3 | `J1-D7` | Pad **Sw2** |
| 4 | `J1-D6` | Pad **Sw2** |
| 5 | `J1-D5` | Pad **Sw2** |
| 6 | `J1-D4` | Pad **Sw2** |
| 7 | `J1-D3` | Pad **Sw1** |
| 8 | `J1-D2` | Pad **Sw1** |
| 9 | `J1-D1` | Pad **Sw1** |
| 10 | `J1-D0` | Pad **Sw1** |

> Chaque pad `Pad x 4` presente **4 contacts** : les 4 contacts du pad **Sw1** sont cables sur `D0`..`D3`, ceux du pad **Sw2** sur `D4`..`D7`. Le contact GND est commun (`J1` broche 1).
>
> Le niveau haut est assure par le pull-up 10 kΩ du module **DIN**.

### `J2` — entree de la cascade LED (vers la sortie WS2812 du Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse |
| 2 a 5, 7, 8, 9 | — | Non connectees |
| 6 | `D501-DI` | **DATA d'entree** de la cascade (vers `D501`) |
| 10 | +5V | Alimentation des LED |

### `J3` — sortie de la cascade LED (vers la carte suivante ou vers le Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse |
| 2 a 5, 7, 8, 9 | — | Non connectees |
| 6 | `D508-DO` | **DATA de sortie** de la cascade (depuis `D508`) |
| 10 | +5V | Alimentation des LED |

### Chaine WS2812
```
Core (J4A/J4B, WS2812)  ->  J2 (broche 6)  ->  D501 -> D502 -> ... -> D508  ->  J3 (broche 6)
```

| Broche | Signal | Destination |
|--------|--------|-------------|
| DATA | Donnee WS2812B (1 fil) | **Une sortie WS2812 du Core32F4** (`J4A` PB10 / PB11, `J4B` **PB6** = TIM4 (reference MIOS32) / `J4B` PB9) |
| +5V | Alimentation LEDs | Alimentation 5V externe (separee du Core) |
| GND | Masse commune | Masse commune Core + LEDs |

> Configuration .NGC : `WS2812_SUPPORTED 1`, sortie de reference sur `GPIOB, GPIO_Pin_6 (TIM4)`, pilote PWM + DMA. Voir [specifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).
>
> Le Core STM32F4 dispose en realite de **4 lignes WS2812** (les 4 lignes de `J4A`/`J4B`), chacune avec un pull-up 2,2 kΩ et une sortie en open-drain : plusieurs cascades peuvent donc fonctionner en parallele sur des lignes distinctes.

## Documentation de fabrication
- `hardware/` : sources KiCad (`Pad.*`)
- `hardware/3D/` : modèles 3D des pads (`.wrl`, `.STEP`)
- `libs/symbols/` : symbole `WS2812-2020.kicad_sym`
- `libs/footprints/` : empreinte `LED_WS2812-2020.kicad_mod`
- `production/` : fichiers de position (`.pos`), datasheet WS2812B

---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

🔋 **Gestion de la puissance** : La gestion de la puissance des LED est indispensable, j'ai paramétré les LED à 10% de puissance.
**Rétro-ingénierie par l'équipe — GPL-3.0**> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
