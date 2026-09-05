# Finite rational sums

A primitive recursion over `MariciNat` now folds rational-valued families. The
indexing convention is the initial segment from zero through the predecessor of
the supplied bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-finite-sum
  ( n : MariciNat)
  ( term : MariciNat → MariciRational)
  : MariciRational
  := match n
      ( marici-zero ⇒ marici-rational-zero
      | marici-succ k ih ⇒ marici-rational-add ih (term k))

#define marici-rational-finite-sum-zero
  ( term : MariciNat → MariciRational)
  : marici-rational-finite-sum marici-zero term
    =_{MariciRational}
    marici-rational-zero
  := refl

#define marici-rational-finite-sum-successor
  ( n : MariciNat)
  ( term : MariciNat → MariciRational)
  : marici-rational-finite-sum (marici-succ n) term
    =_{MariciRational}
    marici-rational-add
      (marici-rational-finite-sum n term)
      (term n)
  := refl
```

## Boundary

This is finite recursion only. It supplies no completed infinite sum,
convergence, or finite-to-global promotion. A Dirichlet partial sum additionally
needs a checked positive-natural reciprocal-power term.
