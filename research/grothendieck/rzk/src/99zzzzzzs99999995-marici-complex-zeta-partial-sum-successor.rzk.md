# Complex zeta approximants satisfy the finite successor recurrence

Applying the rational-to-complex map to the checked rational finite-sum
recurrence identifies each successor approximant with the embedded rational sum
of the preceding approximant and its next Dirichlet term.

```rzk
#lang rzk-1
```

```rzk
#define marici-zeta-complex-partial-sum-successor
  ( bound exponent : MariciNat)
  : marici-zeta-complex-partial-sum (marici-succ bound) exponent
    =_{MariciComplex}
    marici-rational-to-complex
      (marici-rational-add
        (marici-zeta-dirichlet-partial-sum bound exponent)
        (marici-rational-dirichlet-term exponent bound))
  := ap MariciRational MariciComplex
      (marici-zeta-dirichlet-partial-sum
        (marici-succ bound) exponent)
      (marici-rational-add
        (marici-zeta-dirichlet-partial-sum bound exponent)
        (marici-rational-dirichlet-term exponent bound))
      marici-rational-to-complex
      (marici-zeta-dirichlet-partial-sum-successor bound exponent)
```

## Boundary

This is a recurrence for finite complex-valued approximants, not complex
addition or convergence. A Cauchy theorem still requires quantitative bounds on
Dirichlet tails for a stated exponent range.
