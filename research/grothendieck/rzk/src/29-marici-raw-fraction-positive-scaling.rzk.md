# Positive scaling of raw fractions

Multiplying numerator and denominator by the same structurally positive factor
produces a related raw fraction. This supplies the forward scaling operation
needed by later normalization, without asserting that a common factor can be
cancelled.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-denominator-product
  ( d e : MariciNat)
  : marici-int-positive-denominator
      (marici-positive-product-predecessor d e)
    =_{MariciInt}
      marici-int-mul
        (marici-int-positive-denominator d)
        (marici-int-positive-denominator e)
  := concat MariciInt
      (marici-int-embed-nat
        (marici-succ (marici-positive-product-predecessor d e)))
      (marici-int-embed-nat
        (marici-mul (marici-succ d) (marici-succ e)))
      (marici-int-mul
        (marici-int-embed-nat (marici-succ d))
        (marici-int-embed-nat (marici-succ e)))
      (ap MariciNat MariciInt
        (marici-succ (marici-positive-product-predecessor d e))
        (marici-mul (marici-succ d) (marici-succ e))
        marici-int-embed-nat
        (marici-succ-positive-product d e))
      (marici-int-embed-mul (marici-succ d) (marici-succ e))

#define marici-raw-fraction-scale-positive
  ( p : MariciRawFraction)
  ( e : MariciNat)
  : MariciRawFraction
  := match p
      ( marici-raw-fraction a d ⇒
          marici-raw-fraction
            (marici-scale-by-positive-denominator a e)
            (marici-positive-product-predecessor d e))
```

```rzk
#define marici-raw-fraction-scale-positive-equivalent
  ( p : MariciRawFraction)
  ( e : MariciNat)
  : marici-raw-fraction-equivalent p
      (marici-raw-fraction-scale-positive p e)
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciInt
            (marici-int-mul a
              (marici-int-positive-denominator
                (marici-positive-product-predecessor d e)))
            (marici-int-mul
              (marici-int-mul a
                (marici-int-positive-denominator d))
              (marici-int-positive-denominator e))
            (marici-int-mul
              (marici-int-mul a
                (marici-int-positive-denominator e))
              (marici-int-positive-denominator d))
            (concat MariciInt
              (marici-int-mul a
                (marici-int-positive-denominator
                  (marici-positive-product-predecessor d e)))
              (marici-int-mul a
                (marici-int-mul
                  (marici-int-positive-denominator d)
                  (marici-int-positive-denominator e)))
              (marici-int-mul
                (marici-int-mul a
                  (marici-int-positive-denominator d))
                (marici-int-positive-denominator e))
              (ap MariciInt MariciInt
                (marici-int-positive-denominator
                  (marici-positive-product-predecessor d e))
                (marici-int-mul
                  (marici-int-positive-denominator d)
                  (marici-int-positive-denominator e))
                (\ z → marici-int-mul a z)
                (marici-positive-denominator-product d e))
              (rev MariciInt
                (marici-int-mul
                  (marici-int-mul a
                    (marici-int-positive-denominator d))
                  (marici-int-positive-denominator e))
                (marici-int-mul a
                  (marici-int-mul
                    (marici-int-positive-denominator d)
                    (marici-int-positive-denominator e)))
                (marici-int-mul-assoc a
                  (marici-int-positive-denominator d)
                  (marici-int-positive-denominator e))))
            (marici-int-three-factor-swap a
              (marici-int-positive-denominator d)
              (marici-int-positive-denominator e)))
```

## Boundary

Forward common-factor scaling is proved. The reverse operation is not a
normalization theorem: choosing and removing a common factor requires a gcd or
another canonical divisor interface plus positive cancellation and uniqueness.
