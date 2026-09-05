# Second raw-addition order summand aligns

The second source fraction inequality is scaled by the first pair of
 denominators. Adjacent swaps align both endpoints with the second terms of the
cross-multiplied raw sums.

```rzk
#lang rzk-1
```

```rzk
#define marici-second-raw-add-order-summand
  ( c g : MariciInt)
  ( d e f h : MariciNat)
  ( witness : MariciIntAtMost
      (marici-scale-by-positive-denominator c h)
      (marici-scale-by-positive-denominator g f))
  : MariciIntAtMost
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator c d)
          (marici-int-positive-denominator e))
        (marici-int-positive-denominator h))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator g e)
          (marici-int-positive-denominator d))
        (marici-int-positive-denominator f))
  := marici-int-at-most-transport-both
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator c h)
          (marici-int-positive-denominator d))
        (marici-int-positive-denominator e))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator c d)
          (marici-int-positive-denominator e))
        (marici-int-positive-denominator h))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator g f)
          (marici-int-positive-denominator d))
        (marici-int-positive-denominator e))
      (marici-int-mul
        (marici-int-mul
          (marici-scale-by-positive-denominator g e)
          (marici-int-positive-denominator d))
        (marici-int-positive-denominator f))
      (concat MariciInt
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator c h)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator e))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator c d)
            (marici-int-positive-denominator h))
          (marici-int-positive-denominator e))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator c d)
            (marici-int-positive-denominator e))
          (marici-int-positive-denominator h))
        (marici-int-four-scale-swap-first-two
          c (marici-int-positive-denominator h)
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (marici-int-four-scale-swap-last-two
          c (marici-int-positive-denominator d)
          (marici-int-positive-denominator h)
          (marici-int-positive-denominator e)))
      (concat MariciInt
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator g f)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator e))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator g f)
            (marici-int-positive-denominator e))
          (marici-int-positive-denominator d))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator g e)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator f))
        (marici-int-four-scale-swap-last-two
          g (marici-int-positive-denominator f)
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (concat MariciInt
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator g f)
              (marici-int-positive-denominator e))
            (marici-int-positive-denominator d))
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator g e)
              (marici-int-positive-denominator f))
            (marici-int-positive-denominator d))
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator g e)
              (marici-int-positive-denominator d))
            (marici-int-positive-denominator f))
          (marici-int-four-scale-swap-first-two
            g (marici-int-positive-denominator f)
            (marici-int-positive-denominator e)
            (marici-int-positive-denominator d))
          (marici-int-four-scale-swap-last-two
            g (marici-int-positive-denominator e)
            (marici-int-positive-denominator f)
            (marici-int-positive-denominator d))))
      (marici-int-at-most-two-positive-right-scales
        (marici-scale-by-positive-denominator c h)
        (marici-scale-by-positive-denominator g f)
        d e witness)
```

## Boundary

Both summand inequalities are now aligned with the expanded cross-products of
raw sums. Integer addition monotonicity and product-distribution paths can now
finish raw-fraction addition monotonicity.
