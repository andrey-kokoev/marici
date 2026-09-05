# Normalized rational order respects raw equivalence

Order evaluated on canonical normalized representatives transports across raw
fraction equivalence at either endpoint. This isolates normalization transport
needed by rational metric inequalities.

```rzk
#lang rzk-1
```

```rzk
#define MariciNormalizedRawFractionAtMost
  ( p q : MariciRawFraction)
  : U
  := MariciRawFractionAtMost
      (marici-normalized-raw-representative p)
      (marici-normalized-raw-representative q)

#define marici-normalized-raw-at-most-respects-equivalence
  ( p p-prime q q-prime : MariciRawFraction)
  ( left-equivalent : marici-raw-fraction-equivalent p p-prime)
  ( right-equivalent : marici-raw-fraction-equivalent q q-prime)
  ( witness : MariciNormalizedRawFractionAtMost p q)
  : MariciNormalizedRawFractionAtMost p-prime q-prime
  := marici-raw-fraction-at-most-transport-right
      (marici-normalized-raw-representative p-prime)
      (marici-normalized-raw-representative q)
      (marici-normalized-raw-representative q-prime)
      (marici-normalized-raw-representatives-respect-equivalence
        q q-prime right-equivalent)
      (marici-raw-fraction-at-most-transport-left
        (marici-normalized-raw-representative p)
        (marici-normalized-raw-representative p-prime)
        (marici-normalized-raw-representative q)
        (marici-normalized-raw-representatives-respect-equivalence
          p p-prime left-equivalent)
        witness)

#define marici-normalized-raw-at-most-respects-left-equivalence
  ( p p-prime q : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent p p-prime)
  ( witness : MariciNormalizedRawFractionAtMost p q)
  : MariciNormalizedRawFractionAtMost p-prime q
  := marici-normalized-raw-at-most-respects-equivalence
      p p-prime q q equivalent
      (marici-raw-fraction-equivalent-refl q) witness

#define marici-normalized-raw-at-most-respects-right-equivalence
  ( p q q-prime : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent q q-prime)
  ( witness : MariciNormalizedRawFractionAtMost p q)
  : MariciNormalizedRawFractionAtMost p q-prime
  := marici-normalized-raw-at-most-respects-equivalence
      p p q q-prime
      (marici-raw-fraction-equivalent-refl p) equivalent witness
```

## Boundary

Canonical normalized order is invariant under raw equivalence. Establishing a
triangle inequality still requires the raw cross-denominator inequality before
this transport can be applied.
