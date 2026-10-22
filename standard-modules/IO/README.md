# IO — Module Interface MIDI Midi_V0.1 (MIDIbox NG)


## Description
Module de base **IO** (Interface MIDI) de l'ecosysteme MIDIbox NG, equivalent du **MBHP_MIDI_IO**. Il fournit **2 entrees MIDI IN** et **2 sorties MIDI OUT** avec **isolation galvanique par opto-coupleurs**, pour relier le controleur a d'autres equipements MIDI.

> ⚠️ **Attention : le PCB `Midi_V0.1.kicad_pcb` n'est PAS route** (0 piste, 81 pads non connectes). Le schema est complet et correct, mais **la carte n'est pas fabricable en l'etat** : le routage doit etre fait au prealable.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |

![3D top](assets/IO-Midi_V0.1.png)

## Spécifications techniques
- **2 × 6N138** : opto-coupleurs d'**isolation galvanique** pour les **2 MIDI IN**
- **2 × SN74HC00N** (DIP-14) : portes NAND pour la logique de mise en forme / detection de l'activite MIDI OUT
- **4 × connecteur DIN-5** (LEMO5) : `midiIN1`, `midiIN2`, `midiOUT1`, `midiOUT2`
- 4 × LED de temoin (`L7`, `L8`, `L9`, `L10`), 5 mm
- 2 × diode 1N4148 (`D1`, `D2`), 6 × condensateur (2 × 100 nF, 4 × 10 µF)
- Resistances : 220 Ω (LED et limitation), 100 kΩ (pull-up de l'interface MIDI), 4,7 kΩ (bias), 1 kΩ
- 2 × connecteur **IDC 2x05** (`J1`, `J2`) : interface avec le **Core32F4**

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Optocoupleur | 6N138 (DIP-8) | 2 |
| Circuit logique | SN74HC00N (DIP-14) | 2 |
| Connecteur MIDI | DIN-5 / LEMO5 | 4 |
| LED | D5.0mm | 4 |
| Diode | 1N4148 | 2 |
| Condensateur | 100 nF / 10 µF | 6 |
| Résistance axiale | 220 Ω / 100 kΩ / 4,7 kΩ / 1 kΩ | 20 |
| Connecteur | IDC Header 2x05 (`J1`, `J2`) | 2 |
| Empreinte de fixation | MountingHole_3.2mm_M3 | 4 |

## Brochage / Mapping MIDIbox NG

### Connecteurs MIDI
| Connecteur | Fonction |
|------------|----------|
| `midiIN1` | Entree MIDI IN n°1 (via opto-coupleur `IC1`) |
| `midiIN2` | Entree MIDI IN n°2 (via opto-coupleur `IC2`) |
| `midiOUT1` | Sortie MIDI OUT n°1 (via `IC3` = SN74HC00N) |
| `midiOUT2` | Sortie MIDI OUT n°2 (via `IC4` = SN74HC00N) |

### `J1` / `J2` — interface avec le Core32F4
Ce sont les **deux** connecteurs IDC 2x05 du module : ils se branchent sur les entrees/sorties MIDI du **Core32F4** (`J11E`, `J5A`/`J5B` ou connecteurs RS232 selon le schema). Le cablage exact depend de l'affectation des pins GPIO : consulter le schema `Midi_V0.1.kicad_sch` pour le detail.

## Documentation de fabrication
- `hardware/` : sources KiCad (`Midi_V0.1.*`)
- `production/` : Non disponible (PCB non route)

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** — module **MBHP_MIDI_IO** — conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Référence MIDIbox NG — GPL-3.0**> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
