# Base scaled residual for positive-product predecessors

When the smaller source predecessor is zero, subtracting its scaled positive
magnitude from the next larger scaled product leaves the scaled residual. This
is the base case for common-prefix induction on the smaller predecessor.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-residual-base
  ( p r : MariciNat)
  : marici-sub
      (marici-positive-product-predecessor p (marici-succ r))
      (marici-succ (marici-positive-product-predecessor p marici-zero))
    =_{MariciNat} marici-positive-product-predecessor p r
  := concat MariciNat
      (marici-sub
        (marici-positive-product-predecessor p (marici-succ r))
        (marici-succ (marici-positive-product-predecessor p marici-zero)))
      (marici-sub
        (marici-add (marici-succ p)
          (marici-positive-product-predecessor p r))
        (marici-succ p))
      (marici-positive-product-predecessor p r)
      (concat MariciNat
        (marici-sub
          (marici-positive-product-predecessor p (marici-succ r))
          (marici-succ (marici-positive-product-predecessor p marici-zero)))
        (marici-sub
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p r))
          (marici-succ (marici-positive-product-predecessor p marici-zero)))
        (marici-sub
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p r))
          (marici-succ p))
        (ap MariciNat MariciNat
          (marici-positive-product-predecessor p (marici-succ r))
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p r))
          (\ z → marici-sub z
            (marici-succ (marici-positive-product-predecessor p marici-zero)))
          (marici-positive-product-successor-right p r))
        (ap MariciNat MariciNat
          (marici-succ (marici-positive-product-predecessor p marici-zero))
          (marici-succ p)
          (\ z → marici-sub
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p r)) z)
          (ap MariciNat MariciNat
            (marici-positive-product-predecessor p marici-zero)
            p
            marici-succ
            (marici-positive-product-one-right p))))
      (marici-sub-add-prefix (marici-succ p)
        (marici-positive-product-predecessor p r))
```

## Boundary

The theorem covers arbitrary positive scaling and arbitrary residual, but only
the zero smaller-predecessor base. The general theorem still requires induction
that removes matching scaled successor blocks.
