# Fitted UV-potential certificate noninheritance (WP115)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

Introduce hypothetical real moduli `A,R`, with `A` intended to set the
dimensionless coupling scale `alpha` and `R=M/M0` the mediator mass relative
to an independently supplied reference `M0`. The obvious potential targeting
WP114 is

\[
W(A,R)=(A-27/40)^2+(R-15/2)^2.
\]

It is positive, has a unique global minimum at the fitted repair point, and a
positive Hessian `2 I`. If admitted as source dynamics with an independent
`M0`, it would mathematically select a proper point in the `(alpha,M/M0)`
family.

None of those algebraic facts supplies source authority. The coefficients
`27/40` and `15/2` were obtained from the WP114 phenomenological scan. For any
other target `(a_*,r_*)`, the equally coherent potential

\[
W_{a_*,r_*}=(A-a_*)^2+(R-r_*)^2
\]

selects that answer instead. The construction is a universal target encoder,
not an explanation of why the flavor source chooses the WP114 point.

The mass ratio also exposes a separate normalization gate: without an
independently defined `M0`, the numerical statement `R=15/2` has no physical
mass prediction. Choosing `M0` after the desired mediator mass is known is the
WP62 refitted-boundary defect.

Therefore the fitted witness does not inherit source authority, instrument,
repeatability, or ensemble-prediction certificates by being rewritten as a
potential. This is the same task-indexed noninheritance principle established
in WP84, now applied to the repaired mediator parameters.

Classification: exact mathematical point selector, but unauthorized and
fitted as flavor source dynamics; not a texture rigidifier. The smallest exact
falsifier of explanatory content is the alternative potential centered at
`(A,R)=(0,0)`, which has identical positivity and Hessian certificates.
Remaining gate: derive the modulus content, coefficients, and mass reference
from independent UV symmetry/geometry or measurement before consulting the
flavor readouts.

Verification: `uv run --with sympy python
research/flavor/checkers/wp115_fitted_uv_potential_noninheritance.py`.
