# MB_ModulBox_NG — Contrôleur MIDI Modulaire (Écosystème MIDIbox NG)

![Bandeau](docs/assets/system/bandeau.jpg)

> **Construisez votre propre contrôleur MIDI modulaire.**  
> MB_ModulBox_NG est une collection de **cartes d'interface physiques (front-ends)** custom — faders, potentiomètres, boutons, pads RGB, encodeurs, afficheur OLED, clavier, alimentation — conçues pour se brancher sur l'écosystème **MIDIbox NG**.

[![Licence: GPL-3.0](https://img.shields.io/badge/Licence-GPL--3.0-blue.svg)](LICENSE)
[![KiCad](https://img.shields.io/badge/KiCad-9-blueviolet)](https://kicad.org/)
[![Statut: Actif](https://img.shields.io/badge/Statut-En%20développement-green)](PLAN.md)  

---

## 🎯 Le projet en bref

MB_ModulBox_NG, c'est avant tout une **bibliothèque de cartes de contrôle physiques** pour le système MIDIbox NG. Chaque carte est un PCB KiCad complet (schéma, routage, gerbers) prêt à être fabriqué, avec sa documentation d'assemblage.

Les **modules standards MIDIbox** (AIN, DIN, DOUT, Core, IO) sont fournis en **bonus de référence** pour alimenter ces front-ends — ils ne sont pas le cœur du projet. L'essence de ce dépôt, ce sont les **`custom-frontends/`**.

## 🧩 Custom Front-ends — le cœur du dépôt

| Carte | Aperçu | Bus | Rôle | État | Doc |
|-------|--------|-----|------|------|-----|
| 4x-faders | ![Faders](custom-frontends/4x-faders/assets/Fad_1.png) | AIN | Glissières / faders | ✅ Terminé | [📄 README](custom-frontends/4x-faders/README.md) |
| 8x-pots | ![Pots](custom-frontends/8x-pots/assets/Pot.png) | AIN | 8 potentiomètres rotatifs | ✅ Terminé | [📄 README](custom-frontends/8x-pots/README.md) |
| 8x-buttons | ![Boutons](custom-frontends/8x-buttons/assets/BP.png) | DIN | 8 boutons poussoirs | ✅ Terminé | [📄 README](custom-frontends/8x-buttons/README.md) |
| encoders-led-rgb | ![Encodeurs](custom-frontends/encoders-led-rgb/assets/PEC_16_V0.2.png) | DIN + DOUT | Encodeurs avec anneau LED RGB | 🟠 En cours | [📄 README](custom-frontends/encoders-led-rgb/README.md) |
| pad-rgb | ![Pads](custom-frontends/pad-rgb/assets/Pad.png) | DIN + DOUT | Pads rétroéclairés RGB WS2812 | ✅ Terminé | [📄 README](custom-frontends/pad-rgb/README.md) |
| oled-128x64 | ![OLED](custom-frontends/oled-128x64/assets/Oled_1309_x1_V0.0.png) | I2C / SPI | Afficheur OLED 128x64 | ✅ Terminé | [📄 README](custom-frontends/oled-128x64/README.md) |
| keysw-4x2 | ![Clavier](custom-frontends/keysw-4x2/assets/MB-KeySW_4x2_V0.3.png) | DIN | Clavier matricé 4x2 touches | ✅ Terminé | [📄 README](custom-frontends/keysw-4x2/README.md) |
| carte-puissance | ![Alim](custom-frontends/carte-puissance/assets/Carte_puissance.png) | — | Alimentation / distribution | ✅ Terminé | [📄 README](custom-frontends/carte-puissance/README.md) |
| surface-control | ![Surface](custom-frontends/surface-control/assets/Surface%20Control%20V0.1.png) | DIN + DOUT + AIN | Surface de contrôle globale | 🟡 Prototype V0.1 | [📄 README](custom-frontends/surface-control/README.md) |

---
## 🚀 Démarrage rapide

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/papaya/MB_ModulBox_NG.git
   cd MB_ModulBox_NG
   ```

2. **Ouvrir un front-end dans KiCad**
   - Choisissez une carte dans `custom-frontends/` (ex: `4x-faders/`)
   - Ouvrez le fichier `.kicad_pro` avec KiCad (v9 recommandé)

3. **Lier les bibliothèques partagées**
   - `sym-lib-table` → `Mes_Librairies_KiCad/symbols/`
   - `fp-lib-table` → `Mes_Librairies_KiCad/footprints/`
   (chemins relatifs via `${KIPRJMOD}`)

4. **Fabriquer**
   - Les fichiers de production (gerbers, perçages) se trouvent dans `custom-frontends/<carte>/production/`
   - Les modèles 3D et sources brutes sont sur l'[archive Google Drive](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing) (non versionnés sur GitHub pour poids)


## 📦 Contenu de ce dépôt Git (et ce qui n'y est pas)

Ce dépôt est **allégé** pour rester léger et rapide à cloner. Sont versionnés :

| ✅ Inclus | Détail |
|---------|--------|
| Schémas KiCad | `.kicad_sch`, `.kicad_pro` (sources de conception) |
| PCB KiCad | `.kicad_pcb` (fichiers de routage) |
| Gerbers / perçages | `custom-frontends/*/production/` (fichiers de fabrication des cartes courantes) |
| Bibliothèques partagées | `Mes_Librairies_KiCad/` (symboles `.kicad_sym` + empreintes `.pretty`) |
| Documentation & rendus | `README.md`, `PLAN.md`, `common-docs/`, `docs/assets/` (vues 3D en PNG) |
| Outils | `tools/` (scripts de nettoyage, extraction, validation) |

| ❌ Non versionné | Raison |
|------------------|--------|
| `*.wrl`, `*.stl`, `*.step`, `*.FCStd`, `*.dxf` | **CAO 3D volumineuse** (fichiers SolidWorks / Blender / FreeCAD / Wrl) — inutile pour KIcad, mais dépasse la limite de taille de GitHub |
| `archive/sources/` | **Copie brute de sauvegarde** (2,9 Go) des sources d'origine, en doublon — les versions maîtresses sont dans `standard-modules/` et `custom-frontends/` |
| `*.zip` | Archives de fabrication compressées — contenu identique aux gerbers présents |
| Fichiers de cache KiCad | `.kicad_prl`, `.bak`, `__pycache__` — régénérables |

> 📥 **Les fichiers 3D et les sources complètes** sont disponibles via l'archive Google Drive : [ALL FILES — Archive complète](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing)
>
> Les modèles 3D manquants peuvent aussi être récupérés via **kicad-cli / KiCad 3D Viewer** directement depuis les bibliothèques officielles (kicad-footprints, kicad-symbols).
---
![3D quart](docs/assets/system/WIP.jpg)
---

## 📖 Articles et ressources du blog ksir-diy.blogspot.com

| Article du blog | Thème | Lien |
|-----------------|-------|------|
| [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) | Présentation globale du projet (mai 2023) | [Voir sur le blog](https://ksir-diy.blogspot.com/) |
| [ALL FILES — Archive complète](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing) | Tous les fichiers de fabrication, schémas, Gerbers | [Google Drive](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing) |

**Articles par carte :**
| Carte | Article du blog | Dossier |
|-------|----------------|---------|
| 4X2-POTS-v0.2 | Potentiomètres rotatifs | [`8x-pots`](custom-frontends/8x-pots/README.md) |
| 4X1-FAD-1-v0.2 / 4X1-FAD-2-v0.2 | Faders / glissières | [`4x-faders`](custom-frontends/4x-faders/README.md) |
| 4x2-BPL-v0.2 | Boutons poussoirs | [`8x-buttons`](custom-frontends/8x-buttons/README.md) |
| 4X2-PADS-RGB | Pads rétroéclairés RGB WS2812 | [`pad-rgb`](custom-frontends/pad-rgb/README.md) |
| 4X2 ENC-SW-16-LED-RING-RGB (PEC16) | Encodeurs avec anneau LED RGB | [`encoders-led-rgb`](custom-frontends/encoders-led-rgb/README.md) |

> ⚠️ L'article *"4X2 ENC-SW-16-LED-RING-RGB (PEC16)"* est marqué comme **"non terminé, ne fonctionne pas"** sur le blog. Les sources sont néanmoins disponibles pour référence.

---

## ⚡ Modules standards MIDIbox (bonus de référence)

Ces modules standards alimentent les front-ends en bus AIN / DIN / DOUT. Ils sont fournis à titre de référence — ce ne sont pas la raison d’être de ce dépôt.

| Module | Bus | Rôle | Détail |
|--------|-----|------|--------|
| AIN | AIN | Entrées analogiques (64 voies) | [📄 README](standard-modules/AIN/README.md) |
| DIN | DIN | Entrées digitales (DIN4_R5_KS) | [📄 README](standard-modules/DIN/README.md) |
| DOUT | DOUT | Sorties digitales | [📄 README](standard-modules/DOUT/README.md) |
| Core | — | Cœur STM32F4 (Core32F4) | [📄 README](standard-modules/Core/README.md) |
| IO | MIDI | Interface MIDI IN/OUT | [📄 README](standard-modules/IO/README.md) |

---

## Licences, crédits et conditions d'utilisation

Ce dépôt contient deux catégories de matériel distinctes :

### 1. Modules standards officiels (`standard-modules/`)
**Core, AIN, DIN, DOUT, IO** — Ces modules sont des ré-implémentations sous KiCad basées sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / ucapps.de**.  
Crédits : Thorsten Klose & ucapps.de.  
Usage : strictement personnel, éducatif et DIY — **Non-Commercial**.

### 2. Modules et front-ends originaux (`custom-frontends/`)
**4x-faders, 8x-pots, 8x-buttons, encoders-led-rgb, pad-rgb, keysw-4x2, carte-puissance, surface-control** — Cartes d'interface originales conçues sur mesure pour l'écosystème **MB MODULBOX NG**, compatibles avec les bus et modules du système MIDIbox NG.  
Usage : Open-Source Hardware pour un usage DIY / personnel / non-commercial.

> Tous les fichiers de ce dépôt sont fournis à titre documentaire et pédagogique, sans garantie ni support technique. Voir l'avertissement en tête de ce fichier.

---

## Documentation

- 📄 [`common-docs/README.md`](common-docs/README.md) — Hub de la documentation générale
- 📄 [`common-docs/bus-midibox-ng.md`](common-docs/bus-midibox-ng.md) — Schéma de principe des bus AIN, DIN et DOUT de MIDIbox NG
- 📁 [`common-docs/connecteurs/`](common-docs/connecteurs/) — Brochage détaillé des connecteurs de bus
- Chaque front-end possède son propre [`README.md`](custom-frontends/) avec son brochage et ses notes d'assemblage
- 🖼️ [`docs/assets/`](docs/assets/) — Rendus 3D des PCB (vues top et isométrique)
- 🗺️ [`PLAN.md`](PLAN.md) — Feuille de route complète du projet (phases 0-10)
---
Retrouvez plus de photos sur **[Ksir DIY'S](https://ksir-diy.blogspot.com/)** — article principal : *"ModulBox V2" (mai 2023)*.

---
![3D quart](docs/assets/system/pied%20de%20page.jpg)
---


## ⚠️ Avertissement

> **Ce projet n'est pas réalisé par un professionnel.** Les fichiers schématiques, PCB, gerbers et documentations publiés ici sont issus d'un travail amateur, réalisé sur mon temps libre, à des fins personnelles et pédagogiques uniquement.
>
> **L'utilisation de ces fichiers ne m'engage à rien.** Aucune garantie de conformité, de sécurité, de fonctionnalité n'est donnée, ni implicitement ni explicitement.
>
> **Il peut y avoir des erreurs** : schématiques incomplètes, erreurs de routage, valeurs de composants inadaptées, impédances non respectées, alimentation insuffisante, isolation électrique non garantie, défauts de sérigraphie, etc. Certaines cartes listées ici sont explicitement marquées comme **non fonctionnelles** ou non testées.
>
> **À vos risques et périls.** Vous êtes seul responsable de la fabrication, de l'assemblage, de la mise sous tension et de l'utilisation des fichiers de ce dépôt. Vérifiez systématiquement les schémas, les contraintes de fabrication (épaisseurs de cuivre, empilages, clearances), les chaînages de masse et les tensions avant de fabriquer.
>
> Ce dépôt est partagé à titre documentaire et open-source (GPL-3.0) dans l'esprit de l'écosystème MIDIbox NG, mais **n'est pas un support technique, ni un service de conception, ni une référence industrielle**.

---

## Contribuer

1. Consulter `PLAN.md` pour la feuille de route détaillée
2. Chaque modification de front-end doit être accompagnée de son `README.md`
3. Vérifier que les chemins KiCad restent relatifs avant tout commit
4. Les anciennes versions sont conservées dans `archive/` (ne pas supprimer sans validation)

---

**Licence :** GPL-3.0 — Open Source Hardware  
**Rétro-ingénierie et structuration :** Équipe MB_ModulBox_NG
