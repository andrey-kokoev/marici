# Raw additive rearrangement for translated subtraction

The additive group laws of raw fractions hold through cross-product
equivalence. They rearrange a translated difference so that the common
translation becomes an adjacent inverse pair.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-negate-plus-translate-equivalent
  ( b c : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add
        (marici-raw-fraction-negate b)
        (marici-raw-fraction-add b c))
      c
  := marici-raw-fraction-equivalent-trans
      (marici-raw-fraction-add
        (marici-raw-fraction-negate b)
        (marici-raw-fraction-add b c))
      (marici-raw-fraction-add
        (marici-raw-fraction-add (marici-raw-fraction-negate b) b) c)
      c
      (marici-raw-fraction-equivalent-sym
        (marici-raw-fraction-add
          (marici-raw-fraction-add (marici-raw-fraction-negate b) b) c)
        (marici-raw-fraction-add
          (marici-raw-fraction-negate b)
          (marici-raw-fraction-add b c))
        (marici-raw-fraction-add-assoc-equivalent
          (marici-raw-fraction-negate b) b c))
      (marici-raw-fraction-equivalent-trans
        (marici-raw-fraction-add
          (marici-raw-fraction-add (marici-raw-fraction-negate b) b) c)
        (marici-raw-fraction-add (marici-raw-zero-at marici-zero) c)
        c
        (marici-raw-fraction-add-congruent
          (marici-raw-fraction-add (marici-raw-fraction-negate b) b)
          (marici-raw-zero-at marici-zero)
          c c
          (marici-raw-fraction-add-negate-left-equivalent b)
          (marici-raw-fraction-equivalent-refl c))
        (marici-raw-fraction-path-implies-equivalent
          (marici-raw-fraction-add (marici-raw-zero-at marici-zero) c)
          c
          (marici-raw-fraction-add-zero-left c)))

#define marici-raw-translation-rearrangement
  ( a b c : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add
        (marici-raw-fraction-add b c)
        (marici-raw-fraction-subtract a b))
      (marici-raw-fraction-add a c)
  := marici-raw-fraction-equivalent-trans
      (marici-raw-fraction-add
        (marici-raw-fraction-add b c)
        (marici-raw-fraction-subtract a b))
      (marici-raw-fraction-add
        (marici-raw-fraction-subtract a b)
        (marici-raw-fraction-add b c))
      (marici-raw-fraction-add a c)
      (marici-raw-fraction-path-implies-equivalent
        (marici-raw-fraction-add
          (marici-raw-fraction-add b c)
          (marici-raw-fraction-subtract a b))
        (marici-raw-fraction-add
          (marici-raw-fraction-subtract a b)
          (marici-raw-fraction-add b c))
        (marici-raw-fraction-add-comm
          (marici-raw-fraction-add b c)
          (marici-raw-fraction-subtract a b)))
      (marici-raw-fraction-equivalent-trans
        (marici-raw-fraction-add
          (marici-raw-fraction-subtract a b)
          (marici-raw-fraction-add b c))
        (marici-raw-fraction-add a
          (marici-raw-fraction-add (marici-raw-fraction-negate b)
            (marici-raw-fraction-add b c)))
        (marici-raw-fraction-add a c)
        (marici-raw-fraction-add-assoc-equivalent
          a (marici-raw-fraction-negate b)
          (marici-raw-fraction-add b c))
        (marici-raw-fraction-add-congruent
          a a
          (marici-raw-fraction-add (marici-raw-fraction-negate b)
            (marici-raw-fraction-add b c))
          c
          (marici-raw-fraction-equivalent-refl a)
          (marici-raw-negate-plus-translate-equivalent b c)))

#define marici-raw-subtract-common-translation-equivalent
  ( a b c : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-subtract
        (marici-raw-fraction-add a c)
        (marici-raw-fraction-add b c))
      (marici-raw-fraction-subtract a b)
  := marici-raw-fraction-equivalent-trans
      (marici-raw-fraction-subtract
        (marici-raw-fraction-add a c)
        (marici-raw-fraction-add b c))
      (marici-raw-fraction-subtract
        (marici-raw-fraction-add
          (marici-raw-fraction-add b c)
          (marici-raw-fraction-subtract a b))
        (marici-raw-fraction-add b c))
      (marici-raw-fraction-subtract a b)
      (marici-raw-fraction-subtract-congruent
        (marici-raw-fraction-add a c)
        (marici-raw-fraction-add
          (marici-raw-fraction-add b c)
          (marici-raw-fraction-subtract a b))
        (marici-raw-fraction-add b c)
        (marici-raw-fraction-add b c)
        (marici-raw-fraction-equivalent-sym
          (marici-raw-fraction-add
            (marici-raw-fraction-add b c)
            (marici-raw-fraction-subtract a b))
          (marici-raw-fraction-add a c)
          (marici-raw-translation-rearrangement a b c))
        (marici-raw-fraction-equivalent-refl
          (marici-raw-fraction-add b c)))
      (marici-raw-translated-addition-cancellation
        (marici-raw-fraction-add b c)
        (marici-raw-fraction-subtract a b))
```

## Boundary

Raw subtraction is invariant, through cross-product equivalence, under adding
the same raw fraction to both endpoints. Descent through normalization and
absolute value remains required for rational-distance translation invariance.
