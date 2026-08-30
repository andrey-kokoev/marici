# C8 positive-regulator chamber graph to Orlik–Solomon comparison

## Map

Each feasible positive-regulator chamber is encoded by its signs against all primitive minimal-circuit offset forms. Two chambers are adjacent when exactly one circuit sign changes.

Associate to a chamber (s) the graded exterior potential

\[
P(s)=\sum_{C:s_C>0}\partial e_C.
\]

For an oriented adjacent pair (s\to s'),

\[
P(s')-P(s)=\pm\partial e_C,
\]

where (C) is the unique crossed circuit. Hence closed chamber paths telescope before taking any quotient.

## Census

All 288 graphs are connected. Their shapes are:

| chambers | edges | cycle rank | occurrences |
|---:|---:|---:|---:|
| 4 | 3 | 0 | 160 |
| 5 | 5 | 1 | 16 |
| 6 | 6 | 1 | 80 |
| 8 | 8 | 1 | 32 |

Every edge image lies in the full OS ideal by construction. Entry 1923 supplies exact shared-ideal expressions for every private circuit boundary, so even private crossing images vanish without adjoining a new generator.

## What this proves

The induced map from chamber differences to the OS quotient is zero. Therefore the existing Carrier incidence algebra removes regulator-hierarchy dependence at this associated grade.

## What it does not prove

The potential (P) is a combinatorial comparison, not the physical relative current. A physical theorem requires a source-derived Betti/de Rham comparison showing that continued Bunch--Davies chains map to these same oriented crossing classes with compatible normalization and homotopy.

## Artifacts

- `checkers/eight_site_rank4_regulator_os_comparison.py`
- `results/eight-site-rank4-regulator-os-comparison.json`
