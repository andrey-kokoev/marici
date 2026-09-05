# The bounded extended-Euclid step at a nonunit divisor

Assume Bézout certificates are available whenever the positive second
coordinate's predecessor lies below `n`. Divide `x` by `n+2`. A zero remainder
would make the nonunit divisor divide its coprime partner and is impossible. A
positive remainder has predecessor at most `n`; recurse on the swapped pair,
restore orientation by symmetry, and lift through division.

```rzk
#lang rzk-1
```

```rzk
#define MariciPositiveBezoutAvailableUpTo
  ( bound : MariciNat)
  : U
  := ( second-predecessor : MariciNat)
    → MariciNatAtMost second-predecessor bound
    → ( left-value : MariciNat)
    → MariciNatAreCoprime left-value (marici-succ second-predecessor)
    → MariciNatBezoutDifference left-value (marici-succ second-predecessor)

#define marici-bezout-nonunit-bounded-step-from-state
  ( bound x : MariciNat)
  ( previous : MariciPositiveBezoutAvailableUpTo bound)
  ( coprime : MariciNatAreCoprime x
      (marici-succ (marici-succ bound)))
  ( state : MariciNatDivisionState (marici-succ bound) x)
  : MariciNatBezoutDifference x (marici-succ (marici-succ bound))
  := match state
      ( marici-nat-division-state quotient remainder
          remainder-bounded reconstruction ⇒
        (match remainder into
          (\ remainder-prime →
            MariciNatAtMost remainder-prime (marici-succ bound)
            → (marici-add
                (marici-mul quotient (marici-succ (marici-succ bound)))
                remainder-prime
              =_{MariciNat} x)
            → MariciNatBezoutDifference x
                (marici-succ (marici-succ bound)))
          ( marici-zero ⇒ \ zero-bounded zero-reconstruction →
              marici-empty-elim
                (MariciNatBezoutDifference x
                  (marici-succ (marici-succ bound)))
                (marici-coprime-excludes-whole-nonunit-divisor
                  x bound coprime
                  (marici-division-zero-remainder-gives-divides
                    (marici-succ bound) x quotient zero-reconstruction))
          | marici-succ remainder-predecessor remainder-ih ⇒
              \ positive-bounded positive-reconstruction →
                marici-natural-bezout-lifts-through-division
                  x (marici-succ (marici-succ bound)) quotient
                  (marici-succ remainder-predecessor)
                  positive-reconstruction
                  (marici-natural-bezout-difference-symmetric
                    (marici-succ (marici-succ bound))
                    (marici-succ remainder-predecessor)
                    (previous remainder-predecessor
                      (marici-at-most-successors-descend
                        remainder-predecessor bound positive-bounded)
                      (marici-succ (marici-succ bound))
                      (marici-nat-coprime-division-pair-swaps
                        x (marici-succ (marici-succ bound)) quotient
                        (marici-succ remainder-predecessor) coprime
                        positive-reconstruction)))))
          remainder-bounded reconstruction)

#define marici-bezout-nonunit-bounded-step
  ( bound x : MariciNat)
  ( previous : MariciPositiveBezoutAvailableUpTo bound)
  ( coprime : MariciNatAreCoprime x
      (marici-succ (marici-succ bound)))
  : MariciNatBezoutDifference x (marici-succ (marici-succ bound))
  := marici-bezout-nonunit-bounded-step-from-state
      bound x previous coprime
      (marici-nat-divide-by-nonunit bound x)
```

## Boundary

The difficult endpoint of bounded extended Euclid is now complete: certificate
availability through predecessor bound `n` yields the certificate for second
coordinate `n+2`. It uses only total division, strict remainder boundedness,
coprimality descent, symmetry, and the checked coefficient lift. The outer
bounded induction that combines this endpoint with inherited lower cases
remains.
