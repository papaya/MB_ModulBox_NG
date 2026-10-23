# Led Ring — Carte Ring LEDs RGB (WS2812B)

## Description

La **Led Ring** est la carte qui héberge les 128 LED WS2812 en cascade et les connecte au contrôle du Core32F4 via la Control Board.

## Composants principaux

| Type | Dénomination | Qté |
|------|-------------|-----|
| LED RGB adressable | WS2812-2020 (PLCC4) | 128 |
| Condensateur découpling | C 100 nF | 128 |

## Brochage

| Connecteur | Signal | Description |
|------------|--------|-------------|
| J4 | IDC 1x03 | Donnée d'entrée (vers Control Board J20) |
| J5 | IDC 1x03 | Donnée de sortie (vers Control Board J21) |
| J6 | IDC 1x02 | Alimentation +5V (vers Control Board J21) |

## Architecture

- **128 × WS2812-2020** en cascade : D1 → D2 → ... → D128
- Contrôle par une seule ligne de données depuis la Control Board
- Alimentation 5V séparée (pas via la ligne de données)
- 300 mA max par LED, 40 mA par couleur

## Architecture de la Control Board

La **Control Board** est la carte de interface entre le module encodeurs-led-rgb et le module **Core32F4** (MIOS32). Elle gère :
- Shift Registers (74HC595) pour l'extension des lignes DIN/DOUT
- 74HC165 (8 entrées par 74HC165) pour lire les encodeurs
- Décodeur d'adresses (74HC138/139) pour sélectionner les périphériques
- Réseaux de dérivation pour les lignes SPI
- Alimentations : +5V (digital), +3V3, GND

## Production

- `led-ring/production/` : Gerbers, BOM, positions, netlist

---

> ⚠️ Document créé lors de la séparation en 3 sous-projets (23/10/2026). Contenu à compléter avec les sources KiCad réelles après extraction du schéma original.