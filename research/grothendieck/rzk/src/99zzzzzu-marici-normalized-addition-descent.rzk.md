# Normalized addition descends through presentation

Raw addition now preserves fraction equivalence, so total normalization gives
the same canonical components for any equivalent pair of input presentations.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-add-respects-equivalence
  ( p p-prime q q-prime : MariciRawFraction)
  ( p-equivalent : marici-raw-fraction-equivalent p p-prime)
  ( q-equivalent : marici-raw-fraction-equivalent q q-prime)
  : marici-normalized-raw-add p q
      =_{MariciRawFraction}
    marici-normalized-raw-add p-prime q-prime
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-add p q)
      (marici-raw-fraction-add p-prime q-prime)
      (marici-raw-fraction-add-congruent
        p p-prime q q-prime p-equivalent q-equivalent)
```

## Boundary

Normalize-after-raw addition is now presentation-independent at the canonical
component level. This supplies additive descent without claiming a quotient or
higher universal property.
