# Bus MIDIbox NG — Schéma de principe et brochage

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles**. À vos risques et périls.

## Présentation

L'ecosysteme MIDIbox NG repose sur trois bus principaux qui interconnectent le **Core** (STM32F4) aux **front-ends** (cartes de controle physiques) :

| Bus | Rôle | Direction | Connecteur typique |
|-----|------|-----------|-------------------|
| **AIN** | Analog Input — lecture de potentiels (potentiomètres, faders, capteurs) | Core → Front-end | **IDC 2x05** vers `J19` (SPI) |
| **DIN** | Digital Input — lecture d'etats logiques (boutons, switchs, encodeurs) | Front-end → Core | **IDC 2x05** (`J1`..`J6` du module DIN) |
| **DOUT** | Digital Output — pilotage d'actionneurs (**LEDs standards non adressables**, afficheurs 7 segments, relais) | Core → Front-end | **IDC 2x05** (`J1`..`J6` du module DOUT) |

> ℹ️ Les **connecteurs AIN/DIN/DOUT sont des IDC 2x05** (10 broches, pas 2,54 mm), et non des connecteurs D-Sub 24 broches.

---

## Schéma de principe des connexions

```
        ┌─────────────┐
        │   CORE      │  STM32F4 (Core32F4)
        │  (Core32F4) │
        └──────┬──────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌───────┐  ┌───────┐  ┌───────┐
│  AIN  │  │  DIN  │  │  DOUT │
│ Bus   │  │  Bus  │  │  Bus  │
│(64ch) │  │(32ent)│  │(32srt)│
└────┬──┘  └────┬──┘  └────┬──┘
     │          │          │
     ▼          ▼          ▼
┌───────┐  ┌───────┐  ┌───────┐
│8x-pots│  │8x-btns│  │8x-btns│
│4x-fad │  │key-4x2│  │(LEDs) │
│Car.puiss│ │enc-led │  │       │
└───────┘  └───────┘  └───────┘
                  │
                  ▼
         ┌──────────────────┐
         │ WS2812 (J4A/J4B) │  ← ligne de données 1 fil
         │  + alim 5V dédiée │
         └──────────────────┘
```

> Le **DOUT** ne pilote **jamais** de LED RGB WS2812 : celles-ci recoivent une ligne de donnees dediee d'une sortie WS2812 du Core (`J4A` / `J4B`).

---

## Brochage détaillé des connecteurs de bus

### Bus AIN (Analog Input) — connecteur IDC 2x05
Brochage **côté front-end** (carte de pots ou de faders) :

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (reference 0 V) |
| 2 | +3V0 ou +5V | Alimentation des potentiometres (selon la carte) |
| 3 a 10 | A0 .. A7 | Curseurs des potentiometres / faders |

> ⚠️ Les cartes `8x-pots` et `4x-faders` de ce depot alimentent leurs potentiometres en **+3V0** : la plage de mesure de l'AINSER64 est alors **0 .. 3,0 V**.
>
> Le **module AINSER64** (MCP3208 + 8 × CD4051) se branche sur **`J19`** du Core (SPI, 2 chip-selects). Les entrees analogiques non utilisees doivent etre **reliees a la masse**.

### Bus DIN (Digital Input) — connecteur IDC 2x05 (côté front-end)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (contact du bouton) |
| 2 | — | Non connectee |
| 3 a 10 | DIN-0 .. DIN-7 | Entrees digitales |

> Le **pull-up 10 kΩ** est porte par le **module DIN** (74HC165), **pas** par les front-ends.

### Bus DOUT (Digital Output) — connecteur IDC 2x05 (côté front-end)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (cathode des LED) |
| 2 | — | Non connectee |
| 3 a 10 | DOUT-0 .. DOUT-7 | Sorties digitales (deja limitees a 220 Ω sur le module) |

> La **resistance de 220 Ω** est portee par le **module DOUT** (74HC595), **pas** par les front-ends.
>
> Attention a l'ordre historique : la **premiere LED est sur D7** d'un connecteur DOUT, alors que la **premiere entree est sur D0** d'un connecteur DIN.

### Chaine WS2812 (hors DOUT)
| Broche | Signal | Destination |
|--------|--------|-------------|
| DATA | Donnee WS2812 (1 fil) | Sortie WS2812 du Core : `J4A` broche 6 (PB10), `J4A` broche 8 (PB11), `J4B` broche 6 (**PB6** = TIM4, reference MIOS32), `J4B` broche 8 (PB9) |
| +5V | Alimentation LED | Alimentation 5 V **dediee** (20 mA par LED RGB) |
| GND | Masse commune | Masse commune Core + LED |

---

## Règles de câblage

1. **Masse commune :** Tous les GND des front-ends doivent être reliés à la masse du Core.
2. **Alimentation :** +5V distribué sur tous les bus ; les front-ends à forte consommation (LEDs RGB WS2812B) prévoient une **alimentation 5V dédiée séparée** (pas via `J4A`/`J4B` du Core).
3. **LEDs WS2812B :** Se connectent en **1 fil de données sur une sortie WS2812 du Core32F4** (`J4A` / `J4B`) — **PAS** sur le bus DOUT (74HC595). Voir [spécifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).
4. **Longueur des câbles :** Maintenir les câbles de bus courts (< 50 cm) pour éviter les parasitage sur l'AIN.
5. **Déclenchement :** Les entrées DIN utilisent un pull-up **10 kΩ** porté par le module DIN.
6. **Cascade des modules :** un module DIN se branche sur `J1` (Core `J9`) et se prolonge via `J2` ; idem pour le DOUT (`J1` / `J2`).

---

## Liens vers les front-ends

| Front-end | Bus utilisé | Dossier |
|-----------|-------------|---------|
| 4x-faders | AIN | `custom-frontends/4x-faders/` |
| 8x-pots | AIN | `custom-frontends/8x-pots/` |
| 8x-buttons | DIN + DOUT | `custom-frontends/8x-buttons/` |
| encoders-led-rgb | DIN + WS2812 | `custom-frontends/encoders-led-rgb/` |
| pad-rgb | DIN + WS2812 | `custom-frontends/pad-rgb/` |
| keysw-4x2 | DIN + WS2812 | `custom-frontends/keysw-4x2/` |
| oled-128x64 | SPI (hors bus MIDIbox) | `custom-frontends/oled-128x64/` |
| carte-puissance | distribution 5 V / GND | `custom-frontends/carte-puissance/` |
| surface-control | GPIO `J10A`/`J10B` (SCS) | `custom-frontends/surface-control/` |

---

**Rétro-ingénierie par l'équipe — GPL-3.0**