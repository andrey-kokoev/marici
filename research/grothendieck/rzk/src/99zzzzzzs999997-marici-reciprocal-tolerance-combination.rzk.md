# Two tightened reciprocal tolerances fit one target tolerance

Raw equivalence turns the summed tightened presentation into an order witness.
After normalization, component transport replaces its endpoints by the actual
rational tolerance sum and target tolerance.

```rzk
#lang rzk-1
```

```rzk
#define marici-reciprocal-tolerance-combination
  ( k : MariciNat)
  : MariciRationalAtMost
      (marici-rational-add
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one)
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one))
      (marici-rational-positive-reciprocal-power k marici-one)
  := marici-rational-at-most-transport-right-components
      (marici-rational-add
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one)
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one))
      (marici-rational-from-raw (marici-raw-reciprocal-tolerance k))
      (marici-rational-positive-reciprocal-power k marici-one)
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-positive-reciprocal-power k marici-one))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance k)))
        (marici-rational-reciprocal-tolerance-simplified-components k))
      (marici-rational-at-most-transport-left-components
        (marici-rational-from-raw
          (marici-raw-fraction-add
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k))
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k))))
        (marici-rational-add
          (marici-rational-positive-reciprocal-power
            (marici-double-tolerance-index k) marici-one)
          (marici-rational-positive-reciprocal-power
            (marici-double-tolerance-index k) marici-one))
        (marici-rational-from-raw (marici-raw-reciprocal-tolerance k))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-add
              (marici-rational-positive-reciprocal-power
                (marici-double-tolerance-index k) marici-one)
              (marici-rational-positive-reciprocal-power
                (marici-double-tolerance-index k) marici-one)))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-fraction-add
                (marici-raw-reciprocal-tolerance
                  (marici-double-tolerance-index k))
                (marici-raw-reciprocal-tolerance
                  (marici-double-tolerance-index k)))))
          (marici-tight-tolerance-sum-components k))
        (marici-raw-at-most-to-rational-at-most
          (marici-raw-fraction-add
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k))
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k)))
          (marici-raw-reciprocal-tolerance k)
          (marici-raw-fraction-equivalent-implies-at-most
            (marici-raw-fraction-add
              (marici-raw-reciprocal-tolerance
                (marici-double-tolerance-index k))
              (marici-raw-reciprocal-tolerance
                (marici-double-tolerance-index k)))
            (marici-raw-reciprocal-tolerance k)
            (marici-two-tight-tolerances-raw-equivalent k))))
```

## Boundary

The exact tolerance-combination inequality required by Cauchy-equivalence
transitivity is proved. The remaining step combines two sequence moduli at the
tightened index and composes their bounds through rational distance triangle
and rational-order transitivity.
