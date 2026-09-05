# Normalization respects raw equality

Normalization followed by projection to canonical raw components is congruent
under raw-fraction equality. Applying this to opposite subtraction transports
the exact raw identity through canonicalization.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-from-raw-respects-equality-components
  ( p q : MariciRawFraction)
  ( path : p =_{MariciRawFraction} q)
  : marici-rational-forget (marici-rational-from-raw p)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-from-raw q)
  := ap MariciRawFraction MariciRawFraction p q
      (\ raw → marici-rational-forget
        (marici-rational-from-raw raw))
      path

#define marici-rational-opposite-subtraction-normalized-components
  ( p q : MariciRational)
  : marici-rational-forget (marici-rational-subtract q p)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-fraction-negate
          (marici-raw-fraction-subtract
            (marici-rational-forget p)
            (marici-rational-forget q))))
  := marici-rational-from-raw-respects-equality-components
      (marici-raw-fraction-subtract
        (marici-rational-forget q)
        (marici-rational-forget p))
      (marici-raw-fraction-negate
        (marici-raw-fraction-subtract
          (marici-rational-forget p)
          (marici-rational-forget q)))
      (marici-raw-fraction-opposite-subtractions
        (marici-rational-forget p)
        (marici-rational-forget q))
```

## Boundary

This identifies normalized opposite raw subtractions. Comparing normalization
of raw negation with negation of an already normalized rational remains the
next coherence theorem needed for distance symmetry.
