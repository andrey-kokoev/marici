# Three rational difference numerators at a common denominator

Instantiating the three-scale integer identity with positive denominator
integers proves that the two adjacent difference numerators add to the outer
difference numerator after scaling to the common triple denominator.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-difference-numerator
  ( a : MariciInt)
  ( d : MariciNat)
  ( b : MariciInt)
  ( e : MariciNat)
  : MariciInt
  := marici-int-add
      (marici-scale-by-positive-denominator a e)
      (marici-int-negate
        (marici-scale-by-positive-denominator b d))

#define marici-common-denominator-difference-numerators
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : marici-int-add
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator a d b e) f)
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator b e c f) d)
    =_{MariciInt}
    marici-scale-by-positive-denominator
      (marici-raw-difference-numerator a d c f) e
  := marici-int-three-scale-difference-identity
      a b c
      (marici-int-positive-denominator d)
      (marici-int-positive-denominator e)
      (marici-int-positive-denominator f)
```

## Boundary

The three difference numerators are aligned and compose exactly at the common
triple denominator. The raw denominator predecessor paths and absolute-value
order bound remain to assemble the rational triangle inequality.
