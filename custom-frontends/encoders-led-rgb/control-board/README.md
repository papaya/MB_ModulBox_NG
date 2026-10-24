# connect Board — interconnexion des encodeurs et du ring LED
![alt text](<../assets/connect board 3Quart.png>)
Carte custom du système **MB MODULBOX NG**. Le PCB présent (`connect board.kicad_pcb`) est une carte de connectique : il ne contient pas les 74HC165, 74HC595 ou décodeurs décrits dans les anciennes versions de cette page. Aucun schéma autonome correspondant n'est fourni.

## Éléments réellement présents

- 3 connecteurs IDC 2x05 (`J11`, `J12`, `J13`) pour les signaux des encodeurs.
- 4 connecteurs 1x06 (`J30`..`J33`) raccordés aux groupes encodeurs de la carte `En`.
- Connecteurs 1x06 `J34`/`J35` et IDC 2x05 `J44`/`J45` pour alimentations et données du ring.
- Aucun composant de logique active.

## Brochage relevé dans le PCB

Pour `J11`..`J13`, broche 1 = GNDA, broche 2 = NC et broches 3..10 = signaux listés ci-dessous.

| Connecteur | Broches 3 à 10 |
|---|---|
| `J11` | `C_SW8`, `C_SW7`, `C_SW6`, `C_SW5`, `C_SW4`, `C_SW3`, `C_SW2`, `C_SW1` |
| `J12` | `C_ENC8B`, `C_ENC8A`, `C_ENC7B`, `C_ENC7A`, `C_ENC6B`, `C_ENC6A`, `C_ENC5B`, `C_ENC5A` |
| `J13` | `C_ENC4B`, `C_ENC4A`, `C_ENC3B`, `C_ENC3A`, `C_ENC2B`, `C_ENC2A`, `C_ENC1B`, `C_ENC1A` |

Les connecteurs `J30`..`J33` sont des groupes 6 broches :

| Connecteur | Broches 1 à 6 |
|---|---|
| `J30` | `C_SW1`, `C_SW2`, `C_ENC1B`, `C_ENC1A`, `C_ENC2B`, `C_ENC2A` |
| `J31` | `C_ENC3B`, `C_ENC3A`, `C_ENC4B`, `C_ENC4A`, `C_SW3`, `C_SW4` |
| `J32` | `C_ENC5B`, `C_ENC5A`, `C_ENC6B`, `C_ENC6A`, `C_SW5`, `C_SW6` |
| `J33` | `C_SW7`, `C_SW8`, `C_ENC7B`, `C_ENC7A`, `C_ENC8B`, `C_ENC8A` |

`J34` et `J35` reprennent respectivement `+5VA`/`+5VD`, un signal sur leur broche 2 et GNDA sur leur broche 3. Le signal de `J34` est reporté sur `J44` broche 6 ; celui de `J35` sur `J45` broche 6. `J44`/`J45` : broche 1 = GNDA, broche 10 = rail +5 V correspondant ; les autres broches sont NC sauf la broche 6.

## Projet et limites

- PCB : [`hardware/connect board.kicad_pcb`](hardware/connect%20board.kicad_pcb)
- Projet KiCad associé : [`hardware/connect board.kicad_pro`](hardware/connect%20board.kicad_pro)
- Schéma autonome : absent. Le schéma historique [`../hardware/PEC_16_V0.2.kicad_sch`](../hardware/PEC_16_V0.2.kicad_sch) reste la seule source schématique du système complet ; il n'a pas été scindé en feuilles vérifiées par sous-carte.
- Fabrication : aucun jeu Gerber propre à cette carte n'est versionné.

Les brochages ci-dessus sont extraits des nets du PCB, pas vérifiés par un schéma indépendant ni par un prototype. Vérifier la connectique et l'orientation des câbles avant branchement.

Cette carte est une création originale pour MB MODULBOX NG. Voir le README parent pour les conditions d'utilisation et l'état de licence du dépôt.
