# Control Board — Carte d'interface (+ Shift Registers a rajouter non implementé)

## Description

La **Control Board** est la carte de interface entre le module encodeurs-led-rgb et le module **Core32F4** (MIOS32). Elle gère:

- **Shift Registers** (74HC595) pour l'extension des lignes DIN/DOUT
- **74HC165** (8 entrées par 74HC165) pour lire les encodeurs
- **Décodeur d'adresses** (74HC138/139) pour sélectionner les périphériques
- **Réseaux de dérivation** pour les lignes SPI
- **Alimentations** : +5V (digital), +3V3, GND

## Composants principaux

| Type | Dénomination | Qté |
|------|-------------|-----|
| Registre de décalage | SN74HC595N | 2 |
| Registre d'entrée | SN74HC165N | 3 |
| Décodeur d'adresse | SN74HC138N | 1 |
| Connecteur DIN/DOUT | IDC 2x05 | 1 |
| Connecteurs encodeurs | IDC 2x05 + 1x06 | 5 |

## Brochage

| Connecteur | Signal | Description |
|------------|--------|-------------|
| J8/J9 | IDC 2x05 | Bus DIN/DOUT (vers Core32F4) |
| J14 | IDC 1x06 | Poussoirs encodeurs (vers Encoders Board) |
| J15 | IDC 1x06 | Phases A/B encodeurs (vers Encoders Board) |

## Production

- `control-board/production/` : Gerbers, BOM, positions, netlist

---

> ⚠️ Document créé lors de la séparation en 3 sous-projets (23/10/2026). Contenu à compléter avec les sources KiCad réelles après extraction du schéma original.