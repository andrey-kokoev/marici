# Composite-divisor Euclid step

Euclid for two positive factors implies Euclid for their product. The first
factor is extracted from divisibility of the product, then cancelled from the
stored equation; Euclid for the second factor completes the cofactor
factorization and reconstructs divisibility by the product.

```rzk
#lang rzk-1
```

```rzk
#define MariciNatEuclidAt
  ( y : MariciNat)
  : U
  := ( x z : MariciNat)
    → MariciNatAreCoprime x y
    → MariciNatDivides y (marici-mul x z)
    → MariciNatDivides y z

#define marici-nat-divides-reindex-divisor
  ( divisor divisor-prime value : MariciNat)
  ( path : divisor =_{MariciNat} divisor-prime)
  ( divides : MariciNatDivides divisor value)
  : MariciNatDivides divisor-prime value
  := match divides
      ( marici-nat-divides-witness q equation ⇒
          marici-nat-divides-witness divisor-prime value q
            (concat MariciNat
              (marici-mul q divisor-prime)
              (marici-mul q divisor)
              value
              (ap MariciNat MariciNat divisor-prime divisor
                (\ factor → marici-mul q factor)
                (rev MariciNat divisor divisor-prime path))
              equation))

#define marici-nat-euclid-positive-composite
  ( u v : MariciNat)
  ( euclid-u : MariciNatEuclidAt (marici-succ u))
  ( euclid-v : MariciNatEuclidAt (marici-succ v))
  : MariciNatEuclidAt
      (marici-mul (marici-succ u) (marici-succ v))
  := \ x z coprime divides-product →
      match (euclid-u x z
        (marici-nat-coprime-descends-right-divisor
          x
          (marici-mul (marici-succ u) (marici-succ v))
          (marici-succ u) coprime
          (marici-nat-left-factor-divides-product
            (marici-succ u) (marici-succ v)))
        (marici-nat-divides-transitive
          (marici-succ u)
          (marici-mul (marici-succ u) (marici-succ v))
          (marici-mul x z)
          (marici-nat-left-factor-divides-product
            (marici-succ u) (marici-succ v))
          divides-product))
        ( marici-nat-divides-witness q equation-z ⇒
          match (euclid-v x q
            (marici-nat-coprime-descends-right-divisor
              x
              (marici-mul (marici-succ u) (marici-succ v))
              (marici-succ v) coprime
              (marici-nat-right-factor-divides-product
                (marici-succ u) (marici-succ v)))
            (marici-nat-divides-cancel-positive-left-scale u
              (marici-succ v) (marici-mul x q)
              (marici-nat-divides-reindex-value
                (marici-mul (marici-succ u) (marici-succ v))
                (marici-mul x z)
                (marici-mul (marici-succ u) (marici-mul x q))
                (concat MariciNat
                  (marici-mul x z)
                  (marici-mul x (marici-mul q (marici-succ u)))
                  (marici-mul (marici-succ u) (marici-mul x q))
                  (ap MariciNat MariciNat z
                    (marici-mul q (marici-succ u))
                    (\ value → marici-mul x value)
                    (rev MariciNat
                      (marici-mul q (marici-succ u)) z equation-z))
                  (concat MariciNat
                    (marici-mul x (marici-mul q (marici-succ u)))
                    (marici-mul (marici-mul x q) (marici-succ u))
                    (marici-mul (marici-succ u) (marici-mul x q))
                    (rev MariciNat
                      (marici-mul (marici-mul x q) (marici-succ u))
                      (marici-mul x (marici-mul q (marici-succ u)))
                      (marici-mul-assoc x q (marici-succ u)))
                    (marici-mul-comm
                      (marici-mul x q) (marici-succ u))))
                divides-product)))
            ( marici-nat-divides-witness s equation-q ⇒
              marici-nat-divides-reindex-value
                (marici-mul (marici-succ u) (marici-succ v))
                (marici-mul q (marici-succ u)) z equation-z
                (marici-nat-divides-reindex-divisor
                  (marici-mul (marici-succ v) (marici-succ u))
                  (marici-mul (marici-succ u) (marici-succ v))
                  (marici-mul q (marici-succ u))
                  (marici-mul-comm (marici-succ v) (marici-succ u))
                  (marici-nat-divides-scale-divisor-and-value
                    (marici-succ v) q (marici-succ u)
                    (marici-nat-divides-witness
                      (marici-succ v) q s equation-q)))))
```

## Boundary

The composite induction step for standard natural Euclid is now explicit and
uses only divisor descent, transitivity, product transport, and positive-scale
cancellation. A factorization induction still needs a base/irreducible case and
a constructive split of each nonunit divisor into irreducible or positive
composite branches.
