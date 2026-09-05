# Common-successor step for positive-factor mixed distributivity

If positive-factor mixed distributivity holds for two predecessor magnitudes,
it also holds after adding one common successor. Source normalization removes
one common successor; product normalization removes one common positive-factor
prefix.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-factor-mixed-successor-step
  ( p a b : MariciNat)
  ( ih : marici-int-mul (marici-int-pos p)
      (marici-int-add (marici-int-pos a) (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-pos p) (marici-int-pos a))
      (marici-int-mul (marici-int-pos p) (marici-int-neg b)))
  : marici-int-mul (marici-int-pos p)
      (marici-int-add
        (marici-int-pos (marici-succ a))
        (marici-int-neg (marici-succ b)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-pos p)
        (marici-int-pos (marici-succ a)))
      (marici-int-mul (marici-int-pos p)
        (marici-int-neg (marici-succ b)))
  := concat MariciInt
      (marici-int-mul (marici-int-pos p)
        (marici-int-add
          (marici-int-pos (marici-succ a))
          (marici-int-neg (marici-succ b))))
      (marici-int-add
        (marici-int-mul (marici-int-pos p) (marici-int-pos a))
        (marici-int-mul (marici-int-pos p) (marici-int-neg b)))
      (marici-int-add
        (marici-int-mul (marici-int-pos p)
          (marici-int-pos (marici-succ a)))
        (marici-int-mul (marici-int-pos p)
          (marici-int-neg (marici-succ b))))
      (concat MariciInt
        (marici-int-mul (marici-int-pos p)
          (marici-int-add
            (marici-int-pos (marici-succ a))
            (marici-int-neg (marici-succ b))))
        (marici-int-mul (marici-int-pos p)
          (marici-int-add (marici-int-pos a) (marici-int-neg b)))
        (marici-int-add
          (marici-int-mul (marici-int-pos p) (marici-int-pos a))
          (marici-int-mul (marici-int-pos p) (marici-int-neg b)))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-pos (marici-succ a))
            (marici-int-neg (marici-succ b)))
          (marici-int-add (marici-int-pos a) (marici-int-neg b))
          (\ z → marici-int-mul (marici-int-pos p) z)
          (marici-int-add-opposite-common-prefix
            (marici-succ marici-zero) a b))
        ih)
      (rev MariciInt
        (marici-int-add
          (marici-int-mul (marici-int-pos p)
            (marici-int-pos (marici-succ a)))
          (marici-int-mul (marici-int-pos p)
            (marici-int-neg (marici-succ b))))
        (marici-int-add
          (marici-int-mul (marici-int-pos p) (marici-int-pos a))
          (marici-int-mul (marici-int-pos p) (marici-int-neg b)))
        (concat MariciInt
          (marici-int-add
            (marici-int-mul (marici-int-pos p)
              (marici-int-pos (marici-succ a)))
            (marici-int-mul (marici-int-pos p)
              (marici-int-neg (marici-succ b))))
          (marici-int-add
            (marici-int-pos
              (marici-add (marici-succ p)
                (marici-positive-product-predecessor p a)))
            (marici-int-neg
              (marici-add (marici-succ p)
                (marici-positive-product-predecessor p b))))
          (marici-int-add
            (marici-int-mul (marici-int-pos p) (marici-int-pos a))
            (marici-int-mul (marici-int-pos p) (marici-int-neg b)))
          (concat MariciInt
            (marici-int-add
              (marici-int-pos
                (marici-positive-product-predecessor p (marici-succ a)))
              (marici-int-neg
                (marici-positive-product-predecessor p (marici-succ b))))
            (marici-int-add
              (marici-int-pos
                (marici-add (marici-succ p)
                  (marici-positive-product-predecessor p a)))
              (marici-int-neg
                (marici-positive-product-predecessor p (marici-succ b))))
            (marici-int-add
              (marici-int-pos
                (marici-add (marici-succ p)
                  (marici-positive-product-predecessor p a)))
              (marici-int-neg
                (marici-add (marici-succ p)
                  (marici-positive-product-predecessor p b))))
            (ap MariciNat MariciInt
              (marici-positive-product-predecessor p (marici-succ a))
              (marici-add (marici-succ p)
                (marici-positive-product-predecessor p a))
              (\ z → marici-int-add (marici-int-pos z)
                (marici-int-neg
                  (marici-positive-product-predecessor p (marici-succ b))))
              (marici-positive-product-successor-right p a))
            (ap MariciNat MariciInt
              (marici-positive-product-predecessor p (marici-succ b))
              (marici-add (marici-succ p)
                (marici-positive-product-predecessor p b))
              (\ z → marici-int-add
                (marici-int-pos
                  (marici-add (marici-succ p)
                    (marici-positive-product-predecessor p a)))
                (marici-int-neg z))
              (marici-positive-product-successor-right p b)))
          (marici-int-add-opposite-common-prefix (marici-succ p)
            (marici-positive-product-predecessor p a)
            (marici-positive-product-predecessor p b))))
```

## Boundary

This theorem supplies the recursive step only. Combining it with the three
base presentations from modules 58 and 60 yields unrestricted positive-factor
mixed distributivity by simultaneous structural recursion.
