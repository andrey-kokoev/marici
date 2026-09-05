# Finite exponent-two sums have a telescoping-sum majorant

Finite-sum monotonicity folds the pointwise exponent-two inequality. The left
family starts at Dirichlet index one, while the right family consists of
adjacent reciprocal differences with matching zero-based indices.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-shifted-term
  ( n : MariciNat)
  : MariciRational
  := marici-rational-dirichlet-term marici-two (marici-succ n)

#define marici-adjacent-reciprocal-difference-term
  ( n : MariciNat)
  : MariciRational
  := marici-rational-adjacent-reciprocal-difference n

#define marici-exponent-two-finite-sum-at-most-telescoping-sum
  ( bound : MariciNat)
  : MariciRationalAtMost
      (marici-rational-finite-sum bound
        marici-exponent-two-shifted-term)
      (marici-rational-finite-sum bound
        marici-adjacent-reciprocal-difference-term)
  := marici-rational-finite-sum-at-most
      marici-exponent-two-shifted-term
      marici-adjacent-reciprocal-difference-term
      marici-exponent-two-term-at-most-adjacent-reciprocal-difference
      bound
```

## Boundary

Every finite initial sum of exponent-two terms is now bounded by the matching
finite sum of adjacent reciprocal differences. Collapsing that latter sum to
its two boundary terms remains necessary for a usable finite-tail estimate.
