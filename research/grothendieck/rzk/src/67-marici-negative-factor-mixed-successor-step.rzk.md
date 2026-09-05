# Common-successor step for negative-factor mixed distributivity

Source common-prefix normalization and the product reduction of module 66 turn
an induction hypothesis into the corresponding theorem after one common
successor.

```rzk
#lang rzk-1
```

```rzk
#define marici-negative-factor-mixed-successor-step
  ( p a b : MariciNat)
  ( ih : marici-int-mul (marici-int-neg p)
      (marici-int-add (marici-int-pos a) (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p) (marici-int-pos a))
      (marici-int-mul (marici-int-neg p) (marici-int-neg b)))
  : marici-int-mul (marici-int-neg p)
      (marici-int-add
        (marici-int-pos (marici-succ a))
        (marici-int-neg (marici-succ b)))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-neg p)
        (marici-int-pos (marici-succ a)))
      (marici-int-mul (marici-int-neg p)
        (marici-int-neg (marici-succ b)))
  := concat MariciInt
      (marici-int-mul (marici-int-neg p)
        (marici-int-add
          (marici-int-pos (marici-succ a))
          (marici-int-neg (marici-succ b))))
      (marici-int-add
        (marici-int-mul (marici-int-neg p) (marici-int-pos a))
        (marici-int-mul (marici-int-neg p) (marici-int-neg b)))
      (marici-int-add
        (marici-int-mul (marici-int-neg p)
          (marici-int-pos (marici-succ a)))
        (marici-int-mul (marici-int-neg p)
          (marici-int-neg (marici-succ b))))
      (concat MariciInt
        (marici-int-mul (marici-int-neg p)
          (marici-int-add
            (marici-int-pos (marici-succ a))
            (marici-int-neg (marici-succ b))))
        (marici-int-mul (marici-int-neg p)
          (marici-int-add (marici-int-pos a) (marici-int-neg b)))
        (marici-int-add
          (marici-int-mul (marici-int-neg p) (marici-int-pos a))
          (marici-int-mul (marici-int-neg p) (marici-int-neg b)))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-int-pos (marici-succ a))
            (marici-int-neg (marici-succ b)))
          (marici-int-add (marici-int-pos a) (marici-int-neg b))
          (\ z → marici-int-mul (marici-int-neg p) z)
          (marici-int-add-opposite-common-prefix
            (marici-succ marici-zero) a b))
        ih)
      (rev MariciInt
        (marici-int-add
          (marici-int-mul (marici-int-neg p)
            (marici-int-pos (marici-succ a)))
          (marici-int-mul (marici-int-neg p)
            (marici-int-neg (marici-succ b))))
        (marici-int-add
          (marici-int-mul (marici-int-neg p) (marici-int-pos a))
          (marici-int-mul (marici-int-neg p) (marici-int-neg b)))
        (marici-negative-products-common-successor p a b))
```

## Boundary

The recursive step and all zero-edge bases now hold for negative multipliers.
Only the simultaneous recursion remains for the unrestricted family.
