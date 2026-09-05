# Divisibility forces zero bounded remainder

A standard divisibility witness reconstructs the value as a pure multiple.
Explicit trichotomy compares its quotient with the quotient in any bounded
remainder state. Equality gives zero remainder directly; both strict branches
have already been shown impossible.

```rzk
#lang rzk-1
```

```rzk
#define marici-division-state-remainder
  ( divisor-predecessor value : MariciNat)
  ( state : MariciNatDivisionState divisor-predecessor value)
  : MariciNat
  := match state
      ( marici-nat-division-state quotient remainder
          remainder-bounded reconstruction ⇒ remainder)

#define marici-divisibility-forces-division-remainder-zero
  ( divisor-predecessor value : MariciNat)
  ( state : MariciNatDivisionState divisor-predecessor value)
  ( divides : MariciNatDivides
      (marici-succ divisor-predecessor) value)
  : marici-division-state-remainder
      divisor-predecessor value state
      =_{MariciNat} marici-zero
  := match state into
      (\ state-prime →
        MariciNatDivides (marici-succ divisor-predecessor) value
        → marici-division-state-remainder
            divisor-predecessor value state-prime
            =_{MariciNat} marici-zero)
      ( marici-nat-division-state quotient remainder
          remainder-bounded reconstruction ⇒
        \ divides-prime →
          match divides-prime
          ( marici-nat-divides-witness witness-quotient witness-equation ⇒
            match (marici-nat-gap-trichotomy quotient witness-quotient)
            ( marici-nat-gap-less gap quotient-gap ⇒
                marici-empty-elim
                  (remainder =_{MariciNat} marici-zero)
                  (marici-division-smaller-quotient-impossible
                    divisor-predecessor value quotient witness-quotient
                    remainder gap remainder-bounded reconstruction
                    witness-equation quotient-gap)
            | marici-nat-gap-equal quotients-equal ⇒
                marici-division-equal-quotient-remainder-zero
                  divisor-predecessor value quotient witness-quotient
                  remainder reconstruction witness-equation quotients-equal
            | marici-nat-gap-greater gap quotient-gap ⇒
                marici-empty-elim
                  (remainder =_{MariciNat} marici-zero)
                  (marici-division-greater-quotient-impossible
                    divisor-predecessor value quotient witness-quotient
                    remainder gap reconstruction witness-equation
                    quotient-gap))))
      divides

#define marici-computed-nonunit-division-divides-iff-zero-forward
  ( divisor-residual value : MariciNat)
  ( divides : MariciNatDivides
      (marici-succ (marici-succ divisor-residual)) value)
  : marici-division-state-remainder
      (marici-succ divisor-residual) value
      (marici-nat-divide-by-nonunit divisor-residual value)
      =_{MariciNat} marici-zero
  := marici-divisibility-forces-division-remainder-zero
      (marici-succ divisor-residual) value
      (marici-nat-divide-by-nonunit divisor-residual value)
      divides
```

## Boundary

For every divisor at least two, standard divisibility now forces the computed
remainder to zero; the converse was already proved. The total division
algorithm therefore decides divisibility once zero equality for the computed
remainder is projected, and supplies the exact remainder property needed by
the irreducible Euclid proof.
