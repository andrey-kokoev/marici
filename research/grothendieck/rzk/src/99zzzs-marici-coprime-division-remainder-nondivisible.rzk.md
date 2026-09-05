# A coprime division remainder is not divisible by the divisor

Divisibility is closed under addition: cofactor addition witnesses divisibility
of a sum. Therefore, in a reconstruction `x=qd+r`, divisibility of `r` by `d`
would make `d` divide `x`. When `d` is nonunit and coprime to `x`, this is
impossible.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-divides-add
  ( divisor left right : MariciNat)
  ( divides-left : MariciNatDivides divisor left)
  ( divides-right : MariciNatDivides divisor right)
  : MariciNatDivides divisor (marici-add left right)
  := match divides-left
      ( marici-nat-divides-witness left-cofactor left-equation ⇒
        match divides-right
        ( marici-nat-divides-witness right-cofactor right-equation ⇒
          marici-nat-divides-witness divisor (marici-add left right)
            (marici-add left-cofactor right-cofactor)
            (concat MariciNat
              (marici-mul
                (marici-add left-cofactor right-cofactor) divisor)
              (marici-add
                (marici-mul left-cofactor divisor)
                (marici-mul right-cofactor divisor))
              (marici-add left right)
              (marici-mul-add-left-distrib
                left-cofactor right-cofactor divisor)
              (concat MariciNat
                (marici-add
                  (marici-mul left-cofactor divisor)
                  (marici-mul right-cofactor divisor))
                (marici-add left (marici-mul right-cofactor divisor))
                (marici-add left right)
                (ap MariciNat MariciNat
                  (marici-mul left-cofactor divisor) left
                  (\ value → marici-add value
                    (marici-mul right-cofactor divisor))
                  left-equation)
                (ap MariciNat MariciNat
                  (marici-mul right-cofactor divisor) right
                  (\ value → marici-add left value)
                  right-equation)))))

#define marici-explicit-multiple-plus-divisible-residual-divides
  ( divisor prefix-coefficient residual : MariciNat)
  ( divides-residual : MariciNatDivides divisor residual)
  : MariciNatDivides divisor
      (marici-add (marici-mul prefix-coefficient divisor) residual)
  := marici-nat-divides-add divisor
      (marici-mul prefix-coefficient divisor) residual
      (marici-nat-divides-witness divisor
        (marici-mul prefix-coefficient divisor)
        prefix-coefficient refl)
      divides-residual

#define marici-coprime-division-remainder-not-divisible
  ( factor-predecessor x quotient remainder : MariciNat)
  ( coprime : MariciNatAreCoprime x
      (marici-succ (marici-succ factor-predecessor)))
  ( reconstruction : marici-add
      (marici-mul quotient
        (marici-succ (marici-succ factor-predecessor))) remainder
    =_{MariciNat} x)
  : MariciNatDivides
      (marici-succ (marici-succ factor-predecessor)) remainder
    → MariciEmpty
  := \ divides-remainder →
      marici-coprime-excludes-whole-nonunit-divisor
        x factor-predecessor coprime
        (marici-nat-divides-reindex-value
          (marici-succ (marici-succ factor-predecessor))
          (marici-add
            (marici-mul quotient
              (marici-succ (marici-succ factor-predecessor))) remainder)
          x reconstruction
          (marici-explicit-multiple-plus-divisible-residual-divides
            (marici-succ (marici-succ factor-predecessor))
            quotient remainder divides-remainder))
```

## Boundary

The remainder in any division reconstruction of a value coprime to a nonunit
divisor is now provably nondivisible by that divisor. Combined with
irreducibility, this makes the remainder coprime to the divisor and supplies
the recursive premise for irreducible Euclid.
