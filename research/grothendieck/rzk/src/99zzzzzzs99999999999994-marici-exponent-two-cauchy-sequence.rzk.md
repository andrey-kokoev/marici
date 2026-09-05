# Exponent-two Dirichlet partial sums form a rational Cauchy sequence

The modulus at tolerance index `k` is `k+1`. Natural-order totality selects one
of the two index orderings. The increasing case uses metric symmetry; the
reverse case already has the goal's endpoint order. Both invoke the arbitrary
ordered distance estimate.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-partial-sums-cauchy
  : MariciRationalSequenceIsCauchyWithModulus
      marici-exponent-two-partial-sum
      (\ k → marici-succ k)
  := \ k m n cutoff-to-m cutoff-to-n →
      match (marici-nat-at-most-total m n) into
      (\ comparison → MariciRationalAtMost
        (marici-rational-distance
          (marici-exponent-two-partial-sum m)
          (marici-exponent-two-partial-sum n))
        (marici-rational-positive-reciprocal-power k marici-one))
      ( marici-nat-comparison-left m-to-n ⇒
          marici-rational-at-most-transport-left-components
            (marici-rational-distance
              (marici-exponent-two-partial-sum n)
              (marici-exponent-two-partial-sum m))
            (marici-rational-distance
              (marici-exponent-two-partial-sum m)
              (marici-exponent-two-partial-sum n))
            (marici-rational-positive-reciprocal-power k marici-one)
            (rev MariciRawFraction
              (marici-rational-forget
                (marici-rational-distance
                  (marici-exponent-two-partial-sum m)
                  (marici-exponent-two-partial-sum n)))
              (marici-rational-forget
                (marici-rational-distance
                  (marici-exponent-two-partial-sum n)
                  (marici-exponent-two-partial-sum m)))
              (marici-rational-distance-symmetric-components
                (marici-exponent-two-partial-sum m)
                (marici-exponent-two-partial-sum n)))
            (marici-exponent-two-arbitrary-ordered-distance-bound
              k m n cutoff-to-m m-to-n)
      | marici-nat-comparison-right n-to-m ⇒
          marici-exponent-two-arbitrary-ordered-distance-bound
            k n m cutoff-to-n n-to-m)

#define marici-exponent-two-rational-cauchy-sequence
  : MariciRationalCauchySequence
  := marici-rational-cauchy-sequence
      marici-exponent-two-partial-sum
      (\ k → marici-succ k)
      marici-exponent-two-partial-sums-cauchy
```

## Boundary

Exponent-two Dirichlet partial sums now carry explicit rational Cauchy data.
This does not yet certify an Rzk-checked theorem because the newly added module
suffix remains untypechecked. Subject to checking, the conditional set-quotient
completion maps this sequence to a `MariciReal` and then to `MariciComplex`.
