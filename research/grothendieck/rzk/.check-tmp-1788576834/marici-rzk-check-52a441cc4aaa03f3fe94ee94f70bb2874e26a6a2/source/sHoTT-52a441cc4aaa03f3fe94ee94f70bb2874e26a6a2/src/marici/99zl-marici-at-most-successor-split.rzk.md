# Splitting a bound at its successor endpoint

A witness that a candidate lies at most at a successor either has zero gap, in
which case the candidate is the endpoint, or successor gap, in which case
successor injectivity lowers the bound.

```rzk
#lang rzk-1
```

```rzk
#data MariciAtMostSuccessorSplit
  ( candidate bound : MariciNat)
  := marici-at-most-strictly-below-successor
      ( below : MariciNatAtMost candidate bound)
  | marici-at-most-equal-successor
      ( endpoint : candidate =_{MariciNat} marici-succ bound)

#define marici-at-most-lift-successor
  ( q n : MariciNat)
  ( bounded : MariciNatAtMost q n)
  : MariciNatAtMost q (marici-succ n)
  := match bounded
      ( marici-nat-at-most-witness gap equation ⇒
          marici-nat-at-most-witness q (marici-succ n)
            (marici-succ gap)
            (ap MariciNat MariciNat
              (marici-add gap q) n marici-succ equation))

#define marici-at-most-successor-split
  ( q n : MariciNat)
  ( bounded : MariciNatAtMost q (marici-succ n))
  : MariciAtMostSuccessorSplit q n
  := match bounded
      ( marici-nat-at-most-witness gap equation ⇒
          (match gap into
            (\ gap-prime →
              (marici-add gap-prime q =_{MariciNat} marici-succ n)
              → MariciAtMostSuccessorSplit q n)
          ( marici-zero ⇒ \ eq →
              marici-at-most-equal-successor q n eq
          | marici-succ h ih ⇒ \ eq →
              marici-at-most-strictly-below-successor q n
                (marici-nat-at-most-witness q n h
                  (marici-succ-injective
                    (marici-add h q) n eq)))) equation)
```

## Boundary

Bounded cofactor induction can now separate its newly tested endpoint from the
previous search interval and lift earlier hits into the larger interval. The
bounded decision theorem still needs to combine this split with accumulated
refutations.
