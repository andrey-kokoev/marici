# Total natural division by a nonunit divisor

Primitive recursion on the dividend iterates the checked successor transition
from the zero state. Thus every natural admits an executable quotient and
bounded remainder with respect to every divisor at least two.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-divide-by-nonunit
  ( divisor-residual value : MariciNat)
  : MariciNatDivisionState (marici-succ divisor-residual) value
  := ind-MariciNat
      (\ value-prime →
        MariciNatDivisionState
          (marici-succ divisor-residual) value-prime)
      (marici-nat-division-zero-state (marici-succ divisor-residual))
      (\ value-prime state →
        marici-nat-division-successor-state-nonunit
          divisor-residual value-prime state)
      value

#define marici-division-zero-remainder-gives-divides
  ( divisor-predecessor value quotient : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor))
      marici-zero
    =_{MariciNat} value)
  : MariciNatDivides (marici-succ divisor-predecessor) value
  := marici-nat-divides-witness
      (marici-succ divisor-predecessor) value quotient
      (concat MariciNat
        (marici-mul quotient (marici-succ divisor-predecessor))
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor))
          marici-zero)
        value
        (rev MariciNat
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor))
            marici-zero)
          (marici-mul quotient (marici-succ divisor-predecessor))
          (marici-add-zero-right
            (marici-mul quotient (marici-succ divisor-predecessor))))
        reconstruction)

#define marici-division-state-zero-remainder-gives-divides
  ( divisor-predecessor value : MariciNat)
  ( state : MariciNatDivisionState divisor-predecessor value)
  ( remainder-zero : (match state
      ( marici-nat-division-state quotient remainder
          remainder-bounded reconstruction ⇒ remainder))
      =_{MariciNat} marici-zero)
  : MariciNatDivides (marici-succ divisor-predecessor) value
  := match state into
      (\ state-prime →
        ((match state-prime
          ( marici-nat-division-state quotient remainder
              remainder-bounded reconstruction ⇒ remainder))
          =_{MariciNat} marici-zero)
        → MariciNatDivides (marici-succ divisor-predecessor) value)
      ( marici-nat-division-state quotient remainder
          remainder-bounded reconstruction ⇒
        \ zero-path →
          marici-division-zero-remainder-gives-divides
            divisor-predecessor value quotient
            (concat MariciNat
              (marici-add
                (marici-mul quotient (marici-succ divisor-predecessor))
                marici-zero)
              (marici-add
                (marici-mul quotient (marici-succ divisor-predecessor))
                remainder)
              value
              (ap MariciNat MariciNat marici-zero remainder
                (\ remainder-prime → marici-add
                  (marici-mul quotient
                    (marici-succ divisor-predecessor)) remainder-prime)
                (rev MariciNat remainder marici-zero zero-path))
              reconstruction))
      remainder-zero
```

## Boundary

Total quotient/remainder construction is now available for all nonunit natural
divisors, and a zero remainder yields the standard divisibility witness. The
converse—an existing divisibility witness forces the computed bounded remainder
to zero—is the next uniqueness lemma needed for residue-based irreducible
Euclid.
