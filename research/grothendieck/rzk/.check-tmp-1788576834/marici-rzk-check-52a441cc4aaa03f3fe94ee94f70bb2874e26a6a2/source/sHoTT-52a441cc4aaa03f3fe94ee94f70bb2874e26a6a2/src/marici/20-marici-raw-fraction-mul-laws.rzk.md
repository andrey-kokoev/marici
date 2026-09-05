# Raw-fraction multiplication laws

Raw multiplication is commutative and associative already at constructor
level. These results use both numerator laws and the positive-denominator
predecessor laws; no quotient principle is involved.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-mul-comm
  ( p q : MariciRawFraction)
  : marici-raw-fraction-mul p q
    =_{MariciRawFraction} marici-raw-fraction-mul q p
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                concat MariciRawFraction
                  (marici-raw-fraction
                    (marici-int-mul a b)
                    (marici-positive-product-predecessor d e))
                  (marici-raw-fraction
                    (marici-int-mul b a)
                    (marici-positive-product-predecessor d e))
                  (marici-raw-fraction
                    (marici-int-mul b a)
                    (marici-positive-product-predecessor e d))
                  (ap MariciInt MariciRawFraction
                    (marici-int-mul a b)
                    (marici-int-mul b a)
                    (\ n → marici-raw-fraction n
                      (marici-positive-product-predecessor d e))
                    (marici-int-mul-comm a b))
                  (ap MariciNat MariciRawFraction
                    (marici-positive-product-predecessor d e)
                    (marici-positive-product-predecessor e d)
                    (\ g → marici-raw-fraction
                      (marici-int-mul b a) g)
                    (marici-positive-product-predecessor-comm d e))))
```

```rzk
#define marici-raw-fraction-mul-assoc
  ( p q r : MariciRawFraction)
  : marici-raw-fraction-mul
      (marici-raw-fraction-mul p q) r
    =_{MariciRawFraction}
      marici-raw-fraction-mul p
        (marici-raw-fraction-mul q r)
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                match r
                  ( marici-raw-fraction c f ⇒
                      concat MariciRawFraction
                        (marici-raw-fraction
                          (marici-int-mul (marici-int-mul a b) c)
                          (marici-positive-product-predecessor
                            (marici-positive-product-predecessor d e) f))
                        (marici-raw-fraction
                          (marici-int-mul a (marici-int-mul b c))
                          (marici-positive-product-predecessor
                            (marici-positive-product-predecessor d e) f))
                        (marici-raw-fraction
                          (marici-int-mul a (marici-int-mul b c))
                          (marici-positive-product-predecessor d
                            (marici-positive-product-predecessor e f)))
                        (ap MariciInt MariciRawFraction
                          (marici-int-mul (marici-int-mul a b) c)
                          (marici-int-mul a (marici-int-mul b c))
                          (\ n → marici-raw-fraction n
                            (marici-positive-product-predecessor
                              (marici-positive-product-predecessor d e) f))
                          (marici-int-mul-assoc a b c))
                        (ap MariciNat MariciRawFraction
                          (marici-positive-product-predecessor
                            (marici-positive-product-predecessor d e) f)
                          (marici-positive-product-predecessor d
                            (marici-positive-product-predecessor e f))
                          (\ g → marici-raw-fraction
                            (marici-int-mul a (marici-int-mul b c)) g)
                          (marici-positive-product-predecessor-assoc d e f)))))
```

## Boundary

These are raw-constructor laws only. They do not show that multiplication
respects cross-product equivalence; that congruence remains downstream of
integer distributivity and relation transitivity/cancellation.
