# Directed differences are equivalent to common-denominator presentations

A path of raw fractions induces raw equivalence. Composing this with positive
scaling packages each directed difference as equivalent to any path-aligned
common-denominator presentation.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-path-implies-equivalent
  ( p q : MariciRawFraction)
  ( path : p =_{MariciRawFraction} q)
  : marici-raw-fraction-equivalent p q
  := idJ
      ( MariciRawFraction , p
      , \ target equality → marici-raw-fraction-equivalent p target
      , marici-raw-fraction-equivalent-refl p
      , q , path)

#define marici-raw-difference-common-equivalent
  ( a : MariciInt)
  ( d : MariciNat)
  ( b : MariciInt)
  ( e scale : MariciNat)
  ( common : MariciRawFraction)
  ( common-path :
      marici-scaled-raw-difference-fraction a d b e scale
      =_{MariciRawFraction} common)
  : marici-raw-fraction-equivalent
      (marici-raw-difference-fraction a d b e) common
  := marici-raw-fraction-equivalent-trans
      (marici-raw-difference-fraction a d b e)
      (marici-scaled-raw-difference-fraction a d b e scale)
      common
      (marici-raw-difference-fraction-scale-equivalent a d b e scale)
      (marici-raw-fraction-path-implies-equivalent
        (marici-scaled-raw-difference-fraction a d b e scale)
        common common-path)

#define marici-middle-difference-common-equivalent
  ( b c : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-difference-fraction b e c f)
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator b e c f) d)
        (marici-common-triple-denominator-predecessor d e f))
  := marici-raw-difference-common-equivalent
      b e c f d
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator b e c f) d)
        (marici-common-triple-denominator-predecessor d e f))
      (marici-middle-difference-common-denominator b c d e f)

#define marici-outer-difference-common-equivalent
  ( a c : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-difference-fraction a d c f)
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d c f) e)
        (marici-common-triple-denominator-predecessor d e f))
  := marici-raw-difference-common-equivalent
      a d c f e
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d c f) e)
        (marici-common-triple-denominator-predecessor d e f))
      (marici-outer-difference-common-denominator a c d e f)
```

## Boundary

The middle and outer differences now transport to the chosen common denominator
by raw equivalence. The first adjacent difference already scales directly to
that denominator; its analogous specialization and absolute/addition congruence
remain for the final raw triangle theorem.
