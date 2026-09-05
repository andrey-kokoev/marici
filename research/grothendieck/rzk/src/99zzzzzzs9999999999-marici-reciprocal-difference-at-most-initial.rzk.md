# A reciprocal difference is bounded by its initial reciprocal

Addition monotonicity combines reflexivity of the initial reciprocal with the
negative-terminal-reciprocal bound. The normalized right-zero law then
transports the upper endpoint back to the initial reciprocal.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-add-zero-right-components
  ( p : MariciRational)
  : marici-rational-forget
      (marici-rational-add p marici-rational-zero)
    =_{MariciRawFraction}
    marici-rational-forget p
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add p marici-rational-zero))
      (marici-normalized-raw-add
        (marici-rational-forget p) (marici-raw-zero-at marici-zero))
      (marici-rational-forget p)
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-add
          (marici-rational-forget p) (marici-raw-zero-at marici-zero)))
      (concat MariciRawFraction
        (marici-normalized-raw-add
          (marici-rational-forget p) (marici-raw-zero-at marici-zero))
        (marici-normalized-raw-representative
          (marici-rational-forget p))
        (marici-rational-forget p)
        (marici-normalized-raw-add-zero-right
          (marici-rational-forget p))
        (concat MariciRawFraction
          (marici-normalized-raw-representative
            (marici-rational-forget p))
          (marici-rational-forget
            (marici-rational-from-raw (marici-rational-forget p)))
          (marici-rational-forget p)
          (rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw (marici-rational-forget p)))
            (marici-normalized-raw-representative
              (marici-rational-forget p))
            (marici-rational-from-raw-forget-normalized
              (marici-rational-forget p)))
          (marici-rational-normalization-retraction-components p)))

#define marici-rational-reciprocal-difference-at-most-initial
  ( initial terminal : MariciNat)
  : MariciRationalAtMost
      (marici-rational-reciprocal-difference initial terminal)
      (marici-rational-positive-reciprocal-power initial marici-one)
  := marici-rational-at-most-transport-right-components
      (marici-rational-reciprocal-difference initial terminal)
      (marici-rational-add
        (marici-rational-positive-reciprocal-power initial marici-one)
        marici-rational-zero)
      (marici-rational-positive-reciprocal-power initial marici-one)
      (marici-rational-add-zero-right-components
        (marici-rational-positive-reciprocal-power initial marici-one))
      (marici-rational-add-at-most
        (marici-rational-positive-reciprocal-power initial marici-one)
        (marici-rational-positive-reciprocal-power initial marici-one)
        (marici-rational-negate
          (marici-rational-positive-reciprocal-power terminal marici-one))
        marici-rational-zero
        (marici-rational-at-most-reflexive
          (marici-rational-positive-reciprocal-power initial marici-one))
        (marici-rational-negative-reciprocal-at-most-zero terminal))
```

## Boundary

Every outer reciprocal difference is now bounded by its initial reciprocal.
Composing this with the shifted finite-tail majorant gives the uniform bound
required by the exponent-two Cauchy proof.
