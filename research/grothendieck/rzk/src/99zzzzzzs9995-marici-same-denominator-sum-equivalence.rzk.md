# Same-denominator raw sum equivalence

A raw fraction with numerator `x + y` over a shared denominator is equivalent
to the raw-fraction sum of `x` and `y` over that denominator. The proof exposes
the duplicated denominator factor and distributes it through the numerator.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-same-denominator-sum-equivalent
  ( x y : MariciInt)
  ( d : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction (marici-int-add x y) d)
      (marici-raw-fraction-add
        (marici-raw-fraction x d)
        (marici-raw-fraction y d))
  := concat MariciInt
      (marici-int-mul
        (marici-int-add x y)
        (marici-int-positive-denominator
          (marici-positive-product-predecessor d d)))
      (marici-int-mul
        (marici-int-add x y)
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator d)))
      (marici-int-mul
        (marici-int-add
          (marici-int-mul x (marici-int-positive-denominator d))
          (marici-int-mul y (marici-int-positive-denominator d)))
        (marici-int-positive-denominator d))
      (ap MariciInt MariciInt
        (marici-int-positive-denominator
          (marici-positive-product-predecessor d d))
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator d))
        (\ denominator → marici-int-mul (marici-int-add x y) denominator)
        (marici-positive-denominator-product d d))
      (concat MariciInt
        (marici-int-mul
          (marici-int-add x y)
          (marici-int-mul
            (marici-int-positive-denominator d)
            (marici-int-positive-denominator d)))
        (marici-int-mul
          (marici-int-mul
            (marici-int-add x y)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator d))
        (marici-int-mul
          (marici-int-add
            (marici-int-mul x (marici-int-positive-denominator d))
            (marici-int-mul y (marici-int-positive-denominator d)))
          (marici-int-positive-denominator d))
        (rev MariciInt
          (marici-int-mul
            (marici-int-mul
              (marici-int-add x y)
              (marici-int-positive-denominator d))
            (marici-int-positive-denominator d))
          (marici-int-mul
            (marici-int-add x y)
            (marici-int-mul
              (marici-int-positive-denominator d)
              (marici-int-positive-denominator d)))
          (marici-int-mul-assoc
            (marici-int-add x y)
            (marici-int-positive-denominator d)
            (marici-int-positive-denominator d)))
        (ap MariciInt MariciInt
          (marici-int-mul
            (marici-int-add x y)
            (marici-int-positive-denominator d))
          (marici-int-add
            (marici-int-mul x (marici-int-positive-denominator d))
            (marici-int-mul y (marici-int-positive-denominator d)))
          (\ numerator → marici-int-mul numerator
            (marici-int-positive-denominator d))
          (marici-int-mul-add-right-distrib x y
            (marici-int-positive-denominator d))))
```

## Boundary

The common-denominator numerator sum now represents the raw sum of its two
summands. The final raw triangle theorem must transport the common-denominator
absolute presentations back to the original directed differences.
