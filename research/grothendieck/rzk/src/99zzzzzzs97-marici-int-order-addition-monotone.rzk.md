# Integer addition is monotone

Commutativity converts right-translation invariance into left-translation
invariance. Composing one translation in each argument proves two-sided
addition monotonicity.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-at-most-add-left
  ( x y z : MariciInt)
  ( witness : MariciIntAtMost x y)
  : MariciIntAtMost
      (marici-int-add z x) (marici-int-add z y)
  := marici-int-at-most-transport-both
      (marici-int-add x z) (marici-int-add z x)
      (marici-int-add y z) (marici-int-add z y)
      (marici-int-add-comm x z)
      (marici-int-add-comm y z)
      (marici-int-at-most-add-right x y z witness)

#define marici-int-at-most-add-both
  ( x y u v : MariciInt)
  ( left-witness : MariciIntAtMost x y)
  ( right-witness : MariciIntAtMost u v)
  : MariciIntAtMost
      (marici-int-add x u) (marici-int-add y v)
  := marici-int-at-most-transitive
      (marici-int-add x u)
      (marici-int-add y u)
      (marici-int-add y v)
      (marici-int-at-most-add-right x y u left-witness)
      (marici-int-at-most-add-left u v y right-witness)
```

## Boundary

Integer addition is monotone in each argument and jointly monotone. Rational
addition monotonicity still requires cross-denominator transport through
normalization.
