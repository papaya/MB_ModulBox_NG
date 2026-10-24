# Encoders Board — carte de 8 encodeurs PEC16

![alt text](../assets/En_3Quart.png)
Carte custom du système **MB MODULBOX NG** accueillant 8 encodeurs avec poussoirs. Le PCB présent comporte 8 empreintes PEC16 et des connecteurs de report ; il ne comporte pas de 74HC165. La lecture des signaux est assurée hors de cette carte.

## Connectique relevée dans le PCB

Les 4 connecteurs 1x06 femelles sont raccordés broche à broche aux connecteurs `J30`..`J33` de la Control Board :

| Connecteur encodeurs | Broches 1 à 6 |
|---|---|
| `J20` | `SW1`, `SW2`, `ENC1B`, `ENC1A`, `ENC2B`, `ENC2A` |
| `J21` | `ENC3B`, `ENC3A`, `ENC4B`, `ENC4A`, `SW3`, `SW4` |
| `J22` | `ENC5B`, `ENC5A`, `ENC6B`, `ENC6A`, `SW5`, `SW6` |
| `J23` | `SW7`, `SW8`, `ENC7B`, `ENC7A`, `ENC8B`, `ENC8A` |

Les huit contacts poussoir et les seize phases A/B sortent ainsi sur 24 nets distincts. Les connecteurs `J14`/`J15` et `J24`/`J25` portent des nets non nommés dans le PCB ; ne pas les utiliser comme interface définie sans vérification.

## Projet et limites

- PCB : [`hardware/En.kicad_pcb`](hardware/En.kicad_pcb)
- Projet KiCad associé : [`hardware/En.kicad_pro`](hardware/En.kicad_pro)
- Schéma autonome : absent. La seule source schématique disponible est le projet historique [`../hardware/PEC_16_V0.2.kicad_sch`](../hardware/PEC_16_V0.2.kicad_sch), qui décrit l'ensemble du système et n'a pas été séparé en schémas autonomes vérifiés.
- Fabrication : aucun jeu Gerber propre à cette carte n'est versionné.
- Les modèles 3D custom ne sont pas inclus dans Git ; les chemins absolus existants ne sont donc pas portables.

Les références et les nets ci-dessus ont été relevés dans le PCB KiCad. Ce brochage n'a pas été validé par un schéma indépendant ou par un prototype. Contrôler l'orientation des connecteurs et la continuité avant raccordement.

Cette carte est une création originale pour MB MODULBOX NG. Voir le README parent pour les conditions d'utilisation et l'état de licence du dépôt.
