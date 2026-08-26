# Projector flavor-lift no-go (WP324)

## Minimal matching

WP323 supplies a selected rank-one relational projector (B). The minimal
equivariant flavor lift uses only the two available commuting covariants:

\[
Y_u=a_u I+b_uB,
\qquad
Y_d=a_d I+b_dB.
\]

For any coefficients, each characteristic polynomial contains a repeated
factor:

\[
\chi_{Y_u}(\lambda)
=(a_u-\lambda)^2(a_u+b_u-\lambda),
\]

and likewise in the down sector. Both discriminants vanish identically.

## Physical consequence

The two Hermitian flavor covariants commute exactly. Consequently the lift has
a two-dimensional degenerate plane in each sector and cannot produce generic
relative mixing or CP violation. It lies on the degenerate boundary excluded
from the faithful nondegenerate `physical16` chart.

This does not invalidate the WP323 selector. It proves that selecting one
relational projector is insufficient to select a physical flavor point.

## Successor gate

A viable lift needs independently derived noncommuting source covariants that
split both degenerate planes. Their coefficients, stable vacuum, matching, and
instrument must be established upstream; fitting extra projectors to the
observed spectra would surrender selector authority.

Run `uv run --with sympy python
research/flavor/checkers/wp324_projector_flavor_lift_no_go.py` to regenerate
the exact no-go.
