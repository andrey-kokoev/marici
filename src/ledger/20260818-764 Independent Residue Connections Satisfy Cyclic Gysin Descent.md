---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 764 — Independent Residue Connections Satisfy Cyclic Gysin Descent

## Frozen chart geometries

Let \(K_{12}(x,y,z;a,b)\) and \(K_{1,12}\) be the closed
Cayley--Menger residue polynomials with \(c=-E\).  The other two charts were
constructed directly from the labelled cyclic source data:

\[
K_{23}(x,y,z;b,c)=K_{12}(y,z,x;a,b),
\]

\[
K_{31}(x,y,z;c,a)=K_{12}(z,x,y;a,b),
\]

and likewise for \(K_1\).  Thus the retained coordinates are respectively

\[
(a,b),\qquad(b,c),\qquad(c,a).
\]

For each chart and each base derivative, the four master derivatives were
reduced independently modulo that chart's own Jacobian exact image.  Neither
target connection was obtained by conjugating or transporting the existing
\(G_{12}\) matrix.

## Source-derived homogeneous gauge

The residue polynomial is homogeneous of total energy degree six:

\[
K_0\mapsto z^6K_0,
\qquad
K_1\mapsto z^5K_1.
\]

Since \(da\wedge db\) has degree two, the raw master weights are

\[
\boxed{(-2,-1,1,1)}
\]

for the double-pole class and the three simple-pole classes

\[
\frac{K_1\,da\wedge db}{K_0^{3/2}},\quad
\frac{da\wedge db}{K_0^{1/2}},\quad
\frac{a^2da\wedge db}{K_0^{1/2}},\quad
\frac{b^2da\wedge db}{K_0^{1/2}}.
\]

This corrects Entry 761's attempted use of the infinity-coordinate weights
((-1,0,2,2)) for physical energy rescaling.

## Cyclic horizontalities

For

\[
\rho:(X_1,X_2,X_3)\mapsto(X_3,X_1,X_2),
\]

the normalized base map and scale are

\[
U=\frac{2u}{u-v},\qquad
V=\frac{2(2-v)}{u-v},\qquad
z=\frac{u-v}{2}.
\]

The cyclic residue orientations

\[
da\wedge db,\quad db\wedge dc,\quad dc\wedge da
\]

all transport with sign (+1).  With

\[
S=\operatorname{diag}(z^{-2},z^{-1},z,z),
\]

the independently reduced connections satisfy

\[
\boxed{
A_i=dS\,S^{-1}+S\rho^*A_{i+1}S^{-1}
}
\]

for all three edges

\[
G_{12}\to G_{23},\qquad
G_{23}\to G_{31},\qquad
G_{31}\to G_{12}.
\]

Exact finite-field tests at 24 generic points in both base directions give
zero failures on every edge.  The signed cyclic product also gives

\[
S\rho^*S(\rho^2)^*S=1
\]

with zero failures.  The inverse weight convention fails on every edge at
all 24 points.

## Narrow result

The rank-four Gysin extension is a genuine cyclic occurrence object at the
generic connection level.  Entry 761's failure was caused by two type
errors: reuse of the fixed \(G_{12}\) connection for the target charts and
use of infinity-coordinate rather than physical-energy homogeneity.

This does not split the extension.  Entry 763's complete-pole nonsplitting
defect is compatible with the present result and must now be tested for
covariance under these three source-derived intertwiners.

## Evidence

- `research/benincasa/check_independent_three_chart_gysin_connections.py`;
- `research/benincasa/independent-three-chart-gysin-connections.json`;
- Entries 756, 761, and 763;
- allocator claim `seqclaim-89f51465877767c6e677dcf0`.
- epistemic event
  `ev-000000000379-9c5a65c1-0e1b-4c23-b4fa-a014a00ff59e`.

## Next falsifier

Transport the completed Hom operator, cocycle, and twelve-factor pole lattice
of Entries 762--763 through these three horizontal gauges.  Verify that the
rank-one nonsplitting class has a well-defined cyclic orbit and that its
threefold transport is the identity.  A failure would place the obstruction
in occurrence descent rather than in the intrinsic extension class.
