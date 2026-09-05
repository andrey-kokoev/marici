# A positive product plus a natural is nonzero

The product of two structurally positive naturals computes to a successor.
Adding any natural preserves that outer successor, so such a sum cannot equal
zero. This is the terminal contradiction in the greater-quotient branch of
division uniqueness.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-plus-successor-form
  ( left-predecessor right-predecessor remainder : MariciNat)
  : marici-add
      (marici-mul (marici-succ left-predecessor)
        (marici-succ right-predecessor))
      remainder
    =_{MariciNat}
    marici-succ
      (marici-add
        (marici-add right-predecessor
          (marici-mul left-predecessor
            (marici-succ right-predecessor)))
        remainder)
  := refl

#define marici-positive-product-plus-not-zero
  ( left-predecessor right-predecessor remainder : MariciNat)
  : (marici-add
      (marici-mul (marici-succ left-predecessor)
        (marici-succ right-predecessor))
      remainder
    =_{MariciNat} marici-zero)
    → MariciEmpty
  := \ equation →
      marici-succ-not-zero
        (marici-add
          (marici-add right-predecessor
            (marici-mul left-predecessor
              (marici-succ right-predecessor)))
          remainder)
        (concat MariciNat
          (marici-succ
            (marici-add
              (marici-add right-predecessor
                (marici-mul left-predecessor
                  (marici-succ right-predecessor)))
              remainder))
          (marici-add
            (marici-mul (marici-succ left-predecessor)
              (marici-succ right-predecessor))
            remainder)
          marici-zero
          (rev MariciNat
            (marici-add
              (marici-mul (marici-succ left-predecessor)
                (marici-succ right-predecessor))
              remainder)
            (marici-succ
              (marici-add
                (marici-add right-predecessor
                  (marici-mul left-predecessor
                    (marici-succ right-predecessor)))
                remainder))
            (marici-positive-product-plus-successor-form
              left-predecessor right-predecessor remainder))
          equation)
```

## Boundary

Any equation making a positive divisor-gap product plus a remainder equal zero
is now directly eliminable. The remaining greater-quotient proof must use
product distributivity and additive prefix cancellation to derive exactly that
equation from the two reconstructions.
