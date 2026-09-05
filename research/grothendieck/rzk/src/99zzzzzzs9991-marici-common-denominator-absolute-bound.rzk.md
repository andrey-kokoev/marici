# Absolute bound for common-denominator difference numerators

The exact three-scale identity transports the integer absolute-value triangle
inequality from the sum of adjacent scaled difference numerators to the scaled
outer difference numerator.

```rzk
#lang rzk-1
```

```rzk
#define marici-common-denominator-difference-absolute-bound
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : MariciIntAtMost
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
  := marici-int-at-most-transport-left
      (marici-int-absolute
        (marici-int-add
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d b e) f)
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator b e c f) d)))
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
      (ap MariciInt MariciInt
        (marici-int-add
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d b e) f)
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator b e c f) d))
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d c f) e)
        marici-int-absolute
        (marici-common-denominator-difference-numerators a b c d e f))
      (marici-int-absolute-triangle
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator a d b e) f)
        (marici-scale-by-positive-denominator
          (marici-raw-difference-numerator b e c f) d))
```

## Boundary

The required integer inequality at the common triple denominator is complete.
The rational-distance triangle theorem now only needs raw-fraction denominator
transport followed by normalized-order transport.
