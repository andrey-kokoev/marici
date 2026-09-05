# Rational negation commutes with raw normalization

Accessor fusion lifts normalization-negation coherence from canonical raw
representatives to packaged rationals.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-from-raw-forget-normalized
  ( p : MariciRawFraction)
  : marici-rational-forget (marici-rational-from-raw p)
    =_{MariciRawFraction}
    marici-normalized-raw-representative p
  := marici-normalization-representative-forget p
      (marici-normalize-raw-fraction p)

#define marici-rational-negation-normalization-components
  ( p : MariciRawFraction)
  : marici-rational-forget
      (marici-rational-from-raw (marici-raw-fraction-negate p))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-negate (marici-rational-from-raw p))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-from-raw (marici-raw-fraction-negate p)))
      (marici-normalized-raw-representative
        (marici-raw-fraction-negate p))
      (marici-rational-forget
        (marici-rational-negate (marici-rational-from-raw p)))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-negate p))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-negate p))
        (marici-normalized-raw-representative
          (marici-raw-fraction-negate
            (marici-normalized-raw-representative p)))
        (marici-rational-forget
          (marici-rational-negate (marici-rational-from-raw p)))
        (marici-normalized-raw-negation-coherence p)
        (concat MariciRawFraction
          (marici-normalized-raw-representative
            (marici-raw-fraction-negate
              (marici-normalized-raw-representative p)))
          (marici-normalized-raw-representative
            (marici-raw-fraction-negate
              (marici-rational-forget (marici-rational-from-raw p))))
          (marici-rational-forget
            (marici-rational-negate (marici-rational-from-raw p)))
          (ap MariciRawFraction MariciRawFraction
            (marici-normalized-raw-representative p)
            (marici-rational-forget (marici-rational-from-raw p))
            (\ raw → marici-normalized-raw-representative
              (marici-raw-fraction-negate raw))
            (rev MariciRawFraction
              (marici-rational-forget (marici-rational-from-raw p))
              (marici-normalized-raw-representative p)
              (marici-rational-from-raw-forget-normalized p)))
          (rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-negate (marici-rational-from-raw p)))
            (marici-normalized-raw-representative
              (marici-raw-fraction-negate
                (marici-rational-forget (marici-rational-from-raw p))))
            (marici-rational-from-raw-forget-normalized
              (marici-raw-fraction-negate
                (marici-rational-forget
                  (marici-rational-from-raw p)))))))
```

## Boundary

Normalization of raw negation and rational negation now agree on canonical
components. Combining this with opposite-subtraction normalization and absolute
negation invariance yields distance symmetry.
