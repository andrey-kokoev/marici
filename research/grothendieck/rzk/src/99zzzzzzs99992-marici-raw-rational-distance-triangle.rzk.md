# Raw rational distance satisfies the triangle inequality

The common-denominator absolute bound transports at both endpoints: the outer
absolute difference returns to its original presentation, and the contracted
sum returns to the raw sum of the two original absolute differences.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-rational-distance-triangle
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : MariciRawFractionAtMost
      (marici-raw-fraction-absolute
        (marici-raw-difference-fraction a d c f))
      (marici-raw-fraction-add
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction a d b e))
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction b e c f)))
  := marici-raw-fraction-at-most-respects-equivalence
      (marici-raw-fraction-absolute
        (marici-raw-fraction
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d c f) e)
          (marici-common-triple-denominator-predecessor d e f)))
      (marici-raw-fraction-absolute
        (marici-raw-difference-fraction a d c f))
      (marici-raw-fraction
        (marici-int-add
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f))
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)))
        (marici-common-triple-denominator-predecessor d e f))
      (marici-raw-fraction-add
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction a d b e))
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction b e c f)))
      (marici-raw-fraction-equivalent-sym
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction a d c f))
        (marici-raw-fraction-absolute
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d c f) e)
            (marici-common-triple-denominator-predecessor d e f)))
        (marici-outer-absolute-difference-common-equivalent a c d e f))
      (marici-raw-fraction-equivalent-sym
        (marici-raw-fraction-add
          (marici-raw-fraction-absolute
            (marici-raw-difference-fraction a d b e))
          (marici-raw-fraction-absolute
            (marici-raw-difference-fraction b e c f)))
        (marici-raw-fraction
          (marici-int-add
            (marici-int-absolute
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator a d b e) f))
            (marici-int-absolute
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator b e c f) d)))
          (marici-common-triple-denominator-predecessor d e f))
        (marici-absolute-difference-sum-common-equivalent a b c d e f))
      (marici-common-denominator-raw-absolute-bound a b c d e f)
```

## Boundary

The raw directed-distance triangle inequality is proved for arbitrary integer
numerators and positive denominator predecessors. Lifting it to normalized
rationals requires identifying rational subtraction, absolute value, and
addition with these raw expressions under normalization.
