# Exponent-two terms satisfy the pointwise telescoping bound

The raw square-reciprocal majorant descends to canonical rationals. Component
transport identifies its left endpoint with the exponent-two Dirichlet term and
its right endpoint with the adjacent reciprocal difference.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-term-at-most-adjacent-reciprocal-difference
  ( n : MariciNat)
  : MariciRationalAtMost
      (marici-rational-dirichlet-term marici-two (marici-succ n))
      (marici-rational-adjacent-reciprocal-difference n)
  := marici-rational-at-most-transport-right-components
      (marici-rational-dirichlet-term marici-two (marici-succ n))
      (marici-rational-from-raw
        (marici-raw-adjacent-reciprocal-difference n))
      (marici-rational-adjacent-reciprocal-difference n)
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-adjacent-reciprocal-difference n))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-adjacent-reciprocal-difference n)))
        (marici-rational-adjacent-reciprocal-difference-components n))
      (marici-rational-at-most-transport-left-components
        (marici-rational-from-raw
          (marici-raw-square-reciprocal (marici-succ n)))
        (marici-rational-dirichlet-term marici-two (marici-succ n))
        (marici-rational-from-raw
          (marici-raw-adjacent-reciprocal-difference n))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-dirichlet-term marici-two (marici-succ n)))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-square-reciprocal (marici-succ n))))
          (marici-exponent-two-dirichlet-term-square-components
            (marici-succ n)))
        (marici-raw-at-most-to-rational-at-most
          (marici-raw-square-reciprocal (marici-succ n))
          (marici-raw-adjacent-reciprocal-difference n)
          (marici-square-reciprocal-raw-at-most-adjacent-difference n)))
```

## Boundary

The one-term exponent-two telescoping inequality is now complete. Summing it
pointwise and proving the finite adjacent-difference sum identity are the
remaining steps to a finite-tail bound.
