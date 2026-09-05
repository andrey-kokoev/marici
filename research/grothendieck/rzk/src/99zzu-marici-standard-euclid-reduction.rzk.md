# Large-magnitude canonicality reduces to standard natural Euclid

General nonunit common divisors are defined for arbitrary natural pairs.
Reducedness of a fraction with positive numerator magnitude refutes this generic
coprimality obstruction. The cross product then exhibits the denominator as a
divisor of the numerator-magnitude product.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatNonunitCommonDivisor
  ( x y : MariciNat)
  := marici-nat-nonunit-common-divisor
      ( factor-predecessor : MariciNat)
      ( divides-x : MariciNatDivides
          (marici-succ (marici-succ factor-predecessor)) x)
      ( divides-y : MariciNatDivides
          (marici-succ (marici-succ factor-predecessor)) y)

#define MariciNatAreCoprime
  ( x y : MariciNat)
  : U
  := MariciNatNonunitCommonDivisor x y → MariciEmpty

#define marici-nat-common-divisor-specializes-to-magnitude
  ( a : MariciInt)
  ( d : MariciNat)
  ( common : MariciNatNonunitCommonDivisor
      (marici-int-magnitude a) (marici-succ d))
  : MariciMagnitudeGeneralNonunitCommonDivisor a d
  := match common
      ( marici-nat-nonunit-common-divisor f divides-magnitude divides-denominator ⇒
          marici-magnitude-general-nonunit-common-divisor
            a d f divides-magnitude divides-denominator)

#define marici-reduced-positive-magnitude-is-nat-coprime
  ( a : MariciInt)
  ( d magnitude-predecessor : MariciNat)
  ( magnitude-positive : marici-int-magnitude a =_{MariciNat}
      marici-succ magnitude-predecessor)
  ( reduced : MariciRawComponentsAreReduced a d)
  : MariciNatAreCoprime (marici-int-magnitude a) (marici-succ d)
  := \ common →
      reduced
        (marici-magnitude-common-factor-gives-raw-common-factor a d
          (marici-general-common-divisor-gives-magnitude-common-factor
            a d magnitude-predecessor magnitude-positive
            (marici-nat-common-divisor-specializes-to-magnitude
              a d common)))

#define MariciNatCoprimeEuclid
  : U
  := ( x y z : MariciNat)
    → MariciNatAreCoprime x y
    → MariciNatDivides y (marici-mul x z)
    → MariciNatDivides y z

#define marici-positive-right-divides-gives-denominator-divides
  ( factor value : MariciNat)
  ( divides : MariciPositiveNatRightDivides factor value)
  : MariciPositiveDenominatorDivides factor value
  := match divides
      ( marici-positive-nat-right-divides-witness q equation ⇒
          marici-positive-denominator-divides-witness
            factor value q
            (concat MariciNat
              (marici-mul (marici-succ factor) (marici-succ q))
              (marici-mul (marici-succ q) (marici-succ factor))
              (marici-succ value)
              (marici-mul-comm (marici-succ factor) (marici-succ q))
              equation))

#define marici-large-magnitude-coprime-euclid-from-nat-euclid
  ( euclid : MariciNatCoprimeEuclid)
  : MariciLargeMagnitudeCoprimeEuclid
  := \ a b d e nonzero coprime equation residual magnitude-large →
      marici-positive-right-divides-gives-denominator-divides d e
        (marici-nat-divides-positive-value-gives-positive-right d e
          (euclid
          (marici-int-magnitude a)
          (marici-succ d)
          (marici-succ e)
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
```

## Boundary

All Marici-specific normalization structure now reduces to
`MariciNatCoprimeEuclid`: if `x` and `y` have no shared factor at least two and
`y` divides `xz`, then `y` divides `z`. Proving this standard constructive
natural theorem is the sole remaining uniqueness premise.
