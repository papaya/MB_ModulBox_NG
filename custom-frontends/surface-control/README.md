# surface-control — Surface de contrôle globale (DIN + DOUT + AIN)

## Description
Carte de surface de contrôle combinant plusieurs interfaces (boutons, encodeurs, afficheur) sur une seule PCB. Version V0.1 du prototype global de contrôleur MIDIbox NG.

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](docs/assets/frontends/surface-control/Surface Control V0.1.png)

## Spécifications techniques
- Interface DIN (lecture boutons et encodeurs)
- Interface DOUT (pilotage LEDs et afficheur)
- Interface AIN (potentiomètres et faders)
- GND et +5V communs
- Carte prototype V0.1 — à valider avant fabrication

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Boutons / encodeurs | Selon configuration DIN | plusieurs |
| LEDs | Selon configuration DOUT | plusieurs |
| Potentiomètres / faders | Selon configuration AIN | plusieurs |
| Connecteurs | Headers vers bus DIN, DOUT, AIN | plusieurs |

## Brochage / Mapping MIDIbox NG
| Broche | Signal |
|--------|--------|
| Entrées DIN | Boutons et encodeurs |
| Sorties DOUT | LEDs et afficheur |
| Voies AIN | Potentiomètres et faders |
| GND | Masse commune |
| +5V | Alimentation commune |

## Documentation de fabrication
- `hardware/` : sources KiCad (`Surface Control V0.1.*`)
- `hardware/3D/` : modèle 3D de la carte (`.wrl`, `.step`)
- `production/` : Non disponible (carte prototype non fabriquée)

---

**Rétro-ingénierie par l'équipe — GPL-3.0**
