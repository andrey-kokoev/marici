# Adjacent reciprocal subtraction is a unit fraction

Raw subtraction of `1/(n+1)` and `1/(n+2)` has the positive-product
denominator. Multiplication by integer one disappears, and the adjacent
positive-denominator difference reduces its numerator to one.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-adjacent-reciprocal-difference
  ( n : MariciNat)
  : MariciRawFraction
  := marici-raw-fraction marici-int-one
      (marici-positive-product-predecessor n (marici-succ n))

#define marici-raw-adjacent-reciprocal-subtraction-path
  ( n : MariciNat)
  : marici-raw-fraction-subtract
      (marici-raw-reciprocal-tolerance n)
      (marici-raw-reciprocal-tolerance (marici-succ n))
    =_{MariciRawFraction}
    marici-raw-adjacent-reciprocal-difference n
  := ap MariciInt MariciRawFraction
      (marici-int-add
        (marici-scale-by-positive-denominator
          marici-int-one (marici-succ n))
        (marici-int-negate
          (marici-scale-by-positive-denominator marici-int-one n)))
      marici-int-one
      (\ numerator → marici-raw-fraction numerator
        (marici-positive-product-predecessor n (marici-succ n)))
      (concat MariciInt
        (marici-int-add
          (marici-scale-by-positive-denominator
            marici-int-one (marici-succ n))
          (marici-int-negate
            (marici-scale-by-positive-denominator marici-int-one n)))
        (marici-int-add
          (marici-int-positive-denominator (marici-succ n))
          (marici-int-negate (marici-int-positive-denominator n)))
        marici-int-one
        (marici-int-add-congruent
          (marici-scale-by-positive-denominator
            marici-int-one (marici-succ n))
          (marici-int-positive-denominator (marici-succ n))
          (marici-int-negate
            (marici-scale-by-positive-denominator marici-int-one n))
          (marici-int-negate (marici-int-positive-denominator n))
          (marici-int-mul-one-left
            (marici-int-positive-denominator (marici-succ n)))
          (ap MariciInt MariciInt
            (marici-scale-by-positive-denominator marici-int-one n)
            (marici-int-positive-denominator n)
            marici-int-negate
            (marici-int-mul-one-left
              (marici-int-positive-denominator n))))
        (marici-adjacent-positive-denominator-difference n))
```

## Boundary

The telescoping adjacent reciprocal difference now has an exact raw unit-
fraction presentation. The exponent-two Dirichlet term must next be ordered
below this majorant by comparing its square denominator with the adjacent
product denominator.
