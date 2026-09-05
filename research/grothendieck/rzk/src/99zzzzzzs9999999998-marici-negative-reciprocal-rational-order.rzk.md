# Rational negative reciprocal is bounded by canonical zero

Reciprocal simplification and negation congruence identify rational negation
with normalization of the raw negative unit fraction. Normalized raw zero has
the canonical rational-zero components, so endpoint transport yields the
rational inequality.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-negative-reciprocal-components
  ( k : MariciNat)
  : marici-rational-forget
      (marici-rational-negate
        (marici-rational-positive-reciprocal-power k marici-one))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-fraction-negate
          (marici-raw-reciprocal-tolerance k)))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-negate
          (marici-rational-positive-reciprocal-power k marici-one)))
      (marici-rational-forget
        (marici-rational-negate
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance k))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-negate
            (marici-raw-reciprocal-tolerance k))))
      (marici-rational-negate-respects-component-equality
        (marici-rational-positive-reciprocal-power k marici-one)
        (marici-rational-from-raw (marici-raw-reciprocal-tolerance k))
        (marici-rational-reciprocal-tolerance-simplified-components k))
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-negate
              (marici-raw-reciprocal-tolerance k))))
        (marici-rational-forget
          (marici-rational-negate
            (marici-rational-from-raw
              (marici-raw-reciprocal-tolerance k))))
        (marici-rational-negation-normalization-components
          (marici-raw-reciprocal-tolerance k)))

#define marici-rational-from-raw-zero-components
  : marici-rational-forget
      (marici-rational-from-raw (marici-raw-zero-at marici-zero))
    =_{MariciRawFraction}
    marici-rational-forget marici-rational-zero
  := marici-rational-from-raw-forget-normalized (marici-raw-zero-at marici-zero)

#define marici-rational-negative-reciprocal-at-most-zero
  ( k : MariciNat)
  : MariciRationalAtMost
      (marici-rational-negate
        (marici-rational-positive-reciprocal-power k marici-one))
      marici-rational-zero
  := marici-rational-at-most-transport-right-components
      (marici-rational-negate
        (marici-rational-positive-reciprocal-power k marici-one))
      (marici-rational-from-raw (marici-raw-zero-at marici-zero))
      marici-rational-zero
      marici-rational-from-raw-zero-components
      (marici-rational-at-most-transport-left-components
        (marici-rational-from-raw
          (marici-raw-fraction-negate
            (marici-raw-reciprocal-tolerance k)))
        (marici-rational-negate
          (marici-rational-positive-reciprocal-power k marici-one))
        (marici-rational-from-raw (marici-raw-zero-at marici-zero))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-negate
              (marici-rational-positive-reciprocal-power k marici-one)))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-negate
                (marici-raw-reciprocal-tolerance k))))
          (marici-rational-negative-reciprocal-components k))
        (marici-rational-normalized-negative-reciprocal-at-most-zero k))
```

## Boundary

The negative reciprocal tolerance is now below canonical zero. Joint addition
monotonicity and the rational right-zero component law yield the required bound
from an outer reciprocal difference to its initial tolerance.
