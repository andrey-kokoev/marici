# Unit-magnitude numerator case of Euclid

When the left numerator magnitude is one, the natural cross-product equality
already exhibits the left denominator as a factor of the right denominator.
The zero right-numerator branch would identify a successor with zero and is
impossible.

```rzk
#lang rzk-1
```

```rzk
#define marici-denominator-divides-from-magnitude-product
  ( b : MariciInt)
  ( d e : MariciNat)
  ( equation : marici-succ e =_{MariciNat}
      marici-mul (marici-int-magnitude b) (marici-succ d))
  : MariciPositiveDenominatorDivides d e
  := (match b into
      (\ b-prime →
        (marici-succ e =_{MariciNat}
          marici-mul (marici-int-magnitude b-prime) (marici-succ d))
        → MariciPositiveDenominatorDivides d e)
      ( marici-int-zero ⇒ \ equation-prime →
          marici-empty-elim
            (MariciPositiveDenominatorDivides d e)
            (marici-succ-not-zero e equation-prime)
      | marici-int-pos q ⇒ \ equation-prime →
          marici-positive-denominator-divides-witness d e q
            (concat MariciNat
              (marici-mul (marici-succ d) (marici-succ q))
              (marici-mul (marici-succ q) (marici-succ d))
              (marici-succ e)
              (marici-mul-comm (marici-succ d) (marici-succ q))
              (rev MariciNat
                (marici-succ e)
                (marici-mul (marici-succ q) (marici-succ d))
                equation-prime))
      | marici-int-neg q ⇒ \ equation-prime →
          marici-positive-denominator-divides-witness d e q
            (concat MariciNat
              (marici-mul (marici-succ d) (marici-succ q))
              (marici-mul (marici-succ q) (marici-succ d))
              (marici-succ e)
              (marici-mul-comm (marici-succ d) (marici-succ q))
              (rev MariciNat
                (marici-succ e)
                (marici-mul (marici-succ q) (marici-succ d))
                equation-prime)))) equation

#define marici-signed-magnitude-coprime-euclid-unit-magnitude
  ( a b : MariciInt)
  ( d e : MariciNat)
  ( magnitude-one : marici-int-magnitude a =_{MariciNat} marici-succ marici-zero)
  ( equation : marici-mul (marici-int-magnitude a) (marici-succ e)
      =_{MariciNat}
    marici-mul (marici-int-magnitude b) (marici-succ d))
  : MariciPositiveDenominatorDivides d e
  := marici-denominator-divides-from-magnitude-product b d e
      (concat MariciNat
        (marici-succ e)
        (marici-mul (marici-succ marici-zero) (marici-succ e))
        (marici-mul (marici-int-magnitude b) (marici-succ d))
        (rev MariciNat
          (marici-mul (marici-succ marici-zero) (marici-succ e))
          (marici-succ e)
          (marici-mul-one-left (marici-succ e)))
        (concat MariciNat
          (marici-mul (marici-succ marici-zero) (marici-succ e))
          (marici-mul (marici-int-magnitude a) (marici-succ e))
          (marici-mul (marici-int-magnitude b) (marici-succ d))
          (rev MariciNat
            (marici-mul (marici-int-magnitude a) (marici-succ e))
            (marici-mul (marici-succ marici-zero) (marici-succ e))
            (ap MariciNat MariciNat
              (marici-int-magnitude a) (marici-succ marici-zero)
              (\ x → marici-mul x (marici-succ e)) magnitude-one))
          equation))
```

## Boundary

The Euclid theorem is discharged whenever the reduced numerator has unit
magnitude, for every positive denominator. The unresolved successor-denominator
case is now restricted further to numerator magnitude zero or at least two;
the zero case is handled separately by canonical-zero results, while magnitude
at least two requires the genuine coprime argument.
