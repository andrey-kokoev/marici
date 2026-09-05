# Raw translated addition cancels

For arbitrary positive-denominator raw fractions, subtracting the original
fraction from its translate by a second fraction is equivalent to that second
fraction. The proof transports both encoded denominator occurrences to the
explicit integer cross-product cancellation identity.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-translated-addition-cancellation
  ( p q : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-subtract
        (marici-raw-fraction-add p q) p)
      q
  := match p into
      (\ p-prime → marici-raw-fraction-equivalent
        (marici-raw-fraction-subtract
          (marici-raw-fraction-add p-prime q) p-prime) q)
      ( marici-raw-fraction a d ⇒
          match q into
          (\ q-prime → marici-raw-fraction-equivalent
            (marici-raw-fraction-subtract
              (marici-raw-fraction-add
                (marici-raw-fraction a d) q-prime)
              (marici-raw-fraction a d)) q-prime)
          ( marici-raw-fraction b e ⇒
              concat MariciInt
                (marici-int-mul
                  (marici-int-add
                    (marici-scale-by-positive-denominator
                      (marici-int-add
                        (marici-scale-by-positive-denominator a e)
                        (marici-scale-by-positive-denominator b d)) d)
                    (marici-int-negate
                      (marici-scale-by-positive-denominator a
                        (marici-positive-product-predecessor d e))))
                  (marici-int-positive-denominator e))
                (marici-int-mul b
                  (marici-int-mul
                    (marici-int-mul
                      (marici-int-positive-denominator d)
                      (marici-int-positive-denominator e))
                    (marici-int-positive-denominator d)))
                (marici-scale-by-positive-denominator b
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor d e) d))
                (concat MariciInt
                  (marici-int-mul
                    (marici-int-add
                      (marici-scale-by-positive-denominator
                        (marici-int-add
                          (marici-scale-by-positive-denominator a e)
                          (marici-scale-by-positive-denominator b d)) d)
                      (marici-int-negate
                        (marici-scale-by-positive-denominator a
                          (marici-positive-product-predecessor d e))))
                    (marici-int-positive-denominator e))
                  (marici-int-mul
                    (marici-int-add
                      (marici-scale-by-positive-denominator
                        (marici-int-add
                          (marici-scale-by-positive-denominator a e)
                          (marici-scale-by-positive-denominator b d)) d)
                      (marici-int-negate
                        (marici-int-mul a
                          (marici-int-mul
                            (marici-int-positive-denominator e)
                            (marici-int-positive-denominator d)))))
                    (marici-int-positive-denominator e))
                  (marici-int-mul b
                    (marici-int-mul
                      (marici-int-mul
                        (marici-int-positive-denominator d)
                        (marici-int-positive-denominator e))
                      (marici-int-positive-denominator d)))
                  (ap MariciInt MariciInt
                    (marici-scale-by-positive-denominator a
                      (marici-positive-product-predecessor d e))
                    (marici-int-mul a
                      (marici-int-mul
                        (marici-int-positive-denominator e)
                        (marici-int-positive-denominator d)))
                    (\ scaled → marici-int-mul
                      (marici-int-add
                        (marici-scale-by-positive-denominator
                          (marici-int-add
                            (marici-scale-by-positive-denominator a e)
                            (marici-scale-by-positive-denominator b d)) d)
                        (marici-int-negate scaled))
                      (marici-int-positive-denominator e))
                    (marici-scaled-nested-denominator-reordered a d e))
                  (marici-translated-fraction-cross-product-cancellation
                    a b
                    (marici-int-positive-denominator d)
                    (marici-int-positive-denominator e)))
                (ap MariciInt MariciInt
                  (marici-int-mul
                    (marici-int-mul
                      (marici-int-positive-denominator d)
                      (marici-int-positive-denominator e))
                    (marici-int-positive-denominator d))
                  (marici-int-positive-denominator
                    (marici-positive-product-predecessor
                      (marici-positive-product-predecessor d e) d))
                  (\ denominator → marici-int-mul b denominator)
                  (rev MariciInt
                    (marici-int-positive-denominator
                      (marici-positive-product-predecessor
                        (marici-positive-product-predecessor d e) d))
                    (marici-int-mul
                      (marici-int-mul
                        (marici-int-positive-denominator d)
                        (marici-int-positive-denominator e))
                      (marici-int-positive-denominator d))
                    (marici-nested-positive-denominator-product d e))))
          )
```

## Boundary

The raw cancellation `((p + q) - p) ~ q` is now complete. Normalized
representative equality and rational component transport can identify an
accumulated partial-sum difference with its shifted tail.
