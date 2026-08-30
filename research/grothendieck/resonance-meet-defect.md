# Resonance preserves joins but not meets

## General meet bound

For normal kernels `K,L` of a finite group, monotonicity gives

`R(K intersection L) | gcd(R(K),R(L))`.

Equivalently,

`U(K) union U(L) subset U(K intersection L)`.

Neither relation need be equality. Thus the radical resonance decoration is
an exact join-semilattice morphism to squarefree integers under lcm, by
Ledger 1294, but is not a lattice morphism.

## Smallest strict defect

Let `G=C2 x C2` and take its two coordinate subgroups `K` and `L`. Then

`R(K)=R(L)=2`,

but `K intersection L=1`, so

`R(K intersection L)=1 < gcd(2,2)=2`.

Both input spectra contain precisely the odd indices, while the meet spectrum
contains every index. The exact checker verifies strictness through 24. The
join is all of `G`, retains label two, and obeys the exact lcm law.

## Interpretation and scope

A prime obstruction can be present independently in two incomparable kernels
and disappear completely when the selector is refined to their intersection.
This is coefficient algebra only; no physical readout or Betti map follows.
