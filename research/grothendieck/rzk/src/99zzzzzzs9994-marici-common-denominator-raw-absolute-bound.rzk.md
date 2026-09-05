# Common-denominator absolute bound as raw-fraction order

Integer order lifts to raw-fraction order when both fractions have the same
positive denominator. Applying that lift to the established absolute bound
produces the raw comparison required by the rational triangle inequality.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-same-denominator-at-most
  ( x y : MariciInt)
  ( denominator-predecessor : MariciNat)
  ( witness : MariciIntAtMost x y)
  : MariciRawFractionAtMost
      (marici-raw-fraction x denominator-predecessor)
      (marici-raw-fraction y denominator-predecessor)
  := marici-int-at-most-mul-nonnegative-right
      x y
      (marici-int-positive-denominator denominator-predecessor)
      witness marici-trivial

#define marici-common-denominator-raw-absolute-bound
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : MariciRawFractionAtMost
      (marici-raw-fraction-absolute
        (marici-raw-fraction
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d c f) e)
          (marici-common-triple-denominator-predecessor d e f)))
      (marici-raw-fraction
        (marici-int-add
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f))
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)))
        (marici-common-triple-denominator-predecessor d e f))
  := marici-raw-fraction-same-denominator-at-most
      (marici-int-absolute
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d c f) e))
      (marici-int-add
        (marici-int-absolute
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d b e) f))
        (marici-int-absolute
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator b e c f) d)))
      (marici-common-triple-denominator-predecessor d e f)
      (marici-common-denominator-difference-absolute-bound a b c d e f)
```

## Boundary

The integer triangle estimate is now a raw-fraction order comparison over the
common denominator. The right-hand raw fraction must next be identified with
the sum of the two common-denominator absolute difference presentations.
