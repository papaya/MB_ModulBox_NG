# surface-control — Surface de contrôle globale (DIN + DOUT + AIN)

## Description
Carte de surface de contrôle combinant plusieurs interfaces (boutons, encodeurs, afficheur) sur une seule PCB. Version V0.1 du prototype global de contrôleur MIDIbox NG.

> ⚠️ **Carte prototype V0.1 non validée** — les connexions exactes dépendent de la configuration finale. À valider avant toute fabrication.

## Spécifications techniques
- Lecture boutons et encodeurs via bus DIN (module 74HC165 sur J8/J9 du Core32)
- Pilotage LEDs et afficheur via bus DOUT (module 74HC595 sur J8/J9 du Core32)
- Lecture potentiomètres et faders via bus AIN (module AINSER64 sur J19 SPI du Core32)
- LEDs RGB adressables (WS2812B) sur J4B.SC (PB6 / TIM4) du Core32 — **PAS sur DOUT**
- GND et +5V communs
- Carte prototype V0.1 — à valider avant fabrication

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Boutons / encodeurs | Selon configuration DIN | plusieurs |
| LEDs | Selon configuration DOUT ou WS2812B | plusieurs |
| Potentiomètres / faders | Selon configuration AIN | plusieurs |
| Connecteurs | Headers vers bus DIN, DOUT, AIN | plusieurs |

## Brochage / Mapping MIDIbox NG
| Élément | Bus | Connecteur Core |
|---------|-----|-----------------|
| Entrées DIN (boutons, encodeurs) | DIN | J8/J9 (74HC165) |
| Sorties DOUT (LEDs standards) | DOUT | J8/J9 (74HC595) |
| Voies AIN (pots, faders) | AIN | J19 (SPI, AINSER64) |
| Donnée WS2812B (LEDs RGB) | — | J4B.SC (PB6/TIM4) |
| GND / +5V | Commun | — |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Surface Control V0.1.*`)
- `hardware/3D/` : modèle 3D de la carte (`.wrl`, `.step`)
- `production/` : Non disponible (carte prototype non fabriquée)

---

## Conception & Compatibilité

Carte d'interface originale conçue pour le système **MB MODULBOX NG**, compatible avec les bus et modules du système MIDIbox NG.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial.

**Rétro-ingénierie par l'équipe — GPL-3.0**
