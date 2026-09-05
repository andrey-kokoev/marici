# Finite rational summation is monotone

Pointwise rational order bounds fold through finite summation. The zero case is
reflexivity, and the successor case combines the induction witness with the
next pointwise witness using joint addition monotonicity.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-finite-sum-at-most
  ( lower upper : MariciNat → MariciRational)
  ( pointwise : (index : MariciNat)
    → MariciRationalAtMost (lower index) (upper index))
  ( bound : MariciNat)
  : MariciRationalAtMost
      (marici-rational-finite-sum bound lower)
      (marici-rational-finite-sum bound upper)
  := match bound
      ( marici-zero ⇒
          marici-rational-at-most-reflexive marici-rational-zero
      | marici-succ k induction ⇒
          marici-rational-add-at-most
            (marici-rational-finite-sum k lower)
            (marici-rational-finite-sum k upper)
            (lower k) (upper k)
            induction (pointwise k))
```

## Boundary

Finite rational sums now preserve pointwise inequalities. The exponent-two
Dirichlet tail proof still needs a pointwise telescoping majorant and a finite
identity collapsing the majorant sum to its boundary terms.
