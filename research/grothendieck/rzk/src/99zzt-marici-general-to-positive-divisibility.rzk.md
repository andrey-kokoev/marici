# General divisibility recovers positive cofactors on positive values

A general factorization of a successor value cannot have zero cofactor. Splitting
the cofactor therefore either contradicts zero--successor disjointness or
recovers the positive-divisibility witness used by normalization.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-divides-positive-value-gives-positive-right
  ( factor value : MariciNat)
  ( divides : MariciNatDivides
      (marici-succ factor) (marici-succ value))
  : MariciPositiveNatRightDivides factor value
  := match divides
      ( marici-nat-divides-witness q equation ⇒
        (match q into
          (\ q-prime →
            (marici-mul q-prime (marici-succ factor)
              =_{MariciNat} marici-succ value)
            → MariciPositiveNatRightDivides factor value)
          ( marici-zero ⇒ \ equation-prime →
              marici-empty-elim
                (MariciPositiveNatRightDivides factor value)
                (marici-zero-not-succ value equation-prime)
          | marici-succ r induction ⇒ \ equation-prime →
              marici-positive-nat-right-divides-witness
                factor value r equation-prime)) equation)

#define marici-nat-divides-reindex-value
  ( divisor x y : MariciNat)
  ( path : x =_{MariciNat} y)
  ( divides : MariciNatDivides divisor x)
  : MariciNatDivides divisor y
  := match divides
      ( marici-nat-divides-witness q equation ⇒
          marici-nat-divides-witness divisor y q
            (concat MariciNat
              (marici-mul q divisor) x y equation path))

#data MariciMagnitudeGeneralNonunitCommonDivisor
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  := marici-magnitude-general-nonunit-common-divisor
      ( factor-predecessor : MariciNat)
      ( divides-magnitude : MariciNatDivides
          (marici-succ (marici-succ factor-predecessor))
          (marici-int-magnitude numerator))
      ( divides-denominator : MariciNatDivides
          (marici-succ (marici-succ factor-predecessor))
          (marici-succ denominator-predecessor))

#define marici-general-common-divisor-gives-magnitude-common-factor
  ( a : MariciInt)
  ( d magnitude-predecessor : MariciNat)
  ( magnitude-positive : marici-int-magnitude a =_{MariciNat}
      marici-succ magnitude-predecessor)
  ( common : MariciMagnitudeGeneralNonunitCommonDivisor a d)
  : MariciMagnitudeNonunitCommonPositiveFactor a d
  := match common
      ( marici-magnitude-general-nonunit-common-divisor
          f divides-magnitude divides-denominator ⇒
        match (marici-nat-divides-positive-value-gives-positive-right
          (marici-succ f) magnitude-predecessor
          (marici-nat-divides-reindex-value
            (marici-succ (marici-succ f))
            (marici-int-magnitude a)
            (marici-succ magnitude-predecessor)
            magnitude-positive divides-magnitude))
          ( marici-positive-nat-right-divides-witness q equation-magnitude ⇒
            match (marici-nat-divides-positive-value-gives-positive-right
              (marici-succ f) d divides-denominator)
              ( marici-positive-nat-right-divides-witness r equation-denominator ⇒
                marici-magnitude-nonunit-common-positive-factor
                  a d f q r
                  (concat MariciNat
                    (marici-mul (marici-succ q)
                      (marici-succ (marici-succ f)))
                    (marici-succ magnitude-predecessor)
                    (marici-int-magnitude a)
                    equation-magnitude
                    (rev MariciNat
                      (marici-int-magnitude a)
                      (marici-succ magnitude-predecessor)
                      magnitude-positive))
                  equation-denominator)))
```

## Boundary

For positive numerator magnitude, reducedness now excludes nonunit common
divisors expressed in the general zero-capable divisibility calculus. This is
the coprimality formulation needed by standard Euclid arguments rather than the
normalization search's positive-cofactor encoding.
