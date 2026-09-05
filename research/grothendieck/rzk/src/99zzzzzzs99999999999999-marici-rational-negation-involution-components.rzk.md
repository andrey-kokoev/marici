# Rational negation is componentwise involutive

Normalization retraction moves an arbitrary rational to its forgotten raw
presentation. Negation congruence and normalization expose two raw negations,
whose involutive path transports back to the original canonical components.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-negate-involutive-components
  ( p : MariciRational)
  : marici-rational-forget
      (marici-rational-negate (marici-rational-negate p))
    =_{MariciRawFraction}
    marici-rational-forget p
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-negate (marici-rational-negate p)))
      (marici-rational-forget
        (marici-rational-negate
          (marici-rational-negate
            (marici-rational-from-raw (marici-rational-forget p)))))
      (marici-rational-forget p)
      (marici-rational-negate-respects-component-equality
        (marici-rational-negate p)
        (marici-rational-negate
          (marici-rational-from-raw (marici-rational-forget p)))
        (marici-rational-negate-respects-component-equality
          p (marici-rational-from-raw (marici-rational-forget p))
          (marici-rational-to-normalized-forget-components p)))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-negate
            (marici-rational-negate
              (marici-rational-from-raw (marici-rational-forget p)))))
        (marici-rational-forget
          (marici-rational-negate
            (marici-rational-from-raw
              (marici-raw-fraction-negate (marici-rational-forget p)))))
        (marici-rational-forget p)
        (marici-rational-negate-respects-component-equality
          (marici-rational-negate
            (marici-rational-from-raw (marici-rational-forget p)))
          (marici-rational-from-raw
            (marici-raw-fraction-negate (marici-rational-forget p)))
          (rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw
                (marici-raw-fraction-negate (marici-rational-forget p))))
            (marici-rational-forget
              (marici-rational-negate
                (marici-rational-from-raw (marici-rational-forget p))))
            (marici-rational-negation-normalization-components
              (marici-rational-forget p))))
        (concat MariciRawFraction
          (marici-rational-forget
            (marici-rational-negate
              (marici-rational-from-raw
                (marici-raw-fraction-negate (marici-rational-forget p)))))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-negate
                (marici-raw-fraction-negate
                  (marici-rational-forget p)))))
          (marici-rational-forget p)
          (rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw
                (marici-raw-fraction-negate
                  (marici-raw-fraction-negate
                    (marici-rational-forget p)))))
            (marici-rational-forget
              (marici-rational-negate
                (marici-rational-from-raw
                  (marici-raw-fraction-negate
                    (marici-rational-forget p)))))
            (marici-rational-negation-normalization-components
              (marici-raw-fraction-negate (marici-rational-forget p))))
          (concat MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw
                (marici-raw-fraction-negate
                  (marici-raw-fraction-negate
                    (marici-rational-forget p)))))
            (marici-rational-forget
              (marici-rational-from-raw (marici-rational-forget p)))
            (marici-rational-forget p)
            (ap MariciRawFraction MariciRawFraction
              (marici-raw-fraction-negate
                (marici-raw-fraction-negate (marici-rational-forget p)))
              (marici-rational-forget p)
              (\ raw → marici-rational-forget
                (marici-rational-from-raw raw))
              (marici-raw-fraction-negate-involutive
                (marici-rational-forget p)))
            (marici-rational-normalization-retraction-components p))))
```

## Boundary

Rational negation is now involutive at canonical components. Together with
componentwise addition commutativity and absolute-negation invariance, this
supplies simultaneous-negation invariance of rational distance and hence
pointwise negation of rational Cauchy sequences.
