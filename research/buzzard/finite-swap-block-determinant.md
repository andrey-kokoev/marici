# Finite conjugation swap-block determinant: Lean packet

## Source boundary

This increment formalizes the finite determinant identities in
Grothendieck's `conjugation-graph-determinant-class-gate.md`. It does not
assert compactness, trace class, Hilbert--Schmidt class, or existence of an
infinite Fredholm determinant.

## Formal objects and coefficient types

Single-block determinant identities hold over an arbitrary commutative ring.
The pencil is the explicit two-by-two matrix `I - z w J`. A finite cutoff is
an arbitrary finite index set with a weight for each block, and its block
determinant is the finite product of the individual determinants.

## Theorems and hostile

- `swapBlockPencil_det` proves the exact factor `1-(zw)^2`.
- `finiteSwapBlockDeterminant_factorization` proves the weighted finite
  product formula.
- `unweightedSwapBlockDeterminant_power` proves `(1-z^2)^m` for `m` blocks.
- `unweighted_cutoff_nonstabilization_hostile` gives values `-3` and `9` at
  `z=2` for one and two blocks.

## Missing interfaces

The infinite operator theorem needs a Hilbert direct sum, singular values,
compactness, trace and Hilbert--Schmidt norms, summability of weights, and the
precise domains of `det` and regularized `det₂`. A relative determinant
requires a typed reference operator. Source-derived arithmetic decay remains
absent; weights extracted from the desired zero divisor would be circular.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteSwapBlockDeterminant.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
