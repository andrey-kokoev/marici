# Phase-compatible interior constraint census: WP1161

## Question

How constrained is the phase-compatible support-four interior search?

## DPC resolution

- **Problem:** reduce the search after the WP1160 phase obstruction.
- **Conjecture:** some support-four interior point can satisfy the two-overlap
  amplitude equations.
- **Rivals:** minimal \(9+9\) constraint carrier; \(10+10\) carrier;
  \(12+12\) carrier; phase-compatible witness.
- **Risky consequences:** \(67\,950\) carriers, equal amplitude products on
  every two-column row overlap, equal products on every two-row column
  overlap, and an eight-dimensional representative polytope.
- **Falsification attempt:** every carrier has at least \(18\) exact
  two-overlap amplitude constraints; the minimal carrier census is
  \(50\,400\) of \(67\,950\).
- **Residual:** the amplitude equation system remains unsolved; constraint
  count alone neither constructs nor excludes a witness.
- **Disposition:** complete the constraint census and select the minimal
  amplitude-system solve.

Checker: `research/flavor/checkers/wp1161_phase_compatible_constraint_census.py`

Result: `results/wp1161_phase_compatible_constraint_census.json`
