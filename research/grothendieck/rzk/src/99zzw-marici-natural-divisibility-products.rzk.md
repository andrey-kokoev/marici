# Natural divisibility and products

Divisibility is stable under multiplying the value, and a divisor factor may be
multiplied in parallel with the value. Exact associativity and commutativity
paths align the stored cofactor equations.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-left-factor-divides-product
  ( x z : MariciNat)
  : MariciNatDivides x (marici-mul x z)
  := marici-nat-divides-witness x (marici-mul x z) z
      (marici-mul-comm z x)

#define marici-nat-right-factor-divides-product
  ( x z : MariciNat)
  : MariciNatDivides z (marici-mul x z)
  := marici-nat-divides-witness z (marici-mul x z) x refl

#define marici-nat-divides-product-right
  ( divisor x z : MariciNat)
  ( divides : MariciNatDivides divisor x)
  : MariciNatDivides divisor (marici-mul x z)
  := match divides
      ( marici-nat-divides-witness q equation ⇒
        marici-nat-divides-witness divisor (marici-mul x z)
          (marici-mul q z)
          (concat MariciNat
            (marici-mul (marici-mul q z) divisor)
            (marici-mul q (marici-mul z divisor))
            (marici-mul x z)
            (marici-mul-assoc q z divisor)
            (concat MariciNat
              (marici-mul q (marici-mul z divisor))
              (marici-mul (marici-mul q divisor) z)
              (marici-mul x z)
              (concat MariciNat
                (marici-mul q (marici-mul z divisor))
                (marici-mul q (marici-mul divisor z))
                (marici-mul (marici-mul q divisor) z)
                (ap MariciNat MariciNat
                  (marici-mul z divisor) (marici-mul divisor z)
                  (\ value → marici-mul q value)
                  (marici-mul-comm z divisor))
                (rev MariciNat
                  (marici-mul (marici-mul q divisor) z)
                  (marici-mul q (marici-mul divisor z))
                  (marici-mul-assoc q divisor z)))
              (ap MariciNat MariciNat
                (marici-mul q divisor) x
                (\ value → marici-mul value z) equation))))

#define marici-nat-divides-product-left
  ( divisor x z : MariciNat)
  ( divides : MariciNatDivides divisor x)
  : MariciNatDivides divisor (marici-mul z x)
  := marici-nat-divides-reindex-value
      divisor (marici-mul x z) (marici-mul z x)
      (marici-mul-comm x z)
      (marici-nat-divides-product-right divisor x z divides)

#define marici-nat-divides-scale-divisor-and-value
  ( divisor x z : MariciNat)
  ( divides : MariciNatDivides divisor x)
  : MariciNatDivides (marici-mul divisor z) (marici-mul x z)
  := match divides
      ( marici-nat-divides-witness q equation ⇒
        marici-nat-divides-witness
          (marici-mul divisor z) (marici-mul x z) q
          (concat MariciNat
            (marici-mul q (marici-mul divisor z))
            (marici-mul (marici-mul q divisor) z)
            (marici-mul x z)
            (rev MariciNat
              (marici-mul (marici-mul q divisor) z)
              (marici-mul q (marici-mul divisor z))
              (marici-mul-assoc q divisor z))
            (ap MariciNat MariciNat
              (marici-mul q divisor) x
              (\ value → marici-mul value z) equation)))
```

## Boundary

The general divisibility calculus now transports witnesses through products in
the orientations required by a composite-divisor Euclid induction. Cancellation
of a positive factor from a product-divisibility equation remains separate.
