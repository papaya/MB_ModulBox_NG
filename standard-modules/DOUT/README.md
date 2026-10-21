# DOUT — Module Sorties Digitales (MIDIbox NG)

## Description
Module de base DOUT (Digital Output) de l'écosystème MIDIbox NG. Fournit des sorties digitales pour piloter LEDs, afficheurs, relais. Se connecte aux front-ends DOUT (encoders-led-rgb, pad-rgb, surface-control, etc.).

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](assets/DOUT-DOUT.png)

## Spécifications techniques
- Sorties digitales pour LEDs et composants
- Interface DOUT vers bus MIDIbox NG
- Décalage via 74HC595

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Décaleur | 74HC595 | 5 |
| Connecteur IDC 2x05 | P2.54mm Vertical | 5 |
| Capacité | C_Disc_D3.8mm | 4 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 4 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| DOUT-x | Sortie digitale x |
| GND | Masse commune |
| +5V | Alimentation |

## Documentation de fabrication
- `hardware/` : sources KiCad (`DOUT.*`)
- `hardware/3D/` : modèles 3D (`.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, positions

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue.

**Référence MIDIbox NG — GPL-3.0**