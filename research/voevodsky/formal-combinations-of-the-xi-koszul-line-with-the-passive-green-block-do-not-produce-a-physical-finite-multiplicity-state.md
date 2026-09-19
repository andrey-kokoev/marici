# Formal combinations of the Xi Koszul line with the passive Green block do not produce a physical finite-multiplicity state

Let `K_tau` be the two-term Xi Koszul complex and let `P` be the invertible
same-sign passive Green block.

The direct sum

\[
K_\tau\oplus P
\]

has determinant section `tau det(P)` and therefore the Xi divisor up to a unit.
But its cohomology at a zero remains entirely in the external determinant-line
summand.  No history/arithmetic Green state is produced.

Trying to internalize the scalar by multiplication,

\[
F(s)=\tau(s)P(s),
\]

also fails.  Off the divisor it is invertible, but at `tau(s_0)=0` the operator
is zero on the whole passive state space, creating an infinite-dimensional
kernel rather than the local module length `ord_(s_0) tau`.

Tensoring with an acyclic passive complex is no better: under ordinary exact
tensor hypotheses it remains acyclic and erases, rather than realizes, the
Koszul residue.

Thus determinant multiplication alone has three outcomes:

1. direct sum: correct divisor, residue stays external;
2. scalar multiplication of the Green operator: wrong infinite kernel;
3. tensor with an acyclic Green complex: residue disappears.

A physical finite-multiplicity realization requires a nontrivial chain map that
sends the one-dimensional Koszul residue into a finite Green defect module and
preserves local module length.  That map cannot be replaced by formal block
sum, scalar multiplication, or tensor product.
