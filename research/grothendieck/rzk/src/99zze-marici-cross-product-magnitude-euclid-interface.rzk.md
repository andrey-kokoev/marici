# Cross-product equivalence as a magnitude Euclid problem

Applying integer magnitude to raw-fraction cross-product equality and rewriting
positive products yields a natural-number product equality. Together with the
magnitude coprimality extracted from reducedness, this is the exact Euclid
problem needed for denominator divisibility.

```rzk
#lang rzk-1
```

```rzk
#define marici-equivalent-cross-product-magnitudes-equal
  ( a b : MariciInt)
  ( d e : MariciNat)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a d)
      (marici-raw-fraction b e))
  : marici-mul (marici-int-magnitude a) (marici-succ e)
      =_{MariciNat}
    marici-mul (marici-int-magnitude b) (marici-succ d)
  := concat MariciNat
      (marici-mul (marici-int-magnitude a) (marici-succ e))
      (marici-int-magnitude
        (marici-int-mul a (marici-int-positive-denominator e)))
      (marici-mul (marici-int-magnitude b) (marici-succ d))
      (rev MariciNat
        (marici-int-magnitude
          (marici-int-mul a (marici-int-positive-denominator e)))
        (marici-mul (marici-int-magnitude a) (marici-succ e))
        (marici-int-magnitude-positive-right-product a e))
      (concat MariciNat
        (marici-int-magnitude
          (marici-int-mul a (marici-int-positive-denominator e)))
        (marici-int-magnitude
          (marici-int-mul b (marici-int-positive-denominator d)))
        (marici-mul (marici-int-magnitude b) (marici-succ d))
        (ap MariciInt MariciNat
          (marici-int-mul a (marici-int-positive-denominator e))
          (marici-int-mul b (marici-int-positive-denominator d))
          marici-int-magnitude equivalent)
        (marici-int-magnitude-positive-right-product b d))

#define MariciSignedMagnitudeCoprimeEuclid
  : U
  := ( a b : MariciInt)
    → ( d e : MariciNat)
    → ((a =_{MariciInt} marici-int-zero) → MariciEmpty)
    → (MariciMagnitudeNonunitCommonPositiveFactor a d → MariciEmpty)
    → (marici-mul (marici-int-magnitude a) (marici-succ e)
        =_{MariciNat}
      marici-mul (marici-int-magnitude b) (marici-succ d))
    → MariciPositiveDenominatorDivides d e

```

## Boundary

The zero-numerator branch is handled directly: reducedness forces denominator
one. The remaining arithmetic residual is explicitly nonzero: coprimality of
`|a|` with `D`, plus `|a|E=|b|D`, must imply `D|E`. This avoids the false
natural-factor premise that zero magnitude has a positive cofactor.
