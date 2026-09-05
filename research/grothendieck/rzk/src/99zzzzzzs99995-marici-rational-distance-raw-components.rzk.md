# Rational distance has direct raw components

The absolute-value flattening theorem specializes to subtraction, identifying
the forgotten components of rational distance with direct normalization of the
absolute raw subtraction expression.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-distance-raw-components
  ( p q : MariciRational)
  : marici-rational-forget (marici-rational-distance p q)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-fraction-absolute
          (marici-raw-fraction-subtract
            (marici-rational-forget p)
            (marici-rational-forget q))))
  := marici-rational-absolute-from-raw-components
      (marici-raw-fraction-subtract
        (marici-rational-forget p)
        (marici-rational-forget q))
```

## Boundary

Rational distance is now identified with normalization of one raw absolute
difference. The right-hand rational sum still needs an analogous flattening
path from normalized addition to direct normalization of the raw sum.
