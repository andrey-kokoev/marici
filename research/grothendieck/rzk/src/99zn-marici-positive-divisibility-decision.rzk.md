# Total positive-natural divisibility decision

The target predecessor is a complete cofactor bound. The bounded decision's
positive branch yields the indexed divisibility witness; its negative branch
refutes any alleged witness using the global cofactor-bound theorem.

```rzk
#lang rzk-1
```

```rzk
#data MariciPositiveNatRightDivisibilityDecision
  ( factor-predecessor value-predecessor : MariciNat)
  := marici-positive-nat-right-divisible
      ( witness : MariciPositiveNatRightDivides
          factor-predecessor value-predecessor)
  | marici-positive-nat-right-indivisible
      ( refutation : MariciPositiveNatRightDivides
          factor-predecessor value-predecessor → MariciEmpty)

#define marici-decide-positive-nat-right-divisibility
  ( factor value : MariciNat)
  : MariciPositiveNatRightDivisibilityDecision factor value
  := match (marici-decide-positive-cofactor-bounded value factor value)
      ( marici-bounded-positive-cofactor-found q bounded equation ⇒
          marici-positive-nat-right-divisible factor value
            (marici-positive-nat-right-divides-witness
              factor value q equation)
      | marici-bounded-positive-cofactor-absent refutation ⇒
          marici-positive-nat-right-indivisible factor value
            (\ witness → match witness
              ( marici-positive-nat-right-divides-witness q equation ⇒
                  refutation q
                    (marici-positive-cofactor-at-most-target
                      q factor value equation)
                    equation)))
```

A closed factor-two decision for positive four computes to the divisible branch.

```rzk
#define marici-two-right-divides-four-decision
  : MariciPositiveNatRightDivisibilityDecision marici-one marici-three
  := marici-decide-positive-nat-right-divisibility
      marici-one marici-three
```

## Boundary

Positive-natural right divisibility is now fully decidable with witnesses or
universal refutations. Common-factor selection must combine denominator and
integer-magnitude decisions across candidate factors; well-founded
normalization and reduced-representative uniqueness remain open.
