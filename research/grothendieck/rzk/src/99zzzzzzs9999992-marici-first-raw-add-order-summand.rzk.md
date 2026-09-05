# First raw-addition order summand aligns

The first source fraction inequality is scaled by the other two denominators.
Adjacent factor swaps then place its endpoints in the exact order produced by
cross-multiplying the two raw sums.

```rzk
#lang rzk-1
```

```rzk
#define marici-first-raw-add-order-summand
  ( a b : MariciInt)
  ( d e f h : MariciNat)
  ( witness : MariciIntAtMost
      (marici-scale-by-positive-denominator a e)
      (marici-scale-by-positive-denominator b d))
  : MariciIntAtMost
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator a f)
          (marici-int-positive-denominator e))
        (marici-int-positive-denominator h))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator b h)
          (marici-int-positive-denominator d))
        (marici-int-positive-denominator f))
  := marici-int-at-most-transport-both
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator a e)
          (marici-int-positive-denominator f))
        (marici-int-positive-denominator h))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator a f)
          (marici-int-positive-denominator e))
        (marici-int-positive-denominator h))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator b d)
          (marici-int-positive-denominator f))
        (marici-int-positive-denominator h))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator b h)
          (marici-int-positive-denominator d))
        (marici-int-positive-denominator f))
      (marici-int-four-scale-swap-first-two
        a (marici-int-positive-denominator e)
        (marici-int-positive-denominator f)
        (marici-int-positive-denominator h))
      (concat MariciInt
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator b d)
            (marici-int-positive-denominator f))
          (marici-int-positive-denominator h))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator b d)
            (marici-int-positive-denominator h))
          (marici-int-positive-denominator f))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator b h)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator f))
        (marici-int-four-scale-swap-last-two
          b (marici-int-positive-denominator d)
          (marici-int-positive-denominator f)
          (marici-int-positive-denominator h))
        (marici-int-four-scale-swap-first-two
          b (marici-int-positive-denominator d)
          (marici-int-positive-denominator h)
          (marici-int-positive-denominator f)))
      (marici-int-at-most-two-positive-right-scales
        (marici-scale-by-positive-denominator a e)
        (marici-scale-by-positive-denominator b d)
        f h witness)
```

## Boundary

The first summands of the cross-multiplied raw sums are now ordered. The second
source inequality requires its analogous three-factor alignment before integer
addition monotonicity combines them.
