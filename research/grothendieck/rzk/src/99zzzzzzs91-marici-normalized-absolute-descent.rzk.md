# Normalized absolute value descends through equivalence

Raw equality induces cross-product equivalence, and raw absolute value preserves
that equivalence. Canonical normalization therefore gives identical components
for absolute values of equivalent presentations.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-equality-implies-equivalence
  ( p q : MariciRawFraction)
  ( path : p =_{MariciRawFraction} q)
  : marici-raw-fraction-equivalent p q
  := idJ
      ( MariciRawFraction , p
      , \ u equality → marici-raw-fraction-equivalent p u
      , marici-raw-fraction-equivalent-refl p
      , q , path)

#define marici-normalized-raw-absolute-respects-equivalence
  ( p q : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent p q)
  : marici-normalized-raw-representative
      (marici-raw-fraction-absolute p)
    =_{MariciRawFraction}
    marici-normalized-raw-representative
      (marici-raw-fraction-absolute q)
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-absolute p)
      (marici-raw-fraction-absolute q)
      (marici-raw-fraction-absolute-respects-equivalence
        p q equivalent)

#define marici-normalized-raw-absolute-negate
  ( p : MariciRawFraction)
  : marici-normalized-raw-representative
      (marici-raw-fraction-absolute
        (marici-raw-fraction-negate p))
    =_{MariciRawFraction}
    marici-normalized-raw-representative
      (marici-raw-fraction-absolute p)
  := marici-normalized-raw-representatives-respect-equivalence
      (marici-raw-fraction-absolute
        (marici-raw-fraction-negate p))
      (marici-raw-fraction-absolute p)
      (marici-raw-fraction-equality-implies-equivalence
        (marici-raw-fraction-absolute
          (marici-raw-fraction-negate p))
        (marici-raw-fraction-absolute p)
        (marici-raw-fraction-absolute-negate p))
```

## Boundary

Normalized absolute value now descends through raw equivalence. The final
`marici-normalized-raw-absolute-negate` proof uses only definitional equality of
raw absolute representatives and is intended as the immediate distance-symmetry
bridge.
