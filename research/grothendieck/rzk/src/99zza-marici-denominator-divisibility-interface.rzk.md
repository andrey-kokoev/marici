# Denominator divisibility interface for reduced uniqueness

The coprime cross-product argument factors into two arithmetic statements.
Reducedness of the left fraction and cross-product equality force its positive
denominator to divide the right denominator. Mutual positive denominator
divisibility then forces equality of predecessor indices.

```rzk
#lang rzk-1
```

```rzk
#data MariciPositiveDenominatorDivides
  ( divisor-predecessor dividend-predecessor : MariciNat)
  := marici-positive-denominator-divides-witness
      ( quotient-predecessor : MariciNat)
      ( equation : marici-mul
          (marici-succ divisor-predecessor)
          (marici-succ quotient-predecessor)
        =_{MariciNat} marici-succ dividend-predecessor)

#define MariciReducedCrossProductDenominatorDivisibility
  : U
  := ( a b : MariciInt)
    → ( d e : MariciNat)
    → MariciRawComponentsAreReduced a d
    → marici-raw-fraction-equivalent
        (marici-raw-fraction a d)
        (marici-raw-fraction b e)
    → MariciPositiveDenominatorDivides d e

#define MariciPositiveDenominatorDivisibilityAntisymmetry
  : U
  := ( d e : MariciNat)
    → MariciPositiveDenominatorDivides d e
    → MariciPositiveDenominatorDivides e d
    → d =_{MariciNat} e
```

These two statements suffice for denominator equality. The reverse divisibility
application uses symmetry of raw-fraction equivalence and reducedness of the
right fraction.

```rzk
#define marici-equivalent-reduced-denominators-equal-from-divisibility
  ( euclid : MariciReducedCrossProductDenominatorDivisibility)
  ( antisymmetry : MariciPositiveDenominatorDivisibilityAntisymmetry)
  : MariciEquivalentReducedDenominatorsEqual
  := \ a b d e reduced-a reduced-b equivalent →
      antisymmetry d e
        (euclid a b d e reduced-a equivalent)
        (euclid b a e d reduced-b
          (marici-raw-fraction-equivalent-sym
            (marici-raw-fraction a d)
            (marici-raw-fraction b e)
            equivalent))

#define marici-reduced-representative-uniqueness-from-divisibility
  ( euclid : MariciReducedCrossProductDenominatorDivisibility)
  ( antisymmetry : MariciPositiveDenominatorDivisibilityAntisymmetry)
  : MariciReducedRepresentativeUniqueness
  := marici-reduced-representative-uniqueness-from-denominators
      (marici-equivalent-reduced-denominators-equal-from-divisibility
        euclid antisymmetry)
```

## Boundary

The general uniqueness residual is now split without hidden algebra. Positive
mutual-divisibility antisymmetry is a natural-number lemma. The substantive
coprime theorem is the Euclid interface: reducedness must force denominator
divisibility from the cross product. Neither premise is assumed as proved here.
