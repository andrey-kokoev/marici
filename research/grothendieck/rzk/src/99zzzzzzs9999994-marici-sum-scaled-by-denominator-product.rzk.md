# Scaling a sum by a positive denominator product

The encoded denominator product is exposed as integer multiplication,
reassociated into two successive scales, and distributed through the integer
sum.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-sum-scaled-by-denominator-product
  ( x y : MariciInt)
  ( left-scale right-scale : MariciNat)
  : marici-int-mul
      (marici-int-add x y)
      (marici-int-positive-denominator
        (marici-positive-product-predecessor left-scale right-scale))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul
        (marici-int-mul x (marici-int-positive-denominator left-scale))
        (marici-int-positive-denominator right-scale))
      (marici-int-mul
        (marici-int-mul y (marici-int-positive-denominator left-scale))
        (marici-int-positive-denominator right-scale))
  := concat MariciInt
      (marici-int-mul
        (marici-int-add x y)
        (marici-int-positive-denominator
          (marici-positive-product-predecessor left-scale right-scale)))
      (marici-int-mul
        (marici-int-mul (marici-int-add x y)
          (marici-int-positive-denominator left-scale))
        (marici-int-positive-denominator right-scale))
      (marici-int-add
        (marici-int-mul
          (marici-int-mul x (marici-int-positive-denominator left-scale))
          (marici-int-positive-denominator right-scale))
        (marici-int-mul
          (marici-int-mul y (marici-int-positive-denominator left-scale))
          (marici-int-positive-denominator right-scale)))
      (concat MariciInt
        (marici-int-mul
          (marici-int-add x y)
          (marici-int-positive-denominator
            (marici-positive-product-predecessor left-scale right-scale)))
        (marici-int-mul
          (marici-int-add x y)
          (marici-int-mul
            (marici-int-positive-denominator left-scale)
            (marici-int-positive-denominator right-scale)))
        (marici-int-mul
          (marici-int-mul (marici-int-add x y)
            (marici-int-positive-denominator left-scale))
          (marici-int-positive-denominator right-scale))
        (ap MariciInt MariciInt
          (marici-int-positive-denominator
            (marici-positive-product-predecessor left-scale right-scale))
          (marici-int-mul
            (marici-int-positive-denominator left-scale)
            (marici-int-positive-denominator right-scale))
          (\ denominator → marici-int-mul (marici-int-add x y) denominator)
          (marici-positive-denominator-product left-scale right-scale))
        (rev MariciInt
          (marici-int-mul
            (marici-int-mul (marici-int-add x y)
              (marici-int-positive-denominator left-scale))
            (marici-int-positive-denominator right-scale))
          (marici-int-mul
            (marici-int-add x y)
            (marici-int-mul
              (marici-int-positive-denominator left-scale)
              (marici-int-positive-denominator right-scale)))
          (marici-int-mul-assoc
            (marici-int-add x y)
            (marici-int-positive-denominator left-scale)
            (marici-int-positive-denominator right-scale))))
      (concat MariciInt
        (marici-int-mul
          (marici-int-mul (marici-int-add x y)
            (marici-int-positive-denominator left-scale))
          (marici-int-positive-denominator right-scale))
        (marici-int-mul
          (marici-int-add
            (marici-int-mul x (marici-int-positive-denominator left-scale))
            (marici-int-mul y (marici-int-positive-denominator left-scale)))
          (marici-int-positive-denominator right-scale))
        (marici-int-add
          (marici-int-mul
            (marici-int-mul x (marici-int-positive-denominator left-scale))
            (marici-int-positive-denominator right-scale))
          (marici-int-mul
            (marici-int-mul y (marici-int-positive-denominator left-scale))
            (marici-int-positive-denominator right-scale)))
        (ap MariciInt MariciInt
          (marici-int-mul (marici-int-add x y)
            (marici-int-positive-denominator left-scale))
          (marici-int-add
            (marici-int-mul x (marici-int-positive-denominator left-scale))
            (marici-int-mul y (marici-int-positive-denominator left-scale)))
          (\ numerator → marici-int-mul numerator
            (marici-int-positive-denominator right-scale))
          (marici-int-mul-add-right-distrib x y
            (marici-int-positive-denominator left-scale)))
        (marici-int-mul-add-right-distrib
          (marici-int-mul x (marici-int-positive-denominator left-scale))
          (marici-int-mul y (marici-int-positive-denominator left-scale))
          (marici-int-positive-denominator right-scale)))
```

## Boundary

Both raw-sum cross-products can now be expanded into the aligned summands.
Transporting the sum of the two summand inequalities along these paths finishes
raw-fraction addition monotonicity.
