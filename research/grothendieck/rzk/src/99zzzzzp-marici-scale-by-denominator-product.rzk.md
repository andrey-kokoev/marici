# Scaling by a denominator product

This rewrites the structural denominator of a raw sum into the integer product
needed by the product-of-sum normal form.

```rzk
#lang rzk-1
```

```rzk
#define marici-scale-by-denominator-product
  ( z : MariciInt)
  ( d e : MariciNat)
  : marici-scale-by-positive-denominator z
      (marici-positive-product-predecessor d e)
    =_{MariciInt}
    marici-int-mul z
      (marici-int-mul
        (marici-int-positive-denominator d)
        (marici-int-positive-denominator e))
  := ap MariciInt MariciInt
      (marici-int-positive-denominator
        (marici-positive-product-predecessor d e))
      (marici-int-mul
        (marici-int-positive-denominator d)
        (marici-int-positive-denominator e))
      (\ denominator → marici-int-mul z denominator)
      (marici-positive-denominator-product d e)
```

## Boundary

This is a typed denominator rewrite, not cancellation. Together with the
checked product-of-sum rotation it exposes the two input equivalence paths in
raw-fraction addition congruence.
