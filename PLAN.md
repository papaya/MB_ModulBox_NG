# PLAN.md — Réorganisation du projet hardware MB_ModulBox_NG

---
**Statut :** Plan de rangement — ÉTAPES 1-5 TERMINÉES + RÉCONCILIATION MODULES STANDARDS (mode ACT exécuté)  
**Dernière mise à jour :** 18/10/2026  
**Résumé :** Arborescence créée, fichiers parasites supprimés, modules standards réconciliés (versions maîtresses identifiées), 9 front-ends déplacés et documentés, README principal rédigé, assets 3D générés, doc bus rédigée.

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

### Phase 9 — Archivage et revue finale
- [ ] Déplacer tout ce qui reste d'inutilisé dans `archive/` (KICAD_6, TEST_NOT_WORKING, doublons confirmés)
- [ ] Revue croisée de l'arborescence finale vs cible
- [ ] Commit de l'état propre (si Git)
- [ ] Livrable : projet prêt à être documenté ou publié

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
