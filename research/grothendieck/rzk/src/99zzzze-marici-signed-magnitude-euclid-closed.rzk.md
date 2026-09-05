# Closing the signed-magnitude Euclid interface

Positive natural Euclid applies directly to the positive denominator
`d+1`. Reusing the existing magnitude and cross-product conversions closes the
large-magnitude branch; the prior unit split then supplies the complete signed
magnitude theorem required by reduced denominator divisibility.

```rzk
#lang rzk-1
```

```rzk
#define marici-large-magnitude-coprime-euclid-from-positive-nat
  : MariciLargeMagnitudeCoprimeEuclid
  := \ a b d e nonzero coprime equation residual magnitude-large →
      marici-positive-right-divides-gives-denominator-divides d e
        (marici-nat-divides-positive-value-gives-positive-right d e
          (marici-nat-positive-coprime-euclid
            (marici-int-magnitude a) d (marici-succ e)
            (\ common → coprime
              (marici-general-common-divisor-gives-magnitude-common-factor
                a d (marici-succ residual) magnitude-large
                (marici-nat-common-divisor-specializes-to-magnitude
                  a d common)))
            (marici-nat-divides-witness
              (marici-succ d)
              (marici-mul (marici-int-magnitude a) (marici-succ e))
              (marici-int-magnitude b)
              (rev MariciNat
                (marici-mul (marici-int-magnitude a) (marici-succ e))
                (marici-mul (marici-int-magnitude b) (marici-succ d))
                equation))))

#define marici-signed-magnitude-coprime-euclid
  : MariciSignedMagnitudeCoprimeEuclid
  := marici-signed-magnitude-coprime-euclid-from-large-case
      marici-large-magnitude-coprime-euclid-from-positive-nat

#define marici-reduced-cross-product-denominator-divisibility
  : MariciReducedCrossProductDenominatorDivisibility
  := marici-reduced-cross-product-denominator-divisibility-from-euclid
      marici-signed-magnitude-coprime-euclid
```

## Boundary

The formerly assumed signed-magnitude Euclid and one-way reduced denominator
divisibility interfaces now have closed constructive implementations. Reduced
representative uniqueness still requires applying this divisibility in both
directions, denominator antisymmetry, and numerator recovery from the resulting
denominator path.
