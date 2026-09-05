# Adjacent raw differences compose to the outer difference

Both adjacent differences are scaled to the common triple denominator. Same-
denominator addition contracts their sum, and the three-scale numerator identity
identifies it with the outer difference presentation.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-adjacent-differences-compose
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add
        (marici-raw-difference-fraction a d b e)
        (marici-raw-difference-fraction b e c f))
      (marici-raw-difference-fraction a d c f)
  := marici-raw-fraction-equivalent-trans
      (marici-raw-fraction-add
        (marici-raw-difference-fraction a d b e)
        (marici-raw-difference-fraction b e c f))
      (marici-raw-fraction
        (marici-int-add
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d b e) f)
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator b e c f) d))
        (marici-common-triple-denominator-predecessor d e f))
      (marici-raw-difference-fraction a d c f)
      (marici-raw-fraction-equivalent-trans
        (marici-raw-fraction-add
          (marici-raw-difference-fraction a d b e)
          (marici-raw-difference-fraction b e c f))
        (marici-raw-fraction-add
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-common-triple-denominator-predecessor d e f))
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)
            (marici-common-triple-denominator-predecessor d e f)))
        (marici-raw-fraction
          (marici-int-add
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d))
          (marici-common-triple-denominator-predecessor d e f))
        (marici-raw-fraction-add-congruent
          (marici-raw-difference-fraction a d b e)
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-common-triple-denominator-predecessor d e f))
          (marici-raw-difference-fraction b e c f)
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)
            (marici-common-triple-denominator-predecessor d e f))
          (marici-first-difference-common-equivalent a b d e f)
          (marici-middle-difference-common-equivalent b c d e f))
        (marici-raw-fraction-equivalent-sym
          (marici-raw-fraction
            (marici-int-add
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator a d b e) f)
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator b e c f) d))
            (marici-common-triple-denominator-predecessor d e f))
          (marici-raw-fraction-add
            (marici-raw-fraction
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator a d b e) f)
              (marici-common-triple-denominator-predecessor d e f))
            (marici-raw-fraction
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator b e c f) d)
              (marici-common-triple-denominator-predecessor d e f)))
          (marici-raw-fraction-same-denominator-sum-equivalent
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d)
            (marici-common-triple-denominator-predecessor d e f))))
      (marici-raw-fraction-equivalent-trans
        (marici-raw-fraction
          (marici-int-add
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d b e) f)
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator b e c f) d))
          (marici-common-triple-denominator-predecessor d e f))
        (marici-raw-fraction
          (marici-scale-by-positive-denominator
            (marici-raw-difference-numerator a d c f) e)
          (marici-common-triple-denominator-predecessor d e f))
        (marici-raw-difference-fraction a d c f)
        (marici-raw-fraction-path-implies-equivalent
          (marici-raw-fraction
            (marici-int-add
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator a d b e) f)
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator b e c f) d))
            (marici-common-triple-denominator-predecessor d e f))
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d c f) e)
            (marici-common-triple-denominator-predecessor d e f))
          (ap MariciInt MariciRawFraction
            (marici-int-add
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator a d b e) f)
              (marici-scale-by-positive-denominator
                (marici-raw-difference-numerator b e c f) d))
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d c f) e)
            (\ numerator → marici-raw-fraction numerator
              (marici-common-triple-denominator-predecessor d e f))
            (marici-common-denominator-difference-numerators a b c d e f)))
        (marici-raw-fraction-equivalent-sym
          (marici-raw-difference-fraction a d c f)
          (marici-raw-fraction
            (marici-scale-by-positive-denominator
              (marici-raw-difference-numerator a d c f) e)
            (marici-common-triple-denominator-predecessor d e f))
          (marici-outer-difference-common-equivalent a c d e f)))
```

## Boundary

Adjacent directed raw differences now compose by equivalence. Descending this
identity through rational normalization supplies the successor step of finite
telescoping.
