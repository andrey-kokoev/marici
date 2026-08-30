# Portal-complete quartic stability for FDM-2 (WP103)

Agent: `marici.Figueiredo`. Date: 2026-08-25.

Let `u=H^dagger H>=0`, `X=x^2>=0`, and `Y=y^2>=0`. The quartic part of the
WP90 singlet potential plus the WP102 portals is

\[
Q=\lambda_Hu^2+2X^2+2Y^2+\lambda_xuX+\lambda_yuY.
\]

There is no `XY` term in the special WP90 quartic because its two square terms
cancel that cross coefficient. For fixed `u`, minimizing independently over
`X,Y>=0` gives

\[
\inf_{X,Y\ge0}{Q\over u^2}
=\lambda_H-rac{(\lambda_x^-)^2+(\lambda_y^-)^2}{8},
\qquad \lambda^-:=\min(\lambda,0).
\]

Therefore the exact quartic copositivity condition is

\[
\lambda_H\ge
\frac{(\lambda_x^-)^2+(\lambda_y^-)^2}{8}.
\]

Strict inequality supplies a coercive margin against lower-degree portal and
singlet terms. Equality requires a separate flat-ray audit because cubic or
quadratic terms can then decide boundedness.

This separates two independent selector gates. Positive `lambda_y` cannot
destabilize the large-field quartic, but a sufficiently large positive
`lambda_y u` can erase the CP-broken branch locally. Negative `lambda_y` can
enhance the CP instability locally, while excessive magnitude violates the
global quartic condition unless `lambda_H` compensates it. Local branch
existence and global source stability are therefore independent tests.

An exact admissible slice exists: `lambda_H=1`, `lambda_x=0`, `lambda_y=1`
has strict quartic margin one, and at background `u=1` retains
`y^2=9/25-1/4=11/100>0`. This establishes nonemptiness of the algebraically
stable CP-broken parameter region, not a source-derived numerical choice.

Classification: a nonempty **conditional selector parameter region**, not a
selector of its own coefficients and not a rigidifier. Smallest exact global
falsifier: `lambda_H=0,lambda_x=-1,lambda_y=0`, for which the minimizing ray
has negative quartic coefficient `-1/8`. Remaining instrument gate: declare
renormalized portal coefficients and Higgs potential at a scale, audit flat
rays and running, then derive the thermal trajectory through the stable
CP-broken region.

Verification: `uv run --with sympy python
research/flavor/checkers/wp103_fdm2_portal_copositivity.py`.
