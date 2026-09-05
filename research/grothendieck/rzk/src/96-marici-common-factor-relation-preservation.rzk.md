# Common-factor removal preserves raw-fraction equivalence

Positive scaling relates the extracted cofactor fraction to its scaled form.
Transport along the reconstruction path replaces that scaled form by the
original raw fraction; symmetry gives the factor-removal orientation.

```rzk
#lang rzk-1
```

```rzk
#define marici-common-factor-reduced-equivalent-original
  ( a : MariciInt)
  ( d f : MariciNat)
  ( c : MariciRawComponentsCommonPositiveFactor a d f)
  : marici-raw-fraction-equivalent
      (marici-common-factor-reduced-fraction a d f c)
      (marici-raw-fraction a d)
  := transport MariciRawFraction
      (\ q → marici-raw-fraction-equivalent
        (marici-common-factor-reduced-fraction a d f c) q)
      (marici-raw-fraction-scale-positive
        (marici-common-factor-reduced-fraction a d f c) f)
      (marici-raw-fraction a d)
      (marici-common-factor-reconstruction a d f c)
      (marici-raw-fraction-scale-positive-equivalent
        (marici-common-factor-reduced-fraction a d f c) f)

#define marici-common-factor-removal-preserves-equivalent
  ( a : MariciInt)
  ( d f : MariciNat)
  ( c : MariciRawComponentsCommonPositiveFactor a d f)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction a d)
      (marici-common-factor-reduced-fraction a d f c)
  := marici-raw-fraction-equivalent-sym
      (marici-common-factor-reduced-fraction a d f c)
      (marici-raw-fraction a d)
      (marici-common-factor-reduced-equivalent-original a d f c)
```

## Boundary

A supplied common positive factor can now be removed while preserving the raw
fraction relation, and its cofactors form the resulting representative.
Constructive nonunit factor selection, coprimality, termination of repeated
removal, and uniqueness of reduced representatives remain open.
