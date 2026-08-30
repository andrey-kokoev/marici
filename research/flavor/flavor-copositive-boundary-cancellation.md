# Copositive boundary cancellation: WP703

## Hostile stability gate

Continue WP702 in the declared radial quartic grammar

\[
V_4=\frac{\lambda_h h^4}{4}+\frac{\lambda_x x^4}{4}
+\frac{p_{\mathrm{UV}}h^2x^2}{2},
\qquad
p_{\mathrm{low}}=p_{\mathrm{UV}}+\Delta_p.
\]

For nonnegative radial coordinates, boundedness requires

\[
\lambda_h>0,\qquad \lambda_x>0,\qquad
p_{\mathrm{UV}}> -\sqrt{\lambda_h\lambda_x}.
\]

The stronger local mixed-vacuum condition used by WP685 is

\[
\lambda_h\lambda_x-p_{\mathrm{UV}}^2>0.
\]

Neither condition forces a nonnegative UV portal boundary.

## Exact cancellation inside the stable domain

Take

\[
\lambda_h=\lambda_x=2,
\qquad
\Delta_p=1,
\qquad
p_{\mathrm{UV}}=-1.
\]

Then the copositivity margin is one, the mixed-vacuum determinant margin is
three, and yet

\[
p_{\mathrm{low}}=0.
\]

More generally, every positive correction satisfying

\[
0<\Delta_p<\sqrt{\lambda_h\lambda_x}
\]

has the strictly stable cancellation preimage

\[
p_{\mathrm{UV}}=-\Delta_p.
\]

## Disposition

Vacuum boundedness and the radial mixed-vacuum Hessian do not turn affine
threshold matching into a selector. Imposing (p_{\mathrm{UV}}\geq0) would
remove this preimage, but that is an additional boundary postulate, not a
consequence of the admitted stability conditions. Even that postulate would
select only a portal sign/support half-space; it would not fix the WP700 ratio
corridor while the self-coupling boundary remains free.

The smallest exact falsifier is the rational stable point above. The remaining
gate is a source-derived noninvertible boundary law stronger than copositivity,
with its basin and completion stability proved independently of the desired
low-energy portal value.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp703_copositive_boundary_cancellation.py

Generated result: results/wp703_copositive_boundary_cancellation.json.
