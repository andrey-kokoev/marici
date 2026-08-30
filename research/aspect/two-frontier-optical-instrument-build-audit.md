# Two-frontier optical instrument build audit

Owner: `marici.Aspect`

## Bounded question

Are both operator-requested frontier instruments present, executable, passing,
and prevented from borrowing authority from the sectors they emulate?

## Instrument pair

1. `reciprocal-denominator-sewing-network.md` tests denominator/numerator
   separation, Schur first jets, mixed incidence terms, and telescoping.
2. `directional-double-triangle-moving-fiber-interferometer.md` tests
   horizontal forgetting, the allowed reverse extension, kernel holonomy, and
   global gluing.

Both use exact source-fixed finite matrices and phase-calibrated coherent
ports.  Neither constructs the theta/Tate sector matrix or Benincasa's
double-triangle geometric connection.

## Cross-instrument hostile

A determinant identity is not a horizontal quotient map, and an upper
triangular connection is not a zero-free determinant theorem.  The audit
requires each result to declare its own missing source/completion boundary;
passing one instrument cannot fill the other's detector kernel or authority.

## Completion gate

The build is complete as an exact finite optical instrument pair.  Physical
fabrication, uncertainty calibration, continuum limits, source-derived sector
matrices, and experimental data remain open.

Run `python research/aspect/checkers/two_frontier_optical_instrument_build_audit.py`.
The result is
`research/aspect/results/two_frontier_optical_instrument_build_audit.json`.
