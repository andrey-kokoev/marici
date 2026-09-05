# Raw-fraction order transports across equivalence

A cross-product equality supplies an order witness by endpoint transport from
integer reflexivity. Raw-order transitivity then transports either endpoint,
or both endpoints, across raw-fraction equivalence.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-equivalent-implies-at-most
  ( p q : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent p q)
  : MariciRawFractionAtMost p q
  := match p into
      (\ p-prime → marici-raw-fraction-equivalent p-prime q
        → MariciRawFractionAtMost p-prime q)
      ( marici-raw-fraction a d ⇒
          match q into
          (\ q-prime →
            marici-raw-fraction-equivalent
              (marici-raw-fraction a d) q-prime
            → MariciRawFractionAtMost
              (marici-raw-fraction a d) q-prime)
          ( marici-raw-fraction b e ⇒
              \ cross-path →
                marici-int-at-most-transport-right
                  (marici-int-mul a (marici-int-positive-denominator e))
                  (marici-int-mul a (marici-int-positive-denominator e))
                  (marici-int-mul b (marici-int-positive-denominator d))
                  cross-path
                  (marici-int-at-most-reflexive
                    (marici-int-mul a
                      (marici-int-positive-denominator e)))))
      equivalent

#define marici-raw-fraction-at-most-respects-equivalence
  ( p p-prime q q-prime : MariciRawFraction)
  ( left-equivalent : marici-raw-fraction-equivalent p p-prime)
  ( right-equivalent : marici-raw-fraction-equivalent q q-prime)
  ( witness : MariciRawFractionAtMost p q)
  : MariciRawFractionAtMost p-prime q-prime
  := marici-raw-fraction-at-most-transitive
      p-prime q q-prime
      (marici-raw-fraction-at-most-transitive
        p-prime p q
        (marici-raw-fraction-equivalent-implies-at-most
          p-prime p
          (marici-raw-fraction-equivalent-sym
            p p-prime left-equivalent))
        witness)
      (marici-raw-fraction-equivalent-implies-at-most
        q q-prime right-equivalent)

#define marici-raw-fraction-at-most-respects-left-equivalence
  ( p p-prime q : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent p p-prime)
  ( witness : MariciRawFractionAtMost p q)
  : MariciRawFractionAtMost p-prime q
  := marici-raw-fraction-at-most-respects-equivalence
      p p-prime q q equivalent
      (marici-raw-fraction-equivalent-refl q) witness

#define marici-raw-fraction-at-most-respects-right-equivalence
  ( p q q-prime : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent q q-prime)
  ( witness : MariciRawFractionAtMost p q)
  : MariciRawFractionAtMost p q-prime
  := marici-raw-fraction-at-most-respects-equivalence
      p p q q-prime
      (marici-raw-fraction-equivalent-refl p) equivalent witness
```

## Boundary

Raw order is now invariant under replacement by equivalent fractions. This
allows the common-denominator triangle estimate to transport back to the three
unscaled directed differences before normalization.
