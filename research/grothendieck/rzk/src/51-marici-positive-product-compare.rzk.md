# Comparison of positive-product predecessors

The predecessor encoding of positive integer multiplication preserves natural
comparison when both magnitudes are multiplied by the same positive factor.

```rzk
#lang rzk-1
```

```rzk
#define marici-compare-positive-product-predecessor
  ( p a b : MariciNat)
  : marici-compare
      (marici-positive-product-predecessor p a)
      (marici-positive-product-predecessor p b)
    =_{MariciOrdering} marici-compare a b
  := concat MariciOrdering
      (marici-compare
        (marici-positive-product-predecessor p a)
        (marici-positive-product-predecessor p b))
      (marici-compare
        (marici-mul (marici-succ p) (marici-succ a))
        (marici-mul (marici-succ p) (marici-succ b)))
      (marici-compare a b)
      (concat MariciOrdering
        (marici-compare
          (marici-positive-product-predecessor p a)
          (marici-positive-product-predecessor p b))
        (marici-compare
          (marici-succ (marici-positive-product-predecessor p a))
          (marici-succ (marici-positive-product-predecessor p b)))
        (marici-compare
          (marici-mul (marici-succ p) (marici-succ a))
          (marici-mul (marici-succ p) (marici-succ b)))
        refl
        (concat MariciOrdering
          (marici-compare
            (marici-succ (marici-positive-product-predecessor p a))
            (marici-succ (marici-positive-product-predecessor p b)))
          (marici-compare
            (marici-mul (marici-succ p) (marici-succ a))
            (marici-succ (marici-positive-product-predecessor p b)))
          (marici-compare
            (marici-mul (marici-succ p) (marici-succ a))
            (marici-mul (marici-succ p) (marici-succ b)))
          (ap MariciNat MariciOrdering
            (marici-succ (marici-positive-product-predecessor p a))
            (marici-mul (marici-succ p) (marici-succ a))
            (\ z → marici-compare z
              (marici-succ (marici-positive-product-predecessor p b)))
            (marici-succ-positive-product p a))
          (ap MariciNat MariciOrdering
            (marici-succ (marici-positive-product-predecessor p b))
            (marici-mul (marici-succ p) (marici-succ b))
            (\ z → marici-compare
              (marici-mul (marici-succ p) (marici-succ a)) z)
            (marici-succ-positive-product p b))))
      (marici-compare-positive-scale p (marici-succ a) (marici-succ b))
```

## Boundary

This theorem transfers the scaled comparison result from full positive
magnitudes to the predecessor encoding used by normalized integer products. It
does not yet identify the scaled subtraction residual in each comparison
branch.
