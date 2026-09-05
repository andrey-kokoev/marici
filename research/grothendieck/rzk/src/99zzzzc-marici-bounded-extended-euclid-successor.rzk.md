# Successor bound for extended Euclid

Certificate availability through predecessor bound `n` extends through
`n+1`. Explicit at-most splitting either returns an inherited lower case or
identifies the new endpoint; transport aligns that endpoint with the checked
nonunit division step.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-bezout-available-successor
  ( n : MariciNat)
  ( previous : MariciPositiveBezoutAvailableUpTo n)
  : MariciPositiveBezoutAvailableUpTo (marici-succ n)
  := \ k bounded a coprime →
      match (marici-at-most-successor-split k n bounded)
      ( marici-at-most-strictly-below-successor below ⇒
          previous k below a coprime
      | marici-at-most-equal-successor endpoint ⇒
          transport MariciNat
            (\ index →
              MariciNatBezoutDifference a (marici-succ index))
            (marici-succ n) k
            (rev MariciNat k (marici-succ n) endpoint)
            (marici-bezout-nonunit-bounded-step n a previous
              (transport MariciNat
                (\ index → MariciNatAreCoprime a (marici-succ index))
                k (marici-succ n) endpoint coprime)))
```

## Boundary

The successor constructor for bounded positive-coordinate extended Euclid is
checked. Together with the zero-bound base, ordinary natural induction can now
produce certificate availability at every external predecessor bound.
