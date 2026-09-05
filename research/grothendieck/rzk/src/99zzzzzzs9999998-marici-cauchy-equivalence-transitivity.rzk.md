# Cauchy-sequence equivalence is transitive

Both source moduli are evaluated at the tightened tolerance index and combined.
At every later sequence index, distance triangle, addition monotonicity, and the
reciprocal-tolerance combination bound compose to the requested target bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-cauchy-sequences-equivalent-transitive
  ( x y z : MariciRationalCauchySequence)
  ( xy : MariciRationalCauchySequencesEquivalent x y)
  ( yz : MariciRationalCauchySequencesEquivalent y z)
  : MariciRationalCauchySequencesEquivalent x z
  := match xy
      ( marici-rational-cauchy-sequences-equivalent
          first-modulus first-witness ⇒
          match yz
          ( marici-rational-cauchy-sequences-equivalent
              second-modulus second-witness ⇒
              marici-rational-cauchy-sequences-equivalent x z
                (marici-combined-tightened-modulus
                  first-modulus second-modulus)
                (\ k n combined-bound →
                  marici-rational-at-most-transitive
                    (marici-rational-distance
                      (marici-rational-cauchy-sequence-values x n)
                      (marici-rational-cauchy-sequence-values z n))
                    (marici-rational-add
                      (marici-rational-distance
                        (marici-rational-cauchy-sequence-values x n)
                        (marici-rational-cauchy-sequence-values y n))
                      (marici-rational-distance
                        (marici-rational-cauchy-sequence-values y n)
                        (marici-rational-cauchy-sequence-values z n)))
                    (marici-rational-positive-reciprocal-power k marici-one)
                    (marici-rational-distance-triangle
                      (marici-rational-cauchy-sequence-values x n)
                      (marici-rational-cauchy-sequence-values y n)
                      (marici-rational-cauchy-sequence-values z n))
                    (marici-rational-at-most-transitive
                      (marici-rational-add
                        (marici-rational-distance
                          (marici-rational-cauchy-sequence-values x n)
                          (marici-rational-cauchy-sequence-values y n))
                        (marici-rational-distance
                          (marici-rational-cauchy-sequence-values y n)
                          (marici-rational-cauchy-sequence-values z n)))
                      (marici-rational-add
                        (marici-rational-positive-reciprocal-power
                          (marici-double-tolerance-index k) marici-one)
                        (marici-rational-positive-reciprocal-power
                          (marici-double-tolerance-index k) marici-one))
                      (marici-rational-positive-reciprocal-power k marici-one)
                      (marici-rational-add-at-most
                        (marici-rational-distance
                          (marici-rational-cauchy-sequence-values x n)
                          (marici-rational-cauchy-sequence-values y n))
                        (marici-rational-positive-reciprocal-power
                          (marici-double-tolerance-index k) marici-one)
                        (marici-rational-distance
                          (marici-rational-cauchy-sequence-values y n)
                          (marici-rational-cauchy-sequence-values z n))
                        (marici-rational-positive-reciprocal-power
                          (marici-double-tolerance-index k) marici-one)
                        (first-witness
                          (marici-double-tolerance-index k) n
                          (marici-combined-tightened-modulus-left-bound
                            first-modulus second-modulus k n combined-bound))
                        (second-witness
                          (marici-double-tolerance-index k) n
                          (marici-combined-tightened-modulus-right-bound
                            first-modulus second-modulus k n combined-bound)))
                      (marici-reciprocal-tolerance-combination k)))))
```

## Boundary

Cauchy-sequence equivalence is now reflexive, symmetric, and transitive with
explicit quantitative moduli. Constructing the completed real carrier still
requires a quotient or canonical representative construction compatible with
this equivalence relation.
