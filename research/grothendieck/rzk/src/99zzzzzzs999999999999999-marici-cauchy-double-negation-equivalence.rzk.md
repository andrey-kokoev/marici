# Double-negated Cauchy sequences are equivalent to their inputs

Rational negation involution identifies each twice-negated value with its
original value at canonical components. Distance congruence transports the
self-distance tolerance proof pointwise, using the constant-zero equivalence
modulus.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-cauchy-sequence-double-negate-equivalent
  ( x : MariciRationalCauchySequence)
  : MariciRationalCauchySequencesEquivalent
      (marici-rational-cauchy-sequence-negate
        (marici-rational-cauchy-sequence-negate x))
      x
  := match x
      ( marici-rational-cauchy-sequence sequence modulus cauchy ⇒
          marici-rational-cauchy-sequences-equivalent
            (marici-rational-cauchy-sequence-negate
              (marici-rational-cauchy-sequence-negate
                (marici-rational-cauchy-sequence
                  sequence modulus cauchy)))
            (marici-rational-cauchy-sequence sequence modulus cauchy)
            (\ k → marici-zero)
            (\ k n bound →
              marici-rational-at-most-transport-left-components
                (marici-rational-distance (sequence n) (sequence n))
                (marici-rational-distance
                  (marici-rational-negate
                    (marici-rational-negate (sequence n)))
                  (sequence n))
                (marici-rational-positive-reciprocal-power k marici-one)
                (rev MariciRawFraction
                  (marici-rational-forget
                    (marici-rational-distance
                      (marici-rational-negate
                        (marici-rational-negate (sequence n)))
                      (sequence n)))
                  (marici-rational-forget
                    (marici-rational-distance
                      (sequence n) (sequence n)))
                  (marici-rational-distance-left-component-congruence
                    (marici-rational-negate
                      (marici-rational-negate (sequence n)))
                    (sequence n)
                    (sequence n)
                    (marici-rational-negate-involutive-components
                      (sequence n))))
                (marici-rational-distance-self-at-most-tolerance
                  (sequence n) k)))
```

## Boundary

Double pointwise negation is now equivalent, rather than definitionally equal,
to the original Cauchy sequence. Quotient soundness and the recursor computation
rule can therefore prove involutivity of conditional real negation.
