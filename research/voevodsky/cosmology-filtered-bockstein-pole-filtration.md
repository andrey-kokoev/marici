# Pole-filtered algebraic Bockstein

## Question

Does the exhaustive pole-order filtration exclude any certified primitive and thereby expose a filtered connecting class?

## Result

No. All 1,224 seed certificates were checked. For every nonzero word, the maximum grade of a used source generator equals the target grade; none exceeds it. The exact grade-pair census is:

| target to primitive grade | count |
|---|---:|
| 6 to 6 | 32 |
| 7 to 7 | 128 |
| 8 to 8 | 276 |
| 9 to 9 | 360 |
| 10 to 10 | 280 |
| 11 to 11 | 124 |
| 12 to 12 | 24 |

The census includes 576 structurally zero q words. Therefore every exact primitive is admissible at its target filtration grade, and the pole-filtered algebraic Bockstein remains zero.

## Claim boundary

This is a statement about the exhaustive algebraic pole filtration. It does not identify that filtration with a DNC or I-adic filtration and supplies no support, exceptional, or physical Bockstein.

## Disposition

The only available typed filtration does not create the required non-monotone restriction. The next executable rival is to audit whether any already-defined alternative normal interface changes the derivative target rather than merely reparametrizing the certified `nx` interface.

## Verification

- `research/voevodsky/check_cosmology_filtered_bockstein_pole_filtration.py` — exit 0
- `research/voevodsky/results/cosmology_filtered_bockstein_pole_filtration.json`
