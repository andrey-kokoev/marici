# Divisibility descends to the product remainder

Given `x = qd+r`, distributivity rewrites `xz` as the explicit divisor multiple
`(qz)d` plus `rz`. Removing that multiple prefix transports divisibility of
`xz` to divisibility of `rz`.

```rzk
#lang rzk-1
```

```rzk
#define marici-division-product-expansion
  ( divisor-predecessor x z quotient remainder : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} x)
  : marici-mul x z =_{MariciNat}
      marici-add
        (marici-mul (marici-mul quotient z)
          (marici-succ divisor-predecessor))
        (marici-mul remainder z)
  := concat MariciNat
      (marici-mul x z)
      (marici-mul
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
        z)
      (marici-add
        (marici-mul (marici-mul quotient z)
          (marici-succ divisor-predecessor))
        (marici-mul remainder z))
      (ap MariciNat MariciNat x
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
        (\ value → marici-mul value z)
        (rev MariciNat
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
          x reconstruction))
      (concat MariciNat
        (marici-mul
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
          z)
        (marici-add
          (marici-mul
            (marici-mul quotient (marici-succ divisor-predecessor)) z)
          (marici-mul remainder z))
        (marici-add
          (marici-mul (marici-mul quotient z)
            (marici-succ divisor-predecessor))
          (marici-mul remainder z))
        (marici-mul-add-left-distrib
          (marici-mul quotient (marici-succ divisor-predecessor))
          remainder z)
        (ap MariciNat MariciNat
          (marici-mul
            (marici-mul quotient (marici-succ divisor-predecessor)) z)
          (marici-mul (marici-mul quotient z)
            (marici-succ divisor-predecessor))
          (\ prefix → marici-add prefix (marici-mul remainder z))
          (concat MariciNat
            (marici-mul
              (marici-mul quotient (marici-succ divisor-predecessor)) z)
            (marici-mul quotient
              (marici-mul (marici-succ divisor-predecessor) z))
            (marici-mul (marici-mul quotient z)
              (marici-succ divisor-predecessor))
            (marici-mul-assoc
              quotient (marici-succ divisor-predecessor) z)
            (concat MariciNat
              (marici-mul quotient
                (marici-mul (marici-succ divisor-predecessor) z))
              (marici-mul quotient
                (marici-mul z (marici-succ divisor-predecessor)))
              (marici-mul (marici-mul quotient z)
                (marici-succ divisor-predecessor))
              (ap MariciNat MariciNat
                (marici-mul (marici-succ divisor-predecessor) z)
                (marici-mul z (marici-succ divisor-predecessor))
                (\ value → marici-mul quotient value)
                (marici-mul-comm (marici-succ divisor-predecessor) z))
              (rev MariciNat
                (marici-mul (marici-mul quotient z)
                  (marici-succ divisor-predecessor))
                (marici-mul quotient
                  (marici-mul z (marici-succ divisor-predecessor)))
                (marici-mul-assoc
                  quotient z (marici-succ divisor-predecessor)))))))

#define marici-division-product-divisibility-descends
  ( divisor-predecessor x z quotient remainder : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} x)
  ( divides-product : MariciNatDivides
      (marici-succ divisor-predecessor) (marici-mul x z))
  : MariciNatDivides
      (marici-succ divisor-predecessor) (marici-mul remainder z)
  := marici-nat-divisibility-removes-multiple-prefix
      divisor-predecessor (marici-mul quotient z)
      (marici-mul remainder z)
      (marici-nat-divides-reindex-value
        (marici-succ divisor-predecessor)
        (marici-mul x z)
        (marici-add
          (marici-mul (marici-mul quotient z)
            (marici-succ divisor-predecessor))
          (marici-mul remainder z))
        (marici-division-product-expansion
          divisor-predecessor x z quotient remainder reconstruction)
        divides-product)
```

## Boundary

For any bounded or unbounded division reconstruction, divisibility of `xz`
now descends to `rz`. In irreducible Euclid, the computed remainder is strictly
below the divisor; proving it coprime to the irreducible divisor will allow a
smaller-factor induction to conclude divisibility of `z`.
