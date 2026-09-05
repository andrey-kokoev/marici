# Finite sums split by shifted accumulation

A shifted segment can be accumulated directly onto an existing prefix. Because
natural addition recurses on the segment length, this accumulator follows the
same recursion as the longer initial sum and requires no reassociation law.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-shifted-accumulate
  ( prefix length : MariciNat)
  ( term : MariciNat → MariciRational)
  : MariciRational
  := match length
      ( marici-zero ⇒ marici-rational-finite-sum prefix term
      | marici-succ k accumulated ⇒
          marici-rational-add accumulated (term (marici-add k prefix)))

#define marici-rational-finite-sum-shifted-accumulation
  ( prefix length : MariciNat)
  ( term : MariciNat → MariciRational)
  : marici-rational-finite-sum (marici-add length prefix) term
    =_{MariciRational}
    marici-rational-shifted-accumulate prefix length term
  := match length
      ( marici-zero ⇒ refl
      | marici-succ k induction ⇒
          ap MariciRational MariciRational
            (marici-rational-finite-sum (marici-add k prefix) term)
            (marici-rational-shifted-accumulate prefix k term)
            (\ partial → marici-rational-add partial
              (term (marici-add k prefix)))
            induction)

#define marici-exponent-two-shifted-accumulation
  ( prefix length : MariciNat)
  : marici-rational-finite-sum (marici-add length prefix)
      (marici-rational-dirichlet-term marici-two)
    =_{MariciRational}
    marici-rational-shifted-accumulate prefix length
      (marici-rational-dirichlet-term marici-two)
  := marici-rational-finite-sum-shifted-accumulation
      prefix length (marici-rational-dirichlet-term marici-two)
```

## Boundary

A longer exponent-two partial sum is now definitionally tracked as its prefix
with each shifted tail term accumulated in order. Relating this accumulator's
difference from the prefix to the independently folded shifted tail requires a
component-level additive cancellation lemma.
