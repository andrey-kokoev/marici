# Finite difference correspondence and noncompact hostile: Lean packet

## Source boundary

This increment formalizes the finite theorem and diagonal-window hostile in
Grothendieck's `difference-correspondence-noncompact-obstruction.md`. It does
not construct Haar measure or an infinite `L²` operator.

## Formal objects and coefficient types

`G` is an arbitrary finite additive commutative group. Functions are
real-valued and their squared norm is the unnormalized finite sum of squares.
The difference pullback sends `(a,b)` to `f(a-b)`. Finite normalization
divides squared norm by the positive group cardinality.

## Theorems and hostile

- `sum_sq_sub_left_eq` proves translation/reindexing invariance for each
  fixed left coordinate.
- `differencePullback_normSq_eq_card_mul` proves the exact law
  `‖Df‖² = |G| ‖f‖²`.
- `normalized_differencePullback_isometric` proves the normalized squared
  isometry statement.
- `diagonalIndicator_window_normSq` proves that an `n × n` unit diagonal
  has squared norm exactly `n`.
- `diagonalWindow_normSq_unbounded` proves these finite-window norms have no
  uniform natural bound, modeling the discrete infinite-diagonal hostile.

## Missing interfaces

The locally compact theorem needs Haar measure, Tonelli, translation
invariance, sigma-finiteness conventions, extended-valued integrals, and a
proof that noncompact Haar volume is infinite under the chosen hypotheses.
The arithmetic application must independently choose a compact quotient,
relative tensor product, trace per unit volume, compatible weight, or
projective normalization. These repairs are not interchangeable and none is
selected by the finite identity.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteDifferenceCorrespondence.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
