# Bus MIDIbox NG — Schéma de principe et brochage

## Présentation

L'écosystème MIDIbox NG repose sur trois bus principaux qui interconnectent le **Core** (STM32F4) aux **front-ends** (cartes de contrôle physiques) :

| Bus | Rôle | Direction | Connecteur typique |
|-----|------|-----------|-------------------|
| **AIN** | Analog Input — lecture de potentiels (potentiomètres, faders, capteurs) | Core → Front-end | Header mâle 24 broches |
| **DIN** | Digital Input — lecture d'états logiques (boutons, switchs, encodeurs) | Front-end → Core | Header mâle 2x05 (10 broches) |
| **DOUT** | Digital Output — pilotage d'actionneurs (LEDs standards non adressables, afficheurs, relais) | Core → Front-end | Header mâle 2x05 (10 broches) |

---

## Schéma de principe des connexions

```
        ┌─────────────┐
        │   CORE      │  STM32F4
        │  (Core32F4) │
        └──────┬──────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌───────┐  ┌───────┐  ┌───────┐
│  AIN  │  │  DIN  │  │  DOUT │
│ Bus   │  │  Bus  │  │  Bus  │
│ (64ch)│  │       │  │       │
└────┬──┘  └────┬──┘  └────┬──┘
     │          │          │
     ▼          ▼          ▼
┌───────┐  ┌───────┐  ┌───────┐
│8x-pots│  │8x-btns│  │enc-Led│
│Faders │  │keys-4x│  │RGB    │
│Car.puiss│ │surface│  │pad-rgb│
│OLED   │  │control│  │       │
└───────┘  └───────┘  └───────┘
```

---

## Brochage détaillé des connecteurs de bus

### Bus AIN (Analog Input)

| Broche | Signal | Description |
|--------|--------|-------------|
| AIN-1 … AIN-64 | Voie analogique x | Lecture du curseur/potentiomètre |
| GND | Masse commune | Référence 0V |
| +5V | Alimentation | Alimentation des capteurs |

### Bus DIN (Digital Input)

| Broche | Signal | Description |
|--------|--------|-------------|
| DIN-1 … DIN-8 | Entrée digitale x | État logique (bouton, switch) |
| GND | Masse commune | Référence 0V |
| +5V | Alimentation (pull-up) | Alimentation et pull-up |

### Bus DOUT (Digital Output)

| Broche | Signal | Description |
|--------|--------|-------------|
| DOUT-1 … DOUT-8 | Sortie digitale x | Pilotage LED, afficheur, relais |
| GND | Masse commune | Référence 0V |
| +5V | Alimentation | Alimentation des actionneurs |

---

## Règles de câblage

1. **Masse commune :** Tous les GND des front-ends doivent être reliés à la masse du Core.
2. **Alimentation :** +5V distribué sur tous les bus ; les front-ends à forte consommation (LEDs RGB WS2812B) prévoient une **alimentation 5V dédiée séparée** (pas via le connecteur J4B du Core).
3. **LEDs WS2812B :** Se connectent en **1 fil de données sur J4B.SC (PB6 / TIM4)** du Core32F4 — **PAS** sur le bus DOUT (74HC595). Voir [spécifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).
4. **Longueur des câbles :** Maintenir les câbles de bus courts (< 50 cm) pour éviter les parasitage sur l'AIN.
5. **Déclenchement :** Les entrées DIN utilisent des pull-up internes ou externes (10 kΩ typique).

---

## Liens vers les front-ends

| Front-end | Bus utilisé | Dossier |
|-----------|-------------|---------|
| 4x-faders | AIN | `custom-frontends/4x-faders/` |
| 8x-pots | AIN | `custom-frontends/8x-pots/` |
| 8x-buttons | DIN | `custom-frontends/8x-buttons/` |
| encoders-led-rgb | DIN + DOUT | `custom-frontends/encoders-led-rgb/` |
| pad-rgb | DIN + DOUT | `custom-frontends/pad-rgb/` |
| keysw-4x2 | DIN | `custom-frontends/keysw-4x2/` |
| surface-control | DIN + DOUT + AIN | `custom-frontends/surface-control/` |

---

**Rétro-ingénierie par l'équipe — GPL-3.0**