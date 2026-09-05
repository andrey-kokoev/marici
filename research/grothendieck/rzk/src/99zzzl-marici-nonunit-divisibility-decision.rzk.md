# Deciding divisibility by a nonunit natural

Compute bounded division and decide whether its remainder is zero. A zero path
constructs a divisibility witness from reconstruction; a nonzero refutation
composes with the theorem that divisibility forces zero remainder.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatDivisibilityDecision
  ( divisor value : MariciNat)
  := marici-nat-divides-yes
      ( witness : MariciNatDivides divisor value)
  | marici-nat-divides-no
      ( refutation : MariciNatDivides divisor value → MariciEmpty)

#define marici-decide-nonunit-natural-divisibility-from-state
  ( divisor-residual value : MariciNat)
  ( state : MariciNatDivisionState (marici-succ divisor-residual) value)
  : MariciNatDivisibilityDecision
      (marici-succ (marici-succ divisor-residual)) value
  := match state
      ( marici-nat-division-state quotient remainder
          remainder-bounded reconstruction ⇒
        match (marici-nat-decide-equality remainder marici-zero)
        ( marici-nat-equal remainder-zero ⇒
            marici-nat-divides-yes
              (marici-succ (marici-succ divisor-residual)) value
              (marici-division-zero-remainder-gives-divides
                (marici-succ divisor-residual) value quotient
                (concat MariciNat
                  (marici-add
                    (marici-mul quotient
                      (marici-succ (marici-succ divisor-residual)))
                    marici-zero)
                  (marici-add
                    (marici-mul quotient
                      (marici-succ (marici-succ divisor-residual)))
                    remainder)
                  value
                  (ap MariciNat MariciNat marici-zero remainder
                    (\ remainder-prime → marici-add
                      (marici-mul quotient
                        (marici-succ (marici-succ divisor-residual)))
                      remainder-prime)
                    (rev MariciNat remainder marici-zero remainder-zero))
                  reconstruction))
        | marici-nat-unequal remainder-nonzero ⇒
            marici-nat-divides-no
              (marici-succ (marici-succ divisor-residual)) value
              (\ divides → remainder-nonzero
                (marici-divisibility-forces-division-remainder-zero
                  (marici-succ divisor-residual) value
                  (marici-nat-division-state
                    (marici-succ divisor-residual) value
                    quotient remainder remainder-bounded reconstruction)
                  divides))))

#define marici-decide-nonunit-natural-divisibility
  ( divisor-residual value : MariciNat)
  : MariciNatDivisibilityDecision
      (marici-succ (marici-succ divisor-residual)) value
  := marici-decide-nonunit-natural-divisibility-from-state
      divisor-residual value
      (marici-nat-divide-by-nonunit divisor-residual value)
```

## Boundary

Divisibility by every natural divisor at least two is now executable and
soundly decided. The no-proper-factor Euclid branch can use this decision to
split whether the irreducible divisor divides the first product factor; the
coprimality hypothesis eliminates that case, while the complementary case must
force divisibility of the second factor.
