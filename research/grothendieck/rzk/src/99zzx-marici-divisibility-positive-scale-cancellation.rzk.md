# Cancelling a positive scale from divisibility

If a positively scaled divisor divides the correspondingly scaled value, the
same stored cofactor witnesses divisibility before scaling. Reassociation and
commutativity expose a common positive left factor, which is cancelled by the
existing injectivity theorem.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-prefix-cofactor-swap
  ( k q y : MariciNat)
  : marici-mul (marici-succ k) (marici-mul q y)
      =_{MariciNat}
    marici-mul q (marici-mul (marici-succ k) y)
  := concat MariciNat
      (marici-mul (marici-succ k) (marici-mul q y))
      (marici-mul (marici-mul (marici-succ k) q) y)
      (marici-mul q (marici-mul (marici-succ k) y))
      (rev MariciNat
        (marici-mul (marici-mul (marici-succ k) q) y)
        (marici-mul (marici-succ k) (marici-mul q y))
        (marici-mul-assoc (marici-succ k) q y))
      (concat MariciNat
        (marici-mul (marici-mul (marici-succ k) q) y)
        (marici-mul (marici-mul q (marici-succ k)) y)
        (marici-mul q (marici-mul (marici-succ k) y))
        (ap MariciNat MariciNat
          (marici-mul (marici-succ k) q)
          (marici-mul q (marici-succ k))
          (\ value → marici-mul value y)
          (marici-mul-comm (marici-succ k) q))
        (marici-mul-assoc q (marici-succ k) y))

#define marici-nat-divides-cancel-positive-left-scale
  ( k y z : MariciNat)
  ( divides : MariciNatDivides
      (marici-mul (marici-succ k) y)
      (marici-mul (marici-succ k) z))
  : MariciNatDivides y z
  := match divides
      ( marici-nat-divides-witness q equation ⇒
        marici-nat-divides-witness y z q
          (marici-mul-positive-left-injective k
            (marici-mul q y) z
            (concat MariciNat
              (marici-mul (marici-succ k) (marici-mul q y))
              (marici-mul q (marici-mul (marici-succ k) y))
              (marici-mul (marici-succ k) z)
              (marici-positive-prefix-cofactor-swap k q y)
              equation)))

#define marici-nat-divides-cancel-positive-right-scale
  ( k y z : MariciNat)
  ( divides : MariciNatDivides
      (marici-mul y (marici-succ k))
      (marici-mul z (marici-succ k)))
  : MariciNatDivides y z
  := marici-nat-divides-cancel-positive-left-scale k y z
      (marici-nat-divides-reindex-value
        (marici-mul (marici-succ k) y)
        (marici-mul z (marici-succ k))
        (marici-mul (marici-succ k) z)
        (marici-mul-comm z (marici-succ k))
        (match divides
          ( marici-nat-divides-witness q equation ⇒
            marici-nat-divides-witness
              (marici-mul (marici-succ k) y)
              (marici-mul z (marici-succ k)) q
              (concat MariciNat
                (marici-mul q (marici-mul (marici-succ k) y))
                (marici-mul q (marici-mul y (marici-succ k)))
                (marici-mul z (marici-succ k))
                (ap MariciNat MariciNat
                  (marici-mul (marici-succ k) y)
                  (marici-mul y (marici-succ k))
                  (\ value → marici-mul q value)
                  (marici-mul-comm (marici-succ k) y))
                equation))))
```

## Boundary

Positive scaling can now be cancelled from either orientation of a general
natural-divisibility assertion. This is the cancellation step required after a
composite Euclid induction extracts divisibility by one factor.
