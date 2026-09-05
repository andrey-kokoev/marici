# Basic raw-fraction addition laws

Raw fraction addition is commutative at constructor level. The chosen zero with
denominator one is also a strict two-sided unit, because cross multiplication
by denominator one preserves both numerator and denominator.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-comm
  ( p q : MariciRawFraction)
  : marici-raw-fraction-add p q
    =_{MariciRawFraction} marici-raw-fraction-add q p
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                concat MariciRawFraction
                  (marici-raw-fraction
                    (marici-int-add
                      (marici-scale-by-positive-denominator a e)
                      (marici-scale-by-positive-denominator b d))
                    (marici-positive-product-predecessor d e))
                  (marici-raw-fraction
                    (marici-int-add
                      (marici-scale-by-positive-denominator b d)
                      (marici-scale-by-positive-denominator a e))
                    (marici-positive-product-predecessor d e))
                  (marici-raw-fraction
                    (marici-int-add
                      (marici-scale-by-positive-denominator b d)
                      (marici-scale-by-positive-denominator a e))
                    (marici-positive-product-predecessor e d))
                  (ap MariciInt MariciRawFraction
                    (marici-int-add
                      (marici-scale-by-positive-denominator a e)
                      (marici-scale-by-positive-denominator b d))
                    (marici-int-add
                      (marici-scale-by-positive-denominator b d)
                      (marici-scale-by-positive-denominator a e))
                    (\ n → marici-raw-fraction n
                      (marici-positive-product-predecessor d e))
                    (marici-int-add-comm
                      (marici-scale-by-positive-denominator a e)
                      (marici-scale-by-positive-denominator b d)))
                  (ap MariciNat MariciRawFraction
                    (marici-positive-product-predecessor d e)
                    (marici-positive-product-predecessor e d)
                    (\ g → marici-raw-fraction
                      (marici-int-add
                        (marici-scale-by-positive-denominator b d)
                        (marici-scale-by-positive-denominator a e)) g)
                    (marici-positive-product-predecessor-comm d e))))
```

```rzk
#define marici-raw-fraction-add-zero-right
  ( p : MariciRawFraction)
  : marici-raw-fraction-add p (marici-raw-zero-at marici-zero)
    =_{MariciRawFraction} p
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciRawFraction
            (marici-raw-fraction
              (marici-int-add
                (marici-int-mul a marici-int-one)
                marici-int-zero)
              (marici-positive-product-predecessor d marici-zero))
            (marici-raw-fraction a
              (marici-positive-product-predecessor d marici-zero))
            (marici-raw-fraction a d)
            (ap MariciInt MariciRawFraction
              (marici-int-add
                (marici-int-mul a marici-int-one)
                marici-int-zero)
              a
              (\ n → marici-raw-fraction n
                (marici-positive-product-predecessor d marici-zero))
              (concat MariciInt
                (marici-int-add
                  (marici-int-mul a marici-int-one)
                  marici-int-zero)
                (marici-int-mul a marici-int-one)
                a
                (marici-int-add-zero-right
                  (marici-int-mul a marici-int-one))
                (marici-int-mul-one-right a)))
            (ap MariciNat MariciRawFraction
              (marici-positive-product-predecessor d marici-zero) d
              (\ g → marici-raw-fraction a g)
              (marici-positive-product-one-right d)))

#define marici-raw-fraction-add-zero-left
  ( p : MariciRawFraction)
  : marici-raw-fraction-add
      (marici-raw-zero-at marici-zero) p
    =_{MariciRawFraction} p
  := concat MariciRawFraction
      (marici-raw-fraction-add
        (marici-raw-zero-at marici-zero) p)
      (marici-raw-fraction-add p
        (marici-raw-zero-at marici-zero))
      p
      (marici-raw-fraction-add-comm
        (marici-raw-zero-at marici-zero) p)
      (marici-raw-fraction-add-zero-right p)
```

## Boundary

These strict raw laws require only integer addition commutativity and unit laws.
Raw addition associativity and relation congruence still depend on the open
integer addition-associativity and distributivity interfaces.
