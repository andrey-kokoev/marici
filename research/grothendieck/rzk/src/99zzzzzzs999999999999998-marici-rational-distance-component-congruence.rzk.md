# Rational distance respects component equality

Subtraction respects component equality in both inputs, and rational absolute
value preserves component equality. Their composition makes rational distance
well behaved under replacement by canonically equal rational presentations.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-distance-respects-component-equality
  ( p p-prime q q-prime : MariciRational)
  ( p-components : marici-rational-forget p
    =_{MariciRawFraction} marici-rational-forget p-prime)
  ( q-components : marici-rational-forget q
    =_{MariciRawFraction} marici-rational-forget q-prime)
  : marici-rational-forget (marici-rational-distance p q)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-distance p-prime q-prime)
  := marici-rational-absolute-respects-component-equality
      (marici-rational-subtract p q)
      (marici-rational-subtract p-prime q-prime)
      (marici-rational-subtract-component-congruent
        p p-prime q q-prime p-components q-components)

#define marici-rational-distance-left-component-congruence
  ( p p-prime q : MariciRational)
  ( p-components : marici-rational-forget p
    =_{MariciRawFraction} marici-rational-forget p-prime)
  : marici-rational-forget (marici-rational-distance p q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-distance p-prime q)
  := marici-rational-distance-respects-component-equality
      p p-prime q q p-components refl

#define marici-rational-distance-right-component-congruence
  ( p q q-prime : MariciRational)
  ( q-components : marici-rational-forget q
    =_{MariciRawFraction} marici-rational-forget q-prime)
  : marici-rational-forget (marici-rational-distance p q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-distance p q-prime)
  := marici-rational-distance-respects-component-equality
      p p q q-prime refl q-components
```

## Boundary

Distance now transports across canonical component equality in either input.
This enables the double-negation representative to be compared with the
original Cauchy sequence without asserting identity of rational records.
