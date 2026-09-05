# Rational addition is jointly monotone

Raw joint addition monotonicity applies to the forgotten canonical components.
Descending its result through normalization produces the corresponding order
witness between rational sums.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-add-at-most
  ( p p-prime q q-prime : MariciRational)
  ( first-witness : MariciRationalAtMost p p-prime)
  ( second-witness : MariciRationalAtMost q q-prime)
  : MariciRationalAtMost
      (marici-rational-add p q)
      (marici-rational-add p-prime q-prime)
  := marici-raw-at-most-to-rational-at-most
      (marici-raw-fraction-add
        (marici-rational-forget p) (marici-rational-forget q))
      (marici-raw-fraction-add
        (marici-rational-forget p-prime)
        (marici-rational-forget q-prime))
      (marici-raw-fraction-add-at-most
        (marici-rational-forget p)
        (marici-rational-forget p-prime)
        (marici-rational-forget q)
        (marici-rational-forget q-prime)
        first-witness second-witness)
```

## Boundary

Rational addition is jointly monotone. The Cauchy-equivalence transitivity proof
can now combine its two tightened pointwise bounds, then compose distance
triangle, addition monotonicity, and tolerance combination by rational-order
transitivity.
