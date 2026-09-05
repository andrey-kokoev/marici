# Scaled directed differences share one denominator

Transporting the denominator predecessor paths lifts the second adjacent and
outer scaled differences to raw fractions over the same triple denominator as
the first adjacent difference.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-denominator-path
  ( numerator : MariciInt)
  ( d e : MariciNat)
  ( path : d =_{MariciNat} e)
  : marici-raw-fraction numerator d
    =_{MariciRawFraction}
    marici-raw-fraction numerator e
  := ap MariciNat MariciRawFraction d e
      (\ denominator → marici-raw-fraction numerator denominator) path

#define marici-middle-difference-common-denominator
  ( b c : MariciInt)
  ( d e f : MariciNat)
  : marici-scaled-raw-difference-fraction b e c f d
    =_{MariciRawFraction}
    marici-raw-fraction
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator b e c f) d)
      (marici-common-triple-denominator-predecessor d e f)
  := marici-raw-fraction-denominator-path
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator b e c f) d)
      (marici-positive-product-predecessor
        (marici-positive-product-predecessor e f) d)
      (marici-common-triple-denominator-predecessor d e f)
      (marici-triple-denominator-middle-first d e f)

#define marici-outer-difference-common-denominator
  ( a c : MariciInt)
  ( d e f : MariciNat)
  : marici-scaled-raw-difference-fraction a d c f e
    =_{MariciRawFraction}
    marici-raw-fraction
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator a d c f) e)
      (marici-common-triple-denominator-predecessor d e f)
  := marici-raw-fraction-denominator-path
      (marici-scale-by-positive-denominator
        (marici-raw-difference-numerator a d c f) e)
      (marici-positive-product-predecessor
        (marici-positive-product-predecessor d f) e)
      (marici-common-triple-denominator-predecessor d e f)
      (marici-triple-denominator-outer-first d e f)
```

## Boundary

All three scaled directed differences now have paths to presentations over one
triple denominator. The remaining raw triangle step converts the integer
absolute bound into raw-fraction order and transports it back through these
paths and scaling equivalences.
