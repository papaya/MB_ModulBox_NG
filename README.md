# MB_ModulBox_NG — Contrôleur MIDI Modulaire (Écosystème MIDIbox NG)


![Bandeau](docs/assets/system/bandeau.jpg)

> **Construisez votre propre contrôleur MIDI modulaire.**  
> MB_ModulBox_NG rassemble des front-ends originaux et des ré-implémentations KiCad de modules MIDIbox. Les niveaux de validation et les fichiers de fabrication disponibles varient d'une carte à l'autre : consulter la matrice ci-dessous avant toute commande.

[![Licence à clarifier](https://img.shields.io/badge/Licence-%C3%A0%20clarifier-lightgrey)](#licences-cr%C3%A9dits-et-conditions-dutilisation)
[![KiCad 8 et 9](https://img.shields.io/badge/KiCad-8%20%7C%209-blueviolet)](https://kicad.org/)
[![Hardware : revue requise](https://img.shields.io/badge/Hardware-revue%20requise-orange)](PLAN.md)

---

## 🎯 Le projet en bref

MB_ModulBox_NG est une **bibliothèque de cartes de contrôle physiques** pour le système MIDIbox NG. Les sources, schémas, PCB et fichiers de fabrication ne sont pas tous disponibles pour chaque carte. Les états indiqués ci-dessous décrivent les fichiers présents dans le dépôt, pas une certification de fabrication.

Les **modules standards MIDIbox** (AIN, DIN, DOUT, Core, IO) sont fournis en **bonus de référence** pour alimenter ces front-ends — ils ne sont pas le cœur du projet. L'essence de ce dépôt, ce sont les **`custom-frontends/`**.

## 🧩 Les modules: Custom Front-ends — le cœur du dépôt

| Apercu | Module | Dossier | Fonction / bus | Fichiers de fabrication versionnés | État documentaire |
|---|---|---|---|---|---|
| ![Encodeurs](custom-frontends/encoders-led-rgb/assets/Screenshot%202023-05-19%20175512.png)  | encoders-led-rgb | [`custom-frontends/encoders-led-rgb/`](custom-frontends/encoders-led-rgb/) | 8 PEC16, DIN, 128 WS2812 | BOM/positions/netlist uniquement ; pas de Gerbers de sous-cartes | Prototype ; DRC et séparation à revoir |
| ![Faders](custom-frontends/4x-faders/assets/3d%203quart.png)  | 4x-faders | [`custom-frontends/4x-faders/`](custom-frontends/4x-faders/) | 8 faders, AIN (`+3V0`) | Gerbers + perçages pour deux PCB ; pas de BOM dans `production/` | Fichiers disponibles, non certifiés |
|  ![keysw](custom-frontends/keysw-4x2/assets/MB-KeySW_4x2_V0.33quart.png)  | keysw-4x2 | [`custom-frontends/keysw-4x2/`](custom-frontends/keysw-4x2/) | 8 touches, DIN + 8 SK6812 adressables | BOM/positions/netlist ; pas de Gerbers | Sources à vérifier avant fabrication |
| ![Pots](custom-frontends/8x-pots/assets/pot4x2.png) | 8x-pots | [`custom-frontends/8x-pots/`](custom-frontends/8x-pots/) | 8 potentiomètres, AIN (`+3V0`) | Gerbers + perçages ; exports BOM/netlist | Variante Pot-X2 à vérifier séparément |
| ![Boutons](custom-frontends/8x-buttons/assets/Screenshot%202023-05-19%20163416.png) | 8x-buttons | [`custom-frontends/8x-buttons/`](custom-frontends/8x-buttons/) | 8 boutons et 8 LED, DIN + DOUT | Gerbers + perçages + BOM | Fichiers disponibles, non certifiés |
|  ![Pads](custom-frontends/pad-rgb/assets/Pad.png)  | pad-rgb | [`custom-frontends/pad-rgb/`](custom-frontends/pad-rgb/) | 8 contacts, DIN + 8 WS2812 en cascade adressable | Positions + datasheet ; pas de Gerbers/BOM | non fonctionel , rebond , a coriger |
|  ![OLED](custom-frontends/oled-128x64/assets/Oled_1309_x1_V0.0.png)  | oled-128x64 | [`custom-frontends/oled-128x64/`](custom-frontends/oled-128x64/) | SSD1309, SPI | BOM/positions/netlist ; pas de Gerbers | Sources à vérifier avant fabrication |
|  ![cartepuissance](custom-frontends/carte-puissance/assets/Carte_puissance.png)  | carte-puissance | [`custom-frontends/carte-puissance/`](custom-frontends/carte-puissance/) | Distribution passive des rails | BOM/positions/netlist + PDF ; pas de Gerbers | Vérifier courant et routage |
|  ![surface](custom-frontends/surface-control/assets/Surface%20Control%20V0.1.png)  | surface-control | [`custom-frontends/surface-control/`](custom-frontends/surface-control/) | SCS sur GPIO Core32F4 | Aucun fichier de production | Prototype non routé |

## Modules standards MIDIbox — ré-implémentations KiCad

| Type | Module | Dossier | Référence ucapps.de | Fichiers de fabrication versionnés |
|---|---|---|---|---|
| ![Core32](standard-modules/Core/assets/Core-Core32F4.png)  | Core32F4 | [`standard-modules/Core/`](standard-modules/Core/) | [CORE_STM32F4](https://www.ucapps.de/mbhp_core_stm32f4.html) | BOM/positions/netlist ; pas de Gerbers |
| ![ain](standard-modules/AIN/assets/) | AIN / AINSER64 | [`standard-modules/AIN/`](standard-modules/AIN/) | [AINSER64](https://www.ucapps.de/mbhp_ainser64.html) | Sources KiCad et fichiers de production absents |
| ![din](standard-modules/DIN/assets/DIN-DIN4_R5_KS.png) | DIN | [`standard-modules/DIN/`](standard-modules/DIN/) | [DIN](https://www.ucapps.de/mbhp_din.html) | Gerbers + perçages + BOM |
| ![dout](standard-modules/DOUT/assets/DOUT-DOUT.png) | DOUT | [`standard-modules/DOUT/`](standard-modules/DOUT/) | [DOUT](https://www.ucapps.de/mbhp_dout.html) | BOM/positions/netlist ; pas de Gerbers |
| ![io](standard-modules/IO/assets/IO-Midi_V0.1.png) | MIDI IO | [`standard-modules/IO/`](standard-modules/IO/) | [MIDIbox NG Hardware](https://www.ucapps.de/midibox_ng_manual_hw.html) | Pas de fichiers de fabrication ; PCB non routé |
---
![3D quart](docs/assets/system/vue%20ensemble.jpg)
---


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
   - Vérifiez d'abord que la matrice ci-dessus indique des Gerbers et perçages pour la carte choisie.
   - Ouvrez les Gerbers dans un visualiseur indépendant et comparez-les au PCB KiCad avant commande.
   - Ne commandez pas une carte marquée prototype, non routée ou sans Gerbers ; un BOM/netlist seul n'est pas un jeu de fichiers de fabrication.
   - Les modèles 3D et fichiers sources supplémentaires, lorsqu'ils existent, sont sur l'[archive Google Drive](https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing).

## Guide maker : assemblage et commande des PCB

1. Choisissez un module dont la matrice indique des Gerbers et lisez son README avant de fabriquer.
2. Vérifiez le nombre de couches, le contour, les ouvertures de masque, les perçages PTH/NPTH et l'orientation des composants dans les fichiers de production.
3. Transmettez au fabricant les couches et fichiers de perçage publiés pour la carte choisie. Ne modifiez pas l'épaisseur de cuivre, le stack-up ou les dimensions sans revoir les contraintes électriques et mécaniques.
4. Utilisez la BOM et le fichier de positions uniquement s'ils sont publiés pour cette carte ; comparez références, valeurs et empreintes avec le schéma KiCad.
5. Assemblez hors tension, contrôlez les courts-circuits d'alimentation au multimètre, puis alimentez avec une alimentation limitée en courant.
6. Pour les cartes WS2812, utilisez une alimentation 5 V dimensionnée pour la charge et une masse commune. Le Core ne fournit pas l'alimentation des LED.

La présence de Gerbers ne certifie pas une carte ni ne garantit l'absence de défauts. Consultez les avertissements DRC/ERC et les limites propres à chaque README.


## 📦 Contenu de ce dépôt Git (et ce qui n'y est pas)

Ce dépôt est **allégé** pour rester léger et rapide à cloner. Sont versionnés :

| ✅ Inclus | Détail |
|---------|--------|
| Schémas KiCad | `.kicad_sch`, `.kicad_pro` (sources de conception) |
| PCB KiCad | `.kicad_pcb` (fichiers de routage) |
| Gerbers / perçages | Seulement pour les modules explicitement marqués dans la matrice ci-dessus |
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


---

## ⚡ Modules standards MIDIbox (bonus de référence)

Ces modules standards alimentent les front-ends en bus AIN / DIN / DOUT. Ils sont fournis à titre de référence — ce ne sont pas la raison d’être de ce dépôt.

| Module | Bus | Rôle | Détail |
|--------|-----|------|--------|
| AIN | AIN (SPI `J19`) | Entrées analogiques (64 voies, AINSER64) | [📄 README](standard-modules/AIN/README.md) — ⚠️ **sources KiCad absentes** |
| DIN | DIN (`J8J9`) | 32 entrées digitales (4 × 74HC165) | [📄 README](standard-modules/DIN/README.md) |
| DOUT | DOUT (`J8J9`) | 32 sorties digitales (4 × 74HC595) | [📄 README](standard-modules/DOUT/README.md) |
| Core | — | Cœur STM32F4 (Core32F4), 4 lignes WS2812 | [📄 README](standard-modules/Core/README.md) |
| IO | MIDI | Interface MIDI 2 IN / 2 OUT (6N138) | [📄 README](standard-modules/IO/README.md) — ⚠️ **PCB non routé** |

---
> ⚠️ **Note importante sur les LEDs RGB WS2812/WS2812B :** Les cartes `encoders-led-rgb`, `pad-rgb` et `keysw-4x2` utilisent des LEDs adressables qui se connectent en **1 fil de données sur une sortie WS2812 du Core STM32F4** (`J4A` broches 6/8 = PB10/PB11, `J4B` broches 6/8 = **PB6 (TIM4)**/PB9) — **PAS** sur le bus DOUT (74HC595). Voir les README respectifs et [spécifications WS2812 MIOS32](https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html).
>
> ℹ️ Sur les cartes encodeurs, pads et clavier, les LED sont montées **en cascade série** et adressables individuellement depuis une ligne de données.
---
## Licences, crédits et conditions d'utilisation

Ce dépôt contient deux catégories de matériel distinctes :

### 1. Modules standards officiels (`standard-modules/`)
**Core, AIN, DIN, DOUT, IO** — Ces modules sont des ré-implémentations sous KiCad basées sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / ucapps.de**.  
Crédits : Thorsten Klose & ucapps.de.  
Usage : strictement personnel, éducatif et DIY — **Non-Commercial**.

### 2. Modules et front-ends originaux (`custom-frontends/`)
**4x-faders, 8x-pots, 8x-buttons, encoders-led-rgb, pad-rgb, keysw-4x2, carte-puissance, oled-128x64, surface-control** — Cartes d'interface originales conçues pour l'écosystème **MB MODULBOX NG**, compatibles selon leur README avec les bus et modules MIDIbox NG.  
Usage indiqué dans les README : DIY/personnel ; les conditions de redistribution et d'utilisation commerciale restent à formaliser.

> **Licence non publiée :** le dépôt ne contient actuellement aucun fichier `LICENSE`. Les conditions applicables aux ré-implémentations des modules MIDIbox et aux créations originales doivent être clarifiées séparément avant toute redistribution ou utilisation commerciale. Les mentions DIY/non-commercial des README ne remplacent pas une licence formelle.

> **Badge OSHWA non affiché :** une restriction non-commerciale n'est pas une licence open-source matérielle conforme à la définition OSHWA. Il faut d'abord publier des conditions cohérentes, avec attribution et périmètre distincts pour les dérivés MIDIbox et les créations originales.

La documentation de brochage des bus s'appuie sur les pages officielles [MIDIbox NG Hardware](https://www.ucapps.de/midibox_ng_manual_hw.html), [DIN](https://www.ucapps.de/mbhp_din.html), [DOUT](https://www.ucapps.de/mbhp_dout.html), [AINSER64](https://www.ucapps.de/mbhp_ainser64.html) et [Core STM32F4](https://www.ucapps.de/mbhp_core_stm32f4.html). Les brochages des cartes custom sont décrits à partir des sources KiCad locales ; ne pas extrapoler le brochage officiel à un connecteur custom sans vérification.

---

## Documentation

- 📄 [`common-docs/README.md`](common-docs/README.md) — Hub de la documentation générale
- 📄 [`common-docs/bus-midibox-ng.md`](common-docs/bus-midibox-ng.md) — Schéma de principe des bus AIN, DIN et DOUT de MIDIbox NG
- 📁 [`common-docs/connecteurs/`](common-docs/connecteurs/) — Brochage détaillé des connecteurs de bus
- Chaque module standard et chaque front-end possède un README dans son dossier, avec ses limites et les fichiers disponibles
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
> Les droits et conditions de redistribution ne sont pas établis par ce dépôt tant qu'un fichier de licence n'est pas publié. Ce projet **n'est pas un support technique, ni un service de conception, ni une référence industrielle**.

---

## Contribuer

Consulter [`CONTRIBUTING.md`](CONTRIBUTING.md) avant de proposer une modification. Les signalements de défauts matériels doivent inclure le chemin du projet, la version de KiCad, le rapport DRC/ERC et les fichiers Gerber concernés.

---

**Crédits des modules standards :** Thorsten Klose & ucapps.de.  
**Conception des front-ends :** MB MODULBOX NG.> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage, routage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension. Le détail complet de l'avertissement figure en fin de fichier.
