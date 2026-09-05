# Absolute directed differences share common presentations

The first directed difference scales definitionally to the chosen triple
denominator. Applying preservation of equivalence by raw absolute value then
aligns the absolute values of all three original differences with their common-
denominator presentations.

```rzk
#lang rzk-1
```

```rzk
#define marici-first-difference-common-equivalent
  ( a b : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-difference-fraction a d b e)
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d b e) f)
        (marici-common-triple-denominator-predecessor d e f))
  := marici-raw-difference-fraction-scale-equivalent a d b e f

#define marici-first-absolute-difference-common-equivalent
  ( a b : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-absolute
        (marici-raw-difference-fraction a d b e))
      (marici-raw-fraction-absolute
        (marici-raw-fraction
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d b e) f)
          (marici-common-triple-denominator-predecessor d e f)))
  := marici-raw-fraction-absolute-respects-equivalence
      (marici-raw-difference-fraction a d b e)
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d b e) f)
        (marici-common-triple-denominator-predecessor d e f))
      (marici-first-difference-common-equivalent a b d e f)

#define marici-middle-absolute-difference-common-equivalent
  ( b c : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-absolute
        (marici-raw-difference-fraction b e c f))
      (marici-raw-fraction-absolute
        (marici-raw-fraction
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator b e c f) d)
          (marici-common-triple-denominator-predecessor d e f)))
  := marici-raw-fraction-absolute-respects-equivalence
      (marici-raw-difference-fraction b e c f)
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator b e c f) d)
        (marici-common-triple-denominator-predecessor d e f))
      (marici-middle-difference-common-equivalent b c d e f)

#define marici-outer-absolute-difference-common-equivalent
  ( a c : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-absolute
        (marici-raw-difference-fraction a d c f))
      (marici-raw-fraction-absolute
        (marici-raw-fraction
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d c f) e)
          (marici-common-triple-denominator-predecessor d e f)))
  := marici-raw-fraction-absolute-respects-equivalence
      (marici-raw-difference-fraction a d c f)
      (marici-raw-fraction
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d c f) e)
        (marici-common-triple-denominator-predecessor d e f))
      (marici-outer-difference-common-equivalent a c d e f)
```

## Boundary

All three absolute directed differences now have explicit common-denominator
equivalences. Addition congruence and the same-denominator sum equivalence are
the remaining ingredients for the final raw triangle transport.
