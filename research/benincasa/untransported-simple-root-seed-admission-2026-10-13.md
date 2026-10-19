# First simple root: ordinary rational-seed admission fails — 2026-10-13

## Test and result

Tested history 3/root [1,1]'s untransported superfunction F0 against the sourced A-H rational library used by the historical n=8 history matcher. This is a successor test of the explicit candidate, not a change to its definition or normalization.

The library comprises the eight rational seed types on six, seven or eight nonzero columns. At n=8, enumerate every increasing support embedding and cyclic rotation used by the matcher: 320 candidates per fixture. Three exact rational fixtures gave 960 nonsingular evaluations, with no skipped singular candidate.

The transported history Ft is a positive control. Its numerator matches seed F on support {1,2,3,4,5,8}, with columns 6 and 7 zero. All six cyclic presentations of that six-column top-cell key match with full normalization exactly 1. No other library cell key matches its fermionic numerator at the tested fixtures.

F0 has the same fermionic data but full normalization ratios

    3195/9943, 4807/14596, 4122/12337

against those same F presentations. None is +1 or -1. Neither changing the source presentation nor reversing orientation admits F0 as one ordinary normalized seed in this library.

## Comparison mechanics

For each candidate, retain the two five-bracket fermionic rows, denominators and the four-row matrix consisting of the two lambda rows and those two fermionic rows. Compare it to the generalized-R history's matrix.

An exact four-column pivot constructs a prospective row-change matrix; equality on all eight columns determines proportionality of the exterior numerator. For every match, independently verify all 70 four-column minors. Full superfunction normalization uses the fourth power of that exterior ratio and the complete bosonic prefactors/denominators. This rejects fermionic/projective matching alone as admission.

Seed tokens and cell-group definitions are read from literal assignments in `check_eight_point_history_positroid_matching.py`. Its producer main is not executed. The source table in arXiv:1212.5605 was inspected: the bounded A-H library covers the rational six/seven/eight-support types used by the matcher; the algebraic four-mass branch is not tested.

## Exact disposition and scope

**Rejected candidate class:** F0 is one ordinary unit-normalized (or orientation-reversed) A-H rational canonical seed under the specified cyclic/order-preserving embeddings. A claimed rational-function equality in this class is falsified by a nonsingular exact evaluation; three fixtures retain independent normalization controls.

**Not rejected:** a multi-cell combination, the algebraic four-mass branch, a source-authorized new pushforward, coefficient-valued forms, or arbitrary positive geometries. No exhaustive classification outside the library or universal weighted-descent refutation is claimed. A sum can cancel fermionic supports, so failure to match one seed does not exclude sums.

**Still open:** source-authorized canonical/form admission of the desired K0 term. No positive common-chart or logarithmic-Jacobian certificate for F0 was produced. The transported F seed remains the positive control, not an untransported representative.

## Recommended successor

First specify which broader realization class is authorized: an actual sourced multi-cell map or an explicitly coefficient-valued form. Do not change the meaning of canonical form merely to absorb c. If a coefficient-valued extension is selected, preserve c's divisors/localizations and compute how its nonconstant boundary restrictions enter residues; unweighted source cancellation will not settle that test.

A source-authorized multi-cell alternative needs its own declared normalization and map before coefficient fitting. In parallel, the existing composite-normalization-definition task is unaffected and remains actionable. The missing full source bundle still blocks the eventual nine-to-twenty-sector replay.

## Artifacts and reproduction

    python research/benincasa/checkers/check_untransported_simple_root_seed_admission.py

- `research/benincasa/checkers/check_untransported_simple_root_seed_admission.py`
- `research/benincasa/results/untransported_simple_root_seed_admission.json`

Fresh exact rational algebra and written exterior-product comparison, not a new kernel proof or full-atlas replay. Owner producers and missing historical receipts are untouched. Verification passed means the scoped rejection and its positive controls were reproduced, not that canonical admission passed.
