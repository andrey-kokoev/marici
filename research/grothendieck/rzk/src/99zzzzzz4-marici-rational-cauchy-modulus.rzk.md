# Rational Cauchy sequences with explicit moduli

Cauchy data consists of a rational sequence, a natural modulus, and a bound at
each reciprocal tolerance `1/(k+1)`. Index comparisons use the existing natural
at-most witnesses.

```rzk
#lang rzk-1
```

```rzk
#define MariciRationalSequenceIsCauchyWithModulus
  ( sequence : MariciNat → MariciRational)
  ( modulus : MariciNat → MariciNat)
  : U
  := ( k m n : MariciNat)
    → MariciNatAtMost (modulus k) m
    → MariciNatAtMost (modulus k) n
    → MariciRationalAtMost
        (marici-rational-distance (sequence m) (sequence n))
        (marici-rational-positive-reciprocal-power k marici-one)

#data MariciRationalCauchySequence
  := marici-rational-cauchy-sequence
      ( sequence : MariciNat → MariciRational)
      ( modulus : MariciNat → MariciNat)
      ( cauchy : MariciRationalSequenceIsCauchyWithModulus
          sequence modulus)

#define marici-rational-cauchy-sequence-values
  ( x : MariciRationalCauchySequence)
  : MariciNat → MariciRational
  := match x
      ( marici-rational-cauchy-sequence sequence modulus cauchy ⇒
          sequence)

#define marici-rational-cauchy-sequence-modulus
  ( x : MariciRationalCauchySequence)
  : MariciNat → MariciNat
  := match x
      ( marici-rational-cauchy-sequence sequence modulus cauchy ⇒
          modulus)
```

## Boundary

This is explicit Cauchy data, not a completion or quotient of sequences.
Equivalence of Cauchy sequences, completeness, arithmetic closure, and the proof
that Dirichlet partial sums satisfy this predicate remain open.
