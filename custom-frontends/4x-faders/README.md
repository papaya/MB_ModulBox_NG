# 4x-faders — Module custom faders / glissières (AIN)

![3D top](assets/3d%203quart.png)

## Description

Carte de front-end intégrant des faders (glissières) pour le contrôle continu de paramètres MIDI (volume, filtre, effets, etc.). Chaque fader est lu sur une voie analogique indépendante. La carte ne contient **aucun convertisseur analogique-numérique** : elle expose les curseurs sur un connecteur IDC, reliés au module **AINSER64** (MCP3208 + CD4051) du bus AIN.
![3D top](assets/Faderx4.png)
Le répertoire contient **deux cartes complémentaires** :
- `Fad_1` : 4 faders, connecteurs `J3` (curseurs) et `J4` (passage)
- `Fad_2` : 4 faders, connecteur `J5` (curseurs)

![3D top](assets/Fad_1_Bottom.png)
![3D iso](assets/Fad_2_Bottom.png)

## Spécifications techniques

- 4 faders (glissières) par carte, courbe linéaire **RA6020F-10-15F2-B10K** (10 kΩ)
- **Tension de référence : +3V0** (et non +5V) — la borne `+3V0` alimente les deux extrémités de chaque fader
- Sortie : curseurs + GND + +3V0 sur connecteur **IDC 2x05 P2.54mm**
- Lecture : via le module **AINSER64** du bus AIN (broche `J19` du Core32F4, SPI)
- Aucune résistance, aucun condensateur, aucun circuit actif sur la carte

## Composants principaux

| Type | Dénomination | Qté (par carte) |
|------|-------------|-----|
| Fader / glissière | ALPS RA6020F-10-15F2-B10K (10 kΩ) | 4 |
| Connecteur | IDC Header 2x05 P2.54mm Vertical | 1 à 2 |
| Bouton/pommeau de fader | `ALPS Fader Knob.wrl` | 4 |
| Vis de fixation | MountingHole 3.2mm M3 | 4 |

## Brochage / Mapping MIDIbox NG

### `Fad_1` — connecteur `J3` (curseurs)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (référence 0 V) |
| 2 | +3V0 | Alimentation des faders (borne haute) |
| 3 | `J3-A7` | Curseur de **fad6** |
| 4 | `J3-A6` | Curseur de **fad5** |
| 5 | `J3-A5` | Curseur de **fad7** |
| 6 | `J3-A4` | Curseur de **fad8** |
| 7 | `J3-A3` | Curseur de **fad6** (idem broche 3) |
| 8 | `J3-A2` | Curseur de **fad5** (idem broche 4) |
| 9 | `J3-A1` | Curseur de **fad7** (idem broche 5) |
| 10 | `J3-A0` | Curseur de **fad8** (idem broche 6) |

Le connecteur `J4` de `Fad_1` est un **connecteur de passage** : il reproduit les mêmes 8 signaux que `J3` (broches 3 à 6), GND (broches 1, 2) et +3V0 (broches 1, 2) ; ses broches 7 à 10 sont libres. Il permet de chaîner plusieurs cartes.

### `Fad_2` — connecteur `J5` (curseurs)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune |
| 2 | +3V0 | Alimentation des faders |
| 3 | `J5-A7` | Curseur de **fad1** |
| 4 | `J5-A6` | Curseur de **fad2** |
| 5 | `J5-A5` | Curseur de **fad3** |
| 6 | `J5-A4` | Curseur de **fad4** |
| 7 à 10 | — | Non connectées |

> **Câblage du fader (vérifié dans le schéma KiCad)** : patte 1 → GND, patte 2 → **curseur** (→ broche `J3`/`J5` correspondante), patte 3 → **+3V0**.

> Le curseur étant relié à l'entrée analogique de l'AINSER64, la plage de mesure est **0 .. 3,0 V** (et non 0 .. 5 V).

> **Les entrées analogiques non utilisées de l'AINSER64 doivent être reliées à la masse**, sinon l'application émet des valeurs aléatoires.

### Module AINSER64 (rappel)

- Connecteur : **`J19`** du Core STM32F4 (SPI, 2 chip-selects `RC1`/`RC2`)
- Architecture : 1 × **MCP3208** (ADC 12 bits) + 8 × **CD4051** (multiplexeurs 8:1) + 1 × 74HC595
- Capacité : 64 entrées par module, jusqu'à 2 modules (128 voies) supportés par MIDIbox NG

## Documentation de fabrication

- `hardware/` : sources KiCad (`Fad_1.*`, `Fad_2.*`)
- `hardware/3D/` : modèles 3D des faders et boutons (`.wrl`)
- `production/` : Gerbers pour Fad_1 et Fad_2
- Blog : [4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2 sur ksir-diy.blogspot.com](https://ksir-diy.blogspot.com/)

## Assets de visualisation

| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |
| 3D quart | `3d%203quart.png` | Vue 3D quart du PCB |
---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Origine et usage :** conception originale MB MODULBOX NG, prévue pour le DIY/personnel. Aucune licence formelle n'est publiée dans le dépôt ; voir le README racine. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
