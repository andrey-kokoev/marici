# Sum of absolute differences has a common presentation

Addition congruence aligns both original absolute directed differences with
their common-denominator forms. The same-denominator sum theorem then contracts
the raw sum to one fraction with the sum of absolute numerators.

```rzk
#lang rzk-1
```

```rzk
#define marici-absolute-difference-sum-common-equivalent
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
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
  := marici-raw-fraction-equivalent-trans
      (marici-raw-fraction-add
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction a d b e))
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction b e c f)))
      (marici-raw-fraction-add
        (marici-raw-fraction-absolute
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-common-triple-denominator-predecessor d e f)))
        (marici-raw-fraction-absolute
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)
            (marici-common-triple-denominator-predecessor d e f))))
      (marici-raw-fraction
        (marici-int-add
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f))
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)))
        (marici-common-triple-denominator-predecessor d e f))
      (marici-raw-fraction-add-congruent
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction a d b e))
        (marici-raw-fraction-absolute
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-common-triple-denominator-predecessor d e f)))
        (marici-raw-fraction-absolute
          (marici-raw-difference-fraction b e c f))
        (marici-raw-fraction-absolute
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)
            (marici-common-triple-denominator-predecessor d e f)))
        (marici-first-absolute-difference-common-equivalent a b d e f)
        (marici-middle-absolute-difference-common-equivalent b c d e f))
      (marici-raw-fraction-equivalent-sym
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
          (marici-raw-fraction
            (marici-int-absolute
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator a d b e) f))
            (marici-common-triple-denominator-predecessor d e f))
          (marici-raw-fraction
            (marici-int-absolute
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator b e c f) d))
            (marici-common-triple-denominator-predecessor d e f)))
        (marici-raw-fraction-same-denominator-sum-equivalent
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f))
          (marici-int-absolute
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d))
          (marici-common-triple-denominator-predecessor d e f)))
```

## Boundary

The right side of the raw triangle inequality now has exactly the common
presentation used by the integer bound. One final order transport yields the
raw directed-distance triangle theorem.
