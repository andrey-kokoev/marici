# Matching symmetry orbits: WP1146

## Question

Does the equal-weight twin swap reduce six matchings to a unique orbit?

## DPC resolution

- **Problem:** test whether the equal-dimension branches reduce the six
  rank-three matchings without new source authority.
- **Conjecture:** the equal-weight twin symmetry uniquely reduces the six
  matchings.
- **Rivals:** six labeled matchings; three twin-swap orbits; one selected
  orbit; no algebraic uniqueness.
- **Risky consequences:** only branches 4 and 5 have equal source weights; the
  swap preserves \(q\) and \(u\); every orbit has size two; no fixed matching
  exists.
- **Falsification attempt:** the twin swap acts freely and produces exactly
  three two-element orbits, so it does not select a unique matching.
- **Residual:** a sourced branch-exchange representation or production kernel
  may reduce the orbits further.
- **Disposition:** reject algebraic uniqueness and classify three twin-swap
  orbits.

## Exact result

The six candidates form three orbits of size two under swapping the two
dimension-2 branches. Equal weights preserve the algebraic problem but do not
prove physical production-kernel exchange symmetry.

Checker: `research/flavor/checkers/wp1146_matching_symmetry_orbits.py`

Result: `results/wp1146_matching_symmetry_orbits.json`
