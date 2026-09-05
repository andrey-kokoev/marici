# Exponent-two reciprocal has an adjacent telescoping majorant

The adjacent-product denominator inequality is transported through the encoded
positive-product paths. Reversing denominator order for unit numerators gives
the corresponding reciprocal raw-fraction bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-to-unit-cross-product
  ( left-index right-index : MariciNat)
  : marici-int-mul
      (marici-int-positive-denominator left-index)
      (marici-int-positive-denominator right-index)
    =_{MariciInt}
    marici-int-mul marici-int-one
      (marici-int-positive-denominator
        (marici-positive-product-predecessor left-index right-index))
  := concat MariciInt
      (marici-int-mul
        (marici-int-positive-denominator left-index)
        (marici-int-positive-denominator right-index))
      (marici-int-positive-denominator
        (marici-positive-product-predecessor left-index right-index))
      (marici-int-mul marici-int-one
        (marici-int-positive-denominator
          (marici-positive-product-predecessor left-index right-index)))
      (rev MariciInt
        (marici-int-positive-denominator
          (marici-positive-product-predecessor left-index right-index))
        (marici-int-mul
          (marici-int-positive-denominator left-index)
          (marici-int-positive-denominator right-index))
        (marici-positive-denominator-product left-index right-index))
      (rev MariciInt
        (marici-int-mul marici-int-one
          (marici-int-positive-denominator
            (marici-positive-product-predecessor left-index right-index)))
        (marici-int-positive-denominator
          (marici-positive-product-predecessor left-index right-index))
        (marici-int-mul-one-left
          (marici-int-positive-denominator
            (marici-positive-product-predecessor left-index right-index))))

#define marici-square-reciprocal-raw-at-most-adjacent-difference
  ( n : MariciNat)
  : MariciRawFractionAtMost
      (marici-raw-fraction marici-int-one
        (marici-positive-product-predecessor
          (marici-succ n) (marici-succ n)))
      (marici-raw-adjacent-reciprocal-difference n)
  := marici-int-at-most-transport-both
      (marici-int-mul
        (marici-int-positive-denominator n)
        (marici-int-positive-denominator (marici-succ n)))
      (marici-int-mul marici-int-one
        (marici-int-positive-denominator
          (marici-positive-product-predecessor n (marici-succ n))))
      (marici-int-mul
        (marici-int-positive-denominator (marici-succ n))
        (marici-int-positive-denominator (marici-succ n)))
      (marici-int-mul marici-int-one
        (marici-int-positive-denominator
          (marici-positive-product-predecessor
            (marici-succ n) (marici-succ n))))
      (marici-positive-product-to-unit-cross-product n (marici-succ n))
      (marici-positive-product-to-unit-cross-product
        (marici-succ n) (marici-succ n))
      (marici-adjacent-positive-product-at-most-larger-square n)
```

## Boundary

The exponent-two unit fraction at index `n+1` is now bounded by the adjacent
reciprocal difference at index `n`. Identifying the actual Dirichlet term and
rational subtraction with these raw presentations yields the pointwise
rational telescoping majorant.
