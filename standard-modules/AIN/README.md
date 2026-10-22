# AIN — Module Entrées Analogiques (MIDIbox NG)

## Description
Module de base AIN (Analog Input) de l'écosystème MIDIbox NG. Fournit la lecture de voies analogiques pour potentiomètres, faders, capteurs, etc. Se connecte aux front-ends AIN (8x-pots, 4x-faders, etc.).

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Interfaçage MIDIbox
- **Type de bus :** AIN (Analog Input)
- **Connecteur :** J19 (SPI) du Core STM32F4 → module AINSER64 (MCP3208 + CD4051)
- **Voies :** Jusqu'à 64 entrées analogiques multiplexées par module AINSER64 (jusqu'à 2 modules = 128 voies)
- **Composants :** MCP3208 (ADC 12-bit) + 8× CD4051 (multiplexeurs 8:1)

> Câblage des pots/faders : les deux pattes externes se connectent à +5V (Vd) et GND (Vs). Le curseur (patte centrale) se connecte sur l'entrée AIN correspondante (A0..A7). Tous les entrées AIN non utilisées doivent être reliées à la masse (GND).

## Fichiers inclus
| Emplacement | Contenu |
|-------------|---------|
| `production/` | Archive de référence `mbhp_ainser64_v1_2023-06-02.zip` |

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue.

**Référence MIDIbox NG — GPL-3.0**