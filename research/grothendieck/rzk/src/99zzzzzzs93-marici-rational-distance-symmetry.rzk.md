# Rational distance is symmetric

Opposite-subtraction normalization identifies one directed subtraction with
the negation of the other. Absolute-value congruence and negation invariance
then identify the two distances at canonical components.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-subtraction-swap-components
  ( p q : MariciRational)
  : marici-rational-forget (marici-rational-subtract p q)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-negate (marici-rational-subtract q p))
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-subtract p q))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-negate
            (marici-raw-fraction-subtract
              (marici-rational-forget q)
              (marici-rational-forget p)))))
      (marici-rational-forget
        (marici-rational-negate (marici-rational-subtract q p)))
      (marici-rational-opposite-subtraction-normalized-components q p)
      (marici-rational-negation-normalization-components
        (marici-raw-fraction-subtract
          (marici-rational-forget q)
          (marici-rational-forget p)))

#define marici-rational-distance-symmetric-components
  ( p q : MariciRational)
  : marici-rational-forget (marici-rational-distance p q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-distance q p)
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-distance p q))
      (marici-rational-forget
        (marici-rational-absolute
          (marici-rational-negate (marici-rational-subtract q p))))
      (marici-rational-forget (marici-rational-distance q p))
      (marici-rational-absolute-respects-component-equality
        (marici-rational-subtract p q)
        (marici-rational-negate (marici-rational-subtract q p))
        (marici-rational-subtraction-swap-components p q))
      (marici-rational-absolute-negate-components
        (marici-rational-subtract q p))
```

## Boundary

Rational distance is symmetric at the canonical-component equality observed by
order and Cauchy predicates. The triangle inequality remains open.
