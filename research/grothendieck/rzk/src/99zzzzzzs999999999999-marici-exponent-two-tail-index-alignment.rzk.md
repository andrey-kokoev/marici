# Exponent-two shifted-tail indices align

Natural addition's successor-right law identifies `index + succ cutoff` with
`succ (index + cutoff)`. Function congruence transports this index path through
the Dirichlet term, and finite-sum congruence folds the pointwise paths.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-finite-sum-congruent
  ( lower upper : MariciNat → MariciRational)
  ( pointwise : (index : MariciNat)
    → lower index =_{MariciRational} upper index)
  ( bound : MariciNat)
  : marici-rational-finite-sum bound lower
    =_{MariciRational}
    marici-rational-finite-sum bound upper
  := match bound
      ( marici-zero ⇒ refl
      | marici-succ k induction ⇒
          concat MariciRational
            (marici-rational-add
              (marici-rational-finite-sum k lower) (lower k))
            (marici-rational-add
              (marici-rational-finite-sum k upper) (lower k))
            (marici-rational-add
              (marici-rational-finite-sum k upper) (upper k))
            (ap MariciRational MariciRational
              (marici-rational-finite-sum k lower)
              (marici-rational-finite-sum k upper)
              (\ partial → marici-rational-add partial (lower k))
              induction)
            (ap MariciRational MariciRational
              (lower k) (upper k)
              (\ next → marici-rational-add
                (marici-rational-finite-sum k upper) next)
              (pointwise k)))

#define marici-exponent-two-tail-term-index-alignment
  ( cutoff index : MariciNat)
  : marici-rational-shifted-tail-term
      (marici-succ cutoff)
      (marici-rational-dirichlet-term marici-two)
      index
    =_{MariciRational}
    marici-exponent-two-tail-term cutoff index
  := ap MariciNat MariciRational
      (marici-add index (marici-succ cutoff))
      (marici-succ (marici-add index cutoff))
      (marici-rational-dirichlet-term marici-two)
      (marici-add-succ-right index cutoff)

#define marici-exponent-two-shifted-tail-sum-alignment
  ( cutoff length : MariciNat)
  : marici-rational-finite-sum length
      (marici-rational-shifted-tail-term
        (marici-succ cutoff)
        (marici-rational-dirichlet-term marici-two))
    =_{MariciRational}
    marici-rational-finite-sum length
      (marici-exponent-two-tail-term cutoff)
  := marici-rational-finite-sum-congruent
      (marici-rational-shifted-tail-term
        (marici-succ cutoff)
        (marici-rational-dirichlet-term marici-two))
      (marici-exponent-two-tail-term cutoff)
      (marici-exponent-two-tail-term-index-alignment cutoff)
      length
```

## Boundary

The independently folded tail extracted after the successor cutoff is now equal
to the tail family covered by the uniform estimate. Transporting the longer
initial sum through shifted accumulation completes the ordered partial-sum
difference bound.
