# Nonnegative rational order and reciprocal tolerances

A canonical rational with nonnegative numerator lies above zero because its
denominator is positive. Reciprocal-power tolerances inherit numerator
nonnegativity from their raw numerator one through normalization.

```rzk
#lang rzk-1
```

```rzk
#define MariciRationalIsNonnegative
  ( q : MariciRational)
  : U
  := MariciRawFractionNumeratorIsNonnegative
      (marici-rational-forget q)

#define marici-int-zero-at-most-from-nonnegative
  ( x : MariciInt)
  ( x-nonnegative : MariciIntIsNonnegative x)
  : MariciIntAtMost marici-int-zero x
  := x-nonnegative

#define marici-rational-zero-at-most-from-nonnegative
  ( q : MariciRational)
  ( q-nonnegative : MariciRationalIsNonnegative q)
  : MariciRationalAtMost marici-rational-zero q
  := (match q into
      (\ q-prime → MariciRationalIsNonnegative q-prime
        → MariciRationalAtMost marici-rational-zero q-prime)
      ( marici-reduced-raw-fraction numerator denominator reduced ⇒
          \ nonnegative →
            marici-int-at-most-transport-both
              marici-int-zero
              (marici-int-mul marici-int-zero
                (marici-int-positive-denominator denominator))
              numerator
              (marici-int-mul numerator marici-int-one)
              (rev MariciInt
                (marici-int-mul marici-int-zero
                  (marici-int-positive-denominator denominator))
                marici-int-zero
                (marici-int-mul-zero-left
                  (marici-int-positive-denominator denominator)))
              (rev MariciInt
                (marici-int-mul numerator marici-int-one) numerator
                (marici-int-mul-one-right numerator))
              (marici-int-zero-at-most-from-nonnegative
                numerator nonnegative))) q-nonnegative

#define marici-rational-positive-reciprocal-power-nonnegative
  ( base-predecessor exponent : MariciNat)
  : MariciRationalIsNonnegative
      (marici-rational-positive-reciprocal-power
        base-predecessor exponent)
  := marici-rational-from-raw-numerator-nonnegative
      (marici-raw-fraction marici-int-one
        (marici-positive-power-predecessor
          base-predecessor exponent))
      marici-trivial

#define marici-rational-zero-at-most-positive-reciprocal-power
  ( base-predecessor exponent : MariciNat)
  : MariciRationalAtMost marici-rational-zero
      (marici-rational-positive-reciprocal-power
        base-predecessor exponent)
  := marici-rational-zero-at-most-from-nonnegative
      (marici-rational-positive-reciprocal-power
        base-predecessor exponent)
      (marici-rational-positive-reciprocal-power-nonnegative
        base-predecessor exponent)
```

## Boundary

This proves positivity of every reciprocal-power tolerance used in the Cauchy
predicate. Strict positivity, inverse laws, and monotonicity in the tolerance
index remain open.
