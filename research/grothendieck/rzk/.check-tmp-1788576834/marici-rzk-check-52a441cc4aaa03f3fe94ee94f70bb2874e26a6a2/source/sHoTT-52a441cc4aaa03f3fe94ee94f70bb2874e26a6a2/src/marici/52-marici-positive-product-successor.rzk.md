# Successor recurrence for positive-product predecessors

Increasing one encoded positive magnitude by one adds one full copy of the
other positive factor to the product predecessor. This recurrence supplies the
induction step for scaled subtraction residuals.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-successor-right
  ( p a : MariciNat)
  : marici-positive-product-predecessor p (marici-succ a)
    =_{MariciNat}
    marici-add (marici-succ p)
      (marici-positive-product-predecessor p a)
  := ap MariciNat MariciNat
      (marici-succ
        (marici-positive-product-predecessor p (marici-succ a)))
      (marici-succ
        (marici-add (marici-succ p)
          (marici-positive-product-predecessor p a)))
      marici-pred
      (concat MariciNat
        (marici-succ
          (marici-positive-product-predecessor p (marici-succ a)))
        (marici-add (marici-succ p)
          (marici-succ (marici-positive-product-predecessor p a)))
        (marici-succ
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p a)))
        (concat MariciNat
          (marici-succ
            (marici-positive-product-predecessor p (marici-succ a)))
          (marici-mul (marici-succ p)
            (marici-succ (marici-succ a)))
          (marici-add (marici-succ p)
            (marici-succ (marici-positive-product-predecessor p a)))
          (marici-succ-positive-product p (marici-succ a))
          (concat MariciNat
            (marici-mul (marici-succ p)
              (marici-succ (marici-succ a)))
            (marici-add (marici-succ p)
              (marici-mul (marici-succ p) (marici-succ a)))
            (marici-add (marici-succ p)
              (marici-succ (marici-positive-product-predecessor p a)))
            (marici-mul-succ-right (marici-succ p) (marici-succ a))
            (ap MariciNat MariciNat
              (marici-mul (marici-succ p) (marici-succ a))
              (marici-succ (marici-positive-product-predecessor p a))
              (\ z → marici-add (marici-succ p) z)
              (rev MariciNat
                (marici-succ (marici-positive-product-predecessor p a))
                (marici-mul (marici-succ p) (marici-succ a))
                (marici-succ-positive-product p a)))))
        (marici-add-succ-right (marici-succ p)
          (marici-positive-product-predecessor p a)))

#define marici-positive-product-successor-left
  ( p a : MariciNat)
  : marici-positive-product-predecessor (marici-succ p) a
    =_{MariciNat}
    marici-add (marici-succ a)
      (marici-positive-product-predecessor p a)
  := concat MariciNat
      (marici-positive-product-predecessor (marici-succ p) a)
      (marici-positive-product-predecessor a (marici-succ p))
      (marici-add (marici-succ a)
        (marici-positive-product-predecessor p a))
      (marici-positive-product-predecessor-comm (marici-succ p) a)
      (concat MariciNat
        (marici-positive-product-predecessor a (marici-succ p))
        (marici-add (marici-succ a)
          (marici-positive-product-predecessor a p))
        (marici-add (marici-succ a)
          (marici-positive-product-predecessor p a))
        (marici-positive-product-successor-right a p)
        (ap MariciNat MariciNat
          (marici-positive-product-predecessor a p)
          (marici-positive-product-predecessor p a)
          (\ z → marici-add (marici-succ a) z)
          (marici-positive-product-predecessor-comm a p)))
```

## Boundary

Both successor recurrences are checked. They do not yet state the subtraction
residual theorem obtained by iterating these recurrences.
