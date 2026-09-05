# Pointwise negation preserves Cauchy-sequence equivalence

An equivalence witness between two rational Cauchy sequences is transported
through simultaneous-negation invariance of rational distance. Its modulus is
unchanged.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-cauchy-equivalence-negate
  ( left right : MariciRationalCauchySequence)
  ( equivalent : MariciRationalCauchySequencesEquivalent left right)
  : MariciRationalCauchySequencesEquivalent
      (marici-rational-cauchy-sequence-negate left)
      (marici-rational-cauchy-sequence-negate right)
  := match left
      ( marici-rational-cauchy-sequence
          left-sequence left-modulus left-cauchy ⇒
        match right
        ( marici-rational-cauchy-sequence
            right-sequence right-modulus right-cauchy ⇒
          match equivalent
          ( marici-rational-cauchy-sequences-equivalent modulus witness ⇒
            marici-rational-cauchy-sequences-equivalent
              modulus
              (\ k n modulus-to-n →
                transport MariciRawFraction
                  (\ raw-distance →
                    MariciRawFractionAtMost raw-distance
                      (marici-rational-forget
                        (marici-rational-positive-reciprocal-power
                          k marici-one)))
                  (marici-rational-forget
                    (marici-rational-distance
                      (left-sequence n) (right-sequence n)))
                  (marici-rational-forget
                    (marici-rational-distance
                      (marici-rational-negate (left-sequence n))
                      (marici-rational-negate (right-sequence n))))
                  (rev MariciRawFraction
                    (marici-rational-forget
                      (marici-rational-distance
                        (marici-rational-negate (left-sequence n))
                        (marici-rational-negate (right-sequence n))))
                    (marici-rational-forget
                      (marici-rational-distance
                        (left-sequence n) (right-sequence n)))
                    (marici-rational-distance-negations-components
                      (left-sequence n) (right-sequence n)))
                  (witness k n modulus-to-n)))))

#define marici-rational-cauchy-equivalence-negate-modulus-preserved
  ( left right : MariciRationalCauchySequence)
  ( modulus : MariciNat → MariciNat)
  ( witness : MariciRationalSequencesEquivalentWithModulus
      (marici-rational-cauchy-sequence-values left)
      (marici-rational-cauchy-sequence-values right)
      modulus)
  : MariciRationalCauchySequencesEquivalent
      (marici-rational-cauchy-sequence-negate left)
      (marici-rational-cauchy-sequence-negate right)
  := marici-rational-cauchy-equivalence-negate left right
      (marici-rational-cauchy-sequences-equivalent modulus witness)
```

## Boundary

Pointwise negation now respects the equivalence relation used by the conditional
real completion. Defining `MariciReal` negation through quotient recursion still
requires the codomain set proof already exposed by the set-quotient interface.
