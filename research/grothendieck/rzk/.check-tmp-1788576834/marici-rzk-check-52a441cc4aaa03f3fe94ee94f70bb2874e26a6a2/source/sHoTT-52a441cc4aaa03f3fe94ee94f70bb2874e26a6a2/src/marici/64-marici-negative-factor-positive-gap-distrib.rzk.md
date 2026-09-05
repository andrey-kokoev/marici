# Negative-factor distributivity for a positive mixed gap

A negative multiplier reverses the sign of a positive source residual. On the
product side, commutativity of integer addition exposes the scaled negative-gap
normalization from module 57.

```rzk
#lang rzk-1
```

```rzk
#define marici-negative-factor-positive-gap-left-distrib
  ( p b r : MariciNat)
  : marici-int-mul (marici-int-neg p)
      (marici-int-add
        (marici-int-pos (marici-add (marici-succ b) r))
        (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p)
        (marici-int-pos (marici-add (marici-succ b) r)))
      (marici-int-mul (marici-int-neg p) (marici-int-neg b))
  := concat MariciInt
      (marici-int-mul (marici-int-neg p)
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ b) r))
          (marici-int-neg b)))
      (marici-int-neg (marici-positive-product-predecessor p r))
      (marici-int-add
        (marici-int-mul (marici-int-neg p)
          (marici-int-pos (marici-add (marici-succ b) r)))
        (marici-int-mul (marici-int-neg p) (marici-int-neg b)))
      (ap MariciInt MariciInt
        (marici-int-add
          (marici-int-pos (marici-add (marici-succ b) r))
          (marici-int-neg b))
        (marici-int-pos r)
        (\ z → marici-int-mul (marici-int-neg p) z)
        (marici-int-add-pos-neg-gap b r))
      (rev MariciInt
        (marici-int-add
          (marici-int-neg
            (marici-positive-product-predecessor p
              (marici-add (marici-succ b) r)))
          (marici-int-pos (marici-positive-product-predecessor p b)))
        (marici-int-neg (marici-positive-product-predecessor p r))
        (concat MariciInt
          (marici-int-add
            (marici-int-neg
              (marici-positive-product-predecessor p
                (marici-add (marici-succ b) r)))
            (marici-int-pos (marici-positive-product-predecessor p b)))
          (marici-int-add
            (marici-int-pos (marici-positive-product-predecessor p b))
            (marici-int-neg
              (marici-positive-product-predecessor p
                (marici-add (marici-succ b) r))))
          (marici-int-neg (marici-positive-product-predecessor p r))
          (marici-int-add-comm
            (marici-int-neg
              (marici-positive-product-predecessor p
                (marici-add (marici-succ b) r)))
            (marici-int-pos (marici-positive-product-predecessor p b)))
          (marici-int-add-scaled-pos-neg-negative-gap p b r)))
```

## Boundary

This settles the positive-residual strict branch for every negative multiplier.
The negative-residual, equal, and common-successor recursion cases remain.
