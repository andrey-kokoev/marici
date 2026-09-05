# Successor update for division by a nonunit natural

For divisors at least two, splitting a bounded remainder against its endpoint
gives the executable division update. A below-endpoint remainder increments;
an endpoint remainder resets to zero and increments the quotient.

```rzk
#lang rzk-1
```

```rzk
#define marici-at-most-successors
  ( r d : MariciNat)
  ( bounded : MariciNatAtMost r d)
  : MariciNatAtMost (marici-succ r) (marici-succ d)
  := match bounded
      ( marici-nat-at-most-witness gap equation ⇒
        marici-nat-at-most-witness
          (marici-succ r) (marici-succ d) gap
          (concat MariciNat
            (marici-add gap (marici-succ r))
            (marici-succ (marici-add gap r))
            (marici-succ d)
            (marici-add-succ-right gap r)
            (ap MariciNat MariciNat
              (marici-add gap r) d marici-succ equation)))

#define marici-nat-division-successor-state-nonunit
  ( d value : MariciNat)
  ( state : MariciNatDivisionState (marici-succ d) value)
  : MariciNatDivisionState (marici-succ d) (marici-succ value)
  := match state
      ( marici-nat-division-state q r bounded reconstruction ⇒
        match (marici-at-most-successor-split r d bounded)
        ( marici-at-most-strictly-below-successor below ⇒
            marici-nat-division-state
              (marici-succ d) (marici-succ value)
              q (marici-succ r)
              (marici-at-most-successors r d below)
              (marici-division-increment-remainder-equation
                q (marici-succ d) r value reconstruction)
        | marici-at-most-equal-successor endpoint ⇒
            marici-nat-division-state
              (marici-succ d) (marici-succ value)
              (marici-succ q) marici-zero
              (marici-zero-at-most (marici-succ d))
              (concat MariciNat
                (marici-add
                  (marici-mul (marici-succ q)
                    (marici-succ (marici-succ d)))
                  marici-zero)
                (marici-succ
                  (marici-add
                    (marici-mul q (marici-succ (marici-succ d)))
                    (marici-succ d)))
                (marici-succ value)
                (marici-division-carry-product-equation q (marici-succ d))
                (ap MariciNat MariciNat
                  (marici-add
                    (marici-mul q (marici-succ (marici-succ d)))
                    (marici-succ d))
                  value marici-succ
                  (concat MariciNat
                    (marici-add
                      (marici-mul q (marici-succ (marici-succ d)))
                      (marici-succ d))
                    (marici-add
                      (marici-mul q (marici-succ (marici-succ d))) r)
                    value
                    (ap MariciNat MariciNat
                      (marici-succ d) r
                      (\ remainder → marici-add
                        (marici-mul q
                          (marici-succ (marici-succ d))) remainder)
                      (rev MariciNat r (marici-succ d) endpoint))
                    reconstruction)))))
```

## Boundary

The division-state successor transition is executable for every divisor at
least two. Primitive recursion over the value can now construct total quotient
and bounded remainder data for precisely the nonunit divisors required by the
irreducible Euclid branch.
