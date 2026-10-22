# 4x-faders — Carte faders / glissieres (AIN)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

![3D quart](assets/3d%203quart.png)

## Description
Carte de front-end integrant des faders (glissieres) pour le controle continu de parametres MIDI (volume, filtre, effets, etc.). Chaque fader est lu sur une voie analogique independante. La carte ne contient **aucun convertisseur analogique-numerique** : elle expose les curseurs sur un connecteur IDC, relies au module **AINSER64** (MCP3208 + CD4051) du bus AIN.

Le repertoire contient **deux cartes complementaires** :
- `Fad_1` : 4 faders, connecteurs `J3` (curseurs) et `J4` (passage)
- `Fad_2` : 4 faders, connecteur `J5` (curseurs)

Article de reference : [4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2](https://ksir-diy.blogspot.com/) sur le blog Ksir DIY'S.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isometrique avec composants |
| 3D quart | `3d%203quart.png` | Vue 3D quart du PCB |

![3D top](assets/Fad_1.png)
![3D iso](assets/Fad_2.png)

## Specifications techniques
- 4 faders (glissieres) par carte, courbe lineaire **RA6020F-10-15F2-B10K** (10 kOhm)
- **Tension de reference : +3V0** (et non +5V) — la borne `+3V0` alimente les deux extremites de chaque fader
- Sortie : curseurs + GND + +3V0 sur connecteur **IDC 2x05 P2.54mm**
- Lecture : via le module **AINSER64** du bus AIN (broche `J19` du Core32F4, SPI)
- Aucune resistance, aucun condensateur, aucun circuit actif sur la carte

## Composants principaux
| Type | Denomination | Qte (par carte) |
|------|-------------|-----|
| Fader / glissiere | ALPS RA6020F-10-15F2-B10K (10 kOhm) | 4 |
| Connecteur | IDC Header 2x05 P2.54mm Vertical | 1 a 2 |
| Bouton/pommeau de fader | `ALPS Fader Knob.wrl` | 4 |
| Vis de fixation | MountingHole 3.2mm M3 | 4 |

## Brochage / Mapping MIDIbox NG

### `Fad_1` — connecteur `J3` (curseurs)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (reference 0 V) |
| 2 | +3V0 | Alimentation des faders (borne haute) |
| 3 | `J3-A7` | Curseur de **fad6** |
| 4 | `J3-A6` | Curseur de **fad5** |
| 5 | `J3-A5` | Curseur de **fad7** |
| 6 | `J3-A4` | Curseur de **fad8** |
| 7 | `J3-A3` | Curseur de **fad6** (idem broche 3) |
| 8 | `J3-A2` | Curseur de **fad5** (idem broche 4) |
| 9 | `J3-A1` | Curseur de **fad7** (idem broche 5) |
| 10 | `J3-A0` | Curseur de **fad8** (idem broche 6) |

Le connecteur `J4` de `Fad_1` est un **connecteur de passage** : il reproduit les memes 8 signaux que `J3` (broches 3 a 6), GND (broches 1, 2) et +3V0 (broches 1, 2) ; ses broches 7 a 10 sont libres. Il permet de.chainer plusieurs cartes.

### `Fad_2` — connecteur `J5` (curseurs)
| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune |
| 2 | +3V0 | Alimentation des faders |
| 3 | `J5-A7` | Curseur de **fad1** |
| 4 | `J5-A6` | Curseur de **fad2** |
| 5 | `J5-A5` | Curseur de **fad3** |
| 6 | `J5-A4` | Curseur de **fad4** |
| 7 a 10 | — | Non connectees |

> **Cablage du fader (verifie dans le schema KiCad)** : patte 1 -> GND, patte 2 -> **curseur** (-> broche `J3`/`J5` correspondante), patte 3 -> **+3V0**.
>
> Le curseur etant relie a l'entree analogique de l'AINSER64, la plage de mesure est **0 .. 3,0 V** (et non 0 .. 5 V).
>
> **Les entrees analogiques non utilisees de l'AINSER64 doivent etre reliees a la masse**, sinon l'application emet des valeurs aleatoires.

### Module AINSER64 (rappel)
- Connecteur : **`J19`** du Core STM32F4 (SPI, 2 chip-selects `RC1`/`RC2`)
- Architecture : 1 × **MCP3208** (ADC 12 bits) + 8 × **CD4051** (multiplexeurs 8:1) + 1 × 74HC595
- Capacite : 64 entrees par module, jusqu'a 2 modules (128 voies) supportes par MIDIbox NG

## Documentation de fabrication
- `hardware/` : sources KiCad (`Fad_1.*`, `Fad_2.*`)
- `hardware/3D/` : modeles 3D des faders et boutons (.wrl)
- `production/` : Gerbers pour Fad_1 et Fad_2
- Blog : [4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2 sur ksir-diy.blogspot.com](https://ksir-diy.blogspot.com/)

---

## Conception & Compatibilite

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du systeme MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Licence & Usage :** Ces fichiers hardware sont partages sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du cablage ou du routage.

Retro-ingenierie par l'equipe — GPL-3.0

