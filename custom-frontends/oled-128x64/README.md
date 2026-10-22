# oled-128x64 — Carte afficheur OLED 128x64 (I2C)

## Description
Carte de front-end intégrant un afficheur OLED 128x64 pixels pour l'affichage d'informations MIDI (nom de piste, valeur de paramètre, menu, etc.). L'afficheur est piloté en **I2C** (contrôleur SSD1306 ou SH1106 intégré).

> ⚠️ **Note :** Cet afficheur se connecte en I2C directement, il n'utilise **pas** le bus DIN/DOUT du MIDIbox NG. Vérifier la compatibilité avec le Core STM32F4 (ports I2C disponibles).

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](assets/Oled_1309_x1_V0.0.png)

## Spécifications techniques
- Afficheur OLED 128x64 pixels
- Contrôleur I2C intégré (type SSD1306 ou SH1106)
- Interface I2C (SDA, SCL)
- Adresse I2C : 0x3C ou 0x3D (selon modèle)
- Alimentation : 3.3V ou 5V selon l'afficheur choisi

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Afficheur OLED | SSD1306 ou SH1106 | 1 |
| Contrôleur I2C | Intégré | 1 |
| Connecteur | Header mâle 4 broches | 1 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| SDA | Data I2C |
| SCL | Clock I2C |
| GND | Masse commune |
| +3.3V / +5V | Alimentation (selon modèle) |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Oled_1309_x1_V0.0.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archive de fabrication

---

## Conception & Compatibilité

Carte d'interface originale conçue pour le système **MB MODULBOX NG**, compatible avec les bus et modules du système MIDIbox NG.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial.

**Rétro-ingénierie par l'équipe — GPL-3.0**
