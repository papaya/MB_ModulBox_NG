# Encoders Board — Carte Encodeurs (8 × PEC16)

## Description

La **Encoders Board** est la carte qui héberge physiquement les 8 encodeurs PEC16 avec leurs poussoirs.

## Composants principaux

| Type | Dénomination | Qté |
|------|-------------|-----|
| Encodeur rotatif | PEC16 (PEC164120FS0012) | 8 |
| Registre d'entrée | SN74HC165N | 3 |
| Condensateur découpling | C 100 nF | 8 |

## Brochage

| Connecteur | Signal | Description |
|------------|--------|-------------|
| J1-J3 | IDC 2x05 | 8× poussoir (vers Control Board J11) |
| J4-J6 | IDC 1x06 | 8× phases A/B (vers Control Board J15) |

## Architecture

- 8 × PEC16 avec poussoir : 24 entrées DIN (8× A, 8× B, 8× poussoir)
- 3 × 74HC165 : lecture des 24 entrées via 3 registres de décalage
- 8 × C 100 nF : découpling par encodeur

## Production

- `encoders-board/production/` : Gerbers, BOM, positions, netlist

---

> ⚠️ Document créé lors de la séparation en 3 sous-projets (23/10/2026). Contenu à compléter avec les sources KiCad réelles après extraction du schéma original.