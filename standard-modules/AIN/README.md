# AIN — Module Entrées Analogiques AINSER64 (MIDIbox NG)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

## Description
Module d'**entrees analogiques** de l'ecosysteme MIDIbox NG, equivalent du **MBHP_AINSER64**. Il scanne **64 pots / faders** avec une resolution de 12 bits entre 0 et 5 V. C'est le module qui **remplace** l'ancien MBHP_AIN (non supporte par MIOS32).

📖 **Article de référence :** [ucapps.de/mbhp_ainser64](https://www.ucapps.de/mbhp_ainser64.html) (fiche officielle de la plateforme MIDIbox).

> ⚠️ **Les sources KiCad de ce module ne sont PAS disponibles dans ce depot.**
> Le dossier `standard-modules/AIN/hardware/` ne contient **aucun fichier `.kicad_sch` / `.kicad_pcb` / `.kicad_pro`**. La seule archive de reference trouvee est `mbhp_ainser64_v1_2023-06-02.zip`, qui ne contient que des **fichiers Gerber / Eagle** (11 fichiers, `.GBL`, `.GTL`, `.GTO`, `.XLN`…) **sans schema exploitable**.
> Le PCB d'origine ayant ete concu sous **Eagle** (non KiCad), les composants ont ete netlistes directement dans le `.brd`.
>
> **Consequence :** cette page documente le module d'apres la fiche officielle **ucapps.de**, et non d'apres un schema KiCad local. Pour fabriquer ce module, il faut soit reconstruire un schema KiCad equivalent, soit utiliser les Gerbers Eagle fournis.

## Interfaçage MIDIbox NG
- **Type de bus :** AIN (Analog Input)
- **Connecteur :** **`J19`** (SPI 5 V) du **Core32F4** — les modules AINSER64 se connectent **en parallele** sur `J19` et sont distingues par leurs **chip-selects** (`RC1`, `RC2`)
- **Voies :** 64 entrees analogiques par module ; jusqu'a **2 modules** (128 voies) supportes par MIDIbox NG
- **Composants :** 1 × **MCP3208** (ADC 12 bits) + 8 × **CD4051** (multiplexeurs 8:1) + 1 × **74HC595** (controle des multiplexeurs et LED de « link »)
- **Alimentation :** 5 V ; jumper `J5` pour choisir l'alimentation analogique interne (« Dig. ») ou externe (« Ext. »), jumper `J4` pour le chip-select n°1
- **Resolution effective :** environ **10 bits** (jitter de ±1..2 LSB alimenté par USB, ±1 LSB en alimentation externe) — la notice souligne que c'est **nettement meilleur** que les ADC internes du STM32 (±16 LSB)
- **Variante :** MBHP_AINSER8 = version reduite (8 entrees, sans multiplexeur ni regulateur)

### Connecteurs de l'AINSER64 (d'apres la fiche officielle)
| Connecteur | Nb de broches | Fonction |
|------------|---------------|----------|
| `J1` | 2 | Alimentation externe optionnelle (7-10 V) — 500 mA pour des pots de 1 kΩ, 50 mA pour des pots de 10 kΩ |
| `J2` | 10 | Interface serie (vers `J19` du Core) |
| `J3` | 2 | Alimentation du module (USB du Core) |
| `J4` | 2 | Selection du chip-select n°1 |
| `J5` | 3 | Selection de l'alimentation analogique (« Dig. » / « Ext. ») |
| `J6`..`J13` | 8 | **Groupes de 8 entrees analogiques** (A0..A7), avec **+5V (Vd)** et **GND (Vs)** dedies |

### Cablage des pots / faders
> Les deux **pattes externes** du potentiometre se connectent a **+5V (Vd)** et **GND (Vs)** ; la **patte centrale (curseur)** se connecte a l'entree analogique correspondante (A0..A7) du connecteur `J6`..`J13`.
>
> **IMPORTANT — les entrees analogiques non utilisees doivent etre reliees a la masse** (avec des « dummy plugs » ou en supprimant le 4051 correspondant), sinon l'application emet des **valeurs MIDI aleatoires**.
>
> `Vd` n'est **jamais** connecte a `Vs` : court-circuiter l'alimentation analogique est dangereux pour le 4051.

## Fichiers inclus
| Emplacement | Contenu | Statut |
|-------------|---------|--------|
| `hardware/` | `SOURCE_AINSER64_MANQUANTE.txt` — note expliquant l'absence de sources | ⚠️ **Vide** (pas de `.kicad_*`) |
| `production/` | `mbhp_ainser64_v1_2023-06-02.zip` — Gerbers **Eagle** (11 fichiers, sans schema) | ✅ Present |
| `production/` | `mbhp_ainser64_orderlist.txt`, `mbhp_ainser64_interconnections.pdf` | ❌ **Absents du depot** (disponibles sur [ucapps.de/mbhp_ainser64](https://www.ucapps.de/mbhp_ainser64.html)) |

## Actions restant a faire
- [ ] Retrouver ou reconstruire un **schema KiCad** du module (la source Eagle n'est pas dans le depot)
- [ ] Verifier le **brochage exact** de `J2` (10 broches) et de `J6`..`J13` avant de cabler
- [ ] Verifier les **valeurs** des 8 multiplexeurs : la fiche officielle mentionne des **4051** (CD4051) — les references exactes (CD4051B, 74HC4051) doivent etre confirmees sur la nomenclature
- [ ] Produire les **Gerbers** depuis une source KiCad exploitable

---

## Crédits & Origine

Ce module est une ré-implémentation sous KiCad basée sur les schémas originaux de la plateforme **MIDIbox (MBHP)** conçue par **Thorsten Klose / [ucapps.de](http://www.ucapps.de/)**.

> **Licence & Usage :** Ce matériel est fourni sous licence Open Hardware à but strictement personnel, éducatif et DIY (**Non-Commercial**). Toute utilisation commerciale est exclue. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Référence MIDIbox NG — GPL-3.0**
