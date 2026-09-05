# Canonical normalization of raw additive inverses

The existing raw inverse laws establish fraction equivalence rather than
component equality. Canonical normalization now reflects those laws into exact
numerator/denominator equality with normalized zero.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-zero
  : MariciRawFraction
  := marici-normalized-raw-representative
      (marici-raw-zero-at marici-zero)

#define marici-normalized-raw-add-negate-right
  ( p : MariciRawFraction)
  : marici-normalized-raw-representative
      (marici-raw-fraction-add p (marici-raw-fraction-negate p))
      =_{MariciRawFraction}
    marici-normalized-raw-zero
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-add p (marici-raw-fraction-negate p))
      (marici-raw-zero-at marici-zero)
      (marici-raw-fraction-add-negate-right-equivalent p)

#define marici-normalized-raw-add-negate-left
  ( p : MariciRawFraction)
  : marici-normalized-raw-representative
      (marici-raw-fraction-add (marici-raw-fraction-negate p) p)
      =_{MariciRawFraction}
    marici-normalized-raw-zero
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-add (marici-raw-fraction-negate p) p)
      (marici-raw-zero-at marici-zero)
      (marici-raw-fraction-add-negate-left-equivalent p)
```

## Boundary

Normalize-after-raw addition has exact left and right inverse component laws
for every raw presentation. This does not yet prove general additive
congruence or associativity of rational normal forms; those require global
integer distributivity through cross multiplication.
