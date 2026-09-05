# Integer absolute-value triangle inequality

An upper bound for both orientations of an integer bounds its absolute value.
Addition monotonicity supplies those two orientation bounds for a sum.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-absolute-at-most-from-two-orientations
  ( z upper : MariciInt)
  ( positive-bound : MariciIntAtMost z upper)
  ( negative-bound : MariciIntAtMost (marici-int-negate z) upper)
  : MariciIntAtMost (marici-int-absolute z) upper
  := (match z into
      (\ value → MariciIntAtMost value upper
        → MariciIntAtMost (marici-int-negate value) upper
        → MariciIntAtMost (marici-int-absolute value) upper)
      ( marici-int-zero ⇒ \ pos neg → pos
      | marici-int-pos n ⇒ \ pos neg → pos
      | marici-int-neg n ⇒ \ pos neg → neg))
      positive-bound negative-bound

#define marici-int-absolute-triangle
  ( x y : MariciInt)
  : MariciIntAtMost
      (marici-int-absolute (marici-int-add x y))
      (marici-int-add
        (marici-int-absolute x) (marici-int-absolute y))
  := marici-int-absolute-at-most-from-two-orientations
      (marici-int-add x y)
      (marici-int-add (marici-int-absolute x) (marici-int-absolute y))
      (marici-int-at-most-add-both
        x (marici-int-absolute x)
        y (marici-int-absolute y)
        (marici-int-at-most-absolute x)
        (marici-int-at-most-absolute y))
      (marici-int-at-most-transport-both
        (marici-int-add (marici-int-negate x) (marici-int-negate y))
        (marici-int-negate (marici-int-add x y))
        (marici-int-add (marici-int-absolute x) (marici-int-absolute y))
        (marici-int-add (marici-int-absolute x) (marici-int-absolute y))
        (rev MariciInt
          (marici-int-negate (marici-int-add x y))
          (marici-int-add (marici-int-negate x) (marici-int-negate y))
          (marici-int-negate-add x y))
        refl
        (marici-int-at-most-add-both
          (marici-int-negate x) (marici-int-absolute x)
          (marici-int-negate y) (marici-int-absolute y)
          (marici-int-negate-at-most-absolute x)
          (marici-int-negate-at-most-absolute y)))
```

## Boundary

The integer absolute-value triangle inequality is proved. Rational distance
triangle still requires cross-denominator scaling and normalization transport.
