# Raw-fraction addition is associative

The numerator associativity theorem changes the first constructor coordinate;
positive-product-predecessor associativity changes the second. Their composite
is a path between the two raw-addition bracketings and therefore also a raw
fraction equivalence.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-assoc-path
  ( p q r : MariciRawFraction)
  : marici-raw-fraction-add (marici-raw-fraction-add p q) r
    =_{MariciRawFraction}
    marici-raw-fraction-add p (marici-raw-fraction-add q r)
  := match p into
      (\ p-prime → marici-raw-fraction-add
          (marici-raw-fraction-add p-prime q) r
        =_{MariciRawFraction}
        marici-raw-fraction-add p-prime
          (marici-raw-fraction-add q r))
      ( marici-raw-fraction a d ⇒
          match q into
          (\ q-prime → marici-raw-fraction-add
              (marici-raw-fraction-add
                (marici-raw-fraction a d) q-prime) r
            =_{MariciRawFraction}
            marici-raw-fraction-add (marici-raw-fraction a d)
              (marici-raw-fraction-add q-prime r))
          ( marici-raw-fraction b e ⇒
              match r into
              (\ r-prime → marici-raw-fraction-add
                  (marici-raw-fraction-add
                    (marici-raw-fraction a d)
                    (marici-raw-fraction b e)) r-prime
                =_{MariciRawFraction}
                marici-raw-fraction-add (marici-raw-fraction a d)
                  (marici-raw-fraction-add
                    (marici-raw-fraction b e) r-prime))
              ( marici-raw-fraction c f ⇒
                  concat MariciRawFraction
                    (marici-raw-fraction-add
                      (marici-raw-fraction-add
                        (marici-raw-fraction a d)
                        (marici-raw-fraction b e))
                      (marici-raw-fraction c f))
                    (marici-raw-fraction
                      (marici-int-add
                        (marici-scale-by-positive-denominator a
                          (marici-positive-product-predecessor e f))
                        (marici-scale-by-positive-denominator
                          (marici-int-add
                            (marici-scale-by-positive-denominator b f)
                            (marici-scale-by-positive-denominator c e)) d))
                      (marici-positive-product-predecessor
                        (marici-positive-product-predecessor d e) f))
                    (marici-raw-fraction-add (marici-raw-fraction a d)
                      (marici-raw-fraction-add
                        (marici-raw-fraction b e)
                        (marici-raw-fraction c f)))
                    (ap MariciInt MariciRawFraction
                      (marici-int-add
                        (marici-scale-by-positive-denominator
                          (marici-int-add
                            (marici-scale-by-positive-denominator a e)
                            (marici-scale-by-positive-denominator b d)) f)
                        (marici-scale-by-positive-denominator c
                          (marici-positive-product-predecessor d e)))
                      (marici-int-add
                        (marici-scale-by-positive-denominator a
                          (marici-positive-product-predecessor e f))
                        (marici-scale-by-positive-denominator
                          (marici-int-add
                            (marici-scale-by-positive-denominator b f)
                            (marici-scale-by-positive-denominator c e)) d))
                      (\ numerator → marici-raw-fraction numerator
                        (marici-positive-product-predecessor
                          (marici-positive-product-predecessor d e) f))
                      (marici-raw-add-associativity-numerator a b c d e f))
                    (ap MariciNat MariciRawFraction
                      (marici-positive-product-predecessor
                        (marici-positive-product-predecessor d e) f)
                      (marici-positive-product-predecessor d
                        (marici-positive-product-predecessor e f))
                      (\ denominator → marici-raw-fraction
                        (marici-int-add
                          (marici-scale-by-positive-denominator a
                            (marici-positive-product-predecessor e f))
                          (marici-scale-by-positive-denominator
                            (marici-int-add
                              (marici-scale-by-positive-denominator b f)
                              (marici-scale-by-positive-denominator c e)) d))
                        denominator)
                      (marici-positive-product-predecessor-assoc d e f)))
              )
          )

#define marici-raw-fraction-add-assoc-equivalent
  ( p q r : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add (marici-raw-fraction-add p q) r)
      (marici-raw-fraction-add p (marici-raw-fraction-add q r))
  := marici-raw-fraction-path-implies-equivalent
      (marici-raw-fraction-add (marici-raw-fraction-add p q) r)
      (marici-raw-fraction-add p (marici-raw-fraction-add q r))
      (marici-raw-fraction-add-assoc-path p q r)
```

## Boundary

Raw addition is now associative by path and equivalence. Descending this law
through normalization yields rational component associativity, which splits a
shifted accumulator into prefix plus independently folded tail.
