# Raw absolute value respects fraction equivalence

Integer absolute value commutes with multiplication by a positive denominator.
Applying absolute value to a cross-product equality therefore proves that raw
fraction absolute value preserves equivalence.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-absolute
  ( z : MariciInt)
  : MariciInt
  := marici-int-embed-nat (marici-int-magnitude z)

#define marici-int-absolute-positive-right-product
  ( z : MariciInt)
  ( f : MariciNat)
  : marici-int-absolute
      (marici-int-mul z (marici-int-positive-denominator f))
    =_{MariciInt}
    marici-int-mul (marici-int-absolute z)
      (marici-int-positive-denominator f)
  := match z
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ refl
      | marici-int-neg a ⇒ refl)

#define marici-raw-fraction-absolute-respects-equivalence
  ( p q : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent p q)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-absolute p)
      (marici-raw-fraction-absolute q)
  := match p into
      (\ p-prime → marici-raw-fraction-equivalent p-prime q
        → marici-raw-fraction-equivalent
          (marici-raw-fraction-absolute p-prime)
          (marici-raw-fraction-absolute q))
      ( marici-raw-fraction a d ⇒
          match q into
          (\ q-prime → marici-raw-fraction-equivalent
              (marici-raw-fraction a d) q-prime
            → marici-raw-fraction-equivalent
              (marici-raw-fraction-absolute
                (marici-raw-fraction a d))
              (marici-raw-fraction-absolute q-prime))
          ( marici-raw-fraction b e ⇒ \ h →
              concat MariciInt
                (marici-int-mul (marici-int-absolute a)
                  (marici-int-positive-denominator e))
                (marici-int-absolute
                  (marici-int-mul a
                    (marici-int-positive-denominator e)))
                (marici-int-mul (marici-int-absolute b)
                  (marici-int-positive-denominator d))
                (rev MariciInt
                  (marici-int-absolute
                    (marici-int-mul a
                      (marici-int-positive-denominator e)))
                  (marici-int-mul (marici-int-absolute a)
                    (marici-int-positive-denominator e))
                  (marici-int-absolute-positive-right-product a e))
                (concat MariciInt
                  (marici-int-absolute
                    (marici-int-mul a
                      (marici-int-positive-denominator e)))
                  (marici-int-absolute
                    (marici-int-mul b
                      (marici-int-positive-denominator d)))
                  (marici-int-mul (marici-int-absolute b)
                    (marici-int-positive-denominator d))
                  (ap MariciInt MariciInt
                    (marici-int-mul a
                      (marici-int-positive-denominator e))
                    (marici-int-mul b
                      (marici-int-positive-denominator d))
                    marici-int-absolute h)
                  (marici-int-absolute-positive-right-product b d))))
      equivalent
```

## Boundary

Raw absolute value now descends through the cross-product equivalence relation.
This is the missing invariant needed to compare absolute values across
normalization and complete distance symmetry.
