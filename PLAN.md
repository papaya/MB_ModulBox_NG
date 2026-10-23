# PLAN.md — Réorganisation du projet hardware MB_ModulBox_NG

---
**Statut :** Plan de rangement — ÉTAPES 1-5 TERMINÉES + RÉCONCILIATION MODULES STANDARDS + **PUBLICATION GITHUB (allègement du dépôt)**  
**Dernière mise à jour :** 21/10/2026  
**Résumé :** Arborescence créée, fichiers parasites supprimés, modules standards réconciliés (versions maîtresses identifiées), 9 front-ends déplacés et documentés, README principal rédigé, assets 3D générés, doc bus rédigée. **Avertissement « non professionnel » ajouté au README. Dépôt Git allégé (CAO 3D + `archive/sources/` exclus) et historique purgé : `.git` 3,9 Go → 24 Mo.**

---

## 10. PUBLICATION GITHUB — Allègement du dépôt (TERMINÉ ✅)

Date : 21/10/2026. Objectif : publier le projet sur GitHub sans dépasser les limites de taille de GitHub (100 Mo/fichier, 5 Go/dépôt).

### 10.1 Diagnostic
| Élément | Avant | Après |
|---------|-------|-------|
| Taille de `.git` | **3,9 Go** (1,39 Go d'objets loose + 2 072 sidecars macOS `._*`) | **24 Mo** |
| Pack Git | 640 Mo | **8,5 Mo** |
| Fichiers suivis | 1 439 | **295** |
| Taille de l'index | ~700 Mo | **29,7 Mo** |
| Plus gros fichier | 203 Mo (`Assemblage2.SLDASM`) | **2,93 Mo** (`Core32F4.kicad_sch`) |

### 10.2 Actions effectuées
- [x] `.gitignore` étendu : `*.wrl`, `*.stl`, `*.step`, `*.FCStd`, `*.dxf`, `*.blend`, `*.sldprt/sldasm`, `archive/sources/`, `archive/**/production/`, `*.zip`
- [x] Retrait de l'index de la CAO 3D et des copies brutes (fichiers **conservés sur le disque**, uniquement non versionnés)
- [x] Purge de l'historique avec `git-filter-repo` (`--invert-paths` sur `archive/sources`, `MB MODULBOX NG`, `MB Hardware` + `--path-glob` sur toutes les extensions CAO)
- [x] Nettoyage des sidecars AppleDouble `._*` (le volume exFAT en recrée → `git gc` échouait avec « non-monotonic index »)
- [x] `core.fileMode false` (exFAT force le bit exécutable → 295 fichiers faussement « modifiés »)
- [x] Vérification bit-à-bit : les 295 fichiers suivis sont identiques entre le dépôt filtré et le working tree
- [x] Contrôle GitHub : aucun fichier > 50 Mo (limite 100 Mo) ✅
- [x] README : avertissement « non professionnel / aucune garantie » + section « Contenu de ce dépôt Git (et ce qui n'y est pas) »
- [x] Push `origin/main` (force-push : l'historique distant « Add files via upload » n'avait aucun ancêtre commun et ne contenait que 55 fichiers, tous déjà présents en local)

### 10.3 Contenu conservé dans le dépôt
Schémas + PCB KiCad (`.kicad_sch`, `.kicad_pro`, `.kicad_pcb`), gerbers/perçages de production, `Mes_Librairies_KiCad/` (symboles + empreintes), documentation (`README.md`, `PLAN.md`, `common-docs/`, `docs/assets/` en PNG), `tools/`.

### 10.4 Contenu exclu (récupérable via Google Drive)
CAO 3D (SolidWorks / Blender / FreeCAD / Wrl / STL / STEP), `archive/sources/` (copie brute de sauvegarde, 2,9 Go), archives ZIP de fabrication, caches KiCad.
→ Archive : https://drive.google.com/drive/folders/1vpTdcTHLqAW1HyvYF8Y5nkU0c3LeNErb?usp=sharing

---

## 1. Constat d'audit (état actuel)

### 1.1 Deux grandes branches racines
| Dossier | Rôle | État |
|---------|------|------|
| `MB Hardware/` | Modules standards MIDIbox (AINSER64, Core32f4, DIN4_R5_KS, DOUT, Midi IO…) | Déjà structurés par module, mais backups, Gerbers, `.bak`, `._*` et `.DS_Store` mélangés aux sources. |
| `MB MODULBOX NG/` | Cartes additionnelles / front-ends (sujet de ce plan) | **Complètement désordonné** : doublons `2023/KICAD 7` vs `2023/KICAD_6` vs `Kicad`, versions KiCad 6/7/8/9 mêlées, dossiers `TEST_NOT_WORKING`, `TEMP/EXPORT`, backups horodatés, fichiers 3D/CAO (Blender, FreeCAD, SolidWorks), BOM xlsx à la racine, datasheets éparpillées. |

### 1.2 Front-ends identifiés dans `MB MODULBOX NG/` (inventaire partiel)
`FADER` / `Fad_1`, `Fad_2` — glissières ; `POTS` / `Pot`, `Pot-X2` (Horizontal, Vertical) — potentiomètres (AIN) ; `BP` / `MB-BPs-4x2CS` — boutons poussoirs (DIN) ; `CONTROL` / `Surface Control V0.0`, `V0.1` ; `Encoder with led ring RGB` / `PEC_16_V0.2`, `Encoder switch`, `Led_Ring_RGB` ; `encoder led ring NO rgb` / `Led ring NO rgb`, `encoders` ; `Pad RGB` / `Pad`, `WS2812-2020` ; `carte puissance` / `Carte_puissance` ; `Oled` / `Oled_1309_x1_V0.0` ; `MB-KeySW_4x2_V0.1` / `MB-KeySW_4x2_V0.3` ; `AINSER64_DIN_DOUT`, `DIN_DOUT`, `DOUT` — doublons de modules standards.

### 1.3 Fichiers à classer comme « temporaires / inutiles » (polluants)
`._*` (AppleDouble macOS), `.DS_Store` ; `*.bak`, `*.kicad_pcb-bak`, `*.kicad_pro-bak`, `*.sch-bak`, `*-backups/` ; `__autosave-*`, `_autosave-*`, `#auto_saved_files#/` ; `fp-info-cache` (cache d'empreintes KiCad) ; `.kicad_prl` / `.kicad_lock` (préférences locales / verrous — à exclure du versioning) ; `*.zip` exports anciens ; Gerbers dupliqués à la racine des dossiers source ; fichiers CAO mécanique hors périmètre (`.wrl`, `.step`, `.stl`, `.blend`, `.FCStd`, `.dxf`) sauf référence façade liée.

### 1.5 Cartographie finale des modules standards (après réconciliation 18/10/2026)

| Module | Dossier cible | Fichiers | Version maître | Source d'origine | État |
|--------|--------------|----------|----------------|------------------|------|
| **AIN** | `standard-modules/AIN/` | Vide (fichier explicatif uniquement) | Aucune | `MB Hardware/AINSER64/` — **dossier vide** | ⚠️ Source manquante, à retrouver |
| **DIN** | `standard-modules/DIN/` | `DIN4_R5_KS.*` (3 fichiers) | DIN4_R5_KS (version complète) | `MB MODULBOX NG/` (provenance mixte) | ✅ Cohérent |
| **DOUT** | `standard-modules/DOUT/` | `DOUT.*` (3 fichiers) | **Dout2024** (version complète) | `MB Hardware/DOUT/DOUT2024/Dout2024/` | ✅ Version basculée (ancienne DOUT`_2024 archivée) |
| **Core** | `standard-modules/Core/` | `Core32F4.*` (3 fichiers) | **Core32f4_V0.1** (version complète) | `MB Hardware/Core32f4/Core32f4_V0.1/` | ✅ Version basculée (V4 et core32V7 archivés) |
| **IO** | `standard-modules/IO/` | `Midi_V0.1.*` (3 fichiers) | Midi_V0.1 | `MB Hardware/Midi IO/` — **dossier vide de sources** | ⚠️ Source fichiers manquants, copie conservée |

**Décisions clés de la réconciliation :**
- **Core32F4** = `Core32f4_V0.1` (schéma 3 MB + PCB 1.3 MB, ERC 122, DRC 66, 0 non connectés) — supérieure à V4 (443 DRC) et core32V7 (455 DRC, sans schéma)
- **DOUT** = `Dout2024` (schéma 117 kB + PCB complet) — supérieure à DOUT`_2024 (PCB sans schéma)
- **AIN** : `MB Hardware/AINSER64/` est vide, aucun fichier `.kicad_*` trouvé. Le module AIN doit être recréé ou ses sources retrouvées.
- **IO** : `MB Hardware/Midi IO/` ne contient qu'un `.jpg` et un `.kicad_prl`. Les fichiers `Midi_V0.1.*` dans la cible proviennent d'une copie antérieure.

## 2. Arborescence cible

```
MB_ModulBox_NG/
├── PLAN.md                     # Ce document (feuille de route)
├── README.md                   # Présentation du projet global, arbre, comment contribuer
├── .gitignore                  # Exclusion des polluants KiCad et macOS
├── common-docs/                # Documentation générale + bus MIDIbox NG
│   ├── README.md
│   ├── bus-midibox-ng.md       # Schéma de principe des bus AIN / DIN / DOUT
│   ├── connecteurs/            # Brochage des connecteurs de bus communs
│   └── schémas-principe/       # Blocs logiques partagés
├── global-libs/                # Bibliothèques partagées (symboles + empreintes)
│   ├── symbols/                # *.kicad_sym
│   └── footprints/             # *.pretty
├── standard-modules/           # Modules de base centralisés (copie de référence)
│   ├── AIN/
│   ├── DIN/
│   ├── DOUT/
│   └── ...                     # À alimenter depuis MB Hardware/ en phase ACT
└── custom-frontends/           # Nos cartes additionnelles de contrôle
    ├── 4x-faders/              # Ex: carte faders (glissières)
    │   ├── hardware/           # .kicad_pro, .kicad_sch, .kicad_pcb (trio maître)
    │   ├── libs/               # Symboles/empreintes spécifiques à cette carte (si pas dans global-libs)
    │   │   ├── symbols/
    │   │   └── footprints/
    │   ├── production/         # Gerbers, BOM, fichiers de fabrication, correspondance broches vers DIN/AIN
    │   ├── mechanical/         # 3D, façades (uniquement ce qui est réellement utilisé par le PCB)
    │   └── README.md           # Spécificités de câblage sur le bus, version de référence, limitations
    ├── 8x-pots/                # Potentiomètres rotatifs (AIN)
    │   ├── hardware/
    │   ├── production/
    │   └── README.md
    ├── 8x-buttons/             # Boutons poussoirs (DIN)
    │   ├── hardware/
    │   ├── production/
    │   └── README.md
    ├── encoders-led-rgb/       # Encodeurs avec anneau LED RGB
    ├── pad-rgb/                # Pads rétroéclairés RGB (WS2812)
    ├── oled-128x64/            # Afficheur OLED
    ├── keysw-4x2/              # Clavier 4x2 touches
    └── carte-puissance/        # Alimentation / distribution
├── archive/                    # Versions figées à ne plus toucher (KICAD_6, doublons, TEST_NOT_WORKING)
│   ├── 2023-KICAD-6/
│   ├── 2023-KICAD-7-doublons/
│   └── experimental/
└── tools/                      # Scripts de nettoyage / validation (optionnel)
```

> **Nomenclature :** noms de dossiers en minuscules, séparés par tirets, sans espaces ni caractères spéciaux. Les noms de fichiers KiCad conservent leur cas d'origine pour éviter de casser les liens internes.

## 3. Règles de tri et de déploiement (sécurité KiCad)

### 3.1 Règle d'or : ne jamais séparer le trio `.kicad_pro` + `.kicad_sch` + `.kicad_pcb`
Un projet KiCad est lié par ces trois fichiers. Déplacer l'un sans les deux autres rompt le projet. Ils doivent toujours voyager ensemble dans le même dossier `hardware/`.

### 3.2 Préserver les liens de bibliothèques
- Avant tout déplacement, ouvrir le `.kicad_pro` en texte et repérer :
  - les références aux bibliothèques de symboles (`sym-lib-table`, chemins relatifs/absolus),
  - les références aux tables d'empreintes (`fp-lib-table`),
  - les chemins de fichiers 3D (`.step`/`.wrl` absolus risquent de casser).
- Privilégier des **chemins relatifs** dans les projets déplacés.
- Après déplacement de chaque projet, valider l'ouverture avec KiCad (CLI ou MCP `kicad_set_project` + `pcb_get_board_summary`) avant de supprimer l'ancien emplacement.

### 3.3 Choix de la version de référence (déduplication)
Plusieurs branches coexistent (`2023/KICAD 6`, `2023/KICAD 7`, `Kicad` avec `Kicad 8` / `Kicad 9` pour `MB-KeySW_4x2_V0.1`). Pour chaque front-end, il faudra :
1. Identifier le `.kicad_pro` le plus récent **et fonctionnel** (dernière date de modification + ouverture sans erreur DRC bloquante).
2. Le désigner comme « version maître ».
3. Placer les anciennes versions dans `archive/` (ne pas supprimer avant validation finale).

### 3.4 Nettoyage des polluants
Supprimer uniquement après avoir copié/déplacé les sources essentielles :
- `._*`, `.DS_Store`
- `*.bak`, `*-backups/`, `__autosave-*`, `_autosave-*`, `#auto_saved_files#/`
- `fp-info-cache`
- `.kicad_prl`, `.kicad_lock`
- Doublons de Gerbers déjà archivés dans `production/` (à vérifier avant suppression)

## 4. Feuille de route par phase (à exécuter en mode ACT)

### Phase 0 — Audit et gel (lecture seule)
- [x] Relever l'inventaire exhaustif (569 dossiers, 718 fichiers sources KiCad détectés + inventaire des variantes par module le 18/10/2026 : Core×3, DOUT×3, DIN×2, POTS/OLED/Pad/BP/KeySW/CONTROL/FADER comparés).
- [ ] Vérifier si un dépôt Git existe (`MB MODULBOX NG/2023/KICAD 7/.git` et `NGC_NGR/AllIn/.git` détectés — à ne pas casser).
- [ ] Créer une sauvegarde brute (copie `.tar` ou snapshot) de l'état actuel avant toute modification.
- [x] Lister les projets KiCad qui s'ouvrent sans erreur (ERC/DRC `kicad-cli` exécutés sur 18 PCB + schémas ; rapports dans `/tmp/audit_reports_final/`).
- [x] Livrable : inventaire validé des « versions maîtresses » par front-end — recommandations Core→V0.1 et DOUT→Dout2024 (§7.3, protocoles de bascule en attente de feu vert).

### Phase 1 — Création de l'arborescence cible
- [ ] Créer `common-docs/`, `global-libs/`, `standard-modules/`, `custom-frontends/` avec les sous-dossiers `hardware/`, `production/`, `libs/`, `mechanical/`.
- [ ] Créer un `.gitignore` adapté (polluants KiCad + macOS).
- [ ] Créer `README.md` à la racine.
- [ ] Livrable : arborescence vide prête à recevoir les fichiers.

### Phase 2 — Tri des fichiers par front-end
- [ ] Pour chaque carte identifiée (4x-faders, 8x-pots, 8x-buttons, encoders-led-rgb, pad-rgb, oled-128x64, keysw-4x2, carte-puissance…), isoler le trio pro/sch/pcb maître + symboles/empreintes associés.
- [ ] Déplacer les versions obsolètes/doublons dans `archive/` (ne pas supprimer).
- [ ] Déplacer les datasheets critiques vers `production/` ou `common-docs/`.
- [ ] Livrable : chaque carte possède un dossier `hardware/` contenant uniquement ses sources maîtres.

### Phase 3 — Déplacement physique des sources KiCad (sécurisé)
- [ ] Déplacer le trio `.kicad_pro`/`.kicad_sch`/`.kicad_pcb` ensemble vers `custom-frontends/<carte>/hardware/`.
- [ ] Déplacer les `*.kicad_sym` et dossiers `*.pretty` associés soit dans `custom-frontends/<carte>/libs/`, soit dans `global-libs/` si partagés.
- [ ] Vérifier et, si nécessaire, réécrire les chemins relatifs de bibliothèques dans les `.kicad_pro`.
- [ ] Livrable : tous les projets sources sont dans l'arborescence cible.

### Phase 4 — Nettoyage des polluants
- [ ] Supprimer `._*`, `.DS_Store`, `*.bak`, `*-backups/`, `__autosave*`, `_autosave*`, `#auto_saved_files#/`, `fp-info-cache`, `.kicad_prl`, `.kicad_lock`.
- [ ] Supprimer les anciens exports Gerber redondants (après vérification que `production/` en contient une copie).
- [ ] Livrable : arborescence propre, sans fichiers temporaires.

### Phase 5 — Migration production (Gerbers, BOM, documentation de câblage)
- [ ] Déplacer les Gerbers finals vers `custom-frontends/<carte>/production/`.
- [ ] Placer/regénérer le BOM dans `production/` avec une colonne de correspondance broches vers bus DIN/AIN/DOUT.
- [ ] Classer les datasheets composants dans `production/` ou `common-docs/`.
- [ ] Livrable : dossier `production/` complet pour chaque carte prête à l'envoi fabrication.

### Phase 6 — Validation KiCad (réouverture et contrôle d'intégrité) + audit comparatif des variantes ✅ (18/10/2026) + audit comparatif des variantes ✅ (18/10/2026)
- [ ] Pour chaque projet déplacé : `kicad_set_project` sur le nouveau `.kicad_pro`.
- [ ] Vérifier l'ouverture du schéma et du PCB (`pcb_get_board_summary`, `schematic`, `pcb_get_nets`).
- [ ] Contrôler qu'aucun lien de bibliothèque n'est rompu (symboles/empreintes retrouvés).
- [ ] Livrable : rapport de validation projet par projet (PASS/WARN/FAIL).

### Phase 7 — Production des assets visuels & documentation par carte ✅ (18/10/2026)
- [x] Arborescence `docs/assets/system/`, `docs/assets/standard-modules/`, `docs/assets/frontends/<carte>/`, `docs/guides/` créée
- [x] Rendus 3D `-3d-top.png` et `-3d-iso.png` produits pour : Core32F4, DIN4_R5_KS, DIN4_R5_KS_2024, DOUT, Midi_V0.1, Fad_1, Fad_2, BP, Pot, Pot-X2, Carte_puissance, PEC_16_V0.2, MB-KeySW_4x2_V0.3, Oled_1309_x1_V0.0, Pad, Surface Control V0.1
- [x] `README.md` épurés et normalisés pour chaque `custom-frontends/<carte>/` (9 cartes : 4x-faders, 8x-pots, 8x-buttons, encoders-led-rgb, pad-rgb, oled-128x64, keysw-4x2, carte-puissance, surface-control)
- [x] `README.md` système global : présentation du projet, architecture, table des matières, HOWTO contribuer
- [x] `README.md` pour chaque `standard-modules/<module>/` (AIN, DIN, DOUT, Core, IO)

### Phase 8 — Documentation du bus MIDIbox NG ✅ (18/10/2026)
- [x] `common-docs/bus-midibox-ng.md` : Schéma de principe AIN/DIN/DOUT, brochage des connecteurs, mapping des front-ends

### Phase 9 — Archivage et revue finale (✅ 18/10/2026)
- [x] Déplacer tout ce qui reste d'inutilisé dans `archive/` — `MB Hardware/` (59M) et `MB MODULBOX NG/` (2,8G) déplacés vers `archive/sources/` ; rapports DRC déplacés vers `archive/drc-reports/` ; fichiers AppleDouble nettoyés
- [x] `.gitignore` étendu : fichiers binaires lourds de `archive/sources/` (SolidWorks, Blender, STEP — 2,8 Go non versionnés) + fichiers `*.lck` KiCad
- [x] Revue croisée de l'arborescence finale vs cible — tous les dossiers présents et README vérifiés
- [x] Commit de l'état propre (Git)
- [x] Livrable : projet prêt à être documenté ou publié

**Écarts assumés par rapport à l'arborescence cible (§2) :**
- `global-libs/` n'a pas été créé : les bibliothèques partagées sont dans `Mes_Librairies_KiCad/` (symbols/, footprints/, 3d/ — voir §8), déjà liées aux projets via `${KIPRJMOD}`
- `docs/` ajouté en plus de la cible (assets 3D + guides)
- `archive/` enrichi : `sources/`, `drc-reports/`, `pre-refill-2026-10-18/`, `superseded-*`

### Phase 10 — Documentation enrichie depuis le blog ksir-diy.blogspot.com (✅ 18/10/2026)
- [x] Explorer le blog ksir-diy.blogspot.com et identifier les articles par carte (terminé 18/10/2026)
- [ ] Récupérer les images et schémas du blog vers docs/assets/
- [x] Rédiger/enrichir README.md de chaque front-end (format user-friendly + réf. blog) — 9/9 terminés (8x-pots ✅, 8x-buttons ✅, 4x-faders ✅, encoders-led-rgb ✅, pad-rgb ✅, oled-128x64 ✅, keysw-4x2 ✅, carte-puissance ✅, surface-control ✅)
- [x] Rédiger/enrichir README.md de chaque standard-module — 5/5 terminés (AIN ✅, DIN ✅, DOUT ✅, Core ✅, IO ✅)
- [x] Rédiger le README principal à la racine (vitrine du projet avec lien blog) ✅
- [x] Lien vers les articles de blog pertinents dans chaque README ✅

**Détail des références blog associées :**
| Module | Article blog |
|--------|-------------|
| 8x-pots | [4X2-POTS-v0.2](https://ksir-diy.blogspot.com/) — modèle PotX2 |
| 4x-faders | [4X1-FAD-1/2-v0.2](https://ksir-diy.blogspot.com/) — modèle FAD4X1 et FAD4X1_1 |
| 8x-buttons | [4x2-BPL-v0.2](https://ksir-diy.blogspot.com/) — modèle BP4X2 |
| encoders-led-rgb | [4X2 ENC-SW-16-LED-RING-RGB](https://ksir-diy.blogspot.com/) — modèle PEC16 (non terminé ⚠️) |
| pad-rgb | [4X2-PADS-RGB](https://ksir-diy.blogspot.com/) — modèle PAD4X2 |
| oled-128x64 | Aucun article dédié → [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| keysw-4x2 | Aucun article dédié → [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| carte-puissance | Aucun article dédié → [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| surface-control | Aucun article dédié → [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| AIN | Aucun article dédié → [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| DIN | [4X2-BPL-v0.2](https://ksir-diy.blogspot.com/) + [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| DOUT | [4X2-PADS-RGB](https://ksir-diy.blogspot.com/) + [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| Core | [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |
| IO | [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html) |

---

**Mentions de licence, d'attribution et de crédits — appliquées ✅ (19/10/2026)**

- `standard-modules/{AIN,DIN,DOUT,Core,IO}/README.md` : section **Crédits & Origine** ajoutée — crédits **Thorsten Klose / ucapps.de** (schémas MBHP originaux), usage strictement DIY et non-commercial.
- `custom-frontends/{4x-faders,8x-pots,8x-buttons,encoders-led-rgb,pad-rgb,oled-128x64,keysw-4x2,carte-puissance,surface-control}/README.md` : section **Conception & Compatibilité** ajoutée — création originale compatible MB MODULBOX NG, licence Open-Source Hardware, usage DIY / non-commercial.
- `README.md` (racine) : synthèse de la distinction entre modules standards ré-implémentés (crédits ucapps.de / Thorsten Klose) et modules d'extension sur mesure, avec conditions d'utilisation non-commerciales.

## 5. Outils et commandes prévus (mode ACT)

| Tâche | Outil |
|-------|-------|
| Inventaire / recherche de fichiers | `find`, `grep`, `ls` (shell) |
| Création de dossiers et fichiers | `editor` (création `README.md`, `.gitignore`, PLAN.md) |
| Déplacement / suppression | `mv`, `rm` (shell, avec précaution sur le trio KiCad) |
| Inspection KiCad | `kicad_set_project`, `pcb_get_board_summary`, `pcb_get_nets`, `schematic` (MCP KiCad) |
| Vérification CLI KiCad | `kicad-cli` (ouverture/export sans GUI) |
| Git (si dépôt) | `git mv`, `git add`, `git commit` |

## 6. Points de vigilance

1. **Liens de bibliothèques cassés** : un `.kicad_pro` déplacé peut référencer des chemins absolus vers l'ancienne arborescence. Il faudra les corriger manuellement avant de valider le projet.
2. **Fichiers 3D référencés** : si un `.kicad_pcb` pointe vers un `.step` ou `.wrl` par chemin absolu, il faut soit déplacer le fichier 3D avec le projet, soit corriger le chemin.
3. **Doublons de noms** : plusieurs dossiers s'appellent `Pot`, `Pad`, `Control`, `Oled`. Il faut les renommer selon la nomenclature cible (`8x-pots`, `pad-rgb`, etc.) pour éviter les collisions.
4. **Versions de KiCad** : le projet contient des fichiers KiCad 6, 7, 8, 9. Le fichier CLI est en 9.0.2. Certains anciens fichiers pourront nécessiter une migration (ouverture puis réenregistrement) — à faire avec précaution et en conservant une copie dans `archive/`.
5. **Sous-modules Git** : `.git` détecté dans `2023/KICAD 7/` et `NGC_NGR/AllIn/` — ne pas supprimer ces dossiers `.git` lors du nettoyage.

## 7. AUDIT KICAD — Matrice de révision et checklist (étape PLAN)

Cet audit a été réalisé en **lecture seule** (aucun fichier source modifié). Données collectées : lecture des `.kicad_sch` (ERC), exécution DRC via `kicad-cli` sur chaque `.kicad_pcb`, inspection des bibliothèques et chemins 3D.

### 7.1 Tableau récapitulatif ERC (contrôle schématique)

| Carte | Réf. non uniques/génériques | Footprints vides | Datasheet vide | Symboles power | Problèmes ERC majeurs |
|-------|----------------------------|------------------|----------------|----------------|----------------------|
| Core V4 | `U?`, `IC2`×4, `R`, `RN`, `C`, `H`, `J?` | — | — | Oui | Références non annotées |
| DIN4_R5_KS | `U?`, `IC2`×4, `R`, `RN`, `C`, `H`, `J?` | Oui | Oui (41) | Oui (34) | Références non annotées, footprints manquants |
| DOUT | `U`, `C`, `R1`×4, `SR1`×2, `SR3`×2, `RN`, `H`, `J?` | Oui | Oui (10) | Oui (4) | Référence `U` sans numéro |
| Midi_V0.1 | `C`×2, `D`×2, `IC`, `R`, `U`, `P`, `K`, `H` | Oui | Oui (47) | Oui (11) | Références non annotées |
| 8x-pots Pot | `J*` (joker), `H` | — | — | Oui | Référence connecteur générique |
| 8x-buttons BP | `J*` (joker), `H` | — | — | Oui | Référence connecteur générique |
| pad-rgb Pad | `J2`×2, `J?`, `Sw`, `Sw1`, `Sw2` | Oui (34) | Oui (47) | Oui (30) | Références en doublon |
| oled-128x64 | `C`, `R`, `H`, `J`, `JP`, `OLED` | Oui (11) | Oui (8) | Oui (4) | Références non annotées |
| carte-puissance | `J`, `J?`, `J45`×23 | Oui (71) | — | Oui (66) | `J45` en doublon ×23 |
| surface-control | `J`×4, `J?`, `SW` | Oui (308) | — | Oui (295) | 308 footprints vides |

> **Légende :** `#PWR` = symbole de puissance, `?` = référence non annotée, `*` = joker non résolu.

### 7.2 Tableau récapitulatif DRC (contrôle PCB & routage)

| Carte | Fichier PCB | Violations DRC | Non connectés | Types de violations majeurs | Gravité |
|-------|-------------|---------------|--------------|---------------------------|---------|
| Core V4 | `standard-modules/Core/hardware/V4.kicad_pcb` | 991 | 10 | `track_dangling`, `clearance` (0.491mm < 0.508mm) | 🔴 |
| Core core32V7 | `standard-modules/Core/hardware/core32V7.kicad_pcb` | 655 | 39 | `track_dangling`, `clearance`, zones GND | 🔴 |
| encoders-led-rgb | `custom-frontends/encoders-led-rgb/hardware/PEC_16_V0.2.kicad_pcb` | 498 | 0 | `track_dangling`, `isolated_copper`, `courtyards_overlap`, `lib_footprint_issues` | 🔴 |
| keysw-4x2 | `custom-frontends/keysw-4x2/hardware/MB-KeySW_4x2_V0.3.kicad_pcb` | 177 | 0 | `courtyards_overlap`, `clearance` | 🟠 |
| DIN4_R5_KS_2024 | `standard-modules/DIN/hardware/DIN4_R5_KS_2024.kicad_pcb` | 267 | 10 | — | 🟠 |
| DIN4_R5_KS | `standard-modules/DIN/hardware/DIN4_R5_KS.kicad_pcb` | 255 | 0 | — | 🟠 |
| pad-rgb Pad | `custom-frontends/pad-rgb/hardware/Pad.kicad_pcb` | 121 | 0 | — | 🟠 |
| Midi_V0.1 | `standard-modules/IO/hardware/Midi_V0.1.kicad_pcb` | 125 | 94 | `silk_edge_clearance`, `unconnected_items` | 🔴 |
| Pot-X2 | `custom-frontends/8x-pots/hardware/Pot-X2.kicad_pcb` | 61 | 10 | — | 🟠 |
| oled-128x64 | `custom-frontends/oled-128x64/hardware/Oled_1309_x1_V0.0.kicad_pcb` | 38 | 0 | — | 🟡 |
| surface-control | `custom-frontends/surface-control/hardware/Surface Control V0.1.kicad_pcb` | 27 | 21 | `unconnected_items` | 🟡 |
| Carte_puissance | `custom-frontends/carte-puissance/hardware/Carte_puissance.kicad_pcb` | 22 | 0 | — | 🟡 |
| 8x-buttons BP | `custom-frontends/8x-buttons/hardware/BP.kicad_pcb` | 35 | 0 | — | 🟡 |
| 8x-pots Pot | `custom-frontends/8x-pots/hardware/Pot.kicad_pcb` | 32 | 0 | — | 🟡 |
| 4x-faders Fad_1 | `custom-frontends/4x-faders/hardware/Fad_1.kicad_pcb` | 20 | 0 | — | 🟡 |
| 4x-faders Fad_2 | `custom-frontends/4x-faders/hardware/Fad_2.kicad_pcb` | 20 | 0 | — | 🟡 |

> **Gravité :** 🔴 Critique = blocage fabrication, 🟠 Élevé = révision requise, 🟡 Moyen = corrections mineures.

### 7.3 Checklist détaillée par carte (à cocher en mode ACT — lecture seule pour l'instant)

#### standard-modules/AIN — Source AINSER64 manquante ⚠️
- [x] Dossier `standard-modules/AIN/hardware/` créé avec fichier `SOURCE_AINSER64_MANQUANTE.txt`
- [ ] ACTION REQUISE : Retrouver les sources KiCad de AINSER64 (aucun fichier `.kicad_*` dans `MB Hardware/AINSER64/`)

#### standard-modules/DIN/DIN4_R5_KS — Version complète ✅
- [x] Trio complet : `DIN4_R5_KS.kicad_pro`, `.kicad_sch`, `.kicad_pcb`
- [x] `DIN4_R5_KS_2024` (version partielle sans schéma) archivé dans `archive/superseded-din/`
- [x] Production complète (Gerbers, BOM, netlist, positions) présente

#### standard-modules/DOUT/DOUT — Basculé sur Dout2024 ✅
- [x] Ancienne version `DOUT`_2024 (sans schéma) archivée dans `archive/superseded-dout/`
- [x] Nouveau trio : `DOUT.kicad_pro`, `.kicad_sch`, `.kicad_pcb` (provenant de `Dout2024`)
- [x] Tables `sym-lib-table`/`fp-lib-table` créées
- [x] Production complète (Gerbers, BOM, netlist, positions) présente

#### standard-modules/IO/Midi_V0.1 — ERC 61→8 ✅ / DRC 125→121
- [x] Bibliothèques liées : tables `sym-lib-table`/`fp-lib-table` créées, symboles `core-rescue` (8) et `ksir` (1) extraits des lib_symbols embarqués, empreinte `w_conn_av:din-5` extraite du PCB → `w_conn_av.pretty`
- [x] ERC réduit de 61 à 8 violations : les "références non annotées" (C×2, D×2, IC, R, U, P, K, H) étaient des faux positifs du grep (templates `lib_symbols`) — l'ERC officiel ne signale aucune erreur d'annotation
- [ ] Restant ERC : 4× `duplicate_pins` LEMO5 (erreur réelle de symbole, coques GND en double) + 4× `lib_symbol_mismatch` LED (warning)
- [ ] Corriger les 81 éléments non connectés (routage réel — nécessite éditeur KiCad GUI)
- [ ] Corriger 30 `silk_edge_clearance` + 48 `silk_over_copper` (sérigraphie — GUI)
- [ ] `isolated_copper` éliminés (36→0) via refill + suppression d'îlots

#### standard-modules/Core/Core32F4 — Basculé sur Core32f4_V0.1 ✅ (audit 18/10/2026)
- [x] Anciennes versions V4 et core32V7 archivées dans `archive/superseded-core-v4-core32V7/`
- [x] Nouveau trio : `Core32F4.kicad_pro`, `.kicad_sch`, `.kicad_pcb` (provenant de `Core32f4_V0.1`)
- [x] Tables `sym-lib-table`/`fp-lib-table` créées
- [x] Production complète (Gerbers, BOM, netlist, positions) présente
- [x] Variantes comparées : `V4` (1,4 MB PCB sans schéma, 443 DRC, 10 non connectés) vs `core32V7` (0,5 MB PCB sans schéma, 455 DRC, 39 non connectés) vs `Core32f4_V0.1` (schéma 3 MB + PCB 1,3 MB, ERC 122, DRC 66, 0 non connectés) — **V0.1 validée comme version maître**

#### standard-modules/DOUT/DOUT — Basculé sur Dout2024 ✅ (audit 18/10/2026)
- [x] Ancienne version `DOUT`_2024 (sans schéma) archivée dans `archive/superseded-dout/`
- [x] Nouveau trio : `DOUT.kicad_pro`, `.kicad_sch`, `.kicad_pcb` (provenant de `Dout2024`)
- [x] Tables `sym-lib-table`/`fp-lib-table` créées
- [x] Production complète (Gerbers, BOM, netlist, positions) présente
- [x] Variante comparée : DOUT`_2024 (PCB sans schéma) vs `Dout2024` (schéma 117 kB + PCB complet) — **Dout2024 validée comme version maître**

#### 8x-buttons/BP, POTS, Pad, KeySW — variantes équivalentes : conserver l'actuel ✅
- BP : archive KICAD_7 (58 symboles/26 empreintes) identique à l'actuel → conserver
- POTS : variantes Horizontal/Vertical équivalentes (sch ~45-49 kB) → conserver l'actuel
- Pad : variante KICAD_7 (104 kB sch) équivalente → conserver l'actuel
- KeySW : V0.3 actuel (36 empreintes, 22/05/2024) ≥ V0.2 (35 empreintes) → conserver V0.3 ✅
- surface-control V0.1 (16 empreintes) ≥ Control V0.0 (12) → conserver V0.1 ✅
- 4x-faders : Fad_1/Fad_2 actuels ↔ archives identiques (13-14 empreintes) → conserver ; `Fader_Rgb 1` (31 symboles/145 empreintes, 02/06/2024) est une carte différente (RGB) → à classer comme variante dans `4x-faders/hardware/` ou futur `fader-rgb/`


#### custom-frontends/4x-faders/Fad_1 et Fad_2
- [ ] Corriger 20 violations DRC chacune
- [ ] Vérifier les empreintes faders ALPS RA6020F
- [ ] Valider les chemins 3D relatifs (déjà corrigés : `3D/Fad_1.wrl`, `3D/Fad_2.wrl`)

#### custom-frontends/8x-pots/Pot et Pot-X2
- [ ] Annoter `J*` → `J1` (Pot), vérifier Pot-X2
- [ ] Corriger 32 (Pot) et 61 (Pot-X2) violations DRC
- [ ] Corriger les 10 éléments non connectés sur Pot-X2
- [ ] Vérifier le chemin 3D `Pot-X2.kicad_pro` (déjà corrigé : `3D/Potars_V4.wrl`)

#### custom-frontends/8x-buttons/BP
- [ ] Annoter `J*` → `J1`
- [ ] Corriger 35 violations DRC
- [ ] Vérifier le chemin 3D `BP.kicad_pro` (déjà corrigé : `3D/BP V3.wrl`)

#### custom-frontends/encoders-led-rgb/PEC_16_V0.2 — ERC 825→294 ✅ / DRC 498→315 ✅
- [x] Symboles manquants restaurés : `C-100nf`, `WS2812-2020_1` extraits des lib_symbols embarqués → `ksir_2023.kicad_sym`
- [x] Empreintes `ksir 2022` extraites du PCB → `ksir.pretty` (CAPC1005X55N, LED_WS2812B-2020_PLCC4_2.0x2.0mm, PEC164120FS0012) + `lib 2022 ksir` (Hole_9.5mm, IDC-Header_2x05) → entrées ajoutées au `fp-lib-table`
- [x] `isolated_copper` éliminés (11→0) via refill + suppression d'îlots ; chemins 3D corrigés (`PEC16-4X20F-SXXXX.wrl`, `encoders.step`)
- [ ] Reste ERC (294 `lib_symbol_mismatch` = warnings : cache ≠ bibliothèque système — à accepter via "Update Symbols" en GUI)
- [ ] Reste DRC (315) : 199 `text_height` (warnings sérigraphie), 56 `lib_footprint_mismatch` (warnings), 16 `courtyards_overlap` (erreurs placement — GUI), 11 `starved_thermal`

#### custom-frontends/pad-rgb/Pad
- [ ] Annoter `J2`×2 (doublon), `J?`, `Sw`, `Sw1`, `Sw2`
- [ ] Remplir les 34 footprints vides
- [ ] Renseigner les 47 datasheets manquantes
- [ ] Corriger 121 violations DRC

#### custom-frontends/oled-128x64/Oled_1309_x1_V0.0
- [ ] Annoter `C`, `R`, `H`, `J`, `JP`, `OLED` sans numéro
- [ ] Remplir les 11 footprints vides
- [ ] Corriger 38 violations DRC
- [ ] Vider le chemin step cassé (déjà fait : `"step": ""`)

#### custom-frontends/carte-puissance/Carte_puissance
- [ ] Résoudre le doublon `J45`×23 dans le schéma
- [ ] Annoter `J`, `J?`
- [ ] Remplir les 71 footprints vides
- [ ] Corriger 22 violations DRC

#### custom-frontends/keysw-4x2/MB-KeySW_4x2_V0.3
- [ ] Corriger 177 violations DRC (`courtyards_overlap`, `clearance`)
- [ ] Vérifier les empreintes switchs Cherry MX Low Profile / Kailh

#### custom-frontends/surface-control/Surface Control V0.1
- [ ] **Priorité haute :** Corriger les 21 éléments non connectés
- [ ] Remplir les 308 footprints vides (schéma quasi vide d'empreintes)
- [ ] Annoter `J`×4, `J?`, `SW`
- [ ] Corriger 27 violations DRC


### 7.4 Checklist DFM (pré-fabrication) — applicable à toutes les cartes

- [ ] Vérifier la taille des perçages (viés, PHT, NPTH) vs capacités du fabricant
- [ ] Vérifier la lisibilité de la sérigraphie : aucun texte superposé aux pastilles (violations `silk_edge_clearance` sur Midi_V0.1)
- [ ] Vérifier les points d'ancrage (MountingHole) présents et correctement positionnés
- [ ] Vérifier la cohérence des connecteurs de bus (HE10 2x05 P2.54mm pour AIN/DIN/DOUT)
- [ ] Vérifier les largeurs de pistes : alimentation (VCC/5V/3.3V) ≥ signaux (AIN/DIN/DOUT/MIDI)
- [ ] Vérifier la présence et le remplissage des plans de masse (Ground Planes) sur les deux couches
- [ ] Vérifier les distances de clearance pour les séparations haute/basse tension

### 7.5 Priorités de traitement (ordre recommandé)

1. **🔴 Bloquants fonctionnels :** Midi_V0.1 (94 non connectés), Core V4 (991 DRC), Core core32V7 (655 DRC, 39 non connectés)
2. **🔴 Bloquants bibliothèque :** encoders-led-rgb PEC_16_V0.2 (498 DRC, librairies `ksir 2022` manquantes)
3. **🟠 Révisions importantes :** DIN4_R5_KS, DIN4_R5_KS_2024, keysw-4x2, pad-rgb, Pot-X2
4. **🟡 Corrections mineures :** 4x-faders, 8x-buttons, 8x-pots, oled-128x64, carte-puissance, surface-control

## 8. NETTOYAGE DES BIBLIOTHÈKES KiCad — `Mes_Librairies_KiCad/` (TERMINÉ)

### 8.1 État initial
Le dossier contenait : fichiers parasites AppleDouble (`._*`, `.DS_Store`), backups (`*.bak`, `*.zip`), une ancienne bibliothèque KiCad v5 obsolète (`teensy_library-master/` avec `.lib`/`.dcm`), et une export fabricant Texas Instruments (`LIB_SN74AHCT125N/`) avec des dizaines de sous-dossiers pour différents formats CAO (Allegro, Altium, EAGLE, PADS, etc.) dont seul le sous-dossier `KiCad/` nous intéressait.

### 8.2 Nettoyage effectué
| Action | Détail |
|--------|--------|
| Suppression parasites | `._*`, `.DS_Store`, `*.bak`, `*.zip` (AppleDouble, backups) |
| Suppression obsolète | `teensy_library-master/` (format KiCad v5 `.lib`/`.dcm`) |
| Suppression export TI | `LIB_SN74AHCT125N/` (export multi-CAO, fichiers KiCad extraits avant suppression) |
| Restructuration | Création de `symbols/`, `footprints/`, `3d/` |

### 8.3 Structure finale propre
```
Mes_Librairies_KiCad/
├── symbols/
│   ├── SN74AHCT125N.kicad_sym     # Symbole Texas Instruments (valide)
│   ├── ksir_2023.kicad_sym        # Bibliothèque symboles MIDIbox (2248 lignes, valide)
│   └── midibox-rescue.kicad_sym   # Symboles de sauvetage MIDIbox (202 lignes, valide)
├── footprints/
│   ├── Pad_x_4.kicad_mod          # Empreinte pad 4x (renommé sans espace)
│   ├── SN74AHCT125N.mod           # Empreinte TI (ancien format .mod KiCad v5 — à convertir en .kicad_mod)
│   └── teensy.pretty/             # 13 empreintes Teensy (dossier .pretty valide)
│       ├── Teensy1.0.kicad_mod
│       ├── Teensy2.0.kicad_mod
│       ├── Teensy35_36.kicad_mod
│       ├── Teensy40.kicad_mod
│       ├── Teensy41.kicad_mod
│       └── ... (11 empreintes au total)
└── 3d/
    ├── SN74AHCT125N.stp           # Modèle 3D SN74AHCT125N
    ├── Teensy_3.5_3.6_Assembly.STEP
    ├── Teensy_4.0_Assembly.STEP
    └── Teensy_4.1_Assembly.STEP
```

### 8.4 Vérification d'intégrité
Tous les fichiers `.kicad_sym` et `.kicad_mod` ont été vérifiés : en-têtes KiCad valides, aucun fichier corrompu.

### 8.5 Point d'attention
- `SN74AHCT125N.mod` est au format KiCad v5 (`.mod`). KiCad 9 peut le lire, mais il est recommandé de le convertir en `.kicad_mod` avant utilisation en production.
- La bibliothèque `ksir_2023.kicad_sym` contient probablement les symboles pour les composants MIDIbox (74HC165, 74HC595, etc.) — elle doit être liée dans le `sym-lib-table` des projets.

### 8.6 Bibliothèques prêtes à lier
Les bibliothèques sont prêtes à être référencées dans les projets KiCad via :
- `sym-lib-table` → pointer vers `Mes_Librairies_KiCad/symbols/`
- `fp-lib-table` → pointer vers `Mes_Librairies_KiCad/footprints/`

---

## 9. CORRECTIFS PRIORITAIRES 🔴 — Bilan d'exécution (TERMINÉ partiellement)

Date : 18/10/2026. Méthode : `kicad-cli sch erc` / `pcb drc`, API `pcbnew` (refill zones), extraction symboles/empreintes embarqués.

### 9.1 Résultats ERC (bibliothèques)

| Carte | ERC avant | ERC après | Résolu | Reste |
|-------|-----------|-----------|--------|-------|
| Midi_V0.1 | 61 | **8** | 53 `lib_symbol_issues` + 4 `footprint_link_issues` (tables + extraction) | 4 `duplicate_pins` LEMO5 + 4 `lib_symbol_mismatch` |
| PEC_16_V0.2 | 825 | **294** | 261 `lib_symbol_issues` + 11 `footprint_link_issues` | 294 `lib_symbol_mismatch` (warnings — accepter en GUI) |
| Core V4 / core32V7 | — | — | Aucun `.kicad_sch` : ERC impossible | Schéma à retrouver/redessiner ⚠️ |

### 9.2 Résultats DRC (PCB)

| Carte | DRC avant | DRC après | Connectés | Reste principal |
|-------|-----------|-----------|-----------|----------------|
| V4 | 991 | **443** | 10 non connectés | sérigraphie 418 (warn), 61 lib_fp, 11 thermal, 9 dangling |
| core32V7 | 655 | **455** | 39 non connectés | 98 `drill_out_of_range`, 37 lib_fp, 3 invalid_outline |
| Midi_V0.1 | 125 | **121** | 81 non connectés | routage GUI requis |
| PEC_16_V0.2 | 498 | **315** | 0 | 199 text_height (warn), 56 mismatch (warn), 16 courtyards_overlap (GUI) |

### 9.3 Actions effectuées
- [x] Fichiers `sym-lib-table`/`fp-lib-table` créés par projet (3 dossiers prioritaires), chemins via `${KIPRJMOD}` (obligatoire — relatifs bruts non résolus)
- [x] Bibliothèques reconstituées depuis les données embarquées : `ksir_2023` (+C-100nf, +WS2812-2020_1), `core-rescue` (8 symboles), `ksir` (1 symbole), 11 dossiers `.pretty` legacy, `lib_2022_ksir.pretty`, `w_conn_av.pretty`
- [x] Plans de masse rechargés + îlots isolés supprimés (V4 4 zones, core32V7 1 zone, Midi 1 zone, PEC_16 3 zones) → `isolated_copper` éliminés
- [x] Chemins 3D cassés corrigés sur `PEC_16_V0.2.kicad_pro`
- [x] Sauvegardes PCB pré-refill dans `archive/pre-refill-2026-10-18/`
- [x] Outils créés : `tools/extract_symbols.py`, `tools/extract_footprints.py`, `tools/merge_ksir_2023.py`, `tools/refill_zones.py`

### 9.4 Reste à faire (nécessite éditeur KiCad GUI)
- Routage physique : 81 (Midi) + 39 (core32V7) + 10 (V4) éléments non connectés
- Placement : 16 `courtyards_overlap` (PEC_16), repositionnement sérigraphie
- Paramètres : 98 `drill_out_of_range` (core32V7), 3 `invalid_outline`
- Acceptations GUI : 294 `lib_symbol_mismatch` (PEC_16), 56 `lib_footprint_mismatch`


**Prochaine étape (mode ACT) :** corriger le reste en GUI KiCad (routage, placement, sérigraphie — voir §9.4), appliquer la même recette (tables + extraction + refill) aux cartes 🟠 (DIN, keysw-4x2, pad-rgb, Pot-X2), puis passer aux cartes 🟡. Mettre à jour ce PLAN.md après chaque carte validée.

---

## 11. MISE EN VALURE COMMUNAUTÉ — Custom Front-ends au cœur du dépôt (TERMINÉ ✅)

Date : 21/10/2026. Objectif : élever le dépôt au niveau des meilleurs projets hardware open-source (Adafruit, SparkFun, Mutable Instruments) — attractif, clair, robuste, simple à prendre en main.

### 11.1 Positionnement
- **`custom-frontends/` = l'essence du dépôt** : cartes d'interface physiques originales (faders, pots, boutons, pads, encodeurs, OLED, clavier, alimentation, surface de contrôle).
- **`standard-modules/` = bonus de référence** : modules MIDIbox standards (AIN, DIN, DOUT, Core, IO) pour alimenter les front-ends, pas la raison d'être du dépôt.

### 11.2 Refonte du README principal
- [x] Titre + banner + pitch d'accroche mettant en avant les front-ends
- [x] Badges (licence, KiCad, statut)
- [x] Section `🧩 Custom Front-ends — le cœur du dépôt` en premier, avec tableau enrichi (image, bus, rôle, état, lien doc)
- [x] Section `🚀 Démarrage rapide` (cloner, ouvrir KiCad, fabriquer)
- [x] Section `⚡ Modules standards MIDIbox (bonus)` reléguée en second plan
- [x] Section `📦 Contenu du dépôt` (inclus / exclu)
- [x] Avertissement « non professionnel » conservé en tête
- [x] Licences, crédits, contribuer, ressources

### 11.3 État des images par front-end
| Front-end | Image |
|-----------|-------|
| 4x-faders | assets/Fad_1.png, Fad_2.png |
| 8x-pots | assets/Pot.png, Pot-X2.png |
| 8x-buttons | assets/BP.png |
| encoders-led-rgb | assets/PEC_16_V0.2.png |
| pad-rgb | assets/Pad.png |
| oled-128x64 | assets/Oled_1309_x1_V0.0.png |
| keysw-4x2 | assets/MB-KeySW_4x2_V0.3.png |
| carte-puissance | assets/Carte_puissance.png |
| surface-control | assets/Surface Control V0.1.png |

---

## 12. AUDIT TECHNIQUE COMPLET ET CORRECTIONS (2026-10-21) — TERMINE ✅

### 12.1 Méthodologie
- Source de vérité : fichiers `.kicad_sch` versionnés (`custom-frontends/*/hardware/` + `standard-modules/*/hardware/`)
- Spécifications officielles : ucapps.de (MIDIbox NG Hardware), midibox.org (MIOS32 WS2812 driver)
- Résultat : **11 fichiers README corrigés** (le tableau §12.2 en detaille 11) — 5 erreurs critiques retracables
- ⚠️ **Cette premiere passe (2026-10-21) reposait sur une lecture « a l'oeil » des schemas et comportait des erreurs. Elle est reprise et corrigee integralement en §14 (2026-10-22), sur la base d'une extraction de netlist par `kicad-cli` et d'une comparaison bit-a-bit avec les archives.**

### 12.2 Liste des erreurs découvertes et corrigées

#### 🔴 Critique (WS2812B)

| # | Fichier | Erreur détectée | Correction appliquée |
|---|---------|----------------|----------------------|
| 1 | `custom-frontends/encoders-led-rgb/README.md` | LED WS2812 annoncée sur DOUT (3 fils RGB séparés) | Remplacé par : **1 fil de données sur J4B.SC (PB6/TIM4)** du Core32F4, alimentation 5V séparée |
| 2 | `custom-frontends/pad-rgb/README.md` | DOUT-1 annoncé pour Data WS2812 | Remplacé par : **DATA → J4B.SC / PB6**, pas sur DOUT |
| 3 | `common-docs/bus-midibox-ng.md` | DOUT affiché pour « anneaux LED RGB » | Correction : DOUT gère LEDs standards (74HC595), WS2812B sur J4B.SC |

#### 🟠 Erreurs de câblage / mapping

| # | Fichier | Erreur détectée | Correction appliquée |
|---|---------|----------------|----------------------|
| 4 | `custom-frontends/8x-pots/README.md` | "D-Sub 24 broches" (schéma : IDC 2x05 10 broches) ; "pull-up 4.7k sur pots" ; mapping "AIN-1 a DIN-8" faux | Connector IDC 2x05 précisé ; pots : 2 pattes ext. → +5V/GND, curseur → AIN ; AIN via AINSER64 J19 SPI |
| 5 | `custom-frontends/4x-faders/README.md` | Même erreur connecteur 24 broches | Connector IDC 2x05 précisé ; câblage pots/faders correct (Vd/Vs/curseur) |
| 6 | `custom-frontends/keysw-4x2/README.md` | Matrice 4x2 décrite comme "DIN-1→DIN-4 colonnes, DIN-5→DIN-6 lignes" (6 broches = 32 entrées non adaptées à 8 touches) | Précisé : 8 touches = 8 entrées d'un 74HC165 (1 touche = 1 entrée) |
| 7 | `custom-frontends/keysw-4x2/README.md` | LED SK6812 "rétroéclairage optionnel" sans précision de port | Précisé : LED optionnelle, si WS2812-compatible → J4B.SC (PB6) |

#### 🟡 Manquements documentaires

| # | Fichier | Manque | Ajout |
|---|---------|--------|-------|
| 8 | `standard-modules/Core/README.md` | Pas de pinout J4B.SC (WS2812) ni J19 (AINSER64) | Brochage complet J8/J9 (DIN/DOUT), J19 (AINSER64 SPI), J4B.SC (WS2812) |
| 9 | `standard-modules/AIN/README.md` | Imprecision : AIN "Header mâle" | AINSER64 (MCP3208+CD4051) sur J19, 64/128 voies, câblage pots |
| 10 | `custom-frontends/oled-128x64/README.md` | I2C/SPI ambigu sur "module de base MIDIbox" | Précisé I2C SSD1306/SH1106 → pas sur DIN/DOUT |
| 11 | `custom-frontends/surface-control/README.md` | Prototype V0.1 trop vague | Mapping bus + concerné par WS2812 (J4B.SC), validation requise |

### 12.3 Spécifications référencées
- **WS2812B MIOS32** : https://www.midibox.org/mios32/midibox_ng/group___w_s2812.html → J4B.SC (PB6/TIM4), alimentation 5V séparée
- **MBHP_AINSER64** : https://www.ucapps.de/mbhp_ainser64.html → MCP3208 + CD4051, J19 Core, 64 voies, pots Vd/Vs/curseur
- **MBHP_DIN** : https://www.ucapps.de/mbhp_din.html → 74HC165 en cascade, J8/J9, pull-up 10k
- **MBHP_CORE_STM32F4** : https://www.ucapps.de/mbhp_core_stm32f4.html → J8/J9 (DIN/DOUT), J19 (AIN SPI), J15 LCD, J16 SD Card

---

## 13. PROJET SUR LE LONG — SUIVI

- [ ] Corriger les 294 `lib_symbol_mismatch` (PEC_16_V0.2 DRC)
- [ ] Terminer routage des cartes 🟠 (Midi V0.1, core32V7, V4)
- [ ] Valider surface-control V0.1 en fabricant une épreuve
- [ ] Mettre à jour les docs de kit de fabrication pour chaque carte
- [x] ~~Réfléchir à la dualité I2C/SPI pour le OLED (SSD1306 vs SH1106)~~ → **résolu en §14 : le schéma est un SPI SSD1309, pas un I2C**
- [ ] Ajouter un bon de commande / BOM par carte
- [ ] Implémenter un script de test DRC/ERC automatique pour CI
- [ ] Vérifier l'alignement des symboles KiCad avec les bibliothèques officielles MIDIBOX

---

## 14. RÉVISION CIBLÉE DES SOURCES — Grille de vérification KiCad ↔ README ↔ ucapps.de (2026-10-22)

**Méthode :** export netlist de chaque `.kicad_sch` via `kicad-cli 9.0.2` (`sch export netlist`),
analyse des broches par connecteur, comparaison bit-à-bit avec les archives (`diff`),
DRC headless (`kicad-cli pcb drc`), confrontation avec ucapps.de / midibox.org.

### 14.1 Grille de suivi par module — `custom-frontends/`

- [x] **8x-pots**
  - **Statut Cohérence :** ⚠️ **INCOHÉRENT (README)** — le schéma est correct et cohérent
  - **Action Source :** Conservée (`Pot.kicad_sch` = `archive/sources/MB MODULBOX NG/2023/KICAD 7/POTS/Vertical/Pot.kicad_sch`, diff = 0)
  - **README :** Corrigé — tension **+3V0** (et non +5V), curseur → `J1` broches 3-10, GND pin 1, `+3V0` pin 2 ; suppression de la mention « LED verte ×8 » (absente du schéma) ; Pot-X2 = variante 4×2 sans schéma ni annotation
- [x] **4x-faders**
  - **Statut Cohérence :** ⚠️ **INCOHÉRENT (README)**
  - **Action Source :** Conservée (Fad_1 / Fad_2 — identiques aux archives KICAD 7)
  - **README :** Corrigé — **+3V0** (et non +5V) ; `Fad_1` = 4 faders (J3/J4), `Fad_2` = 4 faders (J5) ; pas de AIN sur la carte elle-même, curseur → connecteur → AINSER64
- [x] **8x-buttons**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (README)**
  - **Action Source :** Conservée (`BP.kicad_sch` identique à l'archive KICAD 7)
  - **README :** Corrigé — **pas de D-Sub** : 2 × IDC 2x05 (J1 = 8 entrées DIN, J2 = 8 LEDs) ; **aucune résistance de pull-up sur la carte** (pull-up 10 kΩ porté par le module DIN 74HC165) ; 8 LED + 8 switch à led
- [x] **keysw-4x2**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (README)**
  - **Action Source :** Conservée (`MB-KeySW_4x2_V0.3.kicad_sch`)
  - **README :** Corrigé — **8 touches = 8 entrées 1:1 d'un 74HC165** (pas de matrice) ; **aucune diode anti-ghosting** dans le schéma (contrairement au README) ; SK6812MINI-E **en cascade série** (J2 pin 6 = DI, J3 pin 6 = DO) et non adressables individuellement ; J4 = 1×2 GND
- [x] **pad-rgb**
  - **Statut Cohérence :** ⚠️ **INCOHÉRENT (README)**
  - **Action Source :** Conservée (`Pad.kicad_sch` identique à l'archive KICAD 7)
  - **README :** Corrigé — 8 pads = 8 entrées DIN (J1) ; 8 × **WS2812-2020** (PLCC4) **en cascade** J2 → J3 (et non pilotés individuellement) ; 8 × C 100 nF ; 2 pads × 4 contacts
- [x] **encoders-led-rgb**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (README)**
  - **Action Source :** Conservée (`PEC_16_V0.2.kicad_sch`, PCB identique à l'archive KICAD 7)
  - **README :** Corrigé — 8 × encodeur **PEC16** (A/B + poussoir) = **24 entrées DIN** (J11/J12/J13) ; **128 × WS2812-2020** en cascade (J4 → D1…D128 → J5), pas « 1 anneau » ; 2 lignes WS2812 disponibles
- [x] **oled-128x64**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (README) — erreur de protocole**
  - **Action Source :** Conservée (`Oled_1309_x1_V0.0.kicad_sch`)
  - **README :** Corrigé — **SSD1309 en SPI** (broches `D0`=SCLK, `D1`=SDATA, `DC`, `CS`, `RES`), **pas de I2C** ; 8 cavaliers `JP1..JP8` de sélection CS ; R1 = 1 kΩ + C1 = 10 µF sur `RES` ; J1 = IDC 2x08
- [x] **surface-control**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (README)**
  - **Action Source :** Conservée (`Surface Control V0.1.kicad_sch`)
  - **README :** Corrigé — ce n'est **pas** une carte multi-bus : 1 encodeur + 6 boutons → **J10A/J10B du Core** (SCS officiel, GPIO PE8-PE15 / PC13-PC15), **sans** 74HC165, **sans** DOUT, **sans** AIN ; PCB **non routé** (0 segment, 21 non connectés) → prototype
- [x] **carte-puissance**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (README)**
  - **Action Source :** Conservée (`Carte_puissance.kicad_sch` identique à l'archive KICAD 7)
  - **README :** Corrigé — **distributeur de bus passif**, **aucun régulateur / aucune protection** ; 24 × IDC 2x05 (J2…J25) + 4 borniers ALTECH AK300-2 (J1 entrée, J27 sortie, J28/J29 entrée) + J26/J30/J31 (1×2) + J32 « Disconect » ; 2 nets : `+5VD` (digital) et `+5VA` (analogique, J2 + J32)

### 14.2 Grille de suivi par module — `standard-modules/`

- [x] **Core**
  - **Statut Cohérence :** ⚠️ **INCOHÉRENT (README)**
  - **Action Source :** Conservée — `Core32F4.kicad_sch`/`.kicad_pcb` identiques à `archive/sources/MB Hardware/Core32f4/Core32f4_V0.1/` (diff = 0) ; `core32V7` / `V4` écartés (pas de schéma associé)
  - **README :** Corrigé — **4 lignes WS2812** et non 1 : `J4A` pin 6 = PB10, `J4A` pin 8 = PB11, `J4B` pin 6 = **PB6 (TIM4 — référence MIOS32)**, `J4B` pin 8 = PB9 ; pull-up 2,2 kΩ vers +5V (R7a/R7b/R8a/R8b, sortie open-drain) ; `J19` = SPI AIN (PB4 + 2 chip-selects) ; `J8J9` = DIN+DOUT ; `J10A/J10B` = SCS ; `J16` = SPI SD/ETH 3V3 ; `J15A/J15B` = LCD
- [x] **DIN**
  - **Statut Cohérence :** ✅ **COHÉRENT** (README à compléter)
  - **Action Source :** Conservée (`DIN4_R5_KS.kicad_sch` + PCB 2023 identique aux archives ; `DIN4_R5_KS_2024` = PCB sans schéma, écarté)
  - **README :** Corrigé — 4 × 74HC165 (32 entrées), 36 × pull-up **10 kΩ** + 8 réseaux RN1..RN8, 4 × C 100 nF, J1/J2 = chaînage (J8/J9), J3..J6 = 8 entrées + GND
- [x] **DOUT**
  - **Statut Cohérence :** 🟡 **COHÉRENT (version maintenue = DOUT2024, référence officielle MB Hardware 2024)**
  - **Action Source :** Conservée — `hardware/DOUT.kicad_pro`/`.kicad_sch`/`.kicad_pcb` sont **identiques** à `archive/sources/MB Hardware/DOUT/DOUT2024/Dout2024/Dout2024.kicad_{pro,sch,pcb}` (diff = 0)
  - **README :** Corrigé — 4 × SN74HC595N, R1 réseau 8×220 + R2/R3/R4 individuels, J1..J6, 6 connecteurs ; **21 pads non connectés** au +5V et **74 violations DRC** → version signalée comme non-fabrique en l'état (routage partiel +5V)
- [x] **IO**
  - **Statut Cohérence :** ⚠️ **INCOHÉRENT (README + PCB non routé)**
  - **Action Source :** Conservée (`Midi_V0.1.kicad_sch` + PCB — seul exemplaire existant ; archive `pre-refill` = même PCB)
  - **README :** Corrigé — **2 × 6N138** (2 MIDI IN), 2 × MIDI OUT, 2 × SN74HC00N, 4 LED, 4 × LEMO5/DIN-5 (2 IN + 2 OUT) ; **PCB non routé** (0 segment, 81 pads non connectés) → non fabricable en l'état
- [x] **AIN**
  - **Statut Cohérence :** 🔴 **INCOHÉRENT (source absente)**
  - **Action Source :** ⚠️ **Aucune source KiCad disponible** — `archive/sources/MB Hardware/AINSER64/` est vide ; seul `mbhp_ainser64_v1_2023-06-02.zip` (Gerbers Eagle uniquement, 11 fichiers, pas de `.kicad_sch`) existe
  - **README :** Corrigé — refait sur la base de la fiche **ucapps.de/mbhp_ainser64** (MCP3208 + 8 × CD4051 + 74HC595, SPI sur J19, 2 chip-selects, 64 voies) ; suppression de la fausse impression d'un dépôt de sources KiCad local

### 14.3 Actions correctives globales

- [x] `PLAN.md` : décompte « 9 fichiers README corrigés » → **11 fichiers** (§12) — corrigé
- [x] Avertissement « hobbyist / non professionnel / sans garantie ni engagement / erreurs possibles » **uniformisé sur les 16 documents** (README racine, 9 front-ends, 5 modules standards, `common-docs/bus-midibox-ng.md`)
- [x] `common-docs/bus-midibox-ng.md` : connecteur AIN « Header mâle 24 broches » → IDC 2x05 ; DOUT réservé aux LEDs standards ; WS2812 hors DOUT
- [x] README racine : tableau mis à jour (états réels, `+3V0`, SPI OLED, SCS, carte-puissance passive)

### 14.4 Points ouverts (non corrigibles sans action hardware)

- [ ] `standard-modules/IO` : PCB non routé → à router avant toute fabrication
- [ ] `custom-frontends/surface-control` : PCB non routé (prototype V0.1)
- [ ] `custom-frontends/8x-pots/hardware/Pot-X2.kicad_pcb` : 41 empreintes dont 5 `REF**` non annotées, aucun schéma associé, 10 pads non connectés
- [ ] `standard-modules/AIN` : reconstruire la carte (schéma KiCad) à partir des Gerbers Eagle ou repartir du PDF xcircuit
- [ ] DRC : `encoders-led-rgb` (315), `DIN` (255), `keysw-4x2` (177), `pad-rgb` (121) restent à corriger





---

## 15. PROBLÈMES TECHNIQUES CRITIQUES — 3 INTERVENTIONS IMMÉDIATES

Date : 23/10/2026. Orchestreur : ingénieur CAO (KiCad MCP). Priorité : 🔴 BLOCANT.

Ces 3 tâches ont été identifiées comme les problèmes structurels et techniques les plus critiques de l'ensemble du dépôt :
1. **Liens 3D cassés** (protractions visuelles, rendu 3D en présentation, et possible plantage KiCad)
2. **Facades aluminium absentes** (manque de traceabilité fabrication et de fichiers mécaniques)
3. **Séparation module encodeurs** (1 projet -> 3 sous-projets, pas de modularité OSHW)

---

### Task 1 — Correction des liens 3D cassés (.kicad_pcb)

#### 15.1 Diagnostic
| Type de problème | Présence | Nombre récapitulatif | Impact |
|-----------------|----------|---------------------|--------|
| Chemins absolus Windows (C:/Users/...) | 7 projets | ~90+ occurrences | 🔴 Basculé si KiCad non installé sur Windows |
| Modèles téléchargés non versionnés | 6 projets | ~40 occurrences | 🔴 Fichiers introuvables en local |
| Variables KiCad (${KICAD6_3DMODEL_DIR}, ${KIPRJMOD}) | 12 projets | ~85 occurrences | 🟡 Valides si variables d'environnement corrects |
| Référence à fichier absent | 3 projets | ~35 occurrences | 🔴 CL05B104KO5NNNC.stp dans PEC_16 |

#### 15.2 Actions
- [ ] **1A** : Localiser l'emplacement réel de chaque modèle 3D dans Mes_Librairies_KiCad/3d/ et les dossiers hardware/3D/
- [ ] **1B** : Supprimer les références absolues Windows cassées (aucune correspondance sur disk) : C:/Users/papaya/Downloads/...
- [ ] **1C** : Pour les modèles qui existent localement :
  - PEC_16_V0.2.wrl / .step -> referencer ${KIPRJMOD}/3D/PEC_16_V0.2.wrl (relatif au projet)
  - WS2812-2020.step -> referencer ${KIPRJMOD}/3D/WS2812-2020.step
  - encoders.step / SN74AHCT125N.stp / PEC16-4X20F-SXXXX.wrl -> referencer ${KICAD_USER_3DMOD}/... ou ../../Mes_Librairies_KiCad/3d/...
- [ ] **1D** : Pour les composants sans modèle 3D defini (ex: CL05B104KO5NNNC, capacitor 0603) -> supprimer le model embedding du PCB (conserver le symbole sans 3D, ce n'est pas critique)
- [ ] **1E** : Valider chaque projet corrige avec kicad-cli pcb pcbnew --export-3d ou pcb_get_board_summary (KiCad MCP)
- [ ] **1F** : Documenter la convention de nommage des chemins 3D dans le README.md racine

#### 15.3 Livrables
- PEC_16_V0.2.kicad_pcb : liens 3D corriges
- Tous les autres .kicad_pcb : liens 3D corriges ou supprimes
- Documentation des conventions de chemins 3D






---

### Task 2 — Rapatriement des fichiers de Face Avant Aluminum (Front Panels)

#### 15.1 Diagnostic
| Front panel | Module | Fichier(s) | Statut |
|------------|--------|-----------|--------|
| Facade LCD 20X2 | (archive) | Facade LCD 20X2/ | Archive |
| Facade controle | surface-control | archive/... | Archive |
| Facade enc rgb | encoders-led-rgb | archive/... | Archive |
| Produton facade | keysw-4x2 | archive/... + production/facade_jlcpcb*.zip | Archive + ZIP |
| facade oled 128x64 | oled-128x64 | archive/... | Archive |
| 3D aluminium | 4x-faders | hardware/3D/ existant | WARNINGS 3D seulement |
| 3D aluminium | 8x-pots | hardware/3D/ existant | WARNINGS 3D seulement |

#### 15.2 Actions
- [ ] **2A** : Rechercher dans archive/ et common-docs/ tous les fichiers KiCad lies aux facades : .kicad_pcb, .dxf, .step, .wtf, .igs
- [ ] **2B** : Creer custom-frontends/*/mechanical/ pour chaque module possedant une facade
- [ ] **2C** : Dans mechanical/ :
  - Fichiers .kicad_pcb de la facade (contour mechanique, holes, nichees)
  - .dxf ou .step pour l usinage (deux-tours, laser, clochetage)
  - .zip d export destine au fabricant (ex: facade_jlcpcb.zip)
- [ ] **2D** : Mettre a jour le README.md de chaque module pour reference mechanical/
- [ ] **2E** : Verifier que les files de fabrication de la carte production/ et de la facade mechanical/ sont coherentes (memes trous, memes tolerences)

#### 15.3 Livrables
- Dossier mechanical/ avec fichiers de fabrication pour chaque module ayant une facade
- README.md mis a jour pour chaque module
- Table des correspondances (broches carte -> trous facade)

---

### Task 3 — Modularisation et separation du projet Encodeurs (1 -> 3 PCBs)

#### 15.1 Diagnostic
Le projet PEC_16_V0.2.kicad_pro groupe actuellement 3 PCBs distincts au sein d un seul fichier :
| Carte | Role | Composants cles |
|-------|------|------------------|
| Control Board (Carte Shift Registers / Interfaçage) | Interface avec MIOS32 du Core, shift registers, gestion 74HC165 | STM32F4 (via report), 74HC165x3, 74HC595x2 |
| Encoders / Switches (Carte Encodeurs) | 8 x PEC16 avec poussoir, 24 entrees DIN | PEC164120FS0012x8, 74HC165x3 |
| Ring LEDs RGB (Carte WS2812B) | 128 x WS2812-2020 en cascade | WS2812-2020x128, AOA, 74HC165x1 |

#### 15.2 Actions
- [ ] **3A** : Analyser le .kicad_sch actuel (PEC_16_V0.2.kicad_sch) pour identifier :
  - Les sections separees (schemas logiques)
  - Les connecteurs de liaison entre sous-cartes (J14, J15, J20-J35, J30-J35)
  - Les feuilles d annotations distinctes (EC5, EC6, etc.)
- [ ] **3B** : Creer l arborescence :
  custom-frontends/encoders-led-rgb/
  ├── control-board/          -> Carte Shift Registers / Interfaçage
  │   ├── hardware/
  │   │   ├── Control_Board.kicad_pro
  │   │   ├── Control_Board.kicad_sch
  │   │   ├── Control_Board.kicad_pcb
  │   │   ├── 3D/             -> modeles 3D de la control board
  │   │   └── fp-lib-table
  │   ├── production/
  │   └── README.md
  ├── encoders-board/         -> Carte Encodeurs / Switches
  │   ├── hardware/
  │   │   ├── Encoders.kicad_pro
  │   │   ├── Encoders.kicad_sch
  │   │   ├── Encoders.kicad_pcb
  │   │   ├── 3D/
  │   │   └── fp-lib-table
  │   ├── production/
  │   └── README.md
  ├── led-ring/              -> Carte Ring LEDs RGB (WS2812B)
  │   ├── hardware/
  │   │   ├── Led_Ring.kicad_pro
  │   │   ├── Led_Ring.kicad_sch
  │   │   ├── Led_Ring.kicad_pcb
  │   │   ├── 3D/
  │   │   └── fp-lib-table
  │   ├── production/
  │   └── README.md
  ├── hardware/              -> Raccordement commun (legacy)
  │   ├── PEC_16_V0.2.kicad_pro (s liaison unique)
  │   └── ...
  ├── docs/
  │   └── interconnect.md    -> Documentation des liens entre 3 cartes
  └── README.md
- [ ] **3C** : Separ dans les 3 schemas :
  - Control_Board.kicad_sch (Schema A - Interface + Shift Registers)
  - Encoders.kicad_sch (Schema B - 8 x Encodeurs PEC16)
  - Led_Ring.kicad_sch (Schema C - 128 x WS2812)
- [ ] **3D** : Separ le .kicad_pcb en 3 PCBs :
  - Control_Board.kicad_pcb
  - Encoders.kicad_pcb
  - Led_Ring.kicad_pcb
- [ ] **3E** : Mettre a jour les fp-lib-table et sym-lib-table pour chaque sous-projet
- [ ] **3F** : Generer les connexions IEEE pour les pins de liaison :
  - Control Board -> Encoders Board : DIN signals (J14/J15)
  - Control Board -> Led Ring : DATA WS2812 (J20/J21)
- [ ] **3G** : Documenter l interconnect dans docs/interconnect.md

#### 15.3 Livrables
- 3 sous-projets autonomes sous custom-frontends/encoders-led-rgb/
- docs/interconnect.md avec pinout complet des liaisons
- README.md mis a jour pour chaque sous-projet
- Production (Gerbers, BOM, netlist) generee pour chaque carte

---

### Suivi

| Tache | Sous-tache | Statut |
|-------|-----------|--------|
| **1** Correction liens 3D | 1A Localisation | BLANK |
| | 1B Suppression chemins absolus | BLANK |
| | 1C Repointage vers fichiers existants | BLANK |
| | 1D Suppression model non essentiels | BLANK |
| | 1E Validation | BLANK |
| **2** Face Avant aluminium | 2A Recherche archives | BLANK |
| | 2B Creation mechanical/ | BLANK |
| | 2C Fichiers de fabrication | BLANK |
| | 2D Mise a jour README | BLANK |
| | 2E Coherent production/facade | BLANK |
| **3** Separation encodeurs | 3A Analyse schema | BLANK |
| | 3B Creation arborescence | BLANK |
| | 3C Separation schemas | BLANK |
| | 3D Separation PCB | BLANK |
| | 3E Mise a jour bibliotheques | BLANK |
| | 3F Generation connexions | BLANK |
| | 3G Documentation interconnect | BLANK |

## 16. MATRICE D'AUDIT & SÉCURITÉ (v1.0) — 2026-10-24

### 16.1 État Git et périmètre

- Branche d'audit : `feature/kicad-audit-and-fix`.
- Commit de sauvegarde de l'état local avant audit : `eed4fd2` (`wip: save pre-audit local changes and PCB updates`). Les fichiers présents avant l'audit, y compris les fichiers non suivis, y sont sauvegardés.
- Inventaire : 113 fichiers projet `.kicad_pro` réels ; 10 sidecars macOS `._*.kicad_pro` exclus du décompte.
- Projets actifs : 21, répartis entre 9 projets stables et 12 projets à risque (fichiers modifiés avant l'audit). Les autres 92 projets sont des archives/historiques hors périmètre de normalisation.
- Parmi les 9 projets stables, 6 ont un PCB homonyme et ont reçu des règles de projet ; 3 sont des configurations orphelines sans PCB ni schéma homonyme, donc sans conception à modifier.
- PCB auparavant illisible : `custom-frontends/encoders-led-rgb/hardware/PEC_16_V0.2.kicad_pcb`, restauré depuis `PEC_16_V0.2.kicad_pcb.backup_3d_fix`. KiCad CLI 9.0.2 le charge maintenant et produit un rapport DRC (315 violations préexistantes, 0 élément non connecté).
- La normalisation de cette phase porte sur les 6 PCB stables présents. Aucun composant n'a été déplacé. Les classes et les presets définissent les largeurs cibles ; une géométrie de cuivre existante n'est élargie que si le DRC reste valide.

### 16.2 Normalisation appliquée et limites électriques

- Six fichiers `.kicad_pro` stables avec PCB associé ont des classes `Default`/signal (0,25 mm, clearance 0,20 mm) et `Power` (0,50 mm, clearance 0,20 mm), avec motifs de nets correspondant à chaque carte. La carte LED possède en plus `PowerStrong` (1,20 mm) pour `+5V` et `GND`.
- Les règles globales de fabrication définissent une clearance minimale de 0,127 mm, une largeur minimale de piste de 0,127 mm, un perçage traversant minimal de 0,30 mm et un diamètre de via minimal de 0,50 mm ; toute règle existante plus stricte est conservée. Les presets disponibles incluent 0,25 / 0,50 / 0,80 / 1,00 / 1,20 mm.
- Les segments de signal routés ont été ramenés à 0,25 mm sur Control Board (109 segments), Encoder Board (136) et Led Ring (300) ; leurs DRC restent au même niveau qu'avant cette normalisation. Les segments d'alimentation des cartes Control/Encoder étaient déjà au moins à 0,50 mm.
- Des essais d'élargissement des routes d'alimentation DIN (0,40 → 0,50 mm) et OLED (0,20 → 0,50 mm) ont créé des violations de clearance. Ces largeurs de cuivre ont été restaurées ; les classes restent configurées pour les futurs routages, mais ces routes ne sont pas déclarées conformes à la cible tant qu'une revue/révision de routage n'a pas résolu les conflits.
- Le ring héberge 128 WS2812. Son DRC confirme une zone GND, mais aucune zone +5V ; les pistes +5V existantes restent à 0,50 mm. La classe 1,20 mm n'est qu'une cible de routage et ne certifie pas une alimentation à pleine charge. Le courant de dimensionnement, la distribution d'alimentation et les plans cuivre doivent être revus avant fabrication (les valeurs de courant indiquées dans la documentation sont à réconcilier).
- ERC/DCR n'a pas été « nettoyé » en masquant des défauts électriques : OLED conserve 2 erreurs `power_pin_not_driven` sur des symboles d'alimentation sans réseau de puissance connecté, et IO conserve 4 erreurs de pins dupliquées dans le symbole `LEMO5`. Aucun `PWR_FLAG` ou `No-Connect` n'a été ajouté sans confirmation de la connectivité/sémantique voulue. Les champs secondaires visibles sont déjà masqués dans les instances des trois schémas actifs stables ; aucune modification visuelle risquée n'était justifiée.

### 16.3 Résultats de vérification KiCad CLI

Contrôles exécutés avec KiCad 9.0.2 après normalisation. Les résultats DRC ci-dessous n'ont pas augmenté par rapport à l'état de référence ; les violations restantes sont consignées pour traitement dédié.

| Projet | DRC (erreurs / avertissements ; non-connectés) | ERC (erreurs / avertissements) |
|---|---:|---:|
| `custom-frontends/encoders-led-rgb/control-board/hardware/connect board` | 1 / 20 ; 0 | — (schéma homonyme absent) |
| `custom-frontends/encoders-led-rgb/encoders-board/hardware/En` | 17 / 38 ; 0 | — (schéma homonyme absent) |
| `custom-frontends/encoders-led-rgb/led-ring/leds` | 30 / 403 ; 0 | — (schéma homonyme absent) |
| `custom-frontends/oled-128x64/hardware/Oled_1309_x1_V0.0` | 0 / 38 ; 0 | 2 / 8 |
| `standard-modules/DIN/hardware/DIN4_R5_KS` | 18 / 237 ; 0 | 0 / 48 |
| `standard-modules/IO/hardware/Midi_V0.1` | 0 / 121 ; 81 | 4 / 4 |

Les 81 éléments non connectés du PCB IO correspondent au routage incomplet/non réalisé de cette carte, pas à des changements induits ici. La liste ERC IO attribue les 4 erreurs à des numéros de pins dupliqués du symbole `LEMO5`. La vérification des schémas n'a pas autorisé à conclure que ces erreurs sont cosmétiques.

### 16.4 Matrice exhaustive des fichiers projet

`Stable — normalisé` signifie qu'un PCB homonyme existe et que ses règles de projet ont été normalisées. Les entrées sans fichiers PCB/schéma homonymes sont signalées séparément. `Réparé depuis backup` reste dans le groupe des projets à risque pour la revue électrique.

| # | Projet KiCad (`.kicad_pro`) | PCB homonyme | Schéma homonyme | Statut |
|---:|---|---|---|---|
| 1 | `archive/sources/MB Hardware/Core32f4/Core32f4_V0.0/Core32f4_V0.0.kicad_pro` | `Core32f4_V0.0.kicad_pcb` | — | Archive / hors périmètre |
| 2 | `archive/sources/MB Hardware/Core32f4/Core32f4_V0.1/Core32f4_V0.1/Core32f4_V0.1.kicad_pro` | `Core32f4_V0.1.kicad_pcb` | `Core32f4_V0.1.kicad_sch` | Archive / hors périmètre |
| 3 | ``archive/sources/MB Hardware/DOUT/DOUT/DOUT`_2024.kicad_pro`` | ``DOUT`_2024.kicad_pcb`` | — | Archive / hors périmètre |
| 4 | `archive/sources/MB Hardware/DOUT/DOUT2024/Dout2024/Dout2024.kicad_pro` | `Dout2024.kicad_pcb` | `Dout2024.kicad_sch` | Archive / hors périmètre |
| 5 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/AINSER64_DIN_DOUT/DIN_DOUT/DIN_DOUT/DIN_DOUT.kicad_pro` | `DIN_DOUT.kicad_pcb` | `DIN_DOUT.kicad_sch` | Archive / hors périmètre |
| 6 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/AINSER64_DIN_DOUT/DOUT/DOUT/DOUT.kicad_pro` | `DOUT.kicad_pcb` | `DOUT.kicad_sch` | Archive / hors périmètre |
| 7 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/BP/BP.kicad_pro` | `BP.kicad_pcb` | `BP.kicad_sch` | Archive / hors périmètre |
| 8 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/carte puissance/Carte_puissance/Carte_puissance.kicad_pro` | `Carte_puissance.kicad_pcb` | `Carte_puissance.kicad_sch` | Archive / hors périmètre |
| 9 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/CONTROL/Control.kicad_pro` | `Control.kicad_pcb` | `Control.kicad_sch` | Archive / hors périmètre |
| 10 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/encoder led ring NO rgb/encoders/encoders/encoders.kicad_pro` | — | — | Archive / hors périmètre |
| 11 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/encoder led ring NO rgb/Led ring NO rgb/Led ring NO rgb/Led ring NO rgb.kicad_pro` | `Led ring NO rgb.kicad_pcb` | `Led ring NO rgb.kicad_sch` | Archive / hors périmètre |
| 12 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/PEC_16_V0.2/PEC_16_V0.2/oonnect board Temp/Conect board/Conect board.kicad_pro` | `Conect board.kicad_pcb` | `Conect board.kicad_sch` | Archive / hors périmètre |
| 13 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/PEC_16_V0.2/PEC_16_V0.2/PEC_16_V0.2.kicad_pro` | `PEC_16_V0.2.kicad_pcb` | `PEC_16_V0.2.kicad_sch` | Archive / hors périmètre |
| 14 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders rgb/encoder rgb/au as ou/encoder rgb memokicad_sch.kicad_pro` | — | `encoder rgb memokicad_sch.kicad_sch` | Archive / hors périmètre |
| 15 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders rgb/encoder rgb/encoder rgb.kicad_pro` | `encoder rgb.kicad_pcb` | `encoder rgb.kicad_sch` | Archive / hors périmètre |
| 16 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders rgb/encoder rgb/Encoders/encoder rgb.kicad_pro` | `encoder rgb.kicad_pcb` | `encoder rgb.kicad_sch` | Archive / hors périmètre |
| 17 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders swith/Encoder switch/Encoder switch.kicad_pro` | `Encoder switch.kicad_pcb` | `Encoder switch.kicad_sch` | Archive / hors périmètre |
| 18 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders swith/Encoder switch/oonnect board Temp/Conect board/Conect board.kicad_pro` | `Conect board.kicad_pcb` | `Conect board.kicad_sch` | Archive / hors périmètre |
| 19 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders swith/TEMP/TEMP/TEMP.kicad_pro` | `TEMP.kicad_pcb` | `TEMP.kicad_sch` | Archive / hors périmètre |
| 20 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders/Encoders/Encoders.kicad_pro` | `Encoders.kicad_pcb` | `Encoders.kicad_sch` | Archive / hors périmètre |
| 21 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/pec 16/Encoder switch/Encoder switch.kicad_pro` | `Encoder switch.kicad_pcb` | `Encoder switch.kicad_sch` | Archive / hors périmètre |
| 22 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/pec 16/Encoder switch/oonnect board Temp/Conect board/Conect board.kicad_pro` | `Conect board.kicad_pcb` | `Conect board.kicad_sch` | Archive / hors périmètre |
| 23 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Encoder with led ring RGB/TEST_NOT_WORKING/pec 16/TEMP/TEMP/TEMP.kicad_pro` | `TEMP.kicad_pcb` | `TEMP.kicad_sch` | Archive / hors périmètre |
| 24 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/FADER/1/Fad_1.kicad_pro` | `Fad_1.kicad_pcb` | — | Archive / hors périmètre |
| 25 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/FADER/2/Fad_2.kicad_pro` | `Fad_2.kicad_pcb` | `Fad_2.kicad_sch` | Archive / hors périmètre |
| 26 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/Pad RGB/Kicad/Pad/Pad.kicad_pro` | `Pad.kicad_pcb` | `Pad.kicad_sch` | Archive / hors périmètre |
| 27 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/POTS/Horizontal/Pot-X2.kicad_pro` | `Pot-X2.kicad_pcb` | — | Archive / hors périmètre |
| 28 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/POTS/Horizontal/Pot.kicad_pro` | `Pot.kicad_pcb` | `Pot.kicad_sch` | Archive / hors périmètre |
| 29 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/POTS/Vertical/Pot.kicad_pro` | `Pot.kicad_pcb` | `Pot.kicad_sch` | Archive / hors périmètre |
| 30 | `archive/sources/MB MODULBOX NG/2023/KICAD 7/TEMP/EXPORT/EXPORT.kicad_pro` | `EXPORT.kicad_pcb` | `EXPORT.kicad_sch` | Archive / hors périmètre |
| 31 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/BP/Kicad/BP.kicad_pro` | `BP.kicad_pcb` | `BP.kicad_sch` | Archive / hors périmètre |
| 32 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/Control/Control/Control.kicad_pro` | `Control.kicad_pcb` | `Control.kicad_sch` | Archive / hors périmètre |
| 33 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/encoder led ring NO rgb/encoder led ring NO rgb/encoder led ring NO rgb.kicad_pro` | `encoder led ring NO rgb.kicad_pcb` | `encoder led ring NO rgb.kicad_sch` | Archive / hors périmètre |
| 34 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/Encoder with led ring RGB/Led Ring RGB/Led_Ring_RGB/Led_Ring_RGB.kicad_pro` | `Led_Ring_RGB.kicad_pcb` | `Led_Ring_RGB.kicad_sch` | Archive / hors périmètre |
| 35 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/Fader/Kicad/1/Fad_1/Fad_1.kicad_pro` | `Fad_1.kicad_pcb` | `Fad_1.kicad_sch` | Archive / hors périmètre |
| 36 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/Fader/Kicad/2/Fad_2/Fad_2.kicad_pro` | `Fad_2.kicad_pcb` | `Fad_2.kicad_sch` | Archive / hors périmètre |
| 37 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/Pad RGB/Kicad/Pad/Pad.kicad_pro` | `Pad.kicad_pcb` | `Pad.kicad_sch` | Archive / hors périmètre |
| 38 | `archive/sources/MB MODULBOX NG/2023/KICAD_6/Pot/vertical/Kicad/Pot.kicad_pro` | — | — | Archive / hors périmètre |
| 39 | `archive/sources/MB MODULBOX NG/Kicad/CONTROL/Surface Control V0.0/Control.kicad_pro` | `Control.kicad_pcb` | `Control.kicad_sch` | Archive / hors périmètre |
| 40 | `archive/sources/MB MODULBOX NG/Kicad/CONTROL/Surface Control V0.1/Facade controle/Facade controle/Facade controle.kicad_pro` | `Facade controle.kicad_pcb` | — | Archive / hors périmètre |
| 41 | `archive/sources/MB MODULBOX NG/Kicad/CONTROL/Surface Control V0.1/facade surface_control_v0.1.kicad_pro` | `facade surface_control_v0.1.kicad_pcb` | — | Archive / hors périmètre |
| 42 | `archive/sources/MB MODULBOX NG/Kicad/encoder led ring NO rgb/encoder plus led no rgb/encoder led ring NO rgb.kicad_pro` | `encoder led ring NO rgb.kicad_pcb` | `encoder led ring NO rgb.kicad_sch` | Archive / hors périmètre |
| 43 | `archive/sources/MB MODULBOX NG/Kicad/encoder led ring NO rgb/encoders/encoders/encoders.kicad_pro` | `encoders.kicad_pcb` | `encoders.kicad_sch` | Archive / hors périmètre |
| 44 | `archive/sources/MB MODULBOX NG/Kicad/encoder led ring NO rgb/Led ring NO rgb/Led ring NO rgb/Led ring NO rgb.kicad_pro` | `Led ring NO rgb.kicad_pcb` | — | Archive / hors périmètre |
| 45 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/Kicad 8/PCB/connect board.kicad_pro` | `connect board.kicad_pcb` | — | Archive / hors périmètre |
| 46 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/Kicad 8/PCB/En.kicad_pro` | `En.kicad_pcb` | — | Archive / hors périmètre |
| 47 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/Kicad 8/PCB/leds.kicad_pro` | `leds.kicad_pcb` | — | Archive / hors périmètre |
| 48 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/Kicad 8/PEC_16_V0.2.kicad_pro` | `PEC_16_V0.2.kicad_pcb` | `PEC_16_V0.2.kicad_sch` | Archive / hors périmètre |
| 49 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/PEC_16_V0.2/PEC_16_V0.2/oonnect board Temp/Conect board/Conect board.kicad_pro` | `Conect board.kicad_pcb` | `Conect board.kicad_sch` | Archive / hors périmètre |
| 50 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/PEC_16_V0.2/PEC_16_V0.2/PCB/connect board.kicad_pro` | `connect board.kicad_pcb` | — | Archive / hors périmètre |
| 51 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/PEC_16_V0.2/PEC_16_V0.2/PCB/En.kicad_pro` | `En.kicad_pcb` | — | Archive / hors périmètre |
| 52 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/PEC_16_V0.2/PEC_16_V0.2/PCB/leds.kicad_pro` | `leds.kicad_pcb` | — | Archive / hors périmètre |
| 53 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders rgb/encoder rgb/au as ou/encoder rgb memokicad_sch.kicad_pro` | — | `encoder rgb memokicad_sch.kicad_sch` | Archive / hors périmètre |
| 54 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders rgb/encoder rgb/encoder rgb.kicad_pro` | `encoder rgb.kicad_pcb` | `encoder rgb.kicad_sch` | Archive / hors périmètre |
| 55 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders rgb/encoder rgb/Encoders/encoder rgb.kicad_pro` | `encoder rgb.kicad_pcb` | `encoder rgb.kicad_sch` | Archive / hors périmètre |
| 56 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders swith/Encoder switch/Encoder switch.kicad_pro` | `Encoder switch.kicad_pcb` | `Encoder switch.kicad_sch` | Archive / hors périmètre |
| 57 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders swith/Encoder switch/oonnect board Temp/Conect board/Conect board.kicad_pro` | `Conect board.kicad_pcb` | `Conect board.kicad_sch` | Archive / hors périmètre |
| 58 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders swith/TEMP/TEMP/TEMP.kicad_pro` | `TEMP.kicad_pcb` | `TEMP.kicad_sch` | Archive / hors périmètre |
| 59 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Encoders/Encoders/Encoders.kicad_pro` | `Encoders.kicad_pcb` | `Encoders.kicad_sch` | Archive / hors périmètre |
| 60 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/Led Ring RGB/Led_Ring_RGB/Led_Ring_RGB.kicad_pro` | `Led_Ring_RGB.kicad_pcb` | `Led_Ring_RGB.kicad_sch` | Archive / hors périmètre |
| 61 | `archive/sources/MB MODULBOX NG/Kicad/Encoder with led ring RGB/TEST_NOT_WORKING/pec 16/Encoder switch/oonnect board Temp/Conect board/Conect board.kicad_pro` | `Conect board.kicad_pcb` | `Conect board.kicad_sch` | Archive / hors périmètre |
| 62 | `archive/sources/MB MODULBOX NG/Kicad/Facade LCD 20X2/Facade LCD 20X2/Facade LCD 20X2.kicad_pro` | `Facade LCD 20X2.kicad_pcb` | `Facade LCD 20X2.kicad_sch` | Archive / hors périmètre |
| 63 | `archive/sources/MB MODULBOX NG/Kicad/FADER/Adaptateur/Adaptateur V0.0/Adaptateur V0.0.kicad_pro` | `Adaptateur V0.0.kicad_pcb` | `Adaptateur V0.0.kicad_sch` | Archive / hors périmètre |
| 64 | `archive/sources/MB MODULBOX NG/Kicad/FADER/Fader Facade/Fader Facade_V0.1.kicad_pro` | `Fader Facade_V0.1.kicad_pcb` | — | Archive / hors périmètre |
| 65 | `archive/sources/MB MODULBOX NG/Kicad/FADER/Fader Facade/Fader Facade_V0.2.kicad_pro` | `Fader Facade_V0.2.kicad_pcb` | — | Archive / hors périmètre |
| 66 | `archive/sources/MB MODULBOX NG/Kicad/FADER/Fader Facade/Fader Facade_V0.3.kicad_pro` | `Fader Facade_V0.3.kicad_pcb` | — | Archive / hors périmètre |
| 67 | `archive/sources/MB MODULBOX NG/Kicad/FADER/Fader_Rgb/Fader_Rgb 1/Fader_Rgb 1.kicad_pro` | `Fader_Rgb 1.kicad_pcb` | `Fader_Rgb 1.kicad_sch` | Archive / hors périmètre |
| 68 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 7/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.1.kicad_pro` | `MB-KeySW_4x2_V0.1.kicad_pcb` | `MB-KeySW_4x2_V0.1.kicad_sch` | Archive / hors périmètre |
| 69 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.1/facade jlcpcb.kicad_pro` | `facade jlcpcb.kicad_pcb` | — | Archive / hors périmètre |
| 70 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.1.kicad_pro` | `MB-KeySW_4x2_V0.1.kicad_pcb` | `MB-KeySW_4x2_V0.1.kicad_sch` | Archive / hors périmètre |
| 71 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.2/facade jlcpcb.kicad_pro` | `facade jlcpcb.kicad_pcb` | — | Archive / hors périmètre |
| 72 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.2/MB-KeySW_4x2_V0.2.kicad_pro` | `MB-KeySW_4x2_V0.2.kicad_pcb` | `MB-KeySW_4x2_V0.2.kicad_sch` | Archive / hors périmètre |
| 73 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/facade jlcpcb.kicad_pro` | — | — | Archive / hors périmètre |
| 74 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/facade jlcpcb_v0.3.kicad_pro` | `facade jlcpcb_v0.3.kicad_pcb` | — | Archive / hors périmètre |
| 75 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/facade jlcpcb_v0.3b.kicad_pro` | `facade jlcpcb_v0.3b.kicad_pcb` | — | Archive / hors périmètre |
| 76 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 8/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/MB-KeySW_4x2_V0.3.kicad_pro` | `MB-KeySW_4x2_V0.3.kicad_pcb` | `MB-KeySW_4x2_V0.3.kicad_sch` | Archive / hors périmètre |
| 77 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 9/MB-KeySW_4x2_V0.3/facade jlcpcb.kicad_pro` | — | — | Archive / hors périmètre |
| 78 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 9/MB-KeySW_4x2_V0.3/facade jlcpcb_v0.3.kicad_pro` | `facade jlcpcb_v0.3.kicad_pcb` | — | Archive / hors périmètre |
| 79 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 9/MB-KeySW_4x2_V0.3/facade jlcpcb_v0.3b.kicad_pro` | `facade jlcpcb_v0.3b.kicad_pcb` | — | Archive / hors périmètre |
| 80 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/Kicad 9/MB-KeySW_4x2_V0.3/MB-KeySW_4x2_V0.3.kicad_pro` | `MB-KeySW_4x2_V0.3.kicad_pcb` | `MB-KeySW_4x2_V0.3.kicad_sch` | Archive / hors périmètre |
| 81 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/facade jlcpcb.kicad_pro` | — | — | Archive / hors périmètre |
| 82 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/facade jlcpcb_v0.3.kicad_pro` | `facade jlcpcb_v0.3.kicad_pcb` | — | Archive / hors périmètre |
| 83 | `archive/sources/MB MODULBOX NG/Kicad/MB-KeySW_4x2_V0.1/MB-KeySW_4x2_V0.3/facade jlcpcb_v0.3b.kicad_pro` | `facade jlcpcb_v0.3b.kicad_pcb` | — | Archive / hors périmètre |
| 84 | `archive/sources/MB MODULBOX NG/Kicad/Oled/128x64/facade oled 128x64/facade oled 128x64.kicad_pro` | `facade oled 128x64.kicad_pcb` | `facade oled 128x64.kicad_sch` | Archive / hors périmètre |
| 85 | `archive/sources/MB MODULBOX NG/Kicad/Oled/Oled V2/Oed V2/Oed V2.kicad_pro` | `Oed V2.kicad_pcb` | `Oed V2.kicad_sch` | Archive / hors périmètre |
| 86 | `archive/sources/MB MODULBOX NG/Kicad/Oled/Oled V2/Oed V2/Oed V2X4.kicad_pro` | `Oed V2X4.kicad_pcb` | — | Archive / hors périmètre |
| 87 | `archive/sources/MB MODULBOX NG/Kicad/Oled/Oled/Oled.kicad_pro` | `Oled.kicad_pcb` | `Oled.kicad_sch` | Archive / hors périmètre |
| 88 | `archive/sources/MB MODULBOX NG/Kicad/POTS/Horizontal/Pot.kicad_pro` | `Pot.kicad_pcb` | `Pot.kicad_sch` | Archive / hors périmètre |
| 89 | `archive/superseded-core-v4-core32V7/core32V7.kicad_pro` | `core32V7.kicad_pcb` | — | Archive / hors périmètre |
| 90 | `archive/superseded-core-v4-core32V7/V4.kicad_pro` | `V4.kicad_pcb` | — | Archive / hors périmètre |
| 91 | `archive/superseded-din/DIN4_R5_KS_2024.kicad_pro` | `DIN4_R5_KS_2024.kicad_pcb` | — | Archive / hors périmètre |
| 92 | `archive/superseded-dout/DOUT.kicad_pro` | `DOUT.kicad_pcb` | `DOUT.kicad_sch` | Archive / hors périmètre |
| 93 | `custom-frontends/4x-faders/hardware/Fad_1.kicad_pro` | `Fad_1.kicad_pcb` | `Fad_1.kicad_sch` | À risque — modifié avant audit |
| 94 | `custom-frontends/4x-faders/hardware/Fad_2.kicad_pro` | `Fad_2.kicad_pcb` | `Fad_2.kicad_sch` | À risque — modifié avant audit |
| 95 | `custom-frontends/8x-buttons/hardware/BP.kicad_pro` | `BP.kicad_pcb` | `BP.kicad_sch` | À risque — modifié avant audit |
| 96 | `custom-frontends/8x-pots/hardware/Pot-X2.kicad_pro` | `Pot-X2.kicad_pcb` | — | À risque — modifié avant audit |
| 97 | `custom-frontends/8x-pots/hardware/Pot.kicad_pro` | `Pot.kicad_pcb` | `Pot.kicad_sch` | À risque — modifié avant audit |
| 98 | `custom-frontends/carte-puissance/hardware/Carte_puissance.kicad_pro` | `Carte_puissance.kicad_pcb` | `Carte_puissance.kicad_sch` | À risque — modifié avant audit |
| 99 | `custom-frontends/encoders-led-rgb/control-board/hardware/connect board.kicad_pro` | `connect board.kicad_pcb` | — | Stable — normalisé |
| 100 | `custom-frontends/encoders-led-rgb/control-board/hardware/Control_Board.kicad_pro` | — | — | Stable — configuration orpheline, aucun fichier de conception homonyme |
| 101 | `custom-frontends/encoders-led-rgb/encoders-board/hardware/En.kicad_pro` | `En.kicad_pcb` | — | Stable — normalisé |
| 102 | `custom-frontends/encoders-led-rgb/encoders-board/hardware/Encoders.kicad_pro` | — | — | Stable — configuration orpheline, aucun fichier de conception homonyme |
| 103 | `custom-frontends/encoders-led-rgb/hardware/PEC_16_V0.2.kicad_pro` | `PEC_16_V0.2.kicad_pcb` | `PEC_16_V0.2.kicad_sch` | Réparé depuis backup — reste à risque, revue dédiée |
| 104 | `custom-frontends/encoders-led-rgb/led-ring/hardware/Led_Ring.kicad_pro` | — | — | Stable — configuration orpheline, aucun fichier de conception homonyme |
| 105 | `custom-frontends/encoders-led-rgb/led-ring/leds.kicad_pro` | `leds.kicad_pcb` | — | Stable — normalisé |
| 106 | `custom-frontends/keysw-4x2/hardware/MB-KeySW_4x2_V0.3.kicad_pro` | `MB-KeySW_4x2_V0.3.kicad_pcb` | `MB-KeySW_4x2_V0.3.kicad_sch` | À risque — modifié avant audit |
| 107 | `custom-frontends/oled-128x64/hardware/Oled_1309_x1_V0.0.kicad_pro` | `Oled_1309_x1_V0.0.kicad_pcb` | `Oled_1309_x1_V0.0.kicad_sch` | Stable — normalisé |
| 108 | `custom-frontends/pad-rgb/hardware/Pad.kicad_pro` | `Pad.kicad_pcb` | `Pad.kicad_sch` | À risque — modifié avant audit |
| 109 | `custom-frontends/surface-control/hardware/Surface Control V0.1.kicad_pro` | `Surface Control V0.1.kicad_pcb` | `Surface Control V0.1.kicad_sch` | À risque — modifié avant audit |
| 110 | `standard-modules/Core/hardware/Core32F4.kicad_pro` | `Core32F4.kicad_pcb` | `Core32F4.kicad_sch` | À risque — modifié avant audit |
| 111 | `standard-modules/DIN/hardware/DIN4_R5_KS.kicad_pro` | `DIN4_R5_KS.kicad_pcb` | `DIN4_R5_KS.kicad_sch` | Stable — normalisé |
| 112 | `standard-modules/DOUT/hardware/DOUT.kicad_pro` | `DOUT.kicad_pcb` | `DOUT.kicad_sch` | À risque — modifié avant audit |
| 113 | `standard-modules/IO/hardware/Midi_V0.1.kicad_pro` | `Midi_V0.1.kicad_pcb` | `Midi_V0.1.kicad_sch` | Stable — normalisé |
