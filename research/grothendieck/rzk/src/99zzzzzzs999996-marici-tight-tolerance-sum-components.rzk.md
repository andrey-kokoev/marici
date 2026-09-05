# Tightened rational tolerance sum has direct raw components

The simplified-tolerance component paths replace both rational summands by
normalizations of unit raw fractions. Rational-addition flattening then
identifies their sum with direct normalization of the raw tolerance sum.

```rzk
#lang rzk-1
```

```rzk
#define marici-tight-tolerance-sum-components
  ( k : MariciNat)
  : marici-rational-forget
      (marici-rational-add
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one)
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-fraction-add
          (marici-raw-reciprocal-tolerance
            (marici-double-tolerance-index k))
          (marici-raw-reciprocal-tolerance
            (marici-double-tolerance-index k))))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-positive-reciprocal-power
            (marici-double-tolerance-index k) marici-one)
          (marici-rational-positive-reciprocal-power
            (marici-double-tolerance-index k) marici-one)))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k)))
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k)))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-add
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k))
            (marici-raw-reciprocal-tolerance
              (marici-double-tolerance-index k)))))
      (marici-rational-add-component-congruent
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one)
        (marici-rational-from-raw
          (marici-raw-reciprocal-tolerance
            (marici-double-tolerance-index k)))
        (marici-rational-positive-reciprocal-power
          (marici-double-tolerance-index k) marici-one)
        (marici-rational-from-raw
          (marici-raw-reciprocal-tolerance
            (marici-double-tolerance-index k)))
        (marici-rational-reciprocal-tolerance-simplified-components
          (marici-double-tolerance-index k))
        (marici-rational-reciprocal-tolerance-simplified-components
          (marici-double-tolerance-index k)))
      (marici-rational-add-from-raw-components
        (marici-raw-reciprocal-tolerance
          (marici-double-tolerance-index k))
        (marici-raw-reciprocal-tolerance
          (marici-double-tolerance-index k)))
```

## Boundary

The left endpoint of the reciprocal-tolerance combination bound now has the
direct raw-sum presentation. Raw equivalence and endpoint transport can finish
the rational inequality against the target tolerance.
