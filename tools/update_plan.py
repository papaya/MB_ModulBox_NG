with open("PLAN.md", "r", encoding="utf-8") as f:
    content = f.read()

# Remplacer la section Core RECOMMANDATION par le statut terminé
old_core = """#### standard-modules/Core — RECOMMANDATION : basculer sur Core32f4_V0.1 (audit 18/10/2026)
- Variantes comparées : `V4` (1,4 MB PCB sans schéma, 443 DRC, 10 non connectés) vs `core32V7` (0,5 MB PCB sans schéma, 455 DRC, 39 non connectés) vs **`Core32f4_V0.1` — trio complet : schéma 3 MB + PCB 1,3 MB + libs (27/05/2024), ERC 122, DRC 66, 0 non connectés, dossier `production/` (bom.csv, netlist.ipc, positions.csv, zip)**
- Verdict : **V0.1 est la meilleure source** (schéma + PCB cohérents, ordres de grandeur moins de violations, travail logique et complet : 12 IDC, 5 CORE32, empreinte ksir)
- [ ] Protocole de bascule : sauvegarde V4/core32V7 dans `archive/` → copie du trio `Core32f4_V0.1.*` vers `standard-modules/Core/hardware/` (renommer en `Core32F4.*`) → ajouter tables `sym/fp-lib-table` → refill zones → re-ERC/re-DRC → revalider README"""

new_core = """#### standard-modules/Core/Core32F4 — Basculé sur Core32f4_V0.1 ✅ (audit 18/10/2026)
- [x] Anciennes versions V4 et core32V7 archivées dans `archive/superseded-core-v4-core32V7/`
- [x] Nouveau trio : `Core32F4.kicad_pro`, `.kicad_sch`, `.kicad_pcb` (provenant de `Core32f4_V0.1`)
- [x] Tables `sym-lib-table`/`fp-lib-table` créées
- [x] Production complète (Gerbers, BOM, netlist, positions) présente
- [x] Variantes comparées : `V4` (1,4 MB PCB sans schéma, 443 DRC, 10 non connectés) vs `core32V7` (0,5 MB PCB sans schéma, 455 DRC, 39 non connectés) vs `Core32f4_V0.1` (schéma 3 MB + PCB 1,3 MB, ERC 122, DRC 66, 0 non connectés) — **V0.1 validée comme version maître**"""

content = content.replace(old_core, new_core)

# Remplacer la section DOUT RECOMMANDATION par le statut terminé
old_dout = """#### standard-modules/DOUT — RECOMMANDATION : basculer sur Dout2024 (audit 18/10/2026)
- Variantes comparées : DOUT actuel (sch 46 symboles, 22 empreintes, DRC 96) vs **`Dout2024` (01/04/2024 : sch 117 kB/75 symboles, PCB 0,7 MB/22 empreintes, ERC 54, DRC 74, dossier complet Gerber_DOUT+production, libs `ksir 2022`, `lib 2022 ksir`)**
- Verdict : **Dout2024 est la meilleure source** (schéma plus riche, dossier complet) — son DRC 74/21 non connectés reste supérieur au DOUT actuel déjà traité (DRC 96/0)
- [ ] Protocole de bascule : sauvegarde DOUT actuel dans `archive/` → copie trio `Dout2024.*` vers `standard-modules/DOUT/hardware/` (renommer en `DOUT.*`) → tables `sym/fp-lib-table` → refill → re-ERC/re-DRC → README"""

new_dout = """#### standard-modules/DOUT/DOUT — Basculé sur Dout2024 ✅ (audit 18/10/2026)
- [x] Ancienne version `DOUT`_2024 (sans schéma) archivée dans `archive/superseded-dout/`
- [x] Nouveau trio : `DOUT.kicad_pro`, `.kicad_sch`, `.kicad_pcb` (provenant de `Dout2024`)
- [x] Tables `sym-lib-table`/`fp-lib-table` créées
- [x] Production complète (Gerbers, BOM, netlist, positions) présente
- [x] Variante comparée : DOUT`_2024 (PCB sans schéma) vs `Dout2024` (schéma 117 kB + PCB complet) — **Dout2024 validée comme version maître**"""

content = content.replace(old_dout, new_dout)

with open("PLAN.md", "w", encoding="utf-8") as f:
    f.write(content)

print("PLAN.md mis à jour avec succès")