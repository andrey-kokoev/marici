# Raw-fraction multiplication congruence

Unlike addition congruence, multiplication congruence needs no distributivity.
It follows by regrouping four integer factors and transporting the two input
cross-product equalities.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-four-factor-cross
  ( a b c d : MariciInt)
  : marici-int-mul (marici-int-mul a c) (marici-int-mul b d)
    =_{MariciInt}
    marici-int-mul (marici-int-mul a b) (marici-int-mul c d)
  := concat MariciInt
      (marici-int-mul (marici-int-mul a c) (marici-int-mul b d))
      (marici-int-mul a (marici-int-mul c (marici-int-mul b d)))
      (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-mul-assoc a c (marici-int-mul b d))
      (concat MariciInt
        (marici-int-mul a (marici-int-mul c (marici-int-mul b d)))
        (marici-int-mul a (marici-int-mul b (marici-int-mul c d)))
        (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
        (ap MariciInt MariciInt
          (marici-int-mul c (marici-int-mul b d))
          (marici-int-mul b (marici-int-mul c d))
          (\ z → marici-int-mul a z)
          (concat MariciInt
            (marici-int-mul c (marici-int-mul b d))
            (marici-int-mul (marici-int-mul c b) d)
            (marici-int-mul b (marici-int-mul c d))
            (rev MariciInt
              (marici-int-mul (marici-int-mul c b) d)
              (marici-int-mul c (marici-int-mul b d))
              (marici-int-mul-assoc c b d))
            (concat MariciInt
              (marici-int-mul (marici-int-mul c b) d)
              (marici-int-mul (marici-int-mul b c) d)
              (marici-int-mul b (marici-int-mul c d))
              (ap MariciInt MariciInt
                (marici-int-mul c b) (marici-int-mul b c)
                (\ z → marici-int-mul z d)
                (marici-int-mul-comm c b))
              (marici-int-mul-assoc b c d))))
        (rev MariciInt
          (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
          (marici-int-mul a (marici-int-mul b (marici-int-mul c d)))
          (marici-int-mul-assoc a b (marici-int-mul c d))))
```

```rzk
#define marici-raw-fraction-mul-congruent
  ( p p-prime q q-prime : MariciRawFraction)
  : marici-raw-fraction-equivalent p p-prime
  → marici-raw-fraction-equivalent q q-prime
  → marici-raw-fraction-equivalent
      (marici-raw-fraction-mul p q)
      (marici-raw-fraction-mul p-prime q-prime)
  := match p
      ( marici-raw-fraction a d ⇒
          match p-prime
            ( marici-raw-fraction b e ⇒
                match q
                  ( marici-raw-fraction c f ⇒
                      match q-prime
                        ( marici-raw-fraction g k ⇒
                            \ h j → concat MariciInt
                              (marici-int-mul
                                (marici-int-mul a c)
                                (marici-int-mul
                                  (marici-int-positive-denominator e)
                                  (marici-int-positive-denominator k)))
                              (marici-int-mul
                                (marici-int-mul a
                                  (marici-int-positive-denominator e))
                                (marici-int-mul c
                                  (marici-int-positive-denominator k)))
                              (marici-int-mul
                                (marici-int-mul b g)
                                (marici-int-mul
                                  (marici-int-positive-denominator d)
                                  (marici-int-positive-denominator f)))
                              (marici-int-four-factor-cross a
                                (marici-int-positive-denominator e) c
                                (marici-int-positive-denominator k))
                              (concat MariciInt
                                (marici-int-mul
                                  (marici-int-mul a
                                    (marici-int-positive-denominator e))
                                  (marici-int-mul c
                                    (marici-int-positive-denominator k)))
                                (marici-int-mul
                                  (marici-int-mul b
                                    (marici-int-positive-denominator d))
                                  (marici-int-mul g
                                    (marici-int-positive-denominator f)))
                                (marici-int-mul
                                  (marici-int-mul b g)
                                  (marici-int-mul
                                    (marici-int-positive-denominator d)
                                    (marici-int-positive-denominator f)))
                                (concat MariciInt
                                  (marici-int-mul
                                    (marici-int-mul a
                                      (marici-int-positive-denominator e))
                                    (marici-int-mul c
                                      (marici-int-positive-denominator k)))
                                  (marici-int-mul
                                    (marici-int-mul b
                                      (marici-int-positive-denominator d))
                                    (marici-int-mul c
                                      (marici-int-positive-denominator k)))
                                  (marici-int-mul
                                    (marici-int-mul b
                                      (marici-int-positive-denominator d))
                                    (marici-int-mul g
                                      (marici-int-positive-denominator f)))
                                  (ap MariciInt MariciInt
                                    (marici-int-mul a
                                      (marici-int-positive-denominator e))
                                    (marici-int-mul b
                                      (marici-int-positive-denominator d))
                                    (\ z → marici-int-mul z
                                      (marici-int-mul c
                                        (marici-int-positive-denominator k))) h)
                                  (ap MariciInt MariciInt
                                    (marici-int-mul c
                                      (marici-int-positive-denominator k))
                                    (marici-int-mul g
                                      (marici-int-positive-denominator f))
                                    (\ z → marici-int-mul
                                      (marici-int-mul b
                                        (marici-int-positive-denominator d)) z) j))
                                (rev MariciInt
                                  (marici-int-mul
                                    (marici-int-mul b g)
                                    (marici-int-mul
                                      (marici-int-positive-denominator d)
                                      (marici-int-positive-denominator f)))
                                  (marici-int-mul
                                    (marici-int-mul b
                                      (marici-int-positive-denominator d))
                                    (marici-int-mul g
                                      (marici-int-positive-denominator f)))
                                  (marici-int-four-factor-cross b
                                    (marici-int-positive-denominator d) g
                                    (marici-int-positive-denominator f))))))))
```

## Boundary

Raw multiplication now descends if a quotient/retract for the relation is
constructed. This result does not supply relation transitivity, a quotient, or
canonical representatives. Addition congruence still requires integer
distributivity.
