# Rational distance is invariant under simultaneous negation

Subtracting two negated inputs reverses the directed subtraction. Absolute
value turns that reversal into the symmetric rational distance.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-distance-negations-components
  ( p q : MariciRational)
  : marici-rational-forget
      (marici-rational-distance
        (marici-rational-negate p)
        (marici-rational-negate q))
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-distance p q)
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-distance
          (marici-rational-negate p)
          (marici-rational-negate q)))
      (marici-rational-forget (marici-rational-distance q p))
      (marici-rational-forget (marici-rational-distance p q))
      (marici-rational-absolute-respects-component-equality
        (marici-rational-subtract
          (marici-rational-negate p)
          (marici-rational-negate q))
        (marici-rational-subtract q p)
        (marici-rational-subtract-negations-components p q))
      (marici-rational-distance-symmetric-components q p)
```

## Boundary

This proves the metric equality needed to reuse any Cauchy modulus after
pointwise rational negation. Construction of the negated Cauchy sequence and
descent to the conditional real quotient remain separate steps.
