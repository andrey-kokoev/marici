# Positive divisibility antisymmetry reduces to order antisymmetry

A positive factorization bounds its divisor predecessor by the dividend
predecessor. Therefore mutual positive divisibility gives both natural-number
bounds, and ordinary antisymmetry suffices.

```rzk
#lang rzk-1
```

```rzk
#define MariciNatAtMostAntisymmetry
  : U
  := ( d e : MariciNat)
    → MariciNatAtMost d e
    → MariciNatAtMost e d
    → d =_{MariciNat} e

#define marici-positive-denominator-divisibility-antisymmetry-from-at-most
  ( antisymmetry : MariciNatAtMostAntisymmetry)
  : MariciPositiveDenominatorDivisibilityAntisymmetry
  := \ d e divides-de divides-ed → match divides-de
      ( marici-positive-denominator-divides-witness q equation-de ⇒
        match divides-ed
          ( marici-positive-denominator-divides-witness r equation-ed ⇒
            antisymmetry d e
              (marici-positive-cofactor-at-most-target d q e equation-de)
              (marici-positive-cofactor-at-most-target e r d equation-ed)))

#define marici-reduced-representative-uniqueness-from-euclid-and-order
  ( euclid : MariciReducedCrossProductDenominatorDivisibility)
  ( antisymmetry : MariciNatAtMostAntisymmetry)
  : MariciReducedRepresentativeUniqueness
  := marici-reduced-representative-uniqueness-from-divisibility
      euclid
      (marici-positive-denominator-divisibility-antisymmetry-from-at-most
        antisymmetry)
```

## Boundary

The mutual-divisibility branch contains no additional number theory: it is a
consequence of the already checked positive-factor bound plus natural-order
antisymmetry. The residuals are now natural-order antisymmetry and the coprime
Euclid bridge; only the latter depends on reducedness.
