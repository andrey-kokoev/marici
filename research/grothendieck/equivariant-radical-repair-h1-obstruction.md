# Equivariant radical repair has a first-cohomology obstruction

Epistemic-graph event: 1349.

## Naturality theorem

Suppose a symmetry group `Gamma` preserves the source and target complexes,
the pairing radical, and the repair equation.  Let `T` be the nonempty torsor
of radical repair classes from Ledger 1330, with translation module

`A=H^0(Hom(C(G),R))`.

Choose a repair class `C_0`.  Its symmetry displacement

`b(gamma)=gamma C_0-C_0 in A`

is a group-cohomology one-cocycle.  Changing `C_0` changes `b` by a
coboundary, so the class

`[b] in H^1(Gamma,A)`

is canonical.  An equivariant repair exists exactly when `[b]=0`.  When it
exists, the equivariant repair classes form a torsor under the invariant
module `A^Gamma`.

Thus existence of some pairing-preserving chain map does not imply existence
of an automorphism-natural one.

## Small integral hostile torsor

Let `Gamma=C2` act on the repair torsor `T=Z` by

`sigma(m)=1-m`.

The translation module is `A=Z` with sign action `sigma(a)=-a`.  Choosing
`C_0=0` gives `b(sigma)=1`.  Coboundaries are even integers
`a-sigma(a)=2a`, so `[b]` is the nonzero class in

`H^1(C2,Z_sign)=Z/2`.

There is no fixed integral repair because `m=1-m` would require `m=1/2`.
After inverting two, the obstruction vanishes and the unique fixed point is
`1/2`.  This exposes a new arithmetic naturality boundary.

## Physical consequence

A degenerate physical five-site pairing would require three separate
certificates: radical obstruction vanishing, selection of a repair torsor
point, and vanishing of its symmetry class `[b]`.  Averaging a repair can
create a fixed point only when the symmetry order is invertible and may
violate integral or frozen normalization, just as in the transfer problem.
