# Support-five phase obstruction: WP1169

## Question

Does the explicit support-five interior witness have a unitary phase lift?

## DPC resolution

- **Problem:** test the WP1168 zero-diagonal witness.
- **Conjecture:** the witness is unistochastic.
- **Rivals:** support-induced determinant constraint; row polygon obstruction;
  column polygon obstruction; constrained phase search.
- **Risky consequences:** all \(720\) derangement carriers have only
  four-edge pair overlaps, so support supplies no two-overlap determinant
  constraint.
- **Falsification attempt:** the exact witness has three row and four column
  sqrt-product polygon failures, obstructing any unitary phase lift.
- **Residual:** another point in a support-five fixed-\(q\) polytope may
  still be unistochastic.
- **Disposition:** reject the displayed witness and select constrained
  phase-compatible search.

Checker: `research/flavor/checkers/wp1169_support_five_phase_obstruction.py`

Result: `results/wp1169_support_five_phase_obstruction.json`
