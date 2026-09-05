# Rational zero-order implies numerator nonnegativity

For a reduced rational, the order comparison from canonical zero has cross
products `0 * denominator` and `numerator * 1`. Transporting these products to
zero and the numerator recovers the numerator's nonnegativity witness.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-nonnegative-from-zero-at-most
  ( q : MariciRational)
  ( witness : MariciRationalAtMost marici-rational-zero q)
  : MariciRationalIsNonnegative q
  := (match q into
      (\ q-prime → MariciRationalAtMost marici-rational-zero q-prime
        → MariciRationalIsNonnegative q-prime)
      ( marici-reduced-raw-fraction numerator denominator reduced ⇒
          \ order →
            marici-int-at-most-transport-both
              (marici-int-mul marici-int-zero
                (marici-int-positive-denominator denominator))
              marici-int-zero
              (marici-int-mul numerator marici-int-one)
              numerator
              (marici-int-mul-zero-left
                (marici-int-positive-denominator denominator))
              (marici-int-mul-one-right numerator)
              order))
      witness
```

## Boundary

Order-theoretic nonnegativity can now drive sign-sensitive component theorems.
The next step is proving that integer absolute value fixes a value carrying this
witness, then lifting that path through raw and rational absolute value.
