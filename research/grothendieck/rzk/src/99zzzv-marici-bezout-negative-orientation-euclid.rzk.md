# The negative Bézout orientation implies Euclid

For the opposite natural difference orientation `vy+1=ux`, scaling by `z`
identifies `(vy)z+z` with `(ux)z`. The product hypothesis makes the right side
divisible by `y`; the explicit left summand is also divisible by `y`, so
summand removal yields `y|z`.

```rzk
#lang rzk-1
```

```rzk
#define marici-bezout-right-scaled-equation
  ( x y z u v : MariciNat)
  ( bezout : marici-add (marici-mul v y) (marici-succ marici-zero)
    =_{MariciNat} marici-mul u x)
  : marici-add (marici-mul (marici-mul v y) z) z
      =_{MariciNat} marici-mul (marici-mul u x) z
  := concat MariciNat
      (marici-add (marici-mul (marici-mul v y) z) z)
      (marici-add
        (marici-mul (marici-mul v y) z)
        (marici-mul (marici-succ marici-zero) z))
      (marici-mul (marici-mul u x) z)
      (ap MariciNat MariciNat z
        (marici-mul (marici-succ marici-zero) z)
        (\ value → marici-add (marici-mul (marici-mul v y) z) value)
        (rev MariciNat
          (marici-mul (marici-succ marici-zero) z) z
          (marici-mul-one-left z)))
      (concat MariciNat
        (marici-add
          (marici-mul (marici-mul v y) z)
          (marici-mul (marici-succ marici-zero) z))
        (marici-mul
          (marici-add (marici-mul v y) (marici-succ marici-zero)) z)
        (marici-mul (marici-mul u x) z)
        (rev MariciNat
          (marici-mul
            (marici-add (marici-mul v y) (marici-succ marici-zero)) z)
          (marici-add
            (marici-mul (marici-mul v y) z)
            (marici-mul (marici-succ marici-zero) z))
          (marici-mul-add-left-distrib
            (marici-mul v y) (marici-succ marici-zero) z))
        (ap MariciNat MariciNat
          (marici-add (marici-mul v y) (marici-succ marici-zero))
          (marici-mul u x)
          (\ value → marici-mul value z) bezout))

#define marici-bezout-right-implies-euclid
  ( x y z u v : MariciNat)
  ( bezout : marici-add (marici-mul v y) (marici-succ marici-zero)
    =_{MariciNat} marici-mul u x)
  ( divides-product : MariciNatDivides y (marici-mul x z))
  : MariciNatDivides y z
  := marici-nat-divisibility-removes-divisible-left-summand
      y (marici-mul (marici-mul v y) z) z
      (marici-nat-divides-witness y
        (marici-mul (marici-mul v y) z) (marici-mul v z)
        (concat MariciNat
          (marici-mul (marici-mul v z) y)
          (marici-mul (marici-mul v y) z)
          (marici-mul (marici-mul v y) z)
          (concat MariciNat
            (marici-mul (marici-mul v z) y)
            (marici-mul v (marici-mul z y))
            (marici-mul (marici-mul v y) z)
            (marici-mul-assoc v z y)
            (concat MariciNat
              (marici-mul v (marici-mul z y))
              (marici-mul v (marici-mul y z))
              (marici-mul (marici-mul v y) z)
              (ap MariciNat MariciNat
                (marici-mul z y) (marici-mul y z)
                (\ value → marici-mul v value)
                (marici-mul-comm z y))
              (rev MariciNat
                (marici-mul (marici-mul v y) z)
                (marici-mul v (marici-mul y z))
                (marici-mul-assoc v y z))))
          refl))
      (marici-nat-divides-reindex-value
        y (marici-mul (marici-mul u x) z)
        (marici-add (marici-mul (marici-mul v y) z) z)
        (rev MariciNat
          (marici-add (marici-mul (marici-mul v y) z) z)
          (marici-mul (marici-mul u x) z)
          (marici-bezout-right-scaled-equation x y z u v bezout))
        (marici-nat-divides-reindex-value
          y (marici-mul u (marici-mul x z))
          (marici-mul (marici-mul u x) z)
          (rev MariciNat
            (marici-mul (marici-mul u x) z)
            (marici-mul u (marici-mul x z))
            (marici-mul-assoc u x z))
          (marici-nat-divides-product-left
            y (marici-mul x z) u divides-product)))

#define marici-natural-bezout-difference-implies-euclid
  ( x y : MariciNat)
  ( bezout : MariciNatBezoutDifference x y)
  : (z : MariciNat)
    → MariciNatDivides y (marici-mul x z)
    → MariciNatDivides y z
  := \ z divides-product →
      match bezout
      ( marici-nat-bezout-left u v equation ⇒
          marici-bezout-left-implies-euclid
            x y z u v equation divides-product
      | marici-nat-bezout-right u v equation ⇒
          marici-bezout-right-implies-euclid
            x y z u v equation divides-product)
```

## Boundary

Both natural Bézout difference orientations now imply the fixed-pair Euclid
conclusion. Coprimality is needed upstream to construct the certificate, not in
the elimination theorem. The remaining theorem must construct such a
certificate from natural coprimality by Euclidean division.
