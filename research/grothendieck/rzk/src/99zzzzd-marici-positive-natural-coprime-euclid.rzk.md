# Positive natural coprime Euclid

Natural induction on the external predecessor bound combines the checked zero
base and successor constructor. Instantiating the resulting bounded family at
its own bound constructs a Bézout difference for every coprime pair with
positive second coordinate; Bézout elimination then proves Euclid.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-bezout-available-bounded
  ( bound : MariciNat)
  : MariciPositiveBezoutAvailableUpTo bound
  := ind-MariciNat
      (\ bound-prime → MariciPositiveBezoutAvailableUpTo bound-prime)
      marici-positive-bezout-available-zero
      (\ bound-prime previous →
        marici-positive-bezout-available-successor
          bound-prime previous)
      bound

#define marici-coprime-positive-has-bezout-difference
  ( x y-predecessor : MariciNat)
  ( coprime : MariciNatAreCoprime x (marici-succ y-predecessor))
  : MariciNatBezoutDifference x (marici-succ y-predecessor)
  := marici-positive-bezout-available-bounded y-predecessor
      y-predecessor
      (marici-nat-at-most-witness
        y-predecessor y-predecessor marici-zero refl)
      x coprime

#define MariciNatPositiveCoprimeEuclid
  : U
  := ( x y-predecessor z : MariciNat)
    → MariciNatAreCoprime x (marici-succ y-predecessor)
    → MariciNatDivides
        (marici-succ y-predecessor) (marici-mul x z)
    → MariciNatDivides (marici-succ y-predecessor) z

#define marici-nat-positive-coprime-euclid
  : MariciNatPositiveCoprimeEuclid
  := \ x y-predecessor z coprime divides-product →
      marici-natural-bezout-difference-implies-euclid
        x (marici-succ y-predecessor)
        (marici-coprime-positive-has-bezout-difference
          x y-predecessor coprime)
        z divides-product
```

## Boundary

Standard coprime Euclid is now checked for every positive natural divisor,
which is the exact domain of fraction denominators. The unrestricted alias
`MariciNatCoprimeEuclid` also quantifies over zero; its zero-divisor branch is
separate and is not needed for denominator uniqueness. The next step can wire
this positive theorem directly into the normalization canonicality interface.
