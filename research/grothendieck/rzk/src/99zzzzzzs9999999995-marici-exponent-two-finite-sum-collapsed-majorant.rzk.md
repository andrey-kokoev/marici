# Finite exponent-two sum is bounded by the outer reciprocal difference

The finite telescoping component path transports the right endpoint of the
summed pointwise majorant. This removes the internal finite sum from the bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-finite-sum-at-most-outer-reciprocal-difference
  ( bound : MariciNat)
  : MariciRationalAtMost
      (marici-rational-finite-sum bound
        marici-exponent-two-shifted-term)
      (marici-rational-reciprocal-difference marici-zero bound)
  := marici-rational-at-most-transport-right-components
      (marici-rational-finite-sum bound
        marici-exponent-two-shifted-term)
      (marici-rational-finite-sum bound
        marici-reciprocal-difference-successor-term)
      (marici-rational-reciprocal-difference marici-zero bound)
      (marici-finite-reciprocal-telescoping-components bound)
      (marici-exponent-two-finite-sum-at-most-telescoping-sum bound)
```

## Boundary

The finite exponent-two initial sum is now bounded by
`1 - 1/(bound+1)` in typed reciprocal-difference form. A Cauchy proof needs the
shifted analogue: a finite segment beginning at an arbitrary cutoff is bounded
by the reciprocal tolerance at that cutoff.
