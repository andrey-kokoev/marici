# Subtracting two negated rationals reverses the subtraction

Unfolding subtraction gives addition of the first argument and the negation of
the second. Negation involution removes the inner double negation, and rational
addition commutativity exchanges the two summands.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-subtract-negations-components
  ( p q : MariciRational)
  : marici-rational-forget
      (marici-rational-subtract
        (marici-rational-negate p)
        (marici-rational-negate q))
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-subtract q p)
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-negate p)
          (marici-rational-negate q)))
      (marici-rational-forget
        (marici-rational-add (marici-rational-negate p) q))
      (marici-rational-forget (marici-rational-subtract q p))
      (marici-rational-add-component-congruent
        (marici-rational-negate p) (marici-rational-negate p)
        (marici-rational-negate (marici-rational-negate q)) q
        refl
        (marici-rational-negate-involutive-components q))
      (marici-rational-add-comm-components
        (marici-rational-negate p) q)
```

## Boundary

The result is equality of canonical rational components. It supplies the
algebraic step needed to prove that rational distance is invariant under
simultaneous negation; it does not yet construct negation on the real quotient.
