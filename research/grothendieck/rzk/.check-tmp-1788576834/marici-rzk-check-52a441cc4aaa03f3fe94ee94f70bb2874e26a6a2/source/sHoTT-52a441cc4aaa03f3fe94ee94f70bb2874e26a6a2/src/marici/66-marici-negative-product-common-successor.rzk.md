# Common-successor reduction for negative-factor products

After multiplication by a common negative factor, adding one successor to both
source predecessor magnitudes adds a common positive-factor prefix to the
opposed product magnitudes. Mixed normalization removes that prefix.

```rzk
#lang rzk-1
```

```rzk
#define marici-negative-products-common-successor
  ( p a b : MariciNat)
  : marici-int-add
      (marici-int-mul (marici-int-neg p)
        (marici-int-pos (marici-succ a)))
      (marici-int-mul (marici-int-neg p)
        (marici-int-neg (marici-succ b)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p) (marici-int-pos a))
      (marici-int-mul (marici-int-neg p) (marici-int-neg b))
  := concat MariciInt
      (marici-int-add
        (marici-int-neg
          (marici-positive-product-predecessor p (marici-succ a)))
        (marici-int-pos
          (marici-positive-product-predecessor p (marici-succ b))))
      (marici-int-add
        (marici-int-neg
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p a)))
        (marici-int-pos
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p b))))
      (marici-int-add
        (marici-int-neg (marici-positive-product-predecessor p a))
        (marici-int-pos (marici-positive-product-predecessor p b)))
      (concat MariciInt
        (marici-int-add
          (marici-int-neg
            (marici-positive-product-predecessor p (marici-succ a)))
          (marici-int-pos
            (marici-positive-product-predecessor p (marici-succ b))))
        (marici-int-add
          (marici-int-neg
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p a)))
          (marici-int-pos
            (marici-positive-product-predecessor p (marici-succ b))))
        (marici-int-add
          (marici-int-neg
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p a)))
          (marici-int-pos
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p b))))
        (ap MariciNat MariciInt
          (marici-positive-product-predecessor p (marici-succ a))
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p a))
          (\ z → marici-int-add (marici-int-neg z)
            (marici-int-pos
              (marici-positive-product-predecessor p (marici-succ b))))
          (marici-positive-product-successor-right p a))
        (ap MariciNat MariciInt
          (marici-positive-product-predecessor p (marici-succ b))
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p b))
          (\ z → marici-int-add
            (marici-int-neg
              (marici-add (marici-succ p)
                (marici-positive-product-predecessor p a)))
            (marici-int-pos z))
          (marici-positive-product-successor-right p b)))
      (marici-int-add-reversed-opposite-common-prefix (marici-succ p)
        (marici-positive-product-predecessor p a)
        (marici-positive-product-predecessor p b))
```

## Boundary

This theorem is the product-side half of the negative-factor common-successor
step. Composing it with source common-prefix normalization and an induction
hypothesis remains.
