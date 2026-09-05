# Normalized multiplication descends through presentation

Raw multiplication already preserves fraction equivalence in both arguments.
The closed normalization-respects-equivalence theorem therefore identifies the
canonical components computed from any two equivalent pairs of presentations.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-multiplication
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := marici-normalized-raw-representative
      (marici-raw-fraction-mul p q)

#define marici-normalized-raw-multiplication-respects-equivalence
  ( p p-prime q q-prime : MariciRawFraction)
  ( p-equivalent : marici-raw-fraction-equivalent p p-prime)
  ( q-equivalent : marici-raw-fraction-equivalent q q-prime)
  : marici-normalized-raw-multiplication p q
      =_{MariciRawFraction}
    marici-normalized-raw-multiplication p-prime q-prime
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-mul p q)
      (marici-raw-fraction-mul p-prime q-prime)
      (marici-raw-fraction-mul-congruent
        p p-prime q q-prime p-equivalent q-equivalent)
```

## Boundary

Normalize-after-raw multiplication is now presentation-independent at the
canonical-component level. This is the multiplicative descent gate needed by
a zeta Euler-factor comparison. Addition is not included: its raw congruence
still depends on the outstanding integer distributivity and mixed-sign
addition laws.
