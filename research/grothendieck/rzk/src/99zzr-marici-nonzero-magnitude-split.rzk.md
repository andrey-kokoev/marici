# Nonzero magnitudes split into unit and at-least-two cases

Canonical signed integers expose their magnitude predecessor. Under explicit
nonzeroness, that predecessor is either zero, giving unit magnitude, or a
successor, giving magnitude at least two. This makes the remaining Euclid
branch an exact type rather than an informal exclusion.

```rzk
#lang rzk-1
```

```rzk
#data MariciNonzeroMagnitudeClassification
  ( a : MariciInt)
  := marici-nonzero-magnitude-unit
      ( magnitude-unit : marici-int-magnitude a =_{MariciNat}
          marici-succ marici-zero)
  | marici-nonzero-magnitude-at-least-two
      ( residual-predecessor : MariciNat)
      ( magnitude-large : marici-int-magnitude a =_{MariciNat}
          marici-succ (marici-succ residual-predecessor))

#define marici-classify-nonzero-magnitude
  ( a : MariciInt)
  ( nonzero : (a =_{MariciInt} marici-int-zero) → MariciEmpty)
  : MariciNonzeroMagnitudeClassification a
  := (match a into
      (\ a-prime → ((a-prime =_{MariciInt} marici-int-zero) → MariciEmpty)
        → MariciNonzeroMagnitudeClassification a-prime)
      ( marici-int-zero ⇒ \ nonzero-prime →
          marici-empty-elim
            (MariciNonzeroMagnitudeClassification marici-int-zero)
            (nonzero-prime refl)
      | marici-int-pos n ⇒ \ nonzero-prime → match n into
          (\ n-prime → MariciNonzeroMagnitudeClassification
            (marici-int-pos n-prime))
          ( marici-zero ⇒
              marici-nonzero-magnitude-unit
                (marici-int-pos marici-zero) refl
          | marici-succ k induction ⇒
              marici-nonzero-magnitude-at-least-two
                (marici-int-pos (marici-succ k)) k refl)
      | marici-int-neg n ⇒ \ nonzero-prime → match n into
          (\ n-prime → MariciNonzeroMagnitudeClassification
            (marici-int-neg n-prime))
          ( marici-zero ⇒
              marici-nonzero-magnitude-unit
                (marici-int-neg marici-zero) refl
          | marici-succ k induction ⇒
              marici-nonzero-magnitude-at-least-two
                (marici-int-neg (marici-succ k)) k refl))) nonzero

#define MariciLargeMagnitudeCoprimeEuclid
  : U
  := ( a b : MariciInt)
    → ( d e : MariciNat)
    → ((a =_{MariciInt} marici-int-zero) → MariciEmpty)
    → (MariciMagnitudeNonunitCommonPositiveFactor a d → MariciEmpty)
    → (marici-mul (marici-int-magnitude a) (marici-succ e)
        =_{MariciNat}
      marici-mul (marici-int-magnitude b) (marici-succ d))
    → (residual-predecessor : MariciNat)
    → (marici-int-magnitude a =_{MariciNat}
        marici-succ (marici-succ residual-predecessor))
    → MariciPositiveDenominatorDivides d e

#define marici-signed-magnitude-coprime-euclid-from-large-case
  ( large-euclid : MariciLargeMagnitudeCoprimeEuclid)
  : MariciSignedMagnitudeCoprimeEuclid
  := \ a b d e nonzero coprime equation →
      match (marici-classify-nonzero-magnitude a nonzero)
        ( marici-nonzero-magnitude-unit magnitude-unit ⇒
            marici-signed-magnitude-coprime-euclid-unit-magnitude
              a b d e magnitude-unit equation
        | marici-nonzero-magnitude-at-least-two
            residual-predecessor magnitude-large ⇒
              large-euclid a b d e nonzero coprime equation
                residual-predecessor magnitude-large)
```

## Boundary

All zero and unit-magnitude cases are discharged. Full reduced normalization
canonicality now depends only on `MariciLargeMagnitudeCoprimeEuclid`, whose
numerator magnitude and denominator are both structurally nonunit candidates.
