# Finite-group norm characteristic dichotomy: Lean packet

## Source boundary

This increment formalizes the regular coefficient-fiber core of Grothendieck's
`finite-group-norm-characteristic-dichotomy.md`.

## Formal objects and coefficient types

`G` is any finite group and `K` any field. A regular coefficient packet is a
function `G → K`. `regularFiberNorm` sends it to the constant packet equal to
its augmentation sum. The group multiplication law is deliberately absent
from the formula because left or right regular translation only permutes the
basis.

## Theorems and hostile

- `regularFiberNorm_square` proves `N² = |G|N` pointwise.
- `regularFiberNorm_eq_zero_iff` identifies its kernel with the augmentation
  kernel.
- `regularFiberNorm_square_zero` proves the bad-characteristic differential is
  square-zero when the group order vanishes in the field.
- `regularFiberAverage_idempotent` proves division by the nonzero group order
  gives an idempotent normalized projector in the complementary regime.
- `characteristicTwo_normKernel_hostile` gives a nonzero constant packet on
  the order-two regular fiber over `ZMod 2` whose norm vanishes.

This is the universal regular-module linear identity. It does not identify the
augmentation ideal with a Jacobson radical or the norm line with a full socle.

## Missing interfaces

The homology dimension `|G|-2` requires finite-dimensional quotient/rank
bookkeeping. The integral theorem needs the augmentation basis, a unimodular
change of basis, Smith normal form, and base-change comparison. The arbitrary
finite-surjection conjugation spectrum additionally needs kernel exponent,
conjugation-image exponent, twisted norm-word bijectivity, and nonsplit
extension fixtures. Physical relative-chain pushforward remains absent in all
three cases.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteGroupNormDichotomy.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
