# Integer order survives two positive right scales

Applying positive right-scaling monotonicity twice transports an integer order
witness through the two additional denominator factors required by
raw-fraction addition.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-at-most-two-positive-right-scales
  ( x y : MariciInt)
  ( first-scale second-scale : MariciNat)
  ( witness : MariciIntAtMost x y)
  : MariciIntAtMost
      (marici-int-mul
        (marici-int-mul x (marici-int-positive-denominator first-scale))
        (marici-int-positive-denominator second-scale))
      (marici-int-mul
        (marici-int-mul y (marici-int-positive-denominator first-scale))
        (marici-int-positive-denominator second-scale))
  := marici-int-at-most-mul-nonnegative-right
      (marici-int-mul x (marici-int-positive-denominator first-scale))
      (marici-int-mul y (marici-int-positive-denominator first-scale))
      (marici-int-positive-denominator second-scale)
      (marici-int-at-most-mul-nonnegative-right
        x y (marici-int-positive-denominator first-scale)
        witness marici-trivial)
      marici-trivial
```

## Boundary

Each source cross-product inequality can now be scaled by both remaining
positive denominators. Factor permutation and integer addition monotonicity are
the remaining steps in raw-fraction addition monotonicity.
