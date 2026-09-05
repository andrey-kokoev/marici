# Rational self-subtraction has zero canonical components

Subtraction normalizes the raw sum with raw negation directly. A fusion path
between the reduced-representative accessor and its raw projection connects it
to the existing canonical additive-inverse theorem.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalization-representative-forget
  ( p : MariciRawFraction)
  ( normalization : MariciRawFractionNormalization p)
  : marici-reduced-raw-fraction-forget
      (marici-normalization-representative p normalization)
    =_{MariciRawFraction}
    marici-normalization-forget-representative p normalization
  := match normalization
      ( marici-raw-fraction-normalization representative preserves ⇒ refl)

#define marici-rational-subtract-self-components
  ( q : MariciRational)
  : marici-rational-forget (marici-rational-subtract q q)
    =_{MariciRawFraction}
    marici-rational-forget marici-rational-zero
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-subtract q q))
      (marici-normalized-raw-representative
        (marici-raw-fraction-add
          (marici-rational-forget q)
          (marici-raw-fraction-negate (marici-rational-forget q))))
      (marici-rational-forget marici-rational-zero)
      (marici-normalization-representative-forget
        (marici-raw-fraction-add
          (marici-rational-forget q)
          (marici-raw-fraction-negate (marici-rational-forget q)))
        (marici-normalize-raw-fraction
          (marici-raw-fraction-add
            (marici-rational-forget q)
            (marici-raw-fraction-negate (marici-rational-forget q)))))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-add
            (marici-rational-forget q)
            (marici-raw-fraction-negate (marici-rational-forget q))))
        marici-normalized-raw-zero
        (marici-rational-forget marici-rational-zero)
        (marici-normalized-raw-add-negate-right
          (marici-rational-forget q))
        (rev MariciRawFraction
          (marici-rational-forget marici-rational-zero)
          marici-normalized-raw-zero
          (marici-normalization-representative-forget
            (marici-raw-zero-at marici-zero)
            (marici-normalize-raw-fraction
              (marici-raw-zero-at marici-zero)))))
```

## Boundary

This proves equality of canonical raw components, the equality observed by
rational order. It does not identify reducedness proofs.
