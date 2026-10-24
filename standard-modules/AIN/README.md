# AIN — Module Entrées Analogiques AINSER64 (MIDIbox NG)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage, routage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension. Le détail complet de l'avertissement figure en fin de fichier.

## Description

Module d'**entrées analogiques** de l'écosystème MIDIbox NG, équivalent du **MBHP_AINSER64**. Il scanne **64 pots / faders** avec une résolution de 12 bits entre 0 et 5 V. C'est le module qui **remplace** l'ancien MBHP_AIN (non supporté par MIOS32).

Ce module est une **ré-implémentation KiCad** basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / ucapps.de**.

📖 **Article de référence :** [ucapps.de/mbhp_ainser64](https://www.ucapps.de/mbhp_ainser64.html) (fiche officielle de la plateforme MIDIbox).

> ⚠️ **Les sources KiCad de ce module ne sont PAS disponibles dans ce dépôt.**
> Le dossier `standard-modules/AIN/hardware/` ne contient **aucun fichier `.kicad_sch` / `.kicad_pcb` / `.kicad_pro`**. La seule archive de référence trouvée est `mbhp_ainser64_v1_2023-06-02.zip`, qui ne contient que des **fichiers Gerber / Eagle** (11 fichiers, `.GBL`, `.GTL`, `.GTO`, `.XLN`…) **sans schéma exploitable**.
> Le PCB d'origine ayant été conçu sous **Eagle** (non KiCad), les composants ont été netlistés directement dans le `.brd`.
>
> **Conséquence :** cette page documente le module d'après la fiche officielle **ucapps.de**, et non d'après un schéma KiCad local. Pour fabriquer ce module, il faut soit reconstruire un schéma KiCad équivalent, soit utiliser les Gerbers Eagle fournis.

## Interfaçage MIDIbox NG

- **Type de bus :** AIN (Analog Input)
- **Connecteur :** **`J19`** (SPI 5 V) du **Core32F4** — les modules AINSER64 se connectent **en parallèle** sur `J19` et sont distingués par leurs **chip-selects** (`RC1`, `RC2`)
- **Voies :** 64 entrées analogiques par module ; jusqu'à **2 modules** (128 voies) supportés par MIDIbox NG
- **Composants :** 1 × **MCP3208** (ADC 12 bits) + 8 × **CD4051** (multiplexeurs 8:1) + 1 × **74HC595** (contrôle des multiplexeurs et LED de « link »)
- **Alimentation :** 5 V ; jumper `J5` pour choisir l'alimentation analogique interne (« Dig. ») ou externe (« Ext. »), jumper `J4` pour le chip-select n°1
- **Résolution effective :** environ **10 bits** (jitter de ±1..2 LSB alimenté par USB, ±1 LSB en alimentation externe) — la notice souligne que c'est **nettement meilleur** que les ADC internes du STM32 (±16 LSB)
- **Variante :** MBHP_AINSER8 = version réduite (8 entrées, sans multiplexeur ni régulateur)

### Connecteurs de l'AINSER64 (d'après la fiche officielle)

| Connecteur | Nb de broches | Fonction |
|------------|---------------|----------|
| `J1` | 2 | Alimentation externe optionnelle (7-10 V) — 500 mA pour des pots de 1 kΩ, 50 mA pour des pots de 10 kΩ |
| `J2` | 10 | Interface série (vers `J19` du Core) |
| `J3` | 2 | Alimentation du module (USB du Core) |
| `J4` | 2 | Sélection du chip-select n°1 |
| `J5` | 3 | Sélection de l'alimentation analogique (« Dig. » / « Ext. ») |
| `J6`..`J13` | 8 | **Groupes de 8 entrées analogiques** (A0..A7), avec **+5V (Vd)** et **GND (Vs)** dédiés |

### Câblage des pots / faders

> Les deux **pattes externes** du potentiomètre se connectent à **+5V (Vd)** et **GND (Vs)** ; la **patte centrale (curseur)** se connecte à l'entrée analogique correspondante (A0..A7) du connecteur `J6`..`J13`.

> **IMPORTANT — les entrées analogiques non utilisées doivent être reliées à la masse** (avec des « dummy plugs » ou en supprimant le 4051 correspondant), sinon l'application émet des **valeurs MIDI aléatoires**.

> `Vd` n'est **jamais** connecté à `Vs` : court-circuiter l'alimentation analogique est dangereux pour le 4051.

## Fichiers inclus

| Emplacement | Contenu | Statut |
|-------------|---------|--------|
| `hardware/` | `SOURCE_AINSER64_MANQUANTE.txt` — note expliquant l'absence de sources | ⚠️ **Vide** (pas de `.kicad_*`) |
| `production/` | `mbhp_ainser64_v1_2023-06-02.zip` — Gerbers **Eagle** (11 fichiers, sans schéma) | ✅ Présent |
| `production/` | `mbhp_ainser64_orderlist.txt`, `mbhp_ainser64_interconnections.pdf` | ❌ **Absents du dépôt** (disponibles sur [ucapps.de/mbhp_ainser64](https://www.ucapps.de/mbhp_ainser64.html)) |

## Actions restant à faire

- [ ] Retrouver ou reconstruire un **schéma KiCad** du module (la source Eagle n'est pas dans le dépôt)
- [ ] Vérifier le **brochage exact** de `J2` (10 broches) et de `J6`..`J13` avant de câbler
- [ ] Vérifier les **valeurs** des 8 multiplexeurs : la fiche officielle mentionne des **4051** (CD4051) — les références exactes (CD4051B, 74HC4051) doivent être confirmées sur la nomenclature
- [ ] Produire les **Gerbers** depuis une source KiCad exploitable

---

## Crédits & Origine

Ce module est une **ré-implémentation KiCad** basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

Référence matérielle : [MBHP_AINSER64](https://www.ucapps.de/mbhp_ainser64.html) et [manuel matériel MIDIbox NG](https://www.ucapps.de/midibox_ng_manual_hw.html). Crédits : Thorsten Klose et ucapps.de. Cette page décrit le module d'après la documentation officielle ; aucune ré-implémentation KiCad n'est présente dans ce dépôt. Le dépôt ne publie pas encore de fichier de licence ; vérifier les conditions applicables à l'original avant redistribution.

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.
