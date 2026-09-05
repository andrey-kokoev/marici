# Unit-denominator base of the Euclid bridge

The positive denominator represented by predecessor zero is one. It divides
every positive denominator directly, so the Euclid conclusion at this base
does not require cross-product equality or coprimality.

```rzk
#lang rzk-1
```

```rzk
#define marici-unit-positive-denominator-divides
  ( e : MariciNat)
  : MariciPositiveDenominatorDivides marici-zero e
  := marici-positive-denominator-divides-witness
      marici-zero e e
      (marici-mul-one-left (marici-succ e))

#define MariciSignedMagnitudeCoprimeEuclidAtUnitDenominator
  : U
  := ( a b : MariciInt)
    → ( e : MariciNat)
    → (MariciMagnitudeNonunitCommonPositiveFactor
        a marici-zero → MariciEmpty)
    → (marici-mul (marici-int-magnitude a) (marici-succ e)
        =_{MariciNat}
      marici-mul (marici-int-magnitude b) (marici-succ marici-zero))
    → MariciPositiveDenominatorDivides marici-zero e

#define marici-signed-magnitude-coprime-euclid-unit-denominator
  : MariciSignedMagnitudeCoprimeEuclidAtUnitDenominator
  := \ a b e coprime equation →
      marici-unit-positive-denominator-divides e

#define marici-reduced-cross-product-unit-denominator-divisibility
  ( a b : MariciInt)
  ( e : MariciNat)
  ( reduced : MariciRawComponentsAreReduced a marici-zero)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a marici-zero)
      (marici-raw-fraction b e))
  : MariciPositiveDenominatorDivides marici-zero e
  := marici-unit-positive-denominator-divides e
```

## Boundary

The denominator-one base of both the magnitude Euclid principle and the reduced
cross-product divisibility theorem is discharged. Any constructive induction
for the general theorem may now focus exclusively on successor denominator
predecessors, where nonunit factor structure matters.
