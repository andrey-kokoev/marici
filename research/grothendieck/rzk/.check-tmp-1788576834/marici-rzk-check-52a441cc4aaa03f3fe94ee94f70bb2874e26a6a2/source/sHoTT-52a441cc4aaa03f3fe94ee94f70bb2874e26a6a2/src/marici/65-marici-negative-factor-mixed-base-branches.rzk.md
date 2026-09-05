# Remaining negative-factor mixed base branches

The negative-residual strict branch and equal-magnitude branch complete the
base cases needed for negative-factor structural recursion.

```rzk
#lang rzk-1
```

```rzk
#define marici-negative-factor-negative-gap-left-distrib
  ( p b r : MariciNat)
  : marici-int-mul (marici-int-neg p)
      (marici-int-add
        (marici-int-pos b)
        (marici-int-neg (marici-add (marici-succ b) r)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p) (marici-int-pos b))
      (marici-int-mul (marici-int-neg p)
        (marici-int-neg (marici-add (marici-succ b) r)))
  := concat MariciInt
      (marici-int-mul (marici-int-neg p)
        (marici-int-add
          (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) r))))
      (marici-int-pos (marici-positive-product-predecessor p r))
      (marici-int-add
        (marici-int-mul (marici-int-neg p) (marici-int-pos b))
        (marici-int-mul (marici-int-neg p)
          (marici-int-neg (marici-add (marici-succ b) r))))
      (ap MariciInt MariciInt
        (marici-int-add
          (marici-int-pos b)
          (marici-int-neg (marici-add (marici-succ b) r)))
        (marici-int-neg r)
        (\ z → marici-int-mul (marici-int-neg p) z)
        (marici-int-add-pos-neg-negative-gap b r))
      (rev MariciInt
        (marici-int-add
          (marici-int-neg (marici-positive-product-predecessor p b))
          (marici-int-pos
            (marici-positive-product-predecessor p
              (marici-add (marici-succ b) r))))
        (marici-int-pos (marici-positive-product-predecessor p r))
        (concat MariciInt
          (marici-int-add
            (marici-int-neg (marici-positive-product-predecessor p b))
            (marici-int-pos
              (marici-positive-product-predecessor p
                (marici-add (marici-succ b) r))))
          (marici-int-add
            (marici-int-pos
              (marici-positive-product-predecessor p
                (marici-add (marici-succ b) r)))
            (marici-int-neg (marici-positive-product-predecessor p b)))
          (marici-int-pos (marici-positive-product-predecessor p r))
          (marici-int-add-comm
            (marici-int-neg (marici-positive-product-predecessor p b))
            (marici-int-pos
              (marici-positive-product-predecessor p
                (marici-add (marici-succ b) r))))
          (marici-int-add-scaled-pos-neg-gap p b r)))

#define marici-negative-factor-equal-mixed-left-distrib
  ( p a : MariciNat)
  : marici-int-mul (marici-int-neg p)
      (marici-int-add (marici-int-pos a) (marici-int-neg a))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p) (marici-int-pos a))
      (marici-int-mul (marici-int-neg p) (marici-int-neg a))
  := concat MariciInt
      (marici-int-mul (marici-int-neg p)
        (marici-int-add (marici-int-pos a) (marici-int-neg a)))
      marici-int-zero
      (marici-int-add
        (marici-int-mul (marici-int-neg p) (marici-int-pos a))
        (marici-int-mul (marici-int-neg p) (marici-int-neg a)))
      (concat MariciInt
        (marici-int-mul (marici-int-neg p)
          (marici-int-add (marici-int-pos a) (marici-int-neg a)))
        (marici-int-mul (marici-int-neg p) marici-int-zero)
        marici-int-zero
        (ap MariciInt MariciInt
          (marici-int-add (marici-int-pos a) (marici-int-neg a))
          marici-int-zero
          (\ z → marici-int-mul (marici-int-neg p) z)
          (marici-int-add-pos-neg-self a))
        (marici-int-mul-zero-right (marici-int-neg p)))
      (rev MariciInt
        (marici-int-add
          (marici-int-neg (marici-positive-product-predecessor p a))
          (marici-int-pos (marici-positive-product-predecessor p a)))
        marici-int-zero
        (marici-int-add-pos-neg-self
          (marici-positive-product-predecessor p a)))
```

## Boundary

All three zero-edge/equal base branches now hold for negative multipliers. The
common-successor step and simultaneous recursion remain.
