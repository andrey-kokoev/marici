# Rational absolute value is invariant under negation

Accessor fusion, normalization preservation, absolute-value descent, and raw
negation invariance identify the canonical components of absolute values before
and after rational negation.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-absolute-negate-components
  ( q : MariciRational)
  : marici-rational-forget
      (marici-rational-absolute (marici-rational-negate q))
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-absolute q)
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-absolute (marici-rational-negate q)))
      (marici-normalized-raw-representative
        (marici-raw-fraction-absolute
          (marici-rational-forget (marici-rational-negate q))))
      (marici-rational-forget (marici-rational-absolute q))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-absolute
          (marici-rational-forget (marici-rational-negate q))))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-absolute
            (marici-rational-forget (marici-rational-negate q))))
        (marici-normalized-raw-representative
          (marici-raw-fraction-absolute
            (marici-normalized-raw-representative
              (marici-raw-fraction-negate
                (marici-rational-forget q)))))
        (marici-rational-forget (marici-rational-absolute q))
        (ap MariciRawFraction MariciRawFraction
          (marici-rational-forget (marici-rational-negate q))
          (marici-normalized-raw-representative
            (marici-raw-fraction-negate
              (marici-rational-forget q)))
          (\ raw → marici-normalized-raw-representative
            (marici-raw-fraction-absolute raw))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-negate
              (marici-rational-forget q))))
        (concat MariciRawFraction
          (marici-normalized-raw-representative
            (marici-raw-fraction-absolute
              (marici-normalized-raw-representative
                (marici-raw-fraction-negate
                  (marici-rational-forget q)))))
          (marici-normalized-raw-representative
            (marici-raw-fraction-absolute
              (marici-raw-fraction-negate
                (marici-rational-forget q))))
          (marici-rational-forget (marici-rational-absolute q))
          (marici-normalized-raw-absolute-respects-equivalence
            (marici-normalized-raw-representative
              (marici-raw-fraction-negate
                (marici-rational-forget q)))
            (marici-raw-fraction-negate (marici-rational-forget q))
            (marici-raw-fraction-equivalent-sym
              (marici-raw-fraction-negate (marici-rational-forget q))
              (marici-normalized-raw-representative
                (marici-raw-fraction-negate
                  (marici-rational-forget q)))
              (marici-normalized-raw-representative-preserves-equivalence
                (marici-raw-fraction-negate
                  (marici-rational-forget q)))))
          (concat MariciRawFraction
            (marici-normalized-raw-representative
              (marici-raw-fraction-absolute
                (marici-raw-fraction-negate
                  (marici-rational-forget q))))
            (marici-normalized-raw-representative
              (marici-raw-fraction-absolute
                (marici-rational-forget q)))
            (marici-rational-forget (marici-rational-absolute q))
            (marici-normalized-raw-absolute-negate
              (marici-rational-forget q))
            (rev MariciRawFraction
              (marici-rational-forget (marici-rational-absolute q))
              (marici-normalized-raw-representative
                (marici-raw-fraction-absolute
                  (marici-rational-forget q)))
              (marici-rational-from-raw-forget-normalized
                (marici-raw-fraction-absolute
                  (marici-rational-forget q)))))))
```

## Boundary

Rational absolute value is componentwise invariant under negation. This is the
last local lemma needed to compose the distance-symmetry proof.
