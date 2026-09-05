# Divisibility removes an explicit multiple prefix

If a positive divisor divides a sum consisting of an explicit multiple prefix
and a residual, then it divides the residual. Quotient-gap trichotomy compares
the supplied divisibility cofactor with the explicit prefix coefficient. A
larger supplied cofactor exhibits the residual as a multiple, equality makes it
zero, and a smaller supplied cofactor is impossible.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-divisibility-removes-multiple-prefix
  ( divisor-predecessor prefix-coefficient residual : MariciNat)
  ( divides : MariciNatDivides (marici-succ divisor-predecessor)
      (marici-add
        (marici-mul prefix-coefficient
          (marici-succ divisor-predecessor)) residual))
  : MariciNatDivides (marici-succ divisor-predecessor) residual
  := match divides
      ( marici-nat-divides-witness witness-quotient witness-equation ⇒
        match (marici-nat-gap-trichotomy
          prefix-coefficient witness-quotient)
        ( marici-nat-gap-less gap quotient-gap ⇒
            marici-nat-divides-witness
              (marici-succ divisor-predecessor) residual
              (marici-succ gap)
              (rev MariciNat residual
                (marici-mul (marici-succ gap)
                  (marici-succ divisor-predecessor))
                (marici-division-smaller-quotient-remainder-product
                  divisor-predecessor
                  (marici-add
                    (marici-mul prefix-coefficient
                      (marici-succ divisor-predecessor)) residual)
                  prefix-coefficient witness-quotient residual gap
                  refl witness-equation quotient-gap))
        | marici-nat-gap-equal quotients-equal ⇒
            marici-nat-divides-witness
              (marici-succ divisor-predecessor) residual marici-zero
              (concat MariciNat
                (marici-mul marici-zero
                  (marici-succ divisor-predecessor))
                marici-zero residual refl
                (rev MariciNat residual marici-zero
                  (marici-division-equal-quotient-remainder-zero
                    divisor-predecessor
                    (marici-add
                      (marici-mul prefix-coefficient
                        (marici-succ divisor-predecessor)) residual)
                    prefix-coefficient witness-quotient residual
                    refl witness-equation quotients-equal)))
        | marici-nat-gap-greater gap quotient-gap ⇒
            marici-empty-elim
              (MariciNatDivides
                (marici-succ divisor-predecessor) residual)
              (marici-division-greater-quotient-impossible
                divisor-predecessor
                (marici-add
                  (marici-mul prefix-coefficient
                    (marici-succ divisor-predecessor)) residual)
                prefix-coefficient witness-quotient residual gap
                refl witness-equation quotient-gap)))
```

## Boundary

A known multiple summand can now be removed from a divisibility assertion
without subtraction. Expanding `x = qd+r` inside `xz` and reassociating it as
an explicit `d`-multiple plus `rz` will therefore yield `d | rz`, the descent
step required by additive division induction for irreducible Euclid.
