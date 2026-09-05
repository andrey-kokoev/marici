# Raw-fraction addition is jointly monotone

Eliminating all four raw-fraction constructors lifts the component theorem to a
presentation-independent raw interface.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-at-most
  ( p p-prime q q-prime : MariciRawFraction)
  : MariciRawFractionAtMost p p-prime
  → MariciRawFractionAtMost q q-prime
  → MariciRawFractionAtMost
      (marici-raw-fraction-add p q)
      (marici-raw-fraction-add p-prime q-prime)
  := match p
      ( marici-raw-fraction a d ⇒
          match p-prime
          ( marici-raw-fraction b e ⇒
              match q
              ( marici-raw-fraction c f ⇒
                  match q-prime
                  ( marici-raw-fraction g h ⇒
                      \ first-witness second-witness →
                        marici-raw-fraction-add-at-most-components
                          a b c g d e f h
                          first-witness second-witness))))
```

## Boundary

Raw-fraction addition is now jointly monotone for arbitrary presentations.
Descending this theorem through canonical normalization yields rational
addition monotonicity, the final order operation needed by Cauchy-equivalence
transitivity.
