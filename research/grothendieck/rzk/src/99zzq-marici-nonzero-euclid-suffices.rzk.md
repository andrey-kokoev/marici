# The nonzero magnitude Euclid principle suffices

Zero numerator is separated before invoking magnitude Euclid. Reduced zero has
denominator one, which divides every positive denominator. Positive and
negative numerators provide structural nonzero evidence.

```rzk
#lang rzk-1
```

```rzk
#define marici-reduced-zero-denominator-divides
  ( d e : MariciNat)
  ( reduced : MariciRawComponentsAreReduced marici-int-zero d)
  : MariciPositiveDenominatorDivides d e
  := ind-path MariciNat marici-zero
      (\ d-prime denominator-path →
        MariciRawComponentsAreReduced marici-int-zero d-prime
        → MariciPositiveDenominatorDivides d-prime e)
      (\ reduced-prime → marici-unit-positive-denominator-divides e)
      d
      (rev MariciNat d marici-zero
        (marici-reduced-zero-denominator-is-one d reduced))
      reduced

#define marici-reduced-cross-product-denominator-divisibility-from-euclid
  ( euclid : MariciSignedMagnitudeCoprimeEuclid)
  : MariciReducedCrossProductDenominatorDivisibility
  := \ a → match a into
      (\ a-prime → (b : MariciInt) → (d e : MariciNat)
        → MariciRawComponentsAreReduced a-prime d
        → marici-raw-fraction-equivalent
            (marici-raw-fraction a-prime d)
            (marici-raw-fraction b e)
        → MariciPositiveDenominatorDivides d e)
      ( marici-int-zero ⇒ \ b d e reduced equivalent →
          marici-reduced-zero-denominator-divides d e reduced
      | marici-int-pos n ⇒ \ b d e reduced equivalent →
          euclid (marici-int-pos n) b d e
            (marici-int-pos-not-zero n)
            (marici-reduced-components-have-coprime-magnitude
              (marici-int-pos n) d reduced)
            (marici-equivalent-cross-product-magnitudes-equal
              (marici-int-pos n) b d e equivalent)
      | marici-int-neg n ⇒ \ b d e reduced equivalent →
          euclid (marici-int-neg n) b d e
            (marici-int-neg-not-zero n)
            (marici-reduced-components-have-coprime-magnitude
              (marici-int-neg n) d reduced)
            (marici-equivalent-cross-product-magnitudes-equal
              (marici-int-neg n) b d e equivalent))
```

## Boundary

The remaining Euclid premise is now correctly restricted to nonzero signed
numerators. Zero magnitude never needs a positive natural cofactor: raw
reducedness handles it directly. This repairs the earlier overstrong interface
that silently demanded an impossible zero-magnitude Euclid conclusion.
