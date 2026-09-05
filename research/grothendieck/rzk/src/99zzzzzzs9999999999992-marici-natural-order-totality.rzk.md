# Natural additive-gap order is total

Every pair of naturals is comparable in the additive-gap order. Simultaneous
successors preserve an existing gap equation, while either zero endpoint has an
explicit gap given by the other natural.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatAtMostComparison
  ( m n : MariciNat)
  := marici-nat-comparison-left
      ( witness : MariciNatAtMost m n)
  | marici-nat-comparison-right
      ( witness : MariciNatAtMost n m)

#define marici-nat-at-most-successors
  ( m n : MariciNat)
  ( witness : MariciNatAtMost m n)
  : MariciNatAtMost (marici-succ m) (marici-succ n)
  := match witness
      ( marici-nat-at-most-witness gap equation ⇒
          marici-nat-at-most-witness
            (marici-succ m) (marici-succ n) gap
            (concat MariciNat
              (marici-add gap (marici-succ m))
              (marici-succ (marici-add gap m))
              (marici-succ n)
              (marici-add-succ-right gap m)
              (ap MariciNat MariciNat
                (marici-add gap m) n marici-succ equation)))

#define marici-nat-at-most-total
  ( m : MariciNat)
  : (n : MariciNat) → MariciNatAtMostComparison m n
  := match m into
      (\ m-prime → (n : MariciNat) → MariciNatAtMostComparison m-prime n)
      ( marici-zero ⇒ \ n →
          marici-nat-comparison-left marici-zero n
            (marici-nat-at-most-witness marici-zero n n
              (marici-add-zero-right n))
      | marici-succ m-prime induction ⇒ \ n →
          match n into
            (\ n-prime → MariciNatAtMostComparison
              (marici-succ m-prime) n-prime)
          ( marici-zero ⇒
              marici-nat-comparison-right
                (marici-succ m-prime) marici-zero
                (marici-nat-at-most-witness
                  marici-zero (marici-succ m-prime)
                  (marici-succ m-prime)
                  (marici-add-zero-right (marici-succ m-prime)))
          | marici-succ n-prime n-induction ⇒
              match (induction n-prime)
              ( marici-nat-comparison-left bound ⇒
                  marici-nat-comparison-left
                    (marici-succ m-prime) (marici-succ n-prime)
                    (marici-nat-at-most-successors
                      m-prime n-prime bound)
              | marici-nat-comparison-right bound ⇒
                  marici-nat-comparison-right
                    (marici-succ m-prime) (marici-succ n-prime)
                    (marici-nat-at-most-successors
                      n-prime m-prime bound)))
          )
```

## Boundary

Arbitrary natural indices can now be split into the two ordered cases required
for the Cauchy estimate. Each bound witness still must be converted into the
explicit successor-cutoff-plus-length equation consumed by the ordered partial-
sum theorem.
