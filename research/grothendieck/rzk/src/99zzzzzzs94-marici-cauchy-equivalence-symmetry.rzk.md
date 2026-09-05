# Cauchy-sequence equivalence is symmetric

Distance symmetry transports every eventual pointwise bound while preserving
the original explicit modulus.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-cauchy-sequences-equivalent-symmetric
  ( x y : MariciRationalCauchySequence)
  ( equivalent : MariciRationalCauchySequencesEquivalent x y)
  : MariciRationalCauchySequencesEquivalent y x
  := match equivalent
      ( marici-rational-cauchy-sequences-equivalent modulus witness ⇒
          marici-rational-cauchy-sequences-equivalent y x modulus
            (\ k n bound →
              marici-rational-at-most-transport-left-components
                (marici-rational-distance
                  (marici-rational-cauchy-sequence-values x n)
                  (marici-rational-cauchy-sequence-values y n))
                (marici-rational-distance
                  (marici-rational-cauchy-sequence-values y n)
                  (marici-rational-cauchy-sequence-values x n))
                (marici-rational-positive-reciprocal-power k marici-one)
                (marici-rational-distance-symmetric-components
                  (marici-rational-cauchy-sequence-values x n)
                  (marici-rational-cauchy-sequence-values y n))
                (witness k n bound)))
```

## Boundary

Eventual Cauchy-sequence equivalence is now reflexive and symmetric.
Transitivity still requires the rational triangle inequality and a checked
combination law for reciprocal tolerances.
