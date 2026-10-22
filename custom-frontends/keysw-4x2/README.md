# keysw-4x2 — Clavier 8 touches (DIN) + retroeclairage SK6812 en cascade


## Description
Carte de front-end integrant un clavier de **8 touches mecaniques** (Cherry MX) pour l'envoi d'evenements MIDI (notes, CC, etc.). Chaque touche est lue sur une entree digitale distincte du bus DIN. La carte embarque en outre **8 LED RGB SK6812MINI-E adressables** montees **en cascade serie** (chaque LED est adressable individuellement).

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](assets/MB-KeySW_4x2_V0.3.png)

## Specifications techniques
- 8 touches mecaniques **Cherry MX Low Profile** (`CHERRY MX1B-52NA`)
- **Interface DIN : 8 touches = 8 entrees 1:1** d'un registre 74HC165 (aucune matrice colonnes/lignes)
- **8 × SK6812MINI-E** en **cascade serie** : `J2` (entree DATA) -> D0 -> D1 -> ... -> D7 -> `J3` (sortie DATA)
- 8 × condensateur de decoupling 100 nF (1206) sur chaque LED
- Aucun registre a decalage, aucun CI de logique sur la carte

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Switch mécanique | Cherry MX Low Profile (`SW_Alps_Matias_1.00u_cherry_LP`) | 8 |
| LED RGB adressable | SK6812MINI-E (PLCC4) | 8 |
| Condensateur | C 100 nF 1206 | 8 |
| Connecteur | IDC Header 2x05 P2.54mm (`J1` = DIN, `J2` = entree LED, `J3` = sortie LED) | 3 |
| Connecteur | PinHeader 1x02 (`J4`, masse) | 1 |
| Touches (keycaps) | `beschr. Kappe.wrl` | 8 |

> ⚠️ **Corrections par rapport aux versions anterieures de cette page** :
> - Le clavier **n'est pas matriciel** : 8 touches = 8 entrees distinctes.
> - **Aucune diode anti-ghosting (1N4148) n'est presente dans le schema** : il n'y en a pas dans le composant. Le câblage 1:1 ne le requiert pas.
> - Les LED SK6812 sont **adressees individuellement** : chaque pixel peut afficher sa propre couleur. Elles sont câblees en serie (chaine) pour le câblage physique, chacune decodifie sa propre couleur (R,G,B).

## Brochage / Mapping MIDIbox NG

### `J1` — 8 entrees DIN (vers le module DIN 74HC165, chainage `J8`/`J9` du Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `J1-vss` | Masse commune (reliee a `J4` et GND) |
| 2 | — | Non connectee |
| 3 | `J1-D7` | Touche **SW7** |
| 4 | `J1-D6` | Touche **SW6** |
| 5 | `J1-D5` | Touche **SW5** |
| 6 | `J1-D4` | Touche **SW4** |
| 7 | `J1-D3` | Touche **SW3** |
| 8 | `J1-D2` | Touche **SW2** |
| 9 | `J1-D1` | Touche **SW1** |
| 10 | `J1-D0` | Touche **SW0** |

> Chaque touche est un contact **entre sa broche `J1-Dx` et la masse** (`J1` broche 1 / `J4`). Le niveau haut est assure par le pull-up 10 kΩ du module **DIN**.

### `J2` — entree de la cascade LED (vers la sortie WS2812 du Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse |
| 2 a 5, 7, 8, 9 | — | Non connectees |
| 6 | `D0-DI` | **DATA d'entree** de la cascade (vers `D0`) |
| 10 | +5V | Alimentation des LED |

### `J3` — sortie de la cascade LED (vers la carte suivante ou vers le Core)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse |
| 2 a 5, 7, 8, 9 | — | Non connectees |
| 6 | `D7-DO` | **DATA de sortie** de la cascade (depuis `D7`) |
| 10 | +5V | Alimentation des LED |

### `J4` — masse supplementaire
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `J1-vss` | Relie a la masse des boutons |
| 2 | GND | Masse du plan |

### Chaine WS2812 du Core
Le **data** part d'une sortie WS2812 du **Core32F4** puis traverse toute la cascade :

```
Core (J4A/J4B, WS2812)  ->  J2 (broche 6)  ->  D0 -> D1 -> ... -> D7  ->  J3 (broche 6)
```

- Le Core STM32F4 dispose de **4 lignes WS2812** (`J4A` PB10 / PB11, `J4B` **PB6** = TIM4, reference MIOS32 / `J4B` PB9), chacune avec un pull-up 2,2 kΩ et une sortie en open-drain.
- **L'alimentation +5V des LED doit etre fournie separement** (les LED ne doivent pas etre alimentees via `J4A`/`J4B` du Core : jusqu'a 20 mA par LED RGB). Voir [specifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).
- Comme les LED sont **cascadees**, chaque LED decode et affiche sa propre couleur (une seule ligne de donnees suffit).identique.

## Documentation de fabrication
- `hardware/` : sources KiCad (`MB-KeySW_4x2_V0.3.*`)
- `hardware/3D/shapes3D/` : modèles 3D des touches et switchs (`.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), fichiers de position, archives de fabrication

---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

🔋 **Gestion de la puissance** : La gestion de la puissance des LED est indispensable, j'ai paramétré les LED à 10% de puissance.
**Rétro-ingénierie par l'équipe — GPL-3.0**> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
