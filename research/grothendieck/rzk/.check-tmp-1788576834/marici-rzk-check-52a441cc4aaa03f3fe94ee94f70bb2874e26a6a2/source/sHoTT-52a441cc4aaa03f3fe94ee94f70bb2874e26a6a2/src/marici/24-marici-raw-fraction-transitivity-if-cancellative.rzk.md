# Raw-fraction transitivity from positive cancellation

This module isolates the exact missing premise for transitivity. Cancellation
is required only for factors obtained from structurally positive denominator
predecessors, not for arbitrary integers.

```rzk
#lang rzk-1

#define MariciPositiveRightCancellation
  : U
  := ( x y : MariciInt)
  → ( d : MariciNat)
  → ( marici-int-mul x (marici-int-positive-denominator d)
      =_{MariciInt}
      marici-int-mul y (marici-int-positive-denominator d))
  → x =_{MariciInt} y
```

```rzk
#define marici-int-three-factor-swap
  ( a b c : MariciInt)
  : marici-int-mul (marici-int-mul a b) c
    =_{MariciInt} marici-int-mul (marici-int-mul a c) b
  := concat MariciInt
      (marici-int-mul (marici-int-mul a b) c)
      (marici-int-mul a (marici-int-mul b c))
      (marici-int-mul (marici-int-mul a c) b)
      (marici-int-mul-assoc a b c)
      (concat MariciInt
        (marici-int-mul a (marici-int-mul b c))
        (marici-int-mul a (marici-int-mul c b))
        (marici-int-mul (marici-int-mul a c) b)
        (ap MariciInt MariciInt
          (marici-int-mul b c) (marici-int-mul c b)
          (\ z → marici-int-mul a z)
          (marici-int-mul-comm b c))
        (rev MariciInt
          (marici-int-mul (marici-int-mul a c) b)
          (marici-int-mul a (marici-int-mul c b))
          (marici-int-mul-assoc a c b)))
```

```rzk
#define marici-raw-fraction-equivalent-trans-if-positive-cancellative
  ( cancel-positive : MariciPositiveRightCancellation)
  ( p q r : MariciRawFraction)
  : marici-raw-fraction-equivalent p q
  → marici-raw-fraction-equivalent q r
  → marici-raw-fraction-equivalent p r
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                match r
                  ( marici-raw-fraction c f ⇒
                      \ h j → cancel-positive
                        (marici-int-mul a
                          (marici-int-positive-denominator f))
                        (marici-int-mul c
                          (marici-int-positive-denominator d))
                        e
                        (concat MariciInt
                          (marici-int-mul
                            (marici-int-mul a
                              (marici-int-positive-denominator f))
                            (marici-int-positive-denominator e))
                          (marici-int-mul
                            (marici-int-mul b
                              (marici-int-positive-denominator f))
                            (marici-int-positive-denominator d))
                          (marici-int-mul
                            (marici-int-mul c
                              (marici-int-positive-denominator d))
                            (marici-int-positive-denominator e))
                          (concat MariciInt
                            (marici-int-mul
                              (marici-int-mul a
                                (marici-int-positive-denominator f))
                              (marici-int-positive-denominator e))
                            (marici-int-mul
                              (marici-int-mul a
                                (marici-int-positive-denominator e))
                              (marici-int-positive-denominator f))
                            (marici-int-mul
                              (marici-int-mul b
                                (marici-int-positive-denominator f))
                              (marici-int-positive-denominator d))
                            (marici-int-three-factor-swap a
                              (marici-int-positive-denominator f)
                              (marici-int-positive-denominator e))
                            (concat MariciInt
                              (marici-int-mul
                                (marici-int-mul a
                                  (marici-int-positive-denominator e))
                                (marici-int-positive-denominator f))
                              (marici-int-mul
                                (marici-int-mul b
                                  (marici-int-positive-denominator d))
                                (marici-int-positive-denominator f))
                              (marici-int-mul
                                (marici-int-mul b
                                  (marici-int-positive-denominator f))
                                (marici-int-positive-denominator d))
                              (ap MariciInt MariciInt
                                (marici-int-mul a
                                  (marici-int-positive-denominator e))
                                (marici-int-mul b
                                  (marici-int-positive-denominator d))
                                (\ z → marici-int-mul z
                                  (marici-int-positive-denominator f)) h)
                              (marici-int-three-factor-swap b
                                (marici-int-positive-denominator d)
                                (marici-int-positive-denominator f))))
                          (concat MariciInt
                            (marici-int-mul
                              (marici-int-mul b
                                (marici-int-positive-denominator f))
                              (marici-int-positive-denominator d))
                            (marici-int-mul
                              (marici-int-mul c
                                (marici-int-positive-denominator e))
                              (marici-int-positive-denominator d))
                            (marici-int-mul
                              (marici-int-mul c
                                (marici-int-positive-denominator d))
                              (marici-int-positive-denominator e))
                            (ap MariciInt MariciInt
                              (marici-int-mul b
                                (marici-int-positive-denominator f))
                              (marici-int-mul c
                                (marici-int-positive-denominator e))
                              (\ z → marici-int-mul z
                                (marici-int-positive-denominator d)) j)
                            (marici-int-three-factor-swap c
                              (marici-int-positive-denominator e)
                              (marici-int-positive-denominator d)))))))
```

## Boundary

The raw relation is transitive conditional on positive right cancellation.
The remaining theorem obligation is now exactly the cancellation witness for
normalized integers. No integral-domain, sethood, quotient, or discreteness
claim is inferred from the conditional proof.
