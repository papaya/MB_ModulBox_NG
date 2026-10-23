## Documentation des interconnexions

### Tableau des liaisons entre sous-cartes

| De | Vers | Connecteur | Broche(s) | Signal | Description |
|----|------|------------|-----------|--------|-------------|
| Control Board | Encoders Board | J14 (1x06 PinHeader) | 1-6 | C_SW8..C_SW1, GND, NC | Poussoirs des 8 encodeurs |
| Control Board | Encoders Board | J15 (1x06 PinHeader) | 1-6 | C_ENC8B..C_ENC1A, GND, NC | Phases A/B des 8 encodeurs |
| Control Board | Led Ring | J20 (1x06 PinHeader) | 1-6 | D1-DI, D2, D3, ..., GND, +5V | Données cascade WS2812 |
| Control Board | Led Ring | J21 (1x03 PinHeader) | 1-3 | +5V, GND, D128-DO | Alimentation + sortie cascade |

### Connecteurs de liaison détaillés

#### J14 — Poussoirs encodeurs (Control Board → Encoders Board)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `C_SW1` | Poussoir encodeur 1 |
| 2 | `C_SW2` | Poussoir encodeur 2 |
| 3 | `C_SW3` | Poussoir encodeur 3 |
| 4 | `C_SW4` | Poussoir encodeur 4 |
| 5 | `C_SW5` | Poussoir encodeur 5 |
| 6 | `C_SW6` | Poussoir encodeur 6 |
| 7 | `C_SW7` | Poussoir encodeur 7 |
| 8 | `C_SW8` | Poussoir encodeur 8 |
| 9 | GND | Masse commune |

#### J15 — Phases encodeurs (Control Board → Encoders Board)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `C_ENC1A` | Phase A encodeur 1 |
| 2 | `C_ENC1B` | Phase B encodeur 1 |
| 3 | `C_ENC2A` | Phase A encodeur 2 |
| 4 | `C_ENC2B` | Phase B encodeur 2 |
| 5 | `C_ENC3A` | Phase A encodeur 3 |
| 6 | `C_ENC3B` | Phase B encodeur 3 |
| 7 | `C_ENC4A` | Phase A encodeur 4 |
| 8 | `C_ENC4B` | Phase B encodeur 4 |
| 9 | `C_ENC5A` | Phase A encodeur 5 |
| 10 | `C_ENC5B` | Phase B encodeur 5 |
| 11 | `C_ENC6A` | Phase A encodeur 6 |
| 12 | `C_ENC6B` | Phase B encodeur 6 |
| 13 | `C_ENC7A` | Phase A encodeur 7 |
| 14 | `C_ENC7B` | Phase B encodeur 7 |
| 15 | `C_ENC8A` | Phase A encodeur 8 |
| 16 | `C_ENC8B` | Phase B encodeur 8 |
| 17 | GND | Masse commune |

*Note : Les 24 tensions DIN (8× A, 8× B, 8× poussoir) sont distribuées sur J14/J15/J16.*

#### J20 — Cascade WS2812 (Control Board → Led Ring)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `D1-DI` | Donnée d'entrée |
| 2 | `D2-DI` | Donnée vers D2 |
| 3 | `D3-DI` | Donnée vers D3 |
| ... | ... | 128 données au total |
| 6 | GND | Masse commune |

#### J21 — Alimentation LED

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `+5V` | Alimentation 5V pour les LED |
| 2 | `GND` | Masse des LED |
| 3 | `D128-DO` | Dernière LED de la cascade |

---

## Architecture de la carte maître (Control Board)

La **Control Board** est la carte de interface entre le module encodeurs-led-rgb et le module Core32F4. Elle gère :

- **Shift Registers** (74HC595) pour l'extension des lignes DIN/DOUT
- **74HC165** (8 entrées par 74HC165) pour lire les encodeurs
- **Décodeur d'adresses** (74HC138/139) pour sélectionner les périphériques
- **Réseaux de dérivation** pour les lignes SPI
- **Alimentations** : +5V (digital), +3V3, GND

### Connecteurs de la Control Board

| Connecteur | Type | Signal principaux |
|------------|------|-------------------|
| J8/J9 | IDC 2x05 | Bus DIN/DOUT (vers Core32F4) |
| J11 | IDC 2x05 | Poussoirs encodeurs (vers Encoders Board) |
| J12 | IDC 2x05 | Phases A/B encodeurs (vers Encoders Board) |
| J13 | IDC 2x05 | Données WS2812 (vers Led Ring) |
| J14 | IDC 1x06 | Poussoirs encodeurs (vers Encoders Board) |
| J15 | IDC 1x06 | Phases encodeurs (vers Encoders Board) |
| J16 | IDC 2x05 | SPI / I2C (vers Core32F4) |
| J20 | IDC 1x06 | Données WS2812 (vers Led Ring) |
| J21 | IDC 1x03 | Alimentation LED (vers Led Ring) |
| J30-J35 | IDC 1x06 | Connecteurs de report |

---

## Architecture de la carte encodeurs (Encoders Board)

La **Encoders Board** héberge physiquement les 8 encodeurs PEC16 avec leurs poussoirs.

### Composants principaux

- 8 × **PEC16** (PEC164120FS0012) : encodeurs rotatifs avec poussoir
- 3 × **74HC165** : registoires de décalage pour les 24 entrées DIN
- 1 × **74HC164** : registoire de décalage pour outputs
- 8 × **C 100 nF** : découpling par encodeur

### Connecteurs de l'Encoders Board

| Connecteur | Signal | Description |
|------------|--------|-------------|
| J1-J3 | IDC 2x05 | 8× poussoir (vers Control Board J11) |
| J4-J6 | IDC 1x06 | 8× phases A/B (vers Control Board J15) |
| J7-J11 | IDC 1x02/1x03 | Connecteurs de report |

---

## Architecture de la carte LED (Led Ring)

La **Led Ring** héberge les 128 LED WS2812 en cascade.

### Composants principaux

- 128 × **WS2812-2020** (PLCC4 2.0×2.0mm) : LED RGB adressable
- 128 × **C 100 nF** : découpling par LED

### Connecteurs de la Led Ring

| Connecteur | Signal | Description |
|------------|--------|-------------|
| J4 | IDC 1x03 | Donnée d'entrée (vers Control Board J20) |
| J5 | IDC 1x03 | Donnée de sortie (vers Control Board J21) |
| J6 | IDC 1x02 | Alimentation +5V (vers Control Board J21) |
| J7 | IDC 2x02 | Mise à la masse |

---

## Organisation de fabrication

### Pour chaque sous-carte

1. **Control Board** → `control-board/production/` :
   - `Control_Board.gbr` (Gerbers)
   - `Control_Board-BOM.csv`
   - `Control_Board-position.csv`
   - `Control_Board-netlist.ipc`

2. **Encoders Board** → `encoders-board/production/` :
   - `Encoders_Board.gbr`
   - `Encoders_Board-BOM.csv`
   - `Encoders_Board-position.csv`

3. **Led Ring** → `led-ring/production/` :
   - `Led_Ring.gbr`
   - `Led_Ring-BOM.csv`
   - `Led_Ring-position.csv`

### Assemblage

1. Fabriquer les 3 PCBs séparément
2. Monter les sous-cartes sur une plaque d'assemblage
3. Percer les trous pour les connecteurs de liaison (J14, J15, J20, J21)
4. Câbler les connecteurs de liaison
5. Alimenter l'ensemble depuis le Core32F4

---