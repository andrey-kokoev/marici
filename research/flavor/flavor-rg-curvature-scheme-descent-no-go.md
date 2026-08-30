# RG Curvature Anchors Do Not Descend under Scheme Reparameterization

## Question

Are the WP827 acceleration extrema intrinsic events of the physical RG
trajectory, or extrema of a chosen coupling coordinate?

## Admissible same-orbit hostile

Start with

\[
\dot u=\kappa u(1-u),
\qquad 0\leq u\leq1,
\]

and make the regular monotone coupling redefinition

\[
v=f(u)=u+\frac12u(1-u).
\]

It fixes both endpoints and has

\[
f'(u)=\frac32-u>0
\]

throughout the unit interval. It therefore preserves the oriented physical
trajectory and RG time. The transformed beta function is the chain-rule
pushforward

\[
\dot v=f'(u)\dot u
=\kappa u(u-1)\left(u-\frac32\right).
\]

The linearized exponents at the two fixed points remain \(+\kappa\) and
\(-\kappa\). The same portal event \(u=1/2\) is now labelled \(v=5/8\).

## Curvature anchors move

Extrema of the new coordinate acceleration satisfy

\[
24u^3-48u^2+26u-3=0.
\]

This cubic has exactly two roots in \((0,1)\) and one root above one. The old
anchors

\[
u_\pm=\frac{3\pm\sqrt3}{6}
\]

give respectively \(+\sqrt3/3\) and \(-\sqrt3/3\) when substituted into the
new anchor polynomial, so neither remains an acceleration extremum.

The new two internal roots are not reflection complements. If a root \(x\)
and its complement \(1-x\) both solved the cubic, the polynomial and its
reflection would share a root. Their resultant is the nonzero integer

\[
110592.
\]

Thus the two new acceleration extrema are not equally spaced in RG time around
the unchanged portal event. The WP827 ratio \(2+\sqrt3\) does not descend.

## Threshold meaning

A finite threshold matching map is precisely capable of inducing such a
regular coupling redefinition between effective descriptions. Consequently,
topological survival of the heteroclinic crossing does not imply survival of
coordinate acceleration extrema. Matching the beta coefficient \(\kappa\)
is insufficient: this hostile preserves \(\kappa\) as the endpoint critical
exponent while destroying the curvature triplet.

The first nonfaithful arrow is therefore

\[
\text{physical RG trajectory}
\longrightarrow
\text{chosen coupling-coordinate acceleration jet}.
\]

## Aspect germ disposition

WP828's abstract ternary carrier is structurally well formed, but its proposed
event labels do not survive the relevant scheme fibers. The curvature triplet
is a chart rigidifier unless the source independently supplies a physically
normalized running observable and threshold matching in that same observable.
Only after that freezing may its acceleration extrema be offered to a common
detector.

## Consequence for the portal objective

The logistic orbit still conditionally selects orientation, the midpoint
crossing, and a basin. It does not source-authorize the two curvature anchors
or their numerical scale ratio. The required repair is stronger than deriving
\(\kappa\): derive one operational coupling coordinate from the complete
matter action, carry its calibrated definition through every threshold, and
measure all three events with the same instrument.

## Smallest exact falsifier

The pair \(u\) and \(v=u+u(1-u)/2\) describes the same oriented trajectory,
fixed points, RG clock, critical exponents, and portal event. It produces
different acceleration extrema. This single pair refutes scheme-independent
authority for the WP827 anchors.

## Disposition

Negative descent theorem. Coordinate curvature is not an invariant of the
physical RG flow. WP827's ratio is conditional on a physically frozen running
coordinate and matched instrument, neither of which is currently supplied.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp829_rg_curvature_scheme_descent_no_go.py
```
