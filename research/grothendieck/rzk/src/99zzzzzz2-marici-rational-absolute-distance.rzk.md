# Rational absolute value and distance

Integer sign constructors give an executable magnitude. Applying it to a
rational numerator while retaining the positive denominator defines absolute
value; distance is absolute value of the normalized difference.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-absolute
  ( p : MariciRawFraction)
  : MariciRawFraction
  := match p
      ( marici-raw-fraction numerator denominator-predecessor ⇒
          marici-raw-fraction
            (marici-int-embed-nat
              (marici-int-magnitude numerator))
            denominator-predecessor)

#define marici-rational-absolute
  ( q : MariciRational)
  : MariciRational
  := marici-rational-from-raw
      (marici-raw-fraction-absolute
        (marici-rational-forget q))

#define marici-raw-fraction-subtract
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := marici-raw-fraction-add p
      (marici-raw-fraction-negate q)

#define marici-rational-subtract
  ( p q : MariciRational)
  : MariciRational
  := marici-rational-from-raw
      (marici-raw-fraction-subtract
        (marici-rational-forget p)
        (marici-rational-forget q))

#define marici-rational-distance
  ( p q : MariciRational)
  : MariciRational
  := marici-rational-absolute
      (marici-rational-subtract p q)
```

## Boundary

This supplies the value used by a future rational metric relation. Metric laws,
order comparison, Archimedean bounds, Cauchy moduli, and completion remain to be
proved; the word distance here names the executable absolute difference, not a
completed metric-space structure.
