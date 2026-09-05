# The positive Bézout orientation implies Euclid

A natural difference certificate `ux+1=vy` represents one sign orientation of
an integer Bézout identity. Multiplying by `z` makes `y` divide `(ux)z+z` when
it divides `xz`; removing the already divisible first summand yields `y|z`.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatBezoutDifference
  ( x y : MariciNat)
  := marici-nat-bezout-left
      ( u v : MariciNat)
      ( equation : marici-add (marici-mul u x) (marici-succ marici-zero)
        =_{MariciNat} marici-mul v y)
  | marici-nat-bezout-right
      ( u v : MariciNat)
      ( equation : marici-add (marici-mul v y) (marici-succ marici-zero)
        =_{MariciNat} marici-mul u x)

#define marici-bezout-left-scaled-equation
  ( x y z u v : MariciNat)
  ( bezout : marici-add (marici-mul u x) (marici-succ marici-zero)
    =_{MariciNat} marici-mul v y)
  : marici-mul (marici-mul v z) y =_{MariciNat}
      marici-add (marici-mul (marici-mul u x) z) z
  := concat MariciNat
      (marici-mul (marici-mul v z) y)
      (marici-mul (marici-mul v y) z)
      (marici-add (marici-mul (marici-mul u x) z) z)
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
      (concat MariciNat
        (marici-mul (marici-mul v y) z)
        (marici-mul
          (marici-add (marici-mul u x) (marici-succ marici-zero)) z)
        (marici-add (marici-mul (marici-mul u x) z) z)
        (ap MariciNat MariciNat
          (marici-mul v y)
          (marici-add (marici-mul u x) (marici-succ marici-zero))
          (\ value → marici-mul value z)
          (rev MariciNat
            (marici-add (marici-mul u x) (marici-succ marici-zero))
            (marici-mul v y) bezout))
        (concat MariciNat
          (marici-mul
            (marici-add (marici-mul u x) (marici-succ marici-zero)) z)
          (marici-add
            (marici-mul (marici-mul u x) z)
            (marici-mul (marici-succ marici-zero) z))
          (marici-add (marici-mul (marici-mul u x) z) z)
          (marici-mul-add-left-distrib
            (marici-mul u x) (marici-succ marici-zero) z)
          (ap MariciNat MariciNat
            (marici-mul (marici-succ marici-zero) z) z
            (\ value → marici-add
              (marici-mul (marici-mul u x) z) value)
            (marici-mul-one-left z))))

#define marici-bezout-left-implies-euclid
  ( x y z u v : MariciNat)
  ( bezout : marici-add (marici-mul u x) (marici-succ marici-zero)
    =_{MariciNat} marici-mul v y)
  ( divides-product : MariciNatDivides y (marici-mul x z))
  : MariciNatDivides y z
  := marici-nat-divisibility-removes-divisible-left-summand
      y (marici-mul (marici-mul u x) z) z
      (marici-nat-divides-reindex-value
        y (marici-mul u (marici-mul x z))
        (marici-mul (marici-mul u x) z)
        (rev MariciNat
          (marici-mul (marici-mul u x) z)
          (marici-mul u (marici-mul x z))
          (marici-mul-assoc u x z))
        (marici-nat-divides-product-left
          y (marici-mul x z) u divides-product))
      (marici-nat-divides-witness y
        (marici-add (marici-mul (marici-mul u x) z) z)
        (marici-mul v z)
        (marici-bezout-left-scaled-equation x y z u v bezout))
```

## Boundary

The `ux+1=vy` natural Bézout orientation now implies Euclid's lemma for all
naturals, with no coprimality premise needed beyond construction of the
certificate. The symmetric `vy+1=ux` orientation remains before the full
Bézout-difference type implies Euclid.
