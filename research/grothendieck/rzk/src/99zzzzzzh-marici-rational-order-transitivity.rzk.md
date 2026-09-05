# Rational-order transitivity

The checked cross-product theorem specializes directly to the numerator and
positive-denominator components of three reduced rational representatives.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-at-most-transitive
  ( p q r : MariciRational)
  ( pq : MariciRationalAtMost p q)
  ( qr : MariciRationalAtMost q r)
  : MariciRationalAtMost p r
  := (match p into
      (\ p-prime → MariciRationalAtMost p-prime q
        → MariciRationalAtMost q r
        → MariciRationalAtMost p-prime r)
      ( marici-reduced-raw-fraction a d reduced-p ⇒ \ pq-prime →
          (match q into
            (\ q-prime → MariciRationalAtMost
                (marici-reduced-raw-fraction a d reduced-p) q-prime
              → MariciRationalAtMost q-prime r
              → MariciRationalAtMost
                  (marici-reduced-raw-fraction a d reduced-p) r)
            ( marici-reduced-raw-fraction b e reduced-q ⇒ \ pq-second qr-prime →
                (match r into
                  (\ r-prime → MariciRationalAtMost
                      (marici-reduced-raw-fraction b e reduced-q) r-prime
                    → MariciRationalAtMost
                      (marici-reduced-raw-fraction a d reduced-p) r-prime)
                  ( marici-reduced-raw-fraction c f reduced-r ⇒ \ qr-second →
                      marici-int-fraction-order-cross-transitive
                        a b c d e f pq-second qr-second)) qr-prime))
          pq-prime)) pq qr
```

## Boundary

Canonical rational order is now reflexive and transitive. Antisymmetry,
totality, and compatibility with rational operations remain separate theorems.
