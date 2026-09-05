# Cauchy-sequence equivalence is reflexive

Zero self-distance and positivity of reciprocal tolerances prove every rational
value is within every tolerance of itself. Pointwise application supplies
reflexivity of eventual Cauchy-sequence equivalence.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-distance-self-at-most-tolerance
  ( q : MariciRational)
  ( k : MariciNat)
  : MariciRationalAtMost
      (marici-rational-distance q q)
      (marici-rational-positive-reciprocal-power k marici-one)
  := marici-rational-at-most-transport-left-components
      marici-rational-zero
      (marici-rational-distance q q)
      (marici-rational-positive-reciprocal-power k marici-one)
      (rev MariciRawFraction
        (marici-rational-forget (marici-rational-distance q q))
        (marici-rational-forget marici-rational-zero)
        (marici-rational-distance-self-components q))
      (marici-rational-zero-at-most-positive-reciprocal-power
        k marici-one)

#define marici-rational-cauchy-sequences-equivalent-reflexive
  ( x : MariciRationalCauchySequence)
  : MariciRationalCauchySequencesEquivalent x x
  := marici-rational-cauchy-sequences-equivalent x x
      (\ k → marici-zero)
      (\ k n bound →
        marici-rational-distance-self-at-most-tolerance
          (marici-rational-cauchy-sequence-values x n) k)
```

## Boundary

Eventual Cauchy equivalence is now reflexive. Symmetry and transitivity require
distance symmetry, the triangle inequality, and tolerance-index combination.
