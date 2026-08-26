# Inertia ghost Frobenius: Lean packet

## Source boundary

This increment formalizes the finite permutation core of Grothendieck's
`inertia-ghost-frobenius-system.md` and the power compatibility used by
`inertia-dynamical-euler-factor.md`. It does not attach intrinsic primes to
inertia objects or construct an arithmetic Euler product.

## Formal objects and coefficient types

An inertia automorphism is represented by `Equiv.Perm X`. Its `n`-th power is
ordinary group power. For finite `X` with decidable equality,
`fixedPointCount σ r` is the cardinality of the fixed-point filter of
`σ^r`. No coefficient ring or representation is needed for the ghost law.

## Theorems and hostile

- `inertiaPower_comp` proves `F_m(F_n(σ))=F_(nm)(σ)`.
- `inertiaPower_one` proves the unit law.
- `fixedPointCount_inertiaPower_shift` proves
  `w_r(F_n(σ))=w_(nr)(σ)`.
- `inertiaPower_two_nontrivial_hostile` uses the Boolean transposition: it is
  nonidentity but its square is the identity.

## Missing interfaces

Functoriality on the inertia groupoid needs explicitly typed conjugating
morphisms and conjugacy invariance of fixed-point counts. The dynamical Euler
factor needs the finite permutation representation, trace/fixed-point
identity, formal exponential/determinant identity, and cycle decomposition.
Arithmetic use additionally needs a source-derived prime-to-inertia
attachment and a justified identification of the formal variable with
`p^(-s)`. No physical or geometric Frobenius is supplied.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/InertiaGhostFrobenius.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
