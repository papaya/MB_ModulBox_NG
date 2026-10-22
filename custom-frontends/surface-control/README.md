# surface-control — Surface de controle (SCS du Core32F4)


## Description
Carte de surface de controle pour le **Core32F4**, qui reproduit la **Standard Control Surface (SCS)** officielle de MIDIbox NG : **1 encodeur rotatif** + **6 boutons poussoirs**. Elle se branche directement sur les **GPIO du Core**, sans passer par les registres 74HC165 / 74HC595.

> ⚠️ **Correction majeure : les versions anterieures de cette page decrivaient une carte multi-bus (DIN + DOUT + AIN + WS2812).** Le schema `Surface Control V0.1.kicad_sch` ne contient **que 7 composants** : 1 encodeur (`ENC1`) et 6 boutons (`SWc1`..`SWc6`). Il n'y a **ni registre 74HC165 (DIN), ni 74HC595 (DOUT), ni AIN, ni WS2812** sur cette carte.
>
> ⚠️ **Carte prototype V0.1 non validee** : le PCB **n'est pas route** (0 piste, 21 pads non connectes). A router et a fabriquer en epreuve avant toute utilisation serieuse.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Spécifications techniques
- 1 encodeur rotatif avec poussoir (`EC12E24204A8`) : 2 phases + poussoir = **3 signaux**
- 6 boutons poussoirs (`SWc1`..`SWc6`) = **6 signaux**
- **9 signaux au total**, tous lus par des GPIO directs du STM32F4
- 1 connecteur **IDC 2x05** (`J2`) : GND + 8 signaux (D0..D7)
- Aucun registre a decalage, aucun convertisseur, aucune LED, aucun afficheur

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Encodeur rotatif | `EC12E24204A8` (menu) | 1 |
| Bouton poussoir | `124110828` | 6 |
| Connecteur | IDC Header 2x05 P2.54mm (`J2`) | 1 |
| Vis de fixation | MountingHole | 4 |

## Brochage / Mapping MIDIbox NG

### `J2` — connecteur vers le Core32F4 (`J10A` / `J10B`)
| Broche | Signal | Composant | Fonction |
|--------|--------|-----------|----------|
| 1 | GND | — | Masse commune (tous les boutons et l'encodeur) |
| 2 | — | — | Non connectee |
| 3 | `J2-D7` | `ENC1` broche 1 | **Phase A** de l'encodeur |
| 4 | `J2-D6` | `ENC1` broche 3 | **Phase B** de l'encodeur |
| 5 | `J2-D5` | `SWc6` | Bouton **MENU** |
| 6 | `J2-D4` | `SWc5` | Bouton **soft 1** |
| 7 | `J2-D3` | `SWc4` | Bouton **soft 2** |
| 8 | `J2-D2` | `SWc3` | Bouton **soft 3** |
| 9 | `J2-D1` | `SWc2` | Bouton **soft 4** |
| 10 | `J2-D0` | `SWc1` | Bouton **shift** |

> L'encodeur `ENC1` dispose de 3 contacts : broche 1 = phase A, broche 2 = **GND** (poussoir), broche 3 = phase B. Les phases A/B sont les entrees d'un **compteur de quadrature** pilote directement par le microcontroleur.
>
> Chaque bouton est un contact **entre sa broche `J2-Dx` et GND** (broche 1) : la lecture se fait par lecture directe du GPIO (avec pull-up interne du STM32 ou resistance externe si necessaire).

### Correspondance avec les GPIO du Core32F4
La surface de controle officielle de MIDIbox NG est cablee sur les connecteurs **`J10A` et `J10B`** du Core, exposes en GPIO via les fonctions `MIOS32_BOARD_J10*` :

| Connecteur Core | Broche | GPIO | Utilisable pour |
|------------------|--------|------|-----------------|
| `J10A` | 3 | PE8 | Phase A encodeur |
| `J10A` | 4 | PE9 | Phase B encodeur |
| `J10A` | 5 | PE10 | Bouton MENU |
| `J10A` | 6 | PE11 | Bouton soft 1 |
| `J10A` | 7 | PE12 | Bouton soft 2 |
| `J10A` | 8 | PE13 | Bouton soft 3 |
| `J10A` | 9 | PE14 | Bouton soft 4 |
| `J10A` | 10 | PE15 | Bouton shift |
| `J10B` | 1 | GND | Masse |
| `J10B` | 2 | +3V3 | Alimentation (si necessaire) |

> Le cablage exact a l'interface du Core depend du **logiciel** (application MIOS32). La documentation officielle decrit la SCS sur un schema de reference ([ucapps.de](https://www.ucapps.de/midibox_ng_manual_hw.html), section *Standard Control Surface*) : la correspondance ci-dessus est **indicative** et doit etre verifiee contre l'application utilisee.

## Documentation de fabrication
- `hardware/` : sources KiCad (`Surface Control V0.1.*`)
- `hardware/3D/` : modèle 3D de la carte (`.wrl`, `.step`)
- `production/` : Non disponible (carte prototype non routee / non fabricatee)

---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), **inspiree** de la Standard Control Surface officielle de la plateforme **MIDIbox (MBHP)** de Thorsten Klose / ucapps.de, mais **ce n'est pas** une reimplementation officielle : le schema, le connecteur et l'implantation sont originaux.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Rétro-ingénierie par l'équipe — GPL-3.0**> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
