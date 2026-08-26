# WP128 vacuum-source obstruction (WP436)

## Question

WP435 supplies dynamical adjoint fields and a renormalizable messenger grammar.
Does the existing WP128 scalar potential select the noncommuting flavon vacuum
without importing the infrared Yukawa matrices as external sources?

## Source-free potential

Remove the linear terms involving (H_u,H_d). For positive mass squares, the
source-free adjoint potential is

$$
V_0=
\frac{M_u^2}{2}\operatorname{Tr}A^2
+\frac{M_d^2}{2}\operatorname{Tr}D^2
-lambda\lVert[A,D]\rVert_F^2
+rho\left(\operatorname{Tr}A^2+\operatorname{Tr}D^2\right)^2.
$$

Let (x=\lVert A\rVert_F^2) and (y=\lVert D\rVert_F^2). The
Bottcher-Wenzel and arithmetic-geometric mean bounds give

$$
\lVert[A,D]\rVert_F^2\leq2xy
\leq\frac12(x+y)^2.
$$

Therefore

$$
V_0\geq
\frac{m_{min}^2}{2}(x+y)
+\left(rho-\frac{lambda}{2}\right)(x+y)^2,
$$

where (m_{min}^2=\min(M_u^2,M_d^2)>0). Under WP128's strict stability
condition (rho>lambda/2), this lower bound is strictly positive for every
nonzero pair. The unique global minimum is

$$
A=D=0.
$$

The source-free theory leaves all eight diagonal-(SU(3)_F) gauge bosons
massless and generates no Yukawa hierarchy or mixing.

## What the linear sources do

WP128 instead includes

$$
mu_u\operatorname{Tr}(AH_u)
+mu_d\operatorname{Tr}(DH_d).
$$

At leading heavy-field order these impose

$$
A_0=-\frac{mu_u}{M_u^2}H_u,
\qquad
D_0=-\frac{mu_d}{M_d^2}H_d.
$$

If (H_u,H_d) are the already fitted Yukawa Gram matrices, the flavon vacuum
inherits their spectra and relative orientation. The construction then
reconstructs and rigidifies the input flavor point; it does not select that
point from source dynamics.

In a local diagonal-(SU(3)_F) theory, fixed nontrivial (H_u,H_d) cannot be
external gauge-breaking numbers. If they are promoted to dynamical fields, the
selection problem moves to their own potential and boundary conditions.

## Disposition

WP435 establishes dynamical flavon fields, but the current WP128 potential does
not establish a source-authorized noncommuting vacuum. Positive masses plus the
coercive quartic select the symmetric origin. The nonzero vacuum is carried by
the flavor-dependent linear sources.

This is not a universal no-go for two-adjoint potentials. Tachyonic quadratic
terms, cubic invariants, mixed trace operators, radiative breaking, or a new
boundary law may generate a nonzero vacuum. Each changes the source grammar and
must be frozen before comparing its vacuum with the measured flavor point.

The smallest exact falsifier is a source-free parameter packet satisfying the
stated positive-mass and strict-coercivity assumptions while possessing a
nonzero global minimum. The lower bound excludes such a packet.

Run `uv run --with sympy python
research/flavor/checkers/wp436_wp128_vacuum_source_obstruction.py` to regenerate
the JSON result.
