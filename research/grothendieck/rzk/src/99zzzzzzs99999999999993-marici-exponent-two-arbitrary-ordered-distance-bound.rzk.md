# Arbitrary ordered exponent-two partial sums satisfy the cutoff bound

A smaller index beyond the successor cutoff supplies a local predecessor and a
comparison from the requested cutoff. The ordered gap supplies the tail length.
Index transport applies the explicit metric theorem, and reciprocal
antitonicity weakens its local tolerance to the requested tolerance.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-arbitrary-ordered-distance-bound
  ( cutoff smaller larger : MariciNat)
  ( cutoff-to-smaller : MariciNatAtMost (marici-succ cutoff) smaller)
  ( smaller-to-larger : MariciNatAtMost smaller larger)
  : MariciRationalAtMost
      (marici-rational-distance
        (marici-exponent-two-partial-sum larger)
        (marici-exponent-two-partial-sum smaller))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
  := match (marici-successor-cutoff-decompose
      cutoff smaller cutoff-to-smaller)
      into (\ decomposition → MariciRationalAtMost
        (marici-rational-distance
          (marici-exponent-two-partial-sum larger)
          (marici-exponent-two-partial-sum smaller))
        (marici-rational-positive-reciprocal-power cutoff marici-one))
      ( marici-successor-cutoff-decomposition
          local smaller-path cutoff-to-local ⇒
          match smaller-to-larger
          ( marici-nat-at-most-witness gap larger-equation ⇒
              marici-rational-at-most-transitive
                (marici-rational-distance
                  (marici-exponent-two-partial-sum larger)
                  (marici-exponent-two-partial-sum smaller))
                (marici-rational-positive-reciprocal-power local marici-one)
                (marici-rational-positive-reciprocal-power cutoff marici-one)
                (marici-rational-at-most-transport-left-components
                  (marici-rational-distance
                    (marici-exponent-two-partial-sum
                      (marici-add gap (marici-succ local)))
                    (marici-exponent-two-partial-sum (marici-succ local)))
                  (marici-rational-distance
                    (marici-exponent-two-partial-sum larger)
                    (marici-exponent-two-partial-sum smaller))
                  (marici-rational-positive-reciprocal-power local marici-one)
                  (marici-exponent-two-ordered-distance-index-components
                    local smaller larger gap
                    smaller-path larger-equation)
                  (marici-exponent-two-ordered-partial-sum-distance-bound
                    local gap))
                (marici-rational-reciprocal-tolerance-antitone
                  cutoff local cutoff-to-local)))
```

## Boundary

The requested Cauchy estimate now holds whenever the two arbitrary indices are
supplied in increasing order and the smaller lies beyond the successor modulus.
Natural-order totality and distance symmetry remain to combine the two possible
index orderings into the Cauchy constructor.
