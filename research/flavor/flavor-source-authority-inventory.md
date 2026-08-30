# Source-authority inventory for physical16 selectors (WP60, move 1/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Purpose

Freeze what the declared source actually authorizes before deriving further
selector candidates. Suggestive UV prose, fitted constraints, and derived
operations are kept in separate authority classes.

## Inventory

| Candidate family | Source status | Operation declared? | Proper reduction declared? | Instrument declared? |
|---|---|---:|---:|---:|
| one-loop Standard Model RG | derived equations S16-S21 | yes | no | no |
| (mathbb Z_4) spontaneous-CP vacuum | illustrative and deferred | no | no | no |
| (mathbb Z_8) flavor-spurion relation | illustrative and deferred | no | no | no |
| nine-link texture constraints | fitted presentation | no | no | no |
| texture-zero perturbations | numerical presentation test | no | no | no |

The source contains no threshold-matching law, frozen normalization,
conditional expectation, or physical reference port. Absence here means only
absence from the declared source version, not a theorem about all flavor
theory.

## Consequence

Only the one-loop SM RG is presently a fully derived source operation. It is
transport and has already failed the proper-image gate at leading order. The
other candidates may motivate successor theories, but cannot carry selector
authority until their action, vacuum/boundary rule, quotient map, and
instrument are supplied independently.

This inventory fixes the authority boundary for moves 2-6. Verification:
`python research/flavor/checkers/wp60_source_authority_inventory.py`.
