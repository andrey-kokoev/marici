---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 761 — The Cyclic Gysin Connection Descent Requires Independent Residue Charts

## Frozen cyclic relabelling

For the site cycle

\[
(X_1,X_2,X_3)\longmapsto(X_3,X_1,X_2),
\]

the normalized homogeneous coordinates transform as

\[
U=\frac{2u}{u-v},\qquad
V=\frac{2(2-v)}{u-v},\qquad
z=X_3=\frac{u-v}{2}.
\]

The threefold composition is the identity.  The cyclic permutation of the
ambient residue coordinates is even, so the Poincare-residue orientation
sign is (+1).

## Formal raw-master gauge

The raw final-block representatives have homogeneity weights

\[
(-1,0,2,2)
\]

for the double-pole class and the three simple-pole classes.  If \(P(u,v)\)
is the already derived Gysin-adapted frame, the only gauges induced by the
two possible source/target homogeneity conventions are

\[
S_\pm
=
P(u,v)
\operatorname{diag}(z^{\mp1},1,z^{\pm2},z^{\pm2})
P(U,V)^{-1}.
\]

Both formal gauges satisfy the three-chart product condition

\[
S_\pm\,\rho^*S_\pm\,(\rho^2)^*S_\pm=1.
\]

Thus the base relabelling, residue orientation, and homogeneity data are
internally coherent.

## Connection audit

The only serialized rank-four connection presently available is the
\(q_{\mathcal G_{12}}\)-residue connection.  Reusing it as the target chart
would require

\[
A_{12}
=
dS_\pm S_\pm^{-1}
+S_\pm\rho^*A_{12}S_\pm^{-1}.
\]

Exact finite-field evaluation at 64 generic points, in both coordinate
directions, gives

\[
\boxed{
64/64\text{ failures for }S_+,
\qquad
64/64\text{ failures for }S_-.
}
\]

The three-cycle product has zero failures in both conventions.  Hence this
is not a cocycle-sign or inverse-weight ambiguity.

## Narrow conclusion

The fixed-(G_{12}) connection cannot be transported cyclically by
homogeneity and the adapted-frame matrix alone.  This does **not** establish
a failure of occurrence covariance.  It establishes that the proposed
connection comparison is untyped until the (G_{23}) and (G_{31})
residue-chart connections are independently reconstructed from their frozen
denominators, as Entry 756 already required.

Entry 762 independently completes the rational pole vector of the fixed-chart
Hom splitting problem.  That result governs the filtered splitting census;
it does not supply the missing inter-chart connection matrices.

No gauge was fitted to repair the failed intertwiner.

## Evidence

- `research/benincasa/check_cyclic_gysin_occurrence_descent.py`;
- `research/benincasa/cyclic-gysin-occurrence-descent.json`;
- Entries 756, 758, 760, and 762;
- allocator claim `seqclaim-45de40f3008a73c7ccb689c5`.
- epistemic event
  `ev-000000000376-144edbcb-8f85-461f-8df1-5a6949fdfeee`.

## Next falsifier

Construct the (G_{23}) and (G_{31}) rank-four connections independently
from their labelled residue denominators.  Then test the three inter-chart
horizontalities and their signed cyclic composition.  Only after that may
the Entry 762 Hom cocycle be transported around the occurrence cycle.
