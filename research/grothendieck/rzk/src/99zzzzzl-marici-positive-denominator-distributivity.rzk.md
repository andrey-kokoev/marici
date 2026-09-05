# Positive-denominator scaling distributes over integer addition

This specializes checked global integer distributivity to the denominator
scaling operation used in raw-fraction cross products. It removes one repeated
expansion from the addition-congruence proof.

```rzk
#lang rzk-1
```

```rzk
#define marici-scale-by-positive-denominator-add
  ( x y : MariciInt)
  ( d : MariciNat)
  : marici-scale-by-positive-denominator (marici-int-add x y) d
    =_{MariciInt}
    marici-int-add
      (marici-scale-by-positive-denominator x d)
      (marici-scale-by-positive-denominator y d)
  := marici-int-mul-add-right-distrib
      x y (marici-int-positive-denominator d)
```

## Boundary

This proves distributivity for the exact scaling operation occurring in raw
fraction equivalence. It does not yet prove that raw fraction addition respects
equivalence; that theorem must also reassociate four denominator factors and
transport both input cross-product equalities.
