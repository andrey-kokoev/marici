# A negative reciprocal is bounded by zero

The raw negative unit fraction has cross product `-1` against the raw zero
fraction, while the opposite cross product is zero. Their integer difference is
one, hence nonnegative. Raw order then descends through normalization.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-negative-reciprocal-at-most-zero
  ( k : MariciNat)
  : MariciRawFractionAtMost
      (marici-raw-fraction-negate
        (marici-raw-reciprocal-tolerance k))
      (marici-raw-zero-at marici-zero)
  := marici-trivial

#define marici-rational-normalized-negative-reciprocal-at-most-zero
  ( k : MariciNat)
  : MariciRationalAtMost
      (marici-rational-from-raw
        (marici-raw-fraction-negate
          (marici-raw-reciprocal-tolerance k)))
      (marici-rational-from-raw (marici-raw-zero-at marici-zero))
  := marici-raw-at-most-to-rational-at-most
      (marici-raw-fraction-negate
        (marici-raw-reciprocal-tolerance k))
      (marici-raw-zero-at marici-zero)
      (marici-raw-negative-reciprocal-at-most-zero k)
```

## Boundary

The normalized negative reciprocal is now bounded by normalized zero. Component
transport must identify these endpoints with rational negation of the reciprocal
tolerance and canonical rational zero before addition monotonicity yields
`x - tolerance ≤ x`.
