# Normalization preserves numerator nonnegativity

A normalization witness contains an equivalence from its source to its reduced
representative. The checked sign-transport theorem therefore carries
nonnegativity into every normalized representative.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalization-representative-numerator-nonnegative
  ( p : MariciRawFraction)
  ( normalization : MariciRawFractionNormalization p)
  ( source-nonnegative : MariciRawFractionNumeratorIsNonnegative p)
  : MariciRawFractionNumeratorIsNonnegative
      (marici-reduced-raw-fraction-forget
        (marici-normalization-representative p normalization))
  := (match normalization into
      (\ normalization-prime →
        MariciRawFractionNumeratorIsNonnegative p
        → MariciRawFractionNumeratorIsNonnegative
          (marici-reduced-raw-fraction-forget
            (marici-normalization-representative p normalization-prime)))
      ( marici-raw-fraction-normalization representative preserves ⇒
          \ nonnegative →
            marici-raw-fraction-equivalence-preserves-nonnegative-numerator
              p (marici-reduced-raw-fraction-forget representative)
              preserves nonnegative)) source-nonnegative

#define marici-rational-from-raw-numerator-nonnegative
  ( p : MariciRawFraction)
  ( source-nonnegative : MariciRawFractionNumeratorIsNonnegative p)
  : MariciRawFractionNumeratorIsNonnegative
      (marici-rational-forget (marici-rational-from-raw p))
  := marici-normalization-representative-numerator-nonnegative
      p (marici-normalize-raw-fraction p) source-nonnegative
```

## Boundary

This proves sign preservation for normalized representatives of nonnegative
sources. It does not establish arbitrary order preservation by normalization.
