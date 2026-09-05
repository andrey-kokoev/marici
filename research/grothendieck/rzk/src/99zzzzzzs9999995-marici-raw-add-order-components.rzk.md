# Raw-fraction addition is monotone on components

The two aligned summand inequalities combine by integer addition monotonicity.
The denominator-product distribution paths transport that sum to the actual
cross-products of the raw-fraction sums.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-at-most-components
  ( a b c g : MariciInt)
  ( d e f h : MariciNat)
  ( first-witness : MariciIntAtMost
      (marici-scale-by-positive-denominator a e)
      (marici-scale-by-positive-denominator b d))
  ( second-witness : MariciIntAtMost
      (marici-scale-by-positive-denominator c h)
      (marici-scale-by-positive-denominator g f))
  : MariciRawFractionAtMost
      (marici-raw-fraction-add
        (marici-raw-fraction a d) (marici-raw-fraction c f))
      (marici-raw-fraction-add
        (marici-raw-fraction b e) (marici-raw-fraction g h))
  := marici-int-at-most-transport-both
      (marici-int-add
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator a f)
            (marici-int-positive-denominator e))
          (marici-int-positive-denominator h))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator c d)
            (marici-int-positive-denominator e))
          (marici-int-positive-denominator h)))
      (marici-scale-by-positive-denominator
        (marici-int-add
          (marici-scale-by-positive-denominator a f)
          (marici-scale-by-positive-denominator c d))
        (marici-positive-product-predecessor e h))
      (marici-int-add
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator b h)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator f))
        (marici-int-mul
          (marici-int-mul
            (marici-scale-by-positive-denominator g e)
            (marici-int-positive-denominator d))
          (marici-int-positive-denominator f)))
      (marici-scale-by-positive-denominator
        (marici-int-add
          (marici-scale-by-positive-denominator b h)
          (marici-scale-by-positive-denominator g e))
        (marici-positive-product-predecessor d f))
      (rev MariciInt
        (marici-scale-by-positive-denominator
          (marici-int-add
            (marici-scale-by-positive-denominator a f)
            (marici-scale-by-positive-denominator c d))
          (marici-positive-product-predecessor e h))
        (marici-int-add
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator a f)
              (marici-int-positive-denominator e))
            (marici-int-positive-denominator h))
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator c d)
              (marici-int-positive-denominator e))
            (marici-int-positive-denominator h)))
        (marici-int-sum-scaled-by-denominator-product
          (marici-scale-by-positive-denominator a f)
          (marici-scale-by-positive-denominator c d) e h))
      (rev MariciInt
        (marici-scale-by-positive-denominator
          (marici-int-add
            (marici-scale-by-positive-denominator b h)
            (marici-scale-by-positive-denominator g e))
          (marici-positive-product-predecessor d f))
        (marici-int-add
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator b h)
              (marici-int-positive-denominator d))
            (marici-int-positive-denominator f))
          (marici-int-mul
            (marici-int-mul
              (marici-scale-by-positive-denominator g e)
              (marici-int-positive-denominator d))
            (marici-int-positive-denominator f)))
        (marici-int-sum-scaled-by-denominator-product
          (marici-scale-by-positive-denominator b h)
          (marici-scale-by-positive-denominator g e) d f))
      (marici-int-at-most-add-both
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
        (marici-first-raw-add-order-summand
          a b d e f h first-witness)
        (marici-second-raw-add-order-summand
          c g d e f h second-witness))
```

## Boundary

Raw-fraction addition monotonicity is proved for explicit constructor
components. Constructor elimination and normalization transport remain to expose
it as rational addition monotonicity.
