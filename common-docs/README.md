# common-docs — Documentation générale du projet

Documentation commune à tous les modules de l'écosystème MIDIbox NG.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`bus-midibox-ng.md`](bus-midibox-ng.md) | Schéma de principe des bus AIN / DIN / DOUT, brochage des connecteurs, mapping des front-ends |
| [`connecteurs/`](connecteurs/) | Brochage détaillé des connecteurs de bus communs |
| [`schémas-principe/`](schémas-principe/) | Blocs logiques partagés entre les cartes |

## Bus MIDIbox NG — Résumé

- **AIN** (Analog Input) : lecture de potentiomètres, faders, capteurs — jusqu'à 64 voies multiplexées
- **DIN** (Digital Input) : lecture de boutons, encodeurs, contacts — bascule 74HC165
- **DOUT** (Digital Output) : pilotage d'LED, anneaux LED RGB — bascule 74HC595

> Voir [`bus-midibox-ng.md`](bus-midibox-ng.md) pour le détail complet.

---

**Projet MB_ModulBox_NG — GPL-3.0**