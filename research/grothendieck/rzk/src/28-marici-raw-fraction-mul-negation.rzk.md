# Raw-fraction multiplication and negation

Multiplication commutes with raw negation strictly at constructor level. The
denominator is unchanged on both sides, so each result follows by transporting
the checked integer numerator law.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-mul-negate-left
  ( p q : MariciRawFraction)
  : marici-raw-fraction-mul
      (marici-raw-fraction-negate p) q
    =_{MariciRawFraction}
      marici-raw-fraction-negate
        (marici-raw-fraction-mul p q)
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                ap MariciInt MariciRawFraction
                  (marici-int-mul (marici-int-negate a) b)
                  (marici-int-negate (marici-int-mul a b))
                  (\ n → marici-raw-fraction n
                    (marici-positive-product-predecessor d e))
                  (marici-int-mul-negate-left a b)))

#define marici-raw-fraction-mul-negate-right
  ( p q : MariciRawFraction)
  : marici-raw-fraction-mul p
      (marici-raw-fraction-negate q)
    =_{MariciRawFraction}
      marici-raw-fraction-negate
        (marici-raw-fraction-mul p q)
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                ap MariciInt MariciRawFraction
                  (marici-int-mul a (marici-int-negate b))
                  (marici-int-negate (marici-int-mul a b))
                  (\ n → marici-raw-fraction n
                    (marici-positive-product-predecessor d e))
                  (marici-int-mul-negate-right a b)))

#define marici-raw-fraction-mul-negate-both
  ( p q : MariciRawFraction)
  : marici-raw-fraction-mul
      (marici-raw-fraction-negate p)
      (marici-raw-fraction-negate q)
    =_{MariciRawFraction} marici-raw-fraction-mul p q
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                ap MariciInt MariciRawFraction
                  (marici-int-mul
                    (marici-int-negate a)
                    (marici-int-negate b))
                  (marici-int-mul a b)
                  (\ n → marici-raw-fraction n
                    (marici-positive-product-predecessor d e))
                  (marici-int-mul-negate-both a b)))
```

## Boundary

These are strict raw-constructor laws and need no quotient. Compatibility of
addition with negation remains downstream of integer addition associativity or
a separately checked integer negation-of-sum theorem.
