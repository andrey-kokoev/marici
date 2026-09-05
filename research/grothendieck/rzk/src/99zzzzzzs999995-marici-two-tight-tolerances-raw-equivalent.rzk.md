# Two tightened raw tolerances combine to the target

The sum of two unit-numerator fractions at the tightened denominator first
contracts to a numerator-two fraction. The doubled reciprocal equivalence then
identifies that fraction with the target tolerance.

```rzk
#lang rzk-1
```

```rzk
#define marici-two-tight-tolerances-raw-equivalent
  ( k : MariciNat)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add
        (marici-raw-reciprocal-tolerance
          (marici-double-tolerance-index k))
        (marici-raw-reciprocal-tolerance
          (marici-double-tolerance-index k)))
      (marici-raw-reciprocal-tolerance k)
  := marici-raw-fraction-equivalent-trans
      (marici-raw-fraction-add
        (marici-raw-reciprocal-tolerance
          (marici-double-tolerance-index k))
        (marici-raw-reciprocal-tolerance
          (marici-double-tolerance-index k)))
      (marici-raw-fraction
        (marici-int-add marici-int-one marici-int-one)
        (marici-double-tolerance-index k))
      (marici-raw-reciprocal-tolerance k)
      (marici-raw-fraction-equivalent-sym
        (marici-raw-fraction
          (marici-int-add marici-int-one marici-int-one)
          (marici-double-tolerance-index k))
        (marici-raw-fraction-add
          (marici-raw-reciprocal-tolerance
            (marici-double-tolerance-index k))
          (marici-raw-reciprocal-tolerance
            (marici-double-tolerance-index k)))
        (marici-raw-fraction-same-denominator-sum-equivalent
          marici-int-one marici-int-one
          (marici-double-tolerance-index k)))
      (marici-doubled-reciprocal-raw-equivalent k)
```

## Boundary

The exact raw combination equivalence is complete. Its normalization now gives
the rational bound needed to combine two triangle-inequality summands at the
tightened Cauchy-equivalence modulus.
