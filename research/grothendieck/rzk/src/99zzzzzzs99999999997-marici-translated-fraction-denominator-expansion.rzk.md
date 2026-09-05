# Translated-fraction encoded denominators expand coherently

Nested positive-product predecessor encodings map to the corresponding nested
integer products. The numerator's subtracted denominator product is also
reordered into the orientation used by translated cross-product cancellation.

```rzk
#lang rzk-1
```

```rzk
#define marici-nested-positive-denominator-product
  ( d e : MariciNat)
  : marici-int-positive-denominator
      (marici-positive-product-predecessor
        (marici-positive-product-predecessor d e) d)
    =_{MariciInt}
    marici-int-mul
      (marici-int-mul
        (marici-int-positive-denominator d)
        (marici-int-positive-denominator e))
      (marici-int-positive-denominator d)
  := concat MariciInt
      (marici-int-positive-denominator
        (marici-positive-product-predecessor
          (marici-positive-product-predecessor d e) d))
      (marici-int-mul
        (marici-int-positive-denominator
          (marici-positive-product-predecessor d e))
        (marici-int-positive-denominator d))
      (marici-int-mul
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (marici-int-positive-denominator d))
      (marici-positive-denominator-product
        (marici-positive-product-predecessor d e) d)
      (ap MariciInt MariciInt
        (marici-int-positive-denominator
          (marici-positive-product-predecessor d e))
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (\ left → marici-int-mul left
          (marici-int-positive-denominator d))
        (marici-positive-denominator-product d e))

#define marici-scaled-nested-denominator-reordered
  ( a : MariciInt)
  ( d e : MariciNat)
  : marici-scale-by-positive-denominator a
      (marici-positive-product-predecessor d e)
    =_{MariciInt}
    marici-int-mul a
      (marici-int-mul
        (marici-int-positive-denominator e)
        (marici-int-positive-denominator d))
  := concat MariciInt
      (marici-scale-by-positive-denominator a
        (marici-positive-product-predecessor d e))
      (marici-int-mul a
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e)))
      (marici-int-mul a
        (marici-int-mul
          (marici-int-positive-denominator e)
          (marici-int-positive-denominator d)))
      (ap MariciInt MariciInt
        (marici-int-positive-denominator
          (marici-positive-product-predecessor d e))
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (\ denominator → marici-int-mul a denominator)
        (marici-positive-denominator-product d e))
      (ap MariciInt MariciInt
        (marici-int-mul
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e))
        (marici-int-mul
          (marici-int-positive-denominator e)
          (marici-int-positive-denominator d))
        (\ denominator → marici-int-mul a denominator)
        (marici-int-mul-comm
          (marici-int-positive-denominator d)
          (marici-int-positive-denominator e)))
```

## Boundary

Both encoded denominator paths required by translated-fraction cancellation are
now explicit. They can be applied under numerator negation and cross-product
multiplication to finish `((p + q) - p) ~ q`.
