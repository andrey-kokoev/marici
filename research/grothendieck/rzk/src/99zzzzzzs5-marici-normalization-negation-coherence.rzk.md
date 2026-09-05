# Normalization and negation coherence

Normalizing a negated raw fraction gives the same canonical components as
normalizing the negation of its normalized representative.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-negation-coherence
  ( p : MariciRawFraction)
  : marici-normalized-raw-representative
      (marici-raw-fraction-negate p)
    =_{MariciRawFraction}
    marici-normalized-raw-representative
      (marici-raw-fraction-negate
        (marici-normalized-raw-representative p))
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-negate p)
      (marici-raw-fraction-negate
        (marici-normalized-raw-representative p))
      (marici-raw-fraction-equivalent-negate
        p (marici-normalized-raw-representative p)
        (marici-normalized-raw-representative-preserves-equivalence p))
```

## Boundary

This proves the normalization-negation coherence at canonical raw components.
The accessor fusion paths still have to be composed around it to obtain the
corresponding theorem for packaged rationals.
