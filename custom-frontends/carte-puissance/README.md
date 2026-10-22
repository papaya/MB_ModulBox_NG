# carte-puissance — Carte de distribution des bus (passive)

> ⚠️ **Avertissement :** documentation de passion, **non professionnelle**. Fournie **sans garantie ni engagement**, **sans support technique**. Des **erreurs sont possibles** (schémas, valeurs, câblage). À vos risques et périls : vérifiez tout avant de fabriquer et de mettre sous tension.

## Description
Carte de **distribution des bus** pour l'ecosysteme MIDIbox NG : elle repartit l'alimentation 5 V et la masse vers de nombreux connecteurs IDC afin d'alimenter et de relier les modules DIN, DOUT, AIN et les front-ends.

> ⚠️ **Correction majeure : les versions anterieures de cette page decrivaient une carte d'alimentation a regulateur, avec protection contre l'inversion de polarite et des condensateurs de decouplage.** Le schema `Carte_puissance.kicad_sch` ne contient **que 32 connecteurs** et **aucun composant actif** : **pas de regulateur de tension, pas de diode de protection, pas de condensateur, pas de resistance**. C'est un simple **distributeur passif** de +5 V et GND.

📖 **Article de référence :** Aucun article dédié sur le blog ksir-diy.blogspot.com. Voir l'article global [ModulBox V2](https://ksir-diy.blogspot.com/2023/05/modulbox-v2.html).

## Assets de visualisation
| Type | Fichier | Description |
|------|---------|-------------|
| Top view | `3d-top.png` | Vue de dessus du PCB |
| Iso 3D | `3d-iso.png` | Vue isométrique avec composants |

![3D top](assets/Carte_puissance.png)

## Spécifications techniques
- **Aucun composant actif** : la carte ne fait que distribuer les tensions deja presentes
- **2 nets distincts** :
  - `+5VD` — alimentation **digitale** : alimente les 24 connecteurs IDC `J2`..`J25` (broche 10), les borniers et les entrees 1x2
  - `+5VA` — alimentation **analogique** : uniquement `J2` (broche 10) et `J32` (broche 1), isolee du reste par le jumper `J32`
- `GNDA` — masse analogique, commune a tous les connecteurs
- **Chainage par paires** : les 24 connecteurs de bus `J2`..`J25` forment **12 paires** (`J2`->`J3`, `J4`->`J5`, ... `J24`->`J25`), reliees par la **broche 6** (ligne de signal)
- `J32` est un **cavalier de separation** (« Disconect ») : il permet d'isoler le rail analogique `+5VA` du rail digital `+5VD`
- 24 × connecteurs **IDC 2x05** (`J2`..`J25`) pour le raccordement des modules et front-ends
- 4 × bornier a vis **ALTECH AK300-2** (pas 5,00 mm) : `J1` (entree), `J27` (sortie), `J28` et `J29` (entrees)
- 3 × pin header 1x02 (`J26`, `J30`, `J31`) et 1 × jumper 1x02 (`J32`)

## Composants principaux
| Type | Dénomination | Qté |
|------|-------------|-----|
| Connecteur bus | IDC Header 2x05 P2.54mm Vertical (`J2`..`J25`) | 24 |
| Bornier a vis | ALTECH AK300-2, pas 5,00 mm (`J1`, `J27`, `J28`, `J29`) | 4 |
| Connecteur d'alimentation | PinHeader 1x02 (`J26`, `J30`, `J31`) | 3 |
| Cavalier de separation | PinHeader 1x02 (`J32`, « Disconect ») | 1 |

## Brochage / Mapping MIDIbox NG

### Borniers d'alimentation
| Connecteur | Type | Broche 1 | Broche 2 |
|------------|------|-----------|----------|
| `J1` | ALTECH AK300-2 | `GNDA` | `+5VD` (entree principale) |
| `J27` | ALTECH AK300-2 | `GNDA` | `+5VD` (sortie) |
| `J28` | ALTECH AK300-2 | `GNDA` | `+5VD` (entree) |
| `J29` | ALTECH AK300-2 | `GNDA` | `+5VD` (entree) |

### Connecteurs de bus `J2`..`J25` (IDC 2x05) — chainage par paires
Les 24 connecteurs de bus forment **12 paires chainées** par la broche 6 (ligne de signal) :

| Paire | Connecteurs | Signal de la broche 6 |
|-------|-------------|------------------------|
| 1 | `J2` -> `J3` | `J2-Pad6` |
| 2 | `J4` -> `J5` | `J4-Pad6` |
| 3 | `J6` -> `J7` | `J6-Pad6` |
| 4 | `J8` -> `J9` | `J8-Pad6` |
| 5 | `J10` -> `J11` | `J10-Pad6` |
| 6 | `J12` -> `J13` | `J12-Pad6` |
| 7 | `J14` -> `J15` | `J14-Pad6` |
| 8 | `J16` -> `J17` | `J16-Pad6` |
| 9 | `J18` -> `J19` | `J18-Pad6` |
| 10 | `J20` -> `J21` | `J20-Pad6` |
| 11 | `J22` -> `J23` | `J22-Pad6` |
| 12 | `J24` -> `J25` | `J24-Pad6` |

Brochage type de chaque connecteur de bus :

| Broche | Signal | Description |
|--------|--------|-------------|
| 1 | `GNDA` | Masse commune |
| 6 | *(voir tableau ci-dessus)* | **Ligne de signal** chainee vers le connecteur suivant de la paire |
| 10 | `+5VD` | Alimentation 5 V (**`J2` porte `+5VA`**) |
| 2, 3, 4, 5, 7, 8, 9 | — | Non connectees (libres pour un cablage specifique) |

> Verifie dans le schema : seule la **broche 6** est cablee entre les deux connecteurs d'une paire ; les broches 2 a 5 et 7 a 9 sont **libres** (non connectees) et la broche 10 est l'alimentation 5 V.
>
> Chaque paire peut donc transporter un **bus DIN, DOUT ou AIN** (signal + 5V + GND) : le connecteur d'entree de la paire se branche sur le module ou le front-end, celui de sortie continue la chaine.
>
> Les **lignes de signal** des bus DIN / DOUT / AIN **passent par cette carte** via la broche 6 des paires ; l'alimentation 5 V et la masse sont, elles, communes a tous les connecteurs.

### Connecteurs 1x02
| Connecteur | Broche 1 | Broche 2 | Role |
|------------|-----------|----------|------|
| `J26` | `GNDA` | `+5VD` | Entree d'alimentation |
| `J30` | `GNDA` | `+5VD` | Entree d'alimentation |
| `J31` | `GNDA` | `+5VD` | Entree d'alimentation |

### `J32` — cavalier de separation analogique / digital
| Broche | Signal | Role |
|--------|--------|------|
| 1 | `+5VA` | Rail analogique (relie a `J2` broche 10) |
| 2 | `+5VD` | Rail digital |

> **Position du cavalier :** `J32` **retire** = les rails `+5VA` et `+5VD` sont separes (le rail analogique n'est plus alimente par le rail digital, il faut l'alimenter par ailleurs). `J32` **pose** = `+5VA` et `+5VD` sont relies (alimentation analogique depuis le digital).
>
> Ce cavalier est la seule « intelligence » de la carte : il permet d'isoler l'alimentation analogique de l'AINSER64 pour limiter le bruit, comme recommande par [ucapps.de/mbhp_ainser64](https://www.ucapps.de/mbhp_ainser64.html) ( jumper `J5` sur l'AINSER64).

## Documentation de fabrication
- `hardware/` : sources KiCad (`Carte_puissance.*`)
- `production/` : Gerbers, BOM (`bom.csv`), netlist, PDF du schéma

---

## Conception & Compatibilité

Carte d'interface **originale MB MODULBOX NG** (conception Ksir), compatible avec les bus et modules du système MIDIbox NG. Ce n'est **pas** un module officiel MIDIbox.

> **Licence & Usage :** Ces fichiers hardware sont partagés sous licence Open-Source Hardware pour un usage DIY / personnel / non-commercial. **Aucune garantie ni engagement** n'est fourni sur la justesse du câblage ou du routage.

**Rétro-ingénierie par l'équipe — GPL-3.0**

