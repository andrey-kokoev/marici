# Exact rank-drop locus of the total-energy/defect map

Let

\[
F=(E,\nu_1,\nu_2,\nu_3),
\qquad
E=X_1+X_2+X_3,
\qquad
\nu_i=P_i^2-X_i^2.
\]

## Exact claim

The rank-drop locus of \(dF\) is

\[
\boxed{
V(P_1,P_2,P_3)
\cup
V(X_1,P_1)
\cup
V(X_2,P_2)
\cup
V(X_3,P_3).
}
\]

## Proof

A row dependence has coefficients \(c_0,c_1,c_2,c_3\) and obeys

\[
2c_iP_i=0,
\qquad
c_0-2c_iX_i=0
\quad(i=1,2,3).
\]

If some \(P_j\neq0\), then \(c_j=0\), hence \(c_0=0\). Every remaining
\(c_i\) vanishes unless \(P_i=X_i=0\). Thus a dependence exists precisely
on a coordinate-origin component.

If every \(P_i=0\), choose \(c_i=c_0/(2X_i)\) where \(X_i\neq0\), with the
zero-coordinate cases supplying an even more immediate dependence. Hence the
entire all-momentum-soft locus has rank below four.

The checker audits all 64 coordinate zero strata exactly and confirms this
classification.

## Consequence

The missing total-energy-to-quadratic map cannot be sourced by a generic
simple-soft fold. Its only kinematic rank-drop candidates are:

- the all-momentum-soft intersection;
- a labelled coordinate origin \((X_i,P_i)=(0,0)\).

These are already frozen deeper Carrier intersections. Rank drop alone still
does not define the desired map: one must derive a Gysin, nearby-cycle,
coefficient, or physical-chain morphism on one of them.

## Next falsifier

Restrict the existing soft/coordinate-boundary complexes to one labelled
coordinate origin and test whether their iterated support map reaches

\[
\mathbf Q\langle
\nu_1\nu_2+\nu_1\nu_3+\nu_2\nu_3
\rangle.
\]

The map, its variance, and its normalization must precede evaluation.
