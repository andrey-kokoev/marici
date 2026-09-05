# Ordered exponent-two partial-sum differences are uniformly bounded

The longer initial sum transports to shifted accumulation. Prefix cancellation
extracts the independently folded tail, and index alignment identifies it with
the family covered by the uniform finite-tail theorem. Component transport then
moves that order bound to the partial-sum difference.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-partial-sum
  ( bound : MariciNat)
  : MariciRational
  := marici-rational-finite-sum bound
      (marici-rational-dirichlet-term marici-two)

#define marici-exponent-two-ordered-partial-sum-difference-components
  ( cutoff length : MariciNat)
  : marici-rational-forget
      (marici-rational-subtract
        (marici-exponent-two-partial-sum
          (marici-add length (marici-succ cutoff)))
        (marici-exponent-two-partial-sum (marici-succ cutoff)))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-subtract
          (marici-exponent-two-partial-sum
            (marici-add length (marici-succ cutoff)))
          (marici-exponent-two-partial-sum (marici-succ cutoff))))
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-shifted-accumulate
            (marici-succ cutoff) length
            (marici-rational-dirichlet-term marici-two))
          (marici-exponent-two-partial-sum (marici-succ cutoff))))
      (marici-rational-forget
        (marici-rational-finite-sum length
          (marici-exponent-two-tail-term cutoff)))
      (ap MariciRational MariciRawFraction
        (marici-rational-subtract
          (marici-exponent-two-partial-sum
            (marici-add length (marici-succ cutoff)))
          (marici-exponent-two-partial-sum (marici-succ cutoff)))
        (marici-rational-subtract
          (marici-rational-shifted-accumulate
            (marici-succ cutoff) length
            (marici-rational-dirichlet-term marici-two))
          (marici-exponent-two-partial-sum (marici-succ cutoff)))
        marici-rational-forget
        (ap MariciRational MariciRational
          (marici-exponent-two-partial-sum
            (marici-add length (marici-succ cutoff)))
          (marici-rational-shifted-accumulate
            (marici-succ cutoff) length
            (marici-rational-dirichlet-term marici-two))
          (\ longer → marici-rational-subtract longer
            (marici-exponent-two-partial-sum (marici-succ cutoff)))
          (marici-exponent-two-shifted-accumulation
            (marici-succ cutoff) length)))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-subtract
            (marici-rational-shifted-accumulate
              (marici-succ cutoff) length
              (marici-rational-dirichlet-term marici-two))
            (marici-exponent-two-partial-sum (marici-succ cutoff))))
        (marici-rational-forget
          (marici-rational-finite-sum length
            (marici-rational-shifted-tail-term
              (marici-succ cutoff)
              (marici-rational-dirichlet-term marici-two))))
        (marici-rational-forget
          (marici-rational-finite-sum length
            (marici-exponent-two-tail-term cutoff)))
        (marici-rational-shifted-accumulator-difference-components
          (marici-succ cutoff) length
          (marici-rational-dirichlet-term marici-two))
        (ap MariciRational MariciRawFraction
          (marici-rational-finite-sum length
            (marici-rational-shifted-tail-term
              (marici-succ cutoff)
              (marici-rational-dirichlet-term marici-two)))
          (marici-rational-finite-sum length
            (marici-exponent-two-tail-term cutoff))
          marici-rational-forget
          (marici-exponent-two-shifted-tail-sum-alignment cutoff length)))

#define marici-exponent-two-ordered-partial-sum-bound
  ( cutoff length : MariciNat)
  : MariciRationalAtMost
      (marici-rational-subtract
        (marici-exponent-two-partial-sum
          (marici-add length (marici-succ cutoff)))
        (marici-exponent-two-partial-sum (marici-succ cutoff)))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
  := marici-rational-at-most-transport-left-components
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-subtract
        (marici-exponent-two-partial-sum
          (marici-add length (marici-succ cutoff)))
        (marici-exponent-two-partial-sum (marici-succ cutoff)))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-subtract
            (marici-exponent-two-partial-sum
              (marici-add length (marici-succ cutoff)))
            (marici-exponent-two-partial-sum (marici-succ cutoff))))
        (marici-rational-forget
          (marici-rational-finite-sum length
            (marici-exponent-two-tail-term cutoff)))
        (marici-exponent-two-ordered-partial-sum-difference-components
          cutoff length))
      (marici-exponent-two-uniform-finite-tail-bound cutoff length)
```

## Boundary

Every ordered pair of exponent-two partial sums separated by a supplied finite
length now satisfies the reciprocal-tolerance bound. Constructing the Cauchy
witness requires decomposing arbitrary indices above the cutoff into this
successor-cutoff-plus-length form and handling distance symmetry.
