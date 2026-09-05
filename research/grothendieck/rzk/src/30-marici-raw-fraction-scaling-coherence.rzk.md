# Coherence of positive raw-fraction scaling

Positive scaling has a strict unit and composes according to positive-factor
multiplication. These are constructor-level laws for the scaling operation,
not cancellation or normalization results.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-scale-positive-one
  ( p : MariciRawFraction)
  : marici-raw-fraction-scale-positive p marici-zero
    =_{MariciRawFraction} p
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciRawFraction
            (marici-raw-fraction
              (marici-int-mul a marici-int-one)
              (marici-positive-product-predecessor d marici-zero))
            (marici-raw-fraction a
              (marici-positive-product-predecessor d marici-zero))
            (marici-raw-fraction a d)
            (ap MariciInt MariciRawFraction
              (marici-int-mul a marici-int-one) a
              (\ n → marici-raw-fraction n
                (marici-positive-product-predecessor d marici-zero))
              (marici-int-mul-one-right a))
            (ap MariciNat MariciRawFraction
              (marici-positive-product-predecessor d marici-zero) d
              (\ g → marici-raw-fraction a g)
              (marici-positive-product-one-right d)))
```

```rzk
#define marici-raw-fraction-scale-positive-compose
  ( p : MariciRawFraction)
  ( e f : MariciNat)
  : marici-raw-fraction-scale-positive
      (marici-raw-fraction-scale-positive p e) f
    =_{MariciRawFraction}
      marici-raw-fraction-scale-positive p
        (marici-positive-product-predecessor e f)
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciRawFraction
            (marici-raw-fraction
              (marici-int-mul
                (marici-int-mul a
                  (marici-int-positive-denominator e))
                (marici-int-positive-denominator f))
              (marici-positive-product-predecessor
                (marici-positive-product-predecessor d e) f))
            (marici-raw-fraction
              (marici-int-mul a
                (marici-int-positive-denominator
                  (marici-positive-product-predecessor e f)))
              (marici-positive-product-predecessor
                (marici-positive-product-predecessor d e) f))
            (marici-raw-fraction
              (marici-int-mul a
                (marici-int-positive-denominator
                  (marici-positive-product-predecessor e f)))
              (marici-positive-product-predecessor d
                (marici-positive-product-predecessor e f)))
            (ap MariciInt MariciRawFraction
              (marici-int-mul
                (marici-int-mul a
                  (marici-int-positive-denominator e))
                (marici-int-positive-denominator f))
              (marici-int-mul a
                (marici-int-positive-denominator
                  (marici-positive-product-predecessor e f)))
              (\ n → marici-raw-fraction n
                (marici-positive-product-predecessor
                  (marici-positive-product-predecessor d e) f))
              (concat MariciInt
                (marici-int-mul
                  (marici-int-mul a
                    (marici-int-positive-denominator e))
                  (marici-int-positive-denominator f))
                (marici-int-mul a
                  (marici-int-mul
                    (marici-int-positive-denominator e)
                    (marici-int-positive-denominator f)))
                (marici-int-mul a
                  (marici-int-positive-denominator
                    (marici-positive-product-predecessor e f)))
                (marici-int-mul-assoc a
                  (marici-int-positive-denominator e)
                  (marici-int-positive-denominator f))
                (ap MariciInt MariciInt
                  (marici-int-mul
                    (marici-int-positive-denominator e)
                    (marici-int-positive-denominator f))
                  (marici-int-positive-denominator
                    (marici-positive-product-predecessor e f))
                  (\ z → marici-int-mul a z)
                  (rev MariciInt
                    (marici-int-positive-denominator
                      (marici-positive-product-predecessor e f))
                    (marici-int-mul
                      (marici-int-positive-denominator e)
                      (marici-int-positive-denominator f))
                    (marici-positive-denominator-product e f)))))
            (ap MariciNat MariciRawFraction
              (marici-positive-product-predecessor
                (marici-positive-product-predecessor d e) f)
              (marici-positive-product-predecessor d
                (marici-positive-product-predecessor e f))
              (\ g → marici-raw-fraction
                (marici-int-mul a
                  (marici-int-positive-denominator
                    (marici-positive-product-predecessor e f))) g)
              (marici-positive-product-predecessor-assoc d e f)))
```

## Boundary

Positive scaling is now a coherent action of the checked positive-factor
multiplication law on raw fractions. No inverse action exists without a chosen
divisor and cancellation theorem; coherence does not produce normalization.
