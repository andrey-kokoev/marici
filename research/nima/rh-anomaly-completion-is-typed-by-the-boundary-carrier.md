# Anomaly completion is typed by the boundary carrier

## Boundedness is not an invariant gate

A finite anomaly potential tower does not determine its own completion. The
same compatible sequence can be admitted by a product carrier, rejected by a
convergent-sequence carrier, or admitted only after subtracting a limiting
boundary value.

Let \(d_n\) be source-typed transition increments and normalize \(u_0=0\):

\[
u_N=\sum_{n=1}^{N}d_n.
\]

Three elementary towers separate the possibilities:

\[
d_n=2^{-n},
\qquad
d_n=(-1)^{n+1},
\qquad
d_n=1.
\]

Their potentials respectively converge, remain bounded while oscillating,
and diverge.

## Three possible carriers

The unrestricted product carrier admits every coordinatewise compatible
tower. The bounded-sequence carrier admits the first two examples. The
convergent-sequence carrier admits only the first. If the completed determinant
frame is required to have a scalar boundary value, convergence rather than
boundedness is the relevant gate.

After the limiting value \(u_\infty\) is supplied by a source boundary map,
the remainder

\[
u_N-u_\infty
\]

belongs to the null-at-infinity carrier. This separates two operations that
must not be conflated:

1. proving that a limit exists;
2. selecting and typing that limit as endpoint or archimedean data.

## Categorical correction

The cutoff diagram alone specifies a pro-object. A completed anomaly frame
requires a declared realization functor from that pro-object into a boundary
category. Different realization functors preserve different limits and hence
give different answers to the same finite tower.

Therefore the operative coherencer is not merely a uniformly bounded family of
finite null-homotopies. It is a natural transformation whose image converges
in the source-authorized boundary realization. Its boundary value must agree
with reciprocal dagger sewing and retain the separate primitive and square
gradings.

## Consequence for the theta programme

The current finite determinant and cocycle results do not choose among the
product, bounded, convergent, graph-norm, or distributional realizations. The
theta, Tate, endpoint, and archimedean source maps must determine the carrier.
Only then is completion escape a well-typed proposition.

This also sharpens the finite falsifier. A proposed global determinant frame
fails if its potentials are not Cauchy in the declared realization topology,
even when every finite cocycle is exact and all potential norms are uniformly
bounded.

## DPC verdict

Finite exactness determines a pro-frame, not a completed frame. Completion is
a source-authorized realization functor. Bounded oscillation is the smallest
witness separating those notions.

## Verification

`check_rh_anomaly_boundary_carriers.py` classifies convergent, bounded
oscillatory, and unbounded exact towers under product, bounded, convergent, and
null-at-infinity carrier tests.
