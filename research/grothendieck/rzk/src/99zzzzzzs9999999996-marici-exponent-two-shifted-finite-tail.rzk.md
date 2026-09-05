# Shifted finite exponent-two tails telescope

Index addition recurses on the segment index, so successor indices compute to
the next cutoff position. Pointwise summation and component-level telescoping
therefore extend uniformly to every starting cutoff.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-tail-term
  ( cutoff index : MariciNat)
  : MariciRational
  := marici-rational-dirichlet-term marici-two
      (marici-succ (marici-add index cutoff))

#define marici-shifted-reciprocal-difference-term
  ( cutoff index : MariciNat)
  : MariciRational
  := marici-rational-reciprocal-difference
      (marici-add index cutoff)
      (marici-succ (marici-add index cutoff))

#define marici-exponent-two-tail-at-most-shifted-telescoping-sum
  ( cutoff length : MariciNat)
  : MariciRationalAtMost
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-finite-sum length
        (marici-shifted-reciprocal-difference-term cutoff))
  := marici-rational-finite-sum-at-most
      (marici-exponent-two-tail-term cutoff)
      (marici-shifted-reciprocal-difference-term cutoff)
      (\ index →
        marici-exponent-two-term-at-most-adjacent-reciprocal-difference
          (marici-add index cutoff))
      length

#define marici-shifted-reciprocal-telescoping-components
  ( cutoff length : MariciNat)
  : marici-rational-forget
      (marici-rational-finite-sum length
        (marici-shifted-reciprocal-difference-term cutoff))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-reciprocal-difference
        cutoff (marici-add length cutoff))
  := match length
      ( marici-zero ⇒
          rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-reciprocal-difference cutoff cutoff))
            (marici-rational-forget marici-rational-zero)
            (marici-rational-subtract-self-components
              (marici-rational-positive-reciprocal-power
                cutoff marici-one))
      | marici-succ k induction ⇒
          concat MariciRawFraction
            (marici-rational-forget
              (marici-rational-finite-sum (marici-succ k)
                (marici-shifted-reciprocal-difference-term cutoff)))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-reciprocal-difference
                  cutoff (marici-add k cutoff))
                (marici-rational-reciprocal-difference
                  (marici-add k cutoff)
                  (marici-succ (marici-add k cutoff)))))
            (marici-rational-forget
              (marici-rational-reciprocal-difference
                cutoff (marici-succ (marici-add k cutoff))))
            (marici-rational-add-component-congruent
              (marici-rational-finite-sum k
                (marici-shifted-reciprocal-difference-term cutoff))
              (marici-rational-reciprocal-difference
                cutoff (marici-add k cutoff))
              (marici-rational-reciprocal-difference
                (marici-add k cutoff)
                (marici-succ (marici-add k cutoff)))
              (marici-rational-reciprocal-difference
                (marici-add k cutoff)
                (marici-succ (marici-add k cutoff)))
              induction refl)
            (marici-rational-reciprocal-differences-compose-components
              cutoff (marici-add k cutoff)
              (marici-succ (marici-add k cutoff))))

#define marici-exponent-two-finite-tail-at-most-outer-difference
  ( cutoff length : MariciNat)
  : MariciRationalAtMost
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-reciprocal-difference
        cutoff (marici-add length cutoff))
  := marici-rational-at-most-transport-right-components
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-finite-sum length
        (marici-shifted-reciprocal-difference-term cutoff))
      (marici-rational-reciprocal-difference
        cutoff (marici-add length cutoff))
      (marici-shifted-reciprocal-telescoping-components cutoff length)
      (marici-exponent-two-tail-at-most-shifted-telescoping-sum
        cutoff length)
```

## Boundary

Every finite exponent-two segment beginning immediately beyond `cutoff` is now
bounded by the outer reciprocal difference from that cutoff. Bounding this
difference by the cutoff reciprocal tolerance completes the uniform finite-tail
estimate needed for Cauchy convergence.
