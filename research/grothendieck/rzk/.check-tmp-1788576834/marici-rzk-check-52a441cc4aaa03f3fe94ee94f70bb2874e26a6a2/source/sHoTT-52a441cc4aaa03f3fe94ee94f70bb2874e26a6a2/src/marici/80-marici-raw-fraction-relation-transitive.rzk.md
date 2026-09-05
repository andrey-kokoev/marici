# Raw-fraction relation transitivity

Two cross-product equalities are multiplied by the remaining denominators,
reordered into a common middle-denominator factor, and cancelled using positive
canonical-integer injectivity.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-equivalent-trans
  ( p q r : MariciRawFraction)
  : marici-raw-fraction-equivalent p q
  → marici-raw-fraction-equivalent q r
  → marici-raw-fraction-equivalent p r
  := match p
      ( marici-raw-fraction a d ⇒ match q
          ( marici-raw-fraction b e ⇒ match r
              ( marici-raw-fraction c f ⇒ \ h k →
                  marici-int-positive-right-injective e
                    (marici-scale-by-positive-denominator a f)
                    (marici-scale-by-positive-denominator c d)
                    (concat MariciInt
                      (marici-int-mul
                        (marici-scale-by-positive-denominator a f)
                        (marici-int-positive-denominator e))
                      (marici-int-mul
                        (marici-scale-by-positive-denominator a e)
                        (marici-int-positive-denominator f))
                      (marici-int-mul
                        (marici-scale-by-positive-denominator c d)
                        (marici-int-positive-denominator e))
                      (marici-int-mul-swap-right-factors a
                        (marici-int-positive-denominator f)
                        (marici-int-positive-denominator e))
                      (concat MariciInt
                        (marici-int-mul
                          (marici-scale-by-positive-denominator a e)
                          (marici-int-positive-denominator f))
                        (marici-int-mul
                          (marici-scale-by-positive-denominator b d)
                          (marici-int-positive-denominator f))
                        (marici-int-mul
                          (marici-scale-by-positive-denominator c d)
                          (marici-int-positive-denominator e))
                        (ap MariciInt MariciInt
                          (marici-scale-by-positive-denominator a e)
                          (marici-scale-by-positive-denominator b d)
                          (\ z → marici-int-mul z
                            (marici-int-positive-denominator f)) h)
                        (concat MariciInt
                          (marici-int-mul
                            (marici-scale-by-positive-denominator b d)
                            (marici-int-positive-denominator f))
                          (marici-int-mul
                            (marici-scale-by-positive-denominator b f)
                            (marici-int-positive-denominator d))
                          (marici-int-mul
                            (marici-scale-by-positive-denominator c d)
                            (marici-int-positive-denominator e))
                          (marici-int-mul-swap-right-factors b
                            (marici-int-positive-denominator d)
                            (marici-int-positive-denominator f))
                          (concat MariciInt
                            (marici-int-mul
                              (marici-scale-by-positive-denominator b f)
                              (marici-int-positive-denominator d))
                            (marici-int-mul
                              (marici-scale-by-positive-denominator c e)
                              (marici-int-positive-denominator d))
                            (marici-int-mul
                              (marici-scale-by-positive-denominator c d)
                              (marici-int-positive-denominator e))
                            (ap MariciInt MariciInt
                              (marici-scale-by-positive-denominator b f)
                              (marici-scale-by-positive-denominator c e)
                              (\ z → marici-int-mul z
                                (marici-int-positive-denominator d)) k)
                            (marici-int-mul-swap-right-factors c
                              (marici-int-positive-denominator e)
                              (marici-int-positive-denominator d)))))))))
```

## Boundary

The raw cross-product relation is now reflexive, symmetric, and transitive. This
establishes an equivalence relation on raw fractions; it does not construct its
quotient, select reduced representatives, or prove normalization uniqueness.
