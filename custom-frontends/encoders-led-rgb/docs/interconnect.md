# Interconnexion des trois PCB encodeurs / LED

Ce document relève les nets des PCB séparés actuellement présents. Il ne remplace pas un schéma : les trois PCB n'ont pas de schémas autonomes, les liaisons n'ont pas été vérifiées sur prototype et les Gerbers ne sont pas fournis séparément.

## Control Board vers Encoders Board

Relier les groupes de mêmes numéros de broches :

| Control Board | Encoders Board | Broches 1 à 6 |
|---|---|---|
| `J30` | `J20` | SW1, SW2, ENC1B, ENC1A, ENC2B, ENC2A |
| `J31` | `J21` | ENC3B, ENC3A, ENC4B, ENC4A, SW3, SW4 |
| `J32` | `J22` | ENC5B, ENC5A, ENC6B, ENC6A, SW5, SW6 |
| `J33` | `J23` | SW7, SW8, ENC7B, ENC7A, ENC8B, ENC8A |

Les signaux sortent aussi sur les connecteurs IDC de la Control Board :

- `J11` : broche 1 GNDA, broche 2 NC, broches 3..10 = SW8, SW7, SW6, SW5, SW4, SW3, SW2, SW1.
- `J12` : broche 1 GNDA, broche 2 NC, broches 3..10 = ENC8B, ENC8A, ENC7B, ENC7A, ENC6B, ENC6A, ENC5B, ENC5A.
- `J13` : broche 1 GNDA, broche 2 NC, broches 3..10 = ENC4B, ENC4A, ENC3B, ENC3A, ENC2B, ENC2A, ENC1B, ENC1A.

Ces signaux sont des nets de PCB ; leur affectation logicielle MIDIbox et la polarité des encodeurs restent à configurer/vérifier.

## Control Board vers LED Ring

| Control Board | LED Ring | Broches |
|---|---|---|
| `J34` | `J4` (entrée) | 1 = +5VA/+5V, 2 = signal de données, 3 = GNDA/GND |
| `J35` | `J5` (sortie) | 1 = +5VD/+5V, 2 = retour données, 3 = GNDA/GND |

Les nets des signaux J34/J35 sont reportés respectivement sur la broche 6 des connecteurs IDC `J44`/`J45`. Sur ces deux IDC, la broche 1 est GNDA, la broche 10 le rail +5V associé et les broches 2..5, 7..9 sont NC.

Sur le LED Ring, `J4` broche 2 est l'entrée vers D1 et `J5` broche 2 est la sortie de D128. Les LED sont enchaînées en série ; ne pas interpréter les connecteurs comme un bus DOUT.

## Limites et précautions

- La Control Board est une carte de connectique passive : aucun registre à décalage ni décodeur n'y est implanté.
- La carte encodeurs n'embarque pas de 74HC165 ; elle sort 24 nets de contacts vers les bus de lecture.
- Les connecteurs `J14`/`J15` et `J24`/`J25` de l'Encoders Board portent des nets génériques ; ils ne sont pas décrits comme interfaces fonctionnelles ici.
- L'architecture `J34/J35` et les rails séparés +5VA/+5VD doivent être validés électriquement avant câblage.
- Une alimentation LED dédiée, dimensionnée sur la fiche technique de la LED et le courant simultané maximal, est nécessaire ; réunir les masses.
- Le PCB du LED Ring contient encore des chemins absolus vers des modèles 3D locaux non versionnés et présente des violations DRC consignées dans le README parent.

Sources des brochages : nets des trois fichiers `.kicad_pcb` présents dans `control-board/hardware/`, `encoders-board/hardware/` et `led-ring/`. Le schéma historique `hardware/PEC_16_V0.2.kicad_sch` reste la seule source schématique et ne constitue pas trois schémas validés indépendants.
