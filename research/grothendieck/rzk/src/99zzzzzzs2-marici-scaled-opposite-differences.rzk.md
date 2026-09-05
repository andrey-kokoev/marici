# Opposite differences after denominator scaling

Integer scaling by a positive denominator commutes with negation. The opposite-difference identity therefore applies to cross-multiplied rational numerators.

```rzk
#lang rzk-1
```

```rzk
#define marici-scale-by-positive-denominator-negate
  ( x : MariciInt)
  ( d : MariciNat)
  : marici-scale-by-positive-denominator (marici-int-negate x) d
    =_{MariciInt}
    marici-int-negate (marici-scale-by-positive-denominator x d)
  := marici-int-mul-negate-left x
      (marici-int-positive-denominator d)

#define marici-scaled-opposite-differences
  ( a b : MariciInt)
  ( d e : MariciNat)
  : marici-int-add
      (marici-scale-by-positive-denominator b d)
      (marici-scale-by-positive-denominator (marici-int-negate a) e)
    =_{MariciInt}
    marici-int-negate
      (marici-int-add
        (marici-scale-by-positive-denominator a e)
        (marici-scale-by-positive-denominator (marici-int-negate b) d))
  := concat MariciInt
      (marici-int-add
        (marici-scale-by-positive-denominator b d)
        (marici-scale-by-positive-denominator (marici-int-negate a) e))
      (marici-int-add
        (marici-scale-by-positive-denominator b d)
        (marici-int-negate
          (marici-scale-by-positive-denominator a e)))
      (marici-int-negate
        (marici-int-add
          (marici-scale-by-positive-denominator a e)
          (marici-scale-by-positive-denominator (marici-int-negate b) d)))
      (marici-int-add-congruent
        (marici-scale-by-positive-denominator b d)
        (marici-scale-by-positive-denominator b d)
        (marici-scale-by-positive-denominator (marici-int-negate a) e)
        (marici-int-negate (marici-scale-by-positive-denominator a e))
        refl (marici-scale-by-positive-denominator-negate a e))
      (concat MariciInt
        (marici-int-add
          (marici-scale-by-positive-denominator b d)
          (marici-int-negate
            (marici-scale-by-positive-denominator a e)))
        (marici-int-negate
          (marici-int-add
            (marici-scale-by-positive-denominator a e)
            (marici-int-negate
              (marici-scale-by-positive-denominator b d))))
        (marici-int-negate
          (marici-int-add
            (marici-scale-by-positive-denominator a e)
            (marici-scale-by-positive-denominator (marici-int-negate b) d)))
        (marici-int-opposite-differences
          (marici-scale-by-positive-denominator a e)
          (marici-scale-by-positive-denominator b d))
        (ap MariciInt MariciInt
          (marici-int-add
            (marici-scale-by-positive-denominator a e)
            (marici-int-negate
              (marici-scale-by-positive-denominator b d)))
          (marici-int-add
            (marici-scale-by-positive-denominator a e)
            (marici-scale-by-positive-denominator (marici-int-negate b) d))
          marici-int-negate
          (marici-int-add-congruent
            (marici-scale-by-positive-denominator a e)
            (marici-scale-by-positive-denominator a e)
            (marici-int-negate
              (marici-scale-by-positive-denominator b d))
            (marici-scale-by-positive-denominator (marici-int-negate b) d)
            refl
            (rev MariciInt
              (marici-scale-by-positive-denominator (marici-int-negate b) d)
              (marici-int-negate
                (marici-scale-by-positive-denominator b d))
              (marici-scale-by-positive-denominator-negate b d)))))
```

## Boundary

The cross-multiplied numerator identity is complete. The raw-fraction lift now only needs the existing commutativity path for positive-product denominators.
