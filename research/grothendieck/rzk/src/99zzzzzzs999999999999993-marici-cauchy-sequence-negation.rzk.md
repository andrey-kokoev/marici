# Pointwise negation preserves rational Cauchy sequences

Simultaneous-negation invariance of rational distance transports every original
Cauchy bound to the pointwise-negated sequence. The original modulus is reused
without enlargement.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-cauchy-sequence-negate
  ( x : MariciRationalCauchySequence)
  : MariciRationalCauchySequence
  := match x
      ( marici-rational-cauchy-sequence sequence modulus cauchy ⇒
          marici-rational-cauchy-sequence
            (\ index → marici-rational-negate (sequence index))
            modulus
            (\ k m n modulus-to-m modulus-to-n →
              transport MariciRawFraction
                (\ raw-distance →
                  MariciRawFractionAtMost raw-distance
                    (marici-rational-forget
                      (marici-rational-positive-reciprocal-power
                        k marici-one)))
                (marici-rational-forget
                  (marici-rational-distance (sequence m) (sequence n)))
                (marici-rational-forget
                  (marici-rational-distance
                    (marici-rational-negate (sequence m))
                    (marici-rational-negate (sequence n))))
                (rev MariciRawFraction
                  (marici-rational-forget
                    (marici-rational-distance
                      (marici-rational-negate (sequence m))
                      (marici-rational-negate (sequence n))))
                  (marici-rational-forget
                    (marici-rational-distance (sequence m) (sequence n)))
                  (marici-rational-distance-negations-components
                    (sequence m) (sequence n)))
                (cauchy k m n modulus-to-m modulus-to-n)))

#define marici-rational-cauchy-sequence-negate-values
  ( x : MariciRationalCauchySequence)
  ( index : MariciNat)
  : marici-rational-cauchy-sequence-values
      (marici-rational-cauchy-sequence-negate x) index
    =_{MariciRational}
    marici-rational-negate
      (marici-rational-cauchy-sequence-values x index)
  := match x
      ( marici-rational-cauchy-sequence sequence modulus cauchy ⇒ refl)

#define marici-rational-cauchy-sequence-negate-modulus
  ( x : MariciRationalCauchySequence)
  : marici-rational-cauchy-sequence-modulus
      (marici-rational-cauchy-sequence-negate x)
    =_{MariciNat → MariciNat}
    marici-rational-cauchy-sequence-modulus x
  := match x
      ( marici-rational-cauchy-sequence sequence modulus cauchy ⇒ refl)
```

## Boundary

Rational Cauchy sequences are now closed under pointwise negation with unchanged
modulus. Descent to a negation operation on `MariciReal` additionally requires
proof that pointwise negation preserves Cauchy-sequence equivalence.
