# LED Ring — carte de 128 LED RGB WS2812
![led](../assets/leds_3Quart.png)
Carte custom du système **MB MODULBOX NG** portant 128 LED RGB WS2812-2020 et un condensateur de découplage de 100 nF par LED. La chaîne de données traverse D1 à D128 : les pixels sont adressables individuellement.

## Brochage relevé dans le PCB

| Connecteur | Broche 1 | Broche 2 | Broche 3 |
|---|---|---|---|
| `J4` | `+5V` | Entrée données (`D1-DI`) | `GND` |
| `J5` | `+5V` | Sortie données (`D128-DO`) | `GND` |

La liaison de données doit venir d'une sortie WS2812 supportée par le Core ; la masse du Core et celle de l'alimentation externe doivent être communes. Les connecteurs sont des empreintes 1x06, mais seules les broches 1 à 3 sont affectées dans le PCB.

## Puissance

Ne dimensionnez pas l'alimentation à partir de la valeur « 10 % » mentionnée dans d'anciennes notes : ce réglage logiciel ne garantit pas le courant maximal. Dimensionnez l'alimentation, le câblage, les connecteurs et la distribution cuivre à partir de la fiche technique des LED réellement montées et de la luminosité maximale prévue. Le PCB conserve des problèmes DRC documentés dans le README parent et ne doit pas être considéré comme validé pour la pleine charge.

## Projet et limites

- PCB : [`leds.kicad_pcb`](leds.kicad_pcb)
- Projet KiCad associé : [`leds.kicad_pro`](leds.kicad_pro)
- Schéma autonome : absent. La seule source schématique disponible est [`../hardware/PEC_16_V0.2.kicad_sch`](../hardware/PEC_16_V0.2.kicad_sch), schéma historique de l'ensemble du système.
- Fabrication : le dossier parent `../production/` contient BOM, positions et netlist, mais aucun Gerber distinct pour cette carte.
- Les modèles 3D custom sont ignorés par Git ; le PCB contient encore des chemins absolus Windows vers des fichiers qui ne sont pas présents dans le dépôt.

Les références, valeurs, nets et brochages décrits ici sont issus du PCB. Ils n'ont pas été comparés à un schéma autonome ni validés sur prototype. La séparation en trois PCB existe dans l'arborescence, mais les projets ne sont pas encore autonomes au sens schéma/BOM/Gerbers.

Cette carte est une création originale pour MB MODULBOX NG. Voir le README parent pour les conditions d'utilisation et l'état de licence du dépôt.
