# Opposite raw-fraction subtractions

Swapping raw-fraction subtraction endpoints gives the negation of the original
difference. The numerator path is the scaled opposite-difference theorem; the
denominator path is commutativity of positive denominator products.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-opposite-subtractions
  ( p q : MariciRawFraction)
  : marici-raw-fraction-subtract q p
    =_{MariciRawFraction}
    marici-raw-fraction-negate
      (marici-raw-fraction-subtract p q)
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                concat MariciRawFraction
                  (marici-raw-fraction
                    (marici-int-add
                      (marici-scale-by-positive-denominator b d)
                      (marici-scale-by-positive-denominator
                        (marici-int-negate a) e))
                    (marici-positive-product-predecessor e d))
                  (marici-raw-fraction
                    (marici-int-negate
                      (marici-int-add
                        (marici-scale-by-positive-denominator a e)
                        (marici-scale-by-positive-denominator
                          (marici-int-negate b) d)))
                    (marici-positive-product-predecessor e d))
                  (marici-raw-fraction
                    (marici-int-negate
                      (marici-int-add
                        (marici-scale-by-positive-denominator a e)
                        (marici-scale-by-positive-denominator
                          (marici-int-negate b) d)))
                    (marici-positive-product-predecessor d e))
                  (ap MariciInt MariciRawFraction
                    (marici-int-add
                      (marici-scale-by-positive-denominator b d)
                      (marici-scale-by-positive-denominator
                        (marici-int-negate a) e))
                    (marici-int-negate
                      (marici-int-add
                        (marici-scale-by-positive-denominator a e)
                        (marici-scale-by-positive-denominator
                          (marici-int-negate b) d)))
                    (\ numerator → marici-raw-fraction numerator
                      (marici-positive-product-predecessor e d))
                    (marici-scaled-opposite-differences a b d e))
                  (ap MariciNat MariciRawFraction
                    (marici-positive-product-predecessor e d)
                    (marici-positive-product-predecessor d e)
                    (\ denominator → marici-raw-fraction
                      (marici-int-negate
                        (marici-int-add
                          (marici-scale-by-positive-denominator a e)
                          (marici-scale-by-positive-denominator
                            (marici-int-negate b) d)))
                      denominator)
                    (marici-positive-product-predecessor-comm e d))))
```

## Boundary

This is exact constructor equality for raw fractions. Distance symmetry still
requires passage through normalization and absolute value.
