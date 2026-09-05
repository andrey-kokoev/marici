# Ordered exponent-two partial-sum distance is uniformly bounded

The ordered subtraction has the extracted tail's components. Absolute-value
congruence transports to that tail, whose nonnegativity makes absolute value
componentwise trivial. Order transport then upgrades the subtraction estimate
to the metric estimate.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-ordered-partial-sum-distance-components
  ( cutoff length : MariciNat)
  : marici-rational-forget
      (marici-rational-distance
        (marici-exponent-two-partial-sum
          (marici-add length (marici-succ cutoff)))
        (marici-exponent-two-partial-sum (marici-succ cutoff)))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-distance
          (marici-exponent-two-partial-sum
            (marici-add length (marici-succ cutoff)))
          (marici-exponent-two-partial-sum (marici-succ cutoff))))
      (marici-rational-forget
        (marici-rational-absolute
          (marici-rational-finite-sum length
            (marici-exponent-two-tail-term cutoff))))
      (marici-rational-forget
        (marici-rational-finite-sum length
          (marici-exponent-two-tail-term cutoff)))
      (marici-rational-absolute-respects-component-equality
        (marici-rational-subtract
          (marici-exponent-two-partial-sum
            (marici-add length (marici-succ cutoff)))
          (marici-exponent-two-partial-sum (marici-succ cutoff)))
        (marici-rational-finite-sum length
          (marici-exponent-two-tail-term cutoff))
        (marici-exponent-two-ordered-partial-sum-difference-components
          cutoff length))
      (marici-rational-absolute-nonnegative-components
        (marici-rational-finite-sum length
          (marici-exponent-two-tail-term cutoff))
        (marici-exponent-two-tail-nonnegative cutoff length))

#define marici-exponent-two-ordered-partial-sum-distance-bound
  ( cutoff length : MariciNat)
  : MariciRationalAtMost
      (marici-rational-distance
        (marici-exponent-two-partial-sum
          (marici-add length (marici-succ cutoff)))
        (marici-exponent-two-partial-sum (marici-succ cutoff)))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
  := marici-rational-at-most-transport-left-components
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-distance
        (marici-exponent-two-partial-sum
          (marici-add length (marici-succ cutoff)))
        (marici-exponent-two-partial-sum (marici-succ cutoff)))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-distance
            (marici-exponent-two-partial-sum
              (marici-add length (marici-succ cutoff)))
            (marici-exponent-two-partial-sum (marici-succ cutoff))))
        (marici-rational-forget
          (marici-rational-finite-sum length
            (marici-exponent-two-tail-term cutoff)))
        (marici-exponent-two-ordered-partial-sum-distance-components
          cutoff length))
      (marici-exponent-two-uniform-finite-tail-bound cutoff length)
```

## Boundary

The metric bound is complete for a successor cutoff and an explicitly supplied
ordered length. The Cauchy constructor still requires substituting additive-gap
equations for arbitrary indices and using distance symmetry in the reverse
ordering case.
