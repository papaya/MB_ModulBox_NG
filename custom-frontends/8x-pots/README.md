# 8x-pots — Carte 8 potentiomètres rotatifs (AIN)

## Description
Module potentiomètres rotatifs (8 canaux) pour le contrôle de paramètres continus MIDI. Connexion au bus AIN du contrôleur.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/8x-pots/Pot.png)
![3D iso](docs/assets/frontends/8x-pots/Pot-X2.png)

## Spécifications techniques
- 8 potentiomètres rotatifs (10 kΩ)
- Interface AIN (Analog Input) — 8 canaux
- Connecteur : header 24 broches D-Sub

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-------------|
| Potentiomètre | RK09D (10 kΩ) | 8 |
| Connecteur | D-Sub 24 broches | 1 |
| Résistance | 4.7 kΩ pull-up | 8 |
| LED | Vert 5 mm | 8 |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| AIN-1 → AIN-8 | Potentiomètres P1..P8 |
| GND | Masse commune |
| +12V | Alimentation |

## Documentation de fabrication
| Fichier | Contenu |
|---------|---------|
| `production/` | Gerbers, BOM, positions |

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
| `hardware/` | Sources KiCad : `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` (versions Horizontal 1x et 2x, Vertical 1x) |
| `hardware/3D/` | Modèles 3D des potentiomètres (`.wrl`, `.step`) |
| `production/` | Gerbers, BOM (`Pot.csv`), netlist (`.xml`), archives de fabrication |

## Notes d'assemblage / composantes spécifiques
- Potentiomètres rotatifs type Alpha RK09D ou équivalent (empreinte `rk09d1130c1b`)
- Empreintes potentiomètres personnalisées dans `hardware/` et `global-libs/footprints/`
- Fichiers 3D : `Potars_V4.wrl` (boîtier), `Potars_eurorack.step` (montage Eurorack)
- Deux variantes incluses : montage horizontal (1 pot et 2 pots) et montage vertical (1 pot)
- Vérifier le câblage du curseur vers la broche AIN avant mise sous tension
