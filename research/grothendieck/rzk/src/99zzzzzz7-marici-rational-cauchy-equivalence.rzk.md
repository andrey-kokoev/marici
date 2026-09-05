# Eventual equivalence of rational Cauchy sequences

Two rational sequences are eventually equivalent when an explicit modulus
bounds their pointwise distance by every reciprocal tolerance `1/(k+1)`.
This is the setoid relation required before any completion quotient.

```rzk
#lang rzk-1
```

```rzk
#define MariciRationalSequencesEquivalentWithModulus
  ( left right : MariciNat → MariciRational)
  ( modulus : MariciNat → MariciNat)
  : U
  := ( k n : MariciNat)
    → MariciNatAtMost (modulus k) n
    → MariciRationalAtMost
        (marici-rational-distance (left n) (right n))
        (marici-rational-positive-reciprocal-power k marici-one)

#data MariciRationalCauchySequencesEquivalent
  ( left right : MariciRationalCauchySequence)
  := marici-rational-cauchy-sequences-equivalent
      ( modulus : MariciNat → MariciNat)
      ( witness : MariciRationalSequencesEquivalentWithModulus
          (marici-rational-cauchy-sequence-values left)
          (marici-rational-cauchy-sequence-values right)
          modulus)
```

## Boundary

This defines the intended completion relation with explicit quantitative data.
Reflexivity, symmetry, transitivity, quotient construction, and compatibility
with sequence arithmetic remain open. No completed real number is asserted.
