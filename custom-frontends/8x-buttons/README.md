# 8x-buttons — Module custom 8 boutons poussoirs (DIN + DOUT)
![Screenshot 1](assets/Screenshot%202023-05-19%20163416.png)

## Description

Module boutons poussoirs (8 canaux) pour l'envoi d'événements MIDI numériques (Note On/Off, CC, etc.). La carte se branche sur le **bus DIN** (entrées digitales) du contrôleur MIDIbox NG et fournit en plus **8 sorties DOUT** pour piloter des LEDs.

## Spécifications techniques

- 8 boutons poussoirs mécaniques **à LED incorporée** (empreinte `switch_led_mec`)
- 8 LED supplémentaires (empreinte `LED Switch mec`), câblées en sortie
- **2 connecteurs IDC 2x05 P2.54mm** : `J1` = 8 entrées DIN, `J2` = 8 sorties DOUT
- **Aucune résistance de pull-up sur la carte** : le pull-up 10 kΩ est porté par le module **DIN** (74HC165), conformément à la référence MIDIbox
- Aucun registre à décalage sur la carte : les entrées et sorties sont balayées par les registres du module DIN / DOUT
![Screenshot 2](assets/Screenshot%202023-05-19%20202624.png)
## Composants principaux

| Type | Dénomination | Qté |
|------|-------------|-----|
| Bouton poussoir mécanique à LED | `switch_led_mec` | 8 |
| LED | `LED Switch mec` | 8 |
| Connecteur | IDC Header 2x05 P2.54mm Vertical (`J1`, `J2`) | 2 |
| Vis de fixation | MountingHole 3.2mm M3 | 4 |

> Les versions antérieures de cette page mentionnaient un **connecteur D-Sub 24 broches** et **8 pull-ups 10 kΩ** sur la carte : **ces deux éléments sont absents du schéma KiCad**. Le raccordement se fait par IDC 2x05.

## Brochage / Mapping MIDIbox NG
![botom](assets/BP_Bottom.png)
### `J1` — 8 entrées DIN (vers le module DIN 74HC165, chainage `J8`/`J9` du Core)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (contact du bouton) |
| 2 | — | Non connectée |
| 3 | `J1-D7` | Bouton **SW8** |
| 4 | `J1-D6` | Bouton **SW7** |
| 5 | `J1-D5` | Bouton **SW6** |
| 6 | `J1-D4` | Bouton **SW5** |
| 7 | `J1-D3` | Bouton **SW4** |
| 8 | `J1-D2` | Bouton **SW3** |
| 9 | `J1-D1` | Bouton **SW2** |
| 10 | `J1-D0` | Bouton **SW1** |

> Chaque bouton est un contact **entre sa broche `J1-Dx` et GND** (broche 1). Le niveau haut est assuré par le pull-up 10 kΩ du module DIN.

### `J2` — 8 sorties DOUT (vers le module DOUT 74HC595, chainage `J8`/`J9` du Core)

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | GND | Masse commune (cathode des LED) |
| 2 | — | Non connectée |
| 3 | `D8-A` | LED **D8** (anode) |
| 4 | `D7-A` | LED **D7** (anode) |
| 5 | `D6-A` | LED **D6** (anode) |
| 6 | `D5-A` | LED **D5** (anode) |
| 7 | `D4-A` | LED **D4** (anode) |
| 8 | `D3-A` | LED **D3** (anode) |
| 9 | `D2-A` | LED **D2** (anode) |
| 10 | `D1-A` | LED **D1** (anode) |

> L'anode de chaque LED est tirée vers la sortie DOUT correspondante ; la cathode est sur GND. La résistance de limitation (**220 Ω**) est portée par le module **DOUT** (74HC595), pas par cette carte.

## Notes de montage et astuces DIY

- Vérifier la configuration des entrées (active haut / active bas) avant câblage
- Pour un fonctionnement « high-active », il faut inverser le câblage du pull-up côté module DIN (procédure décrite sur [ucapps.de/mbhp_din](https://www.ucapps.de/mbhp_din.html))
- La LED de chaque bouton est câblée indépendamment sur `J2` : une LED du bouton peut être allumée indépendamment de l'état du bouton

## Documentation de fabrication

- `hardware/` : sources KiCad (`BP.*`)
- `hardware/3D/` : modèle 3D du boîtier (`BP V3.wrl`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, archives de fabrication
## Assets de visualisation

| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Screenshot 1 | `Screenshot%202023-05-19%20163416.png` | Capture d'écran du design |
| Screenshot 2 | `Screenshot%202023-05-19%20202624.png` | Capture d'écran du design |
---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Origine et usage :** conception originale MB MODULBOX NG, prévue pour le DIY/personnel. Aucune licence formelle n'est publiée dans le dépôt ; voir le README racine. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
