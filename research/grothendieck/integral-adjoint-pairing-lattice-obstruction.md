# Rational nondegeneracy does not guarantee an integral Betti adjoint

Epistemic-graph event: 1352.

## Matrix criterion

Choose integral coefficient and Betti bases.  Write the pairings as matrices
`P_G,P_H` and coefficient pullback as `Q:A(H)->A(G)`.  A Betti matrix
`S:C(G)->C(H)` is adjoint to `Q` exactly when

`P_H S=Q^T P_G`.

Therefore an integral adjoint exists if and only if every column of
`Q^T P_G` lies in the integral column lattice of `P_H`.  When the right
radical `ker(P_H)` is zero, such an adjoint is unique.  When `P_H` is square
and unimodular,

`S=P_H^(-1)Q^T P_G`

is automatically integral and unique.

## Lattice-index obstruction

If `P_H` is nondegenerate only over the fraction field, the rational formula
still exists but can leave the Betti lattice.  The smallest example is

`P_H=[2]`, `P_G=[1]`, `Q=[1]`.

Adjunction forces `S=[1/2]`.  There is a unique rational adjoint but no
integral Betti pushforward.  After inverting two the obstruction disappears.

Smith normal form of `P_H` makes the general falsifier exact: transform
`Q^T P_G` by the same left basis change and test divisibility of its rows by
the corresponding nonzero Smith factors.  One failed divisibility condition
excludes every integral adjoint before boundary compatibility is considered.

## Relation to the radical tower

The lattice obstruction and the radical obstruction are distinct.
`ker(P_H)=0` can hold while `coker(P_H)` has torsion, as in `[2]`; then the
adjoint is rationally unique but integrally nonexistent.  A nonzero radical
instead creates nonuniqueness and the repair tower of Ledgers 1328--1332.

## Five-site consequence

The formal delta sheet pairing has `P_H=I`, so this gate passes algebraically.
The physical relative pairing is unavailable.  It must be audited for both
kernel and cokernel: proving rational nondegeneracy alone would not authorize
an integral chain transfer or its norm.
