# Raw-fraction addition congruence

Raw addition now respects cross-product equivalence in both arguments. This is
the missing descent theorem for presentation-independent rational addition.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-congruent
  ( p p-prime q q-prime : MariciRawFraction)
  : marici-raw-fraction-equivalent p p-prime
  → marici-raw-fraction-equivalent q q-prime
  → marici-raw-fraction-equivalent
      (marici-raw-fraction-add p q)
      (marici-raw-fraction-add p-prime q-prime)
  := match p
      ( marici-raw-fraction a d ⇒
          match p-prime
            ( marici-raw-fraction b e ⇒
                match q
                  ( marici-raw-fraction c f ⇒
                      match q-prime
                        ( marici-raw-fraction g k ⇒
                            \ h j → concat MariciInt
                              (marici-scale-by-positive-denominator
                                (marici-int-add
                                  (marici-scale-by-positive-denominator a f)
                                  (marici-scale-by-positive-denominator c d))
                                (marici-positive-product-predecessor e k))
                              (marici-int-mul
                                (marici-int-add
                                  (marici-int-mul a
                                    (marici-int-positive-denominator f))
                                  (marici-int-mul c
                                    (marici-int-positive-denominator d)))
                                (marici-int-mul
                                  (marici-int-positive-denominator e)
                                  (marici-int-positive-denominator k)))
                              (marici-scale-by-positive-denominator
                                (marici-int-add
                                  (marici-scale-by-positive-denominator b k)
                                  (marici-scale-by-positive-denominator g e))
                                (marici-positive-product-predecessor d f))
                              (marici-scale-by-denominator-product
                                (marici-int-add
                                  (marici-scale-by-positive-denominator a f)
                                  (marici-scale-by-positive-denominator c d))
                                e k)
                              (concat MariciInt
                                (marici-int-mul
                                  (marici-int-add
                                    (marici-int-mul a
                                      (marici-int-positive-denominator f))
                                    (marici-int-mul c
                                      (marici-int-positive-denominator d)))
                                  (marici-int-mul
                                    (marici-int-positive-denominator e)
                                    (marici-int-positive-denominator k)))
                                (marici-int-mul
                                  (marici-int-add
                                    (marici-int-mul b
                                      (marici-int-positive-denominator k))
                                    (marici-int-mul g
                                      (marici-int-positive-denominator e)))
                                  (marici-int-mul
                                    (marici-int-positive-denominator d)
                                    (marici-int-positive-denominator f)))
                                (marici-scale-by-positive-denominator
                                  (marici-int-add
                                    (marici-scale-by-positive-denominator b k)
                                    (marici-scale-by-positive-denominator g e))
                                  (marici-positive-product-predecessor d f))
                                (marici-int-fraction-add-cross
                                  a b c g
                                  (marici-int-positive-denominator d)
                                  (marici-int-positive-denominator e)
                                  (marici-int-positive-denominator f)
                                  (marici-int-positive-denominator k)
                                  h j)
                                (rev MariciInt
                                  (marici-scale-by-positive-denominator
                                    (marici-int-add
                                      (marici-scale-by-positive-denominator b k)
                                      (marici-scale-by-positive-denominator g e))
                                    (marici-positive-product-predecessor d f))
                                  (marici-int-mul
                                    (marici-int-add
                                      (marici-int-mul b
                                        (marici-int-positive-denominator k))
                                      (marici-int-mul g
                                        (marici-int-positive-denominator e)))
                                    (marici-int-mul
                                      (marici-int-positive-denominator d)
                                      (marici-int-positive-denominator f)))
                                  (marici-scale-by-denominator-product
                                    (marici-int-add
                                      (marici-scale-by-positive-denominator b k)
                                      (marici-scale-by-positive-denominator g e))
                                    d f)))))))
```

## Boundary

Addition now descends through raw fraction equivalence. This does not construct
a quotient type; it supplies the missing presentation-independence theorem for
the existing canonical-normalization route.
