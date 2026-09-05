# Irreducible nonunit divisors are the whole value

For a value at least three, define irreducibility by refuting every exact
nonunit factorization whose factor index lies in the proper search interval.
Then any nonunit divisor of the value equals the whole value: a zero cofactor is
impossible, a unit cofactor gives equality, and a nonunit cofactor makes the
divisor proper by strict factor-removal decrease.

```rzk
#lang rzk-1
```

```rzk
#define MariciNatNoProperNonunitFactor
  ( residual : MariciNat)
  : U
  := ( factor-predecessor cofactor-predecessor : MariciNat)
    → MariciNatAtMost factor-predecessor residual
    → (marici-mul (marici-succ cofactor-predecessor)
        (marici-succ (marici-succ factor-predecessor))
      =_{MariciNat}
      marici-succ (marici-succ (marici-succ residual)))
    → MariciEmpty

#define marici-irreducible-nonunit-divisor-rigid
  ( residual factor-predecessor : MariciNat)
  ( irreducible : MariciNatNoProperNonunitFactor residual)
  ( divides : MariciNatDivides
      (marici-succ (marici-succ factor-predecessor))
      (marici-succ (marici-succ (marici-succ residual))))
  : marici-succ (marici-succ factor-predecessor)
      =_{MariciNat}
    marici-succ (marici-succ (marici-succ residual))
  := match divides into
      (\ divides-prime →
        marici-succ (marici-succ factor-predecessor)
          =_{MariciNat}
        marici-succ (marici-succ (marici-succ residual)))
      ( marici-nat-divides-witness cofactor equation ⇒
        (match cofactor into
        (\ cofactor-prime →
          (marici-mul cofactor-prime
              (marici-succ (marici-succ factor-predecessor))
            =_{MariciNat}
            marici-succ (marici-succ (marici-succ residual)))
          → marici-succ (marici-succ factor-predecessor)
              =_{MariciNat}
            marici-succ (marici-succ (marici-succ residual)))
        ( marici-zero ⇒ \ zero-equation →
            marici-empty-elim
              (marici-succ (marici-succ factor-predecessor)
                =_{MariciNat}
               marici-succ (marici-succ (marici-succ residual)))
              (marici-zero-not-succ
                (marici-succ (marici-succ residual)) zero-equation)
        | marici-succ q ih ⇒
            match q into
            (\ q-prime →
              (marici-mul (marici-succ q-prime)
                  (marici-succ (marici-succ factor-predecessor))
                =_{MariciNat}
                marici-succ (marici-succ (marici-succ residual)))
              → marici-succ (marici-succ factor-predecessor)
                  =_{MariciNat}
                marici-succ (marici-succ (marici-succ residual)))
            ( marici-zero ⇒ \ unit-equation →
                concat MariciNat
                  (marici-succ (marici-succ factor-predecessor))
                  (marici-mul (marici-succ marici-zero)
                    (marici-succ (marici-succ factor-predecessor)))
                  (marici-succ (marici-succ (marici-succ residual)))
                  (rev MariciNat
                    (marici-mul (marici-succ marici-zero)
                      (marici-succ (marici-succ factor-predecessor)))
                    (marici-succ (marici-succ factor-predecessor))
                    (marici-add-zero-right
                      (marici-succ (marici-succ factor-predecessor))))
                  unit-equation
            | marici-succ h h-ih ⇒ \ nonunit-equation →
                marici-empty-elim
                  (marici-succ (marici-succ factor-predecessor)
                    =_{MariciNat}
                   marici-succ (marici-succ (marici-succ residual)))
                  (irreducible h (marici-succ factor-predecessor)
                    (marici-at-most-successors-descend h residual
                      (marici-strictly-less-successor-gives-at-most
                        (marici-succ h) (marici-succ residual)
                        (marici-nonunit-positive-factor-decreases
                          (marici-succ (marici-succ residual))
                          (marici-succ h) factor-predecessor
                          nonunit-equation)))
                    (concat MariciNat
                      (marici-mul
                        (marici-succ (marici-succ factor-predecessor))
                        (marici-succ (marici-succ h)))
                      (marici-mul
                        (marici-succ (marici-succ h))
                        (marici-succ (marici-succ factor-predecessor)))
                      (marici-succ
                        (marici-succ (marici-succ residual)))
                      (marici-mul-comm
                        (marici-succ (marici-succ factor-predecessor))
                        (marici-succ (marici-succ h)))
                      nonunit-equation)))
            )) equation)
```

## Boundary

Every nonunit divisor of a value with no proper nonunit factor is now equal to
the value. Connecting a proper-factor search miss to the irreducibility
predicate is mechanical certificate projection. The Euclid branch still needs
the additive division argument that converts this divisor rigidity into the
prime-divisor property for products.
