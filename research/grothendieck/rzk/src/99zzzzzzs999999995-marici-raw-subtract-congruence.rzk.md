# Raw subtraction preserves fraction equivalence

Negating both numerators transports a cross-product equality by integer
negation. Addition congruence then proves that raw subtraction respects
equivalence in both inputs.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-negate-congruent-components
  ( a b : MariciInt)
  ( d e : MariciNat)
  ( cross-path : marici-scale-by-positive-denominator a e
    =_{MariciInt}
    marici-scale-by-positive-denominator b d)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-negate (marici-raw-fraction a d))
      (marici-raw-fraction-negate (marici-raw-fraction b e))
  := concat MariciInt
      (marici-int-mul (marici-int-negate a)
        (marici-int-positive-denominator e))
      (marici-int-negate
        (marici-int-mul b (marici-int-positive-denominator d)))
      (marici-int-mul (marici-int-negate b)
        (marici-int-positive-denominator d))
      (concat MariciInt
        (marici-int-mul (marici-int-negate a)
          (marici-int-positive-denominator e))
        (marici-int-negate
          (marici-int-mul a (marici-int-positive-denominator e)))
        (marici-int-negate
          (marici-int-mul b (marici-int-positive-denominator d)))
        (marici-int-mul-negate-left a
          (marici-int-positive-denominator e))
        (ap MariciInt MariciInt
          (marici-int-mul a (marici-int-positive-denominator e))
          (marici-int-mul b (marici-int-positive-denominator d))
          marici-int-negate cross-path))
      (rev MariciInt
        (marici-int-mul (marici-int-negate b)
          (marici-int-positive-denominator d))
        (marici-int-negate
          (marici-int-mul b (marici-int-positive-denominator d)))
        (marici-int-mul-negate-left b
          (marici-int-positive-denominator d)))

#define marici-raw-fraction-negate-congruent
  ( p q : MariciRawFraction)
  : marici-raw-fraction-equivalent p q
    → marici-raw-fraction-equivalent
      (marici-raw-fraction-negate p)
      (marici-raw-fraction-negate q)
  := match p into
      (\ p-prime → marici-raw-fraction-equivalent p-prime q
        → marici-raw-fraction-equivalent
          (marici-raw-fraction-negate p-prime)
          (marici-raw-fraction-negate q))
      ( marici-raw-fraction a d ⇒
        match q into
        (\ q-prime →
          marici-raw-fraction-equivalent
            (marici-raw-fraction a d) q-prime
          → marici-raw-fraction-equivalent
            (marici-raw-fraction-negate (marici-raw-fraction a d))
            (marici-raw-fraction-negate q-prime))
        ( marici-raw-fraction b e ⇒
          marici-raw-fraction-negate-congruent-components a b d e))

#define marici-raw-fraction-subtract-congruent
  ( p p-prime q q-prime : MariciRawFraction)
  ( left-equivalent : marici-raw-fraction-equivalent p p-prime)
  ( right-equivalent : marici-raw-fraction-equivalent q q-prime)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-subtract p q)
      (marici-raw-fraction-subtract p-prime q-prime)
  := marici-raw-fraction-add-congruent
      p p-prime
      (marici-raw-fraction-negate q)
      (marici-raw-fraction-negate q-prime)
      left-equivalent
      (marici-raw-fraction-negate-congruent
        q q-prime right-equivalent)
```

## Boundary

Raw subtraction now descends across fraction equivalence. This enables
flattening rational subtraction of normalized raw inputs and identifying the
adjacent reciprocal majorant at the rational component level.
