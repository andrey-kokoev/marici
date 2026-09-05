# Positive scaling reflects raw-fraction equivalence

Symmetry turns forward positive scaling into a common-factor removal path.
Transitivity then shows that scaling both raw fractions by the same positive
factor reflects the cross-product relation.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-scale-positive-equivalent-back
  ( p : MariciRawFraction)
  ( e : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-scale-positive p e) p
  := marici-raw-fraction-equivalent-sym p
      (marici-raw-fraction-scale-positive p e)
      (marici-raw-fraction-scale-positive-equivalent p e)

#define marici-raw-fraction-scale-positive-reflects-equivalent
  ( p q : MariciRawFraction)
  ( e : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-scale-positive p e)
      (marici-raw-fraction-scale-positive q e)
  → marici-raw-fraction-equivalent p q
  := \ h → marici-raw-fraction-equivalent-trans
      p
      (marici-raw-fraction-scale-positive p e)
      q
      (marici-raw-fraction-scale-positive-equivalent p e)
      (marici-raw-fraction-equivalent-trans
        (marici-raw-fraction-scale-positive p e)
        (marici-raw-fraction-scale-positive q e)
        q
        h
        (marici-raw-fraction-scale-positive-equivalent-back q e))
```

## Boundary

A supplied common positive scaling factor can now be removed at the relation
level. This does not choose a factor, prove coprimality, construct a reduced
representative, or establish uniqueness of normalization.
