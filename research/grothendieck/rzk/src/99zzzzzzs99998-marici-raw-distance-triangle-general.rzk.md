# Raw distance triangle for arbitrary raw fractions

Eliminating the three raw-fraction constructors lifts the component theorem to
an interface stated directly in raw subtraction, absolute value, and addition.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-distance-triangle
  ( p q r : MariciRawFraction)
  : MariciRawFractionAtMost
      (marici-raw-fraction-absolute
        (marici-raw-fraction-subtract p r))
      (marici-raw-fraction-add
        (marici-raw-fraction-absolute
          (marici-raw-fraction-subtract p q))
        (marici-raw-fraction-absolute
          (marici-raw-fraction-subtract q r)))
  := match p into
      (\ p-prime →
        MariciRawFractionAtMost
          (marici-raw-fraction-absolute
            (marici-raw-fraction-subtract p-prime r))
          (marici-raw-fraction-add
            (marici-raw-fraction-absolute
              (marici-raw-fraction-subtract p-prime q))
            (marici-raw-fraction-absolute
              (marici-raw-fraction-subtract q r))))
      ( marici-raw-fraction a d ⇒
          match q into
          (\ q-prime →
            MariciRawFractionAtMost
              (marici-raw-fraction-absolute
                (marici-raw-fraction-subtract
                  (marici-raw-fraction a d) r))
              (marici-raw-fraction-add
                (marici-raw-fraction-absolute
                  (marici-raw-fraction-subtract
                    (marici-raw-fraction a d) q-prime))
                (marici-raw-fraction-absolute
                  (marici-raw-fraction-subtract q-prime r))))
          ( marici-raw-fraction b e ⇒
              match r into
              (\ r-prime →
                MariciRawFractionAtMost
                  (marici-raw-fraction-absolute
                    (marici-raw-fraction-subtract
                      (marici-raw-fraction a d) r-prime))
                  (marici-raw-fraction-add
                    (marici-raw-fraction-absolute
                      (marici-raw-fraction-subtract
                        (marici-raw-fraction a d)
                        (marici-raw-fraction b e)))
                    (marici-raw-fraction-absolute
                      (marici-raw-fraction-subtract
                        (marici-raw-fraction b e) r-prime))))
              ( marici-raw-fraction c f ⇒
                  marici-raw-rational-distance-triangle
                    a b c d e f)))
```

## Boundary

The raw triangle inequality now accepts arbitrary raw fractions. It can be
instantiated directly with the forgotten components of three rationals, avoiding
elimination of reducedness witnesses in the rational theorem.
