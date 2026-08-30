# Primitive Dual-Pairing Portal Inevitability Audit

## Question

Can a primitive nondegenerate dual pairing exclude the zero-coupling cusp and
turn WP872's conditional nonzero selector into an unavoidable portal?

## Claim boundary

Introduce a dual source coupling \(g_D>0\) and require the primitive pairing

\[
\Delta_Q\,g\,g_D=1.
\]

For the frozen primitive diameter \(\Delta_Q=2\), this is a nondegenerate
source constraint. Neither \(g\) nor \(g_D\) can vanish. Exact duality exchanges
the two couplings:

\[
\sigma(g,g_D)=(g_D,g).
\]

The unique positive self-dual point on the primitive pairing locus is

\[
g=g_D=\frac1{\sqrt{\Delta_Q}}
=\frac1{\sqrt2}.
\]

Thus a primitive dual pair supplies precisely the datum missing in WP872:
zero coupling is not an object of the admitted source domain. The integer
pairing must be primitive. A pairing level \(n>0\),

\[
\Delta_Qgg_D=n,
\]

would instead select \(\sqrt{n/\Delta_Q}\), so primitivity is substantive
rather than conventional.

## Pairing-preserving reciprocal basin

Set

\[
y=\log\frac{g}{g_D}
=\log(\Delta_Qg^2)
\]

on the primitive locus. The flow

\[
\frac{d\log g}{d\tau}=-\frac12\tanh y,
\qquad
\frac{d\log g_D}{d\tau}=+\frac12\tanh y
\]

preserves \(\Delta_Qgg_D=1\) exactly and gives

\[
\dot y=-\tanh y.
\]

It is the WP872 log-cosh reciprocal gradient. Every admitted source point
converges to the self-dual coupling, with exact solution

\[
\sinh y(\tau)=e^{-\tau}\sinh y(0).
\]

The nonzero portal and its full basin are therefore consequences of one
primitive self-dual pairing packet rather than an exclusion appended to the
flow.

## Sign and groupoid

The positive pairing fixes magnitudes. The portal sign remains relative to the
oriented odd boundary of WP859 and WP867. Reversing the pairing orientation
and boundary orientation gives the mirror source. Selecting the positive
orientation restricts the groupoid to the stabilizer of a reference
orientation; it does not reveal an absolute sign.

## Threshold hierarchy

Pairing preservation alone is insufficient. The threshold rescaling

\[
(g,g_D)\longmapsto(\lambda g,g_D/\lambda)
\]

preserves the primitive product for every \(\lambda>0\) but changes the
electric portal amplitude. It commutes with duality exchange only for
\(\lambda=1\). Therefore exact survival requires the threshold operation to
intertwine both:

1. the primitive pairing;
2. the electric–dual exchange.

Together with WP869's marked-projector transport and WP870's Ward vertex, this
would preserve the selected coupling and its detector attachment.

## Physical source and instrument boundary

No admitted flavor source currently supplies \(g_D\) as a physical dual
coupling or the primitive pairing as an experimentally accessible operation.
Adding such a port changes the source theory and its physical groupoid. It is
not a reinterpretation of the original electric flavor experiment.

A typed realization would require:

- a microscopic flavor sector carrying electric and dual charges;
- an exact primitive pairing with \(\Delta_Q=2\) normalization;
- a duality-intertwining threshold theorem;
- a Ward-locked electric detector and an executable dual/reference port;
- finite-width calibration into 'physical16' detector units.

Without these objects, the pairing is a mathematically sufficient candidate
principle, not an established flavor theorem.

## Smallest exact falsifiers

- Pairing level \(n=2\) selects \(g=1\), not \(1/\sqrt2\).
- The product-preserving threshold \(\lambda=2\) sends the self-dual point to
  \((\sqrt2,1/(2\sqrt2))\), preserving the pairing while destroying
  self-duality and the electric prediction.
- Removing the dual port returns the zero-cusp ambiguity of WP872.

## Disposition

Strongest sufficient abstract source principle found: a primitive,
nondegenerate, self-dual boundary pairing. It excludes exact decoupling, fixes
the positive magnitude, carries the reciprocal global basin, and—when combined
with the odd boundary, duality-intertwining Kato threshold transport, and Ward
vertex—supplies the requested sign, magnitude, basin, threshold survival, and
source-level readout.

The result remains conditional because flavor has no admitted microscopic
dual port, primitive pairing, or calibrated realization. The next decisive
test is existence: construct such a flavor dual pair independently of the
desired \(1/\sqrt2\), or close this branch as an added-source architecture.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp873_primitive_dual_pairing_portal_inevitability_audit.py
~~~
