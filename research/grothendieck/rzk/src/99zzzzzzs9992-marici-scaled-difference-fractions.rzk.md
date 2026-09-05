# Directed difference fractions scale to common denominators

A directed raw difference is packaged from its cross-product numerator and
positive-product denominator. Generic positive scaling then gives an equivalent
presentation whose numerator is the scaled difference numerator used by the
common-denominator absolute bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-difference-fraction
  ( a : MariciInt)
  ( d : MariciNat)
  ( b : MariciInt)
  ( e : MariciNat)
  : MariciRawFraction
  := marici-raw-fraction
      (marici-raw-difference-numerator a d b e)
      (marici-positive-product-predecessor d e)

#define marici-scaled-raw-difference-fraction
  ( a : MariciInt)
  ( d : MariciNat)
  ( b : MariciInt)
  ( e scale : MariciNat)
  : MariciRawFraction
  := marici-raw-fraction
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator a d b e) scale)
      (marici-positive-product-predecessor
        (marici-positive-product-predecessor d e) scale)

#define marici-raw-difference-fraction-scale-equivalent
  ( a : MariciInt)
  ( d : MariciNat)
  ( b : MariciInt)
  ( e scale : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-difference-fraction a d b e)
      (marici-scaled-raw-difference-fraction a d b e scale)
  := marici-raw-fraction-scale-positive-equivalent
      (marici-raw-difference-fraction a d b e) scale
```

## Boundary

Each directed difference now has a proved equivalent scaled presentation. The
second and outer scaled denominators still require transport along the common
triple-denominator predecessor paths before one raw order comparison can be
formed.
