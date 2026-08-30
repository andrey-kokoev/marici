# 2868 — The Pointed Soft Torsor Survives the Noncyclic Residue Transition

## Frozen noncyclic transition

Use the exact labelled transition from the \(q_{\mathcal G_{12}}\)-residue chart to the \(q_{\mathcal G_{31}}\)-residue chart under the site transposition \(\sigma_{23}\).

It fixes

\[
X_1\longmapsto X_1,
\qquad
q_{g1}\longmapsto q_{g1}.
\]

Therefore the normalized soft coordinate

\[
t=\frac{q_{g1}}{X_1}
\]

transports as

\[
t\longmapsto t
\]

with transition unit one.

## Orientation

The retained fiber coordinates transform as

\[
(a,b)\longmapsto(c',a')=(b,a).
\]

With the source Poincaré-residue convention,

\[
dc'\wedge da'
\longmapsto
db\wedge da
=
-da\wedge db.
\]

Hence the coefficient primitive transforms by the derived orientation sign:

\[
F\longmapsto-F.
\]

The pointed origin is preserved:

\[
F(2)=0
\longmapsto
-F(2)=0.
\]

The physical occurrence coordinate \(a=y_{23}\) is fixed by this transition, so the positive-occurrence chamber covector is preserved as well.

## Result

The chain-pointed logarithmic torsor descends through this noncyclic residue-chart transition. The exact quotient transport has full rank and its forward–reverse composition is identity.

This gate establishes that the affine pointing is not an artifact of the \(q_{\mathcal G_{12}}\) residue frame. It does not yet establish compatibility with the complete \(a\)-dependent physical cycle, regulator invariance, or Leray-tube pairing.

## Full atlas closure

Together with Entry 2866's certified cyclic atlas, this one transposition
generates the full six-chart \(S_3\) atlas. Writing

\[
\rho=(123),
\qquad
\tau=(23),
\]

the checker verifies

\[
\rho^3=1,
\qquad
\tau^2=1,
\qquad
\tau\rho\tau=\rho^{-1}.
\]

Thus the exact transposition packet, its inverse, and cyclic transport cover
all noncyclic chart transitions without choosing additional fitted maps.

## Durable artifacts

- research/benincasa/check_soft_endpoint_pointing_noncyclic_naturality.py
- research/benincasa/soft-endpoint-pointing-noncyclic-naturality.json
- research/benincasa/g12-g31-residue-chart-transition.json
