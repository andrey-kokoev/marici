# Positive-oriented integer differences compose

Two differences written as `x + (-y)` and `y + (-z)` compose by cancellation
of the middle integer. This is the orientation occurring in raw rational
subtraction numerators.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-positive-differences
  ( x y z : MariciInt)
  : marici-int-add
      (marici-int-add x (marici-int-negate y))
      (marici-int-add y (marici-int-negate z))
    =_{MariciInt}
    marici-int-add x (marici-int-negate z)
  := concat MariciInt
      (marici-int-add
        (marici-int-add x (marici-int-negate y))
        (marici-int-add y (marici-int-negate z)))
      (marici-int-add x
        (marici-int-add (marici-int-negate y)
          (marici-int-add y (marici-int-negate z))))
      (marici-int-add x (marici-int-negate z))
      (marici-int-add-assoc x (marici-int-negate y)
        (marici-int-add y (marici-int-negate z)))
      (ap MariciInt MariciInt
        (marici-int-add (marici-int-negate y)
          (marici-int-add y (marici-int-negate z)))
        (marici-int-negate z)
        (\ remainder → marici-int-add x remainder)
        (concat MariciInt
          (marici-int-add (marici-int-negate y)
            (marici-int-add y (marici-int-negate z)))
          (marici-int-add (marici-int-negate y)
            (marici-int-add
              (marici-int-negate (marici-int-negate y))
              (marici-int-negate z)))
          (marici-int-negate z)
          (ap MariciInt MariciInt
            y (marici-int-negate (marici-int-negate y))
            (\ middle → marici-int-add (marici-int-negate y)
              (marici-int-add middle (marici-int-negate z)))
            (rev MariciInt
              (marici-int-negate (marici-int-negate y)) y
              (marici-int-negate-involutive y)))
          (marici-int-middle-cancel
            (marici-int-negate y) (marici-int-negate z))))
```

## Boundary

Positive-oriented differences now compose exactly. The common-denominator
triangle lift still requires distributing the three positive denominator
factors before applying this identity.
