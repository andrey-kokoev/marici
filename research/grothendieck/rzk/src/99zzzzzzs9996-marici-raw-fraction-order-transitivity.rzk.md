# Raw-fraction order is transitive

The previously proved cross-product integer theorem lifts directly through the
three raw-fraction constructors, giving transitivity of raw-fraction order.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-at-most-transitive
  ( p q r : MariciRawFraction)
  ( pq : MariciRawFractionAtMost p q)
  ( qr : MariciRawFractionAtMost q r)
  : MariciRawFractionAtMost p r
  := match p into
      (\ p-prime → MariciRawFractionAtMost p-prime q
        → MariciRawFractionAtMost q r
        → MariciRawFractionAtMost p-prime r)
      ( marici-raw-fraction a d ⇒
          match q into
          (\ q-prime →
            MariciRawFractionAtMost (marici-raw-fraction a d) q-prime
            → MariciRawFractionAtMost q-prime r
            → MariciRawFractionAtMost (marici-raw-fraction a d) r)
          ( marici-raw-fraction b e ⇒
              match r into
              (\ r-prime →
                MariciRawFractionAtMost
                  (marici-raw-fraction a d) (marici-raw-fraction b e)
                → MariciRawFractionAtMost
                  (marici-raw-fraction b e) r-prime
                → MariciRawFractionAtMost
                  (marici-raw-fraction a d) r-prime)
              ( marici-raw-fraction c f ⇒
                  \ ab bc →
                    marici-int-fraction-order-cross-transitive
                      a b c d e f ab bc)))
      pq qr
```

## Boundary

Raw-fraction order now composes. Transport across raw equivalence can next be
constructed by turning each cross-product equality into order witnesses in both
directions and composing them with this theorem.
