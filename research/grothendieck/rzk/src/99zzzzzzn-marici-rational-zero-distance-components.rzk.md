# Rational self-distance has zero canonical components

Absolute value fixes normalized zero. Combining this with self-subtraction and
absolute-value component congruence identifies every self-distance with zero at
the canonical-component level.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-absolute-zero-components
  : marici-rational-forget
      (marici-rational-absolute marici-rational-zero)
    =_{MariciRawFraction}
    marici-rational-forget marici-rational-zero
  := refl

#define marici-rational-distance-self-components
  ( q : MariciRational)
  : marici-rational-forget (marici-rational-distance q q)
    =_{MariciRawFraction}
    marici-rational-forget marici-rational-zero
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-distance q q))
      (marici-rational-forget
        (marici-rational-absolute marici-rational-zero))
      (marici-rational-forget marici-rational-zero)
      (marici-rational-absolute-respects-component-equality
        (marici-rational-subtract q q)
        marici-rational-zero
        (marici-rational-subtract-self-components q))
      marici-rational-absolute-zero-components
```

## Boundary

This proves zero self-distance for canonical raw components. Metric symmetry and
the triangle inequality remain open.
