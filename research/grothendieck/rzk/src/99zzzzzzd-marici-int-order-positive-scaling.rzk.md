# Integer order is preserved by nonnegative right scaling

The scaled difference factors as the original difference times the scale.
Nonnegative multiplicative closure then transports the order witness.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-scaled-difference-right
  ( x y d : MariciInt)
  : marici-int-mul
      (marici-int-add (marici-int-negate x) y) d
    =_{MariciInt}
    marici-int-add
      (marici-int-negate (marici-int-mul x d))
      (marici-int-mul y d)
  := concat MariciInt
      (marici-int-mul (marici-int-add (marici-int-negate x) y) d)
      (marici-int-add
        (marici-int-mul (marici-int-negate x) d)
        (marici-int-mul y d))
      (marici-int-add
        (marici-int-negate (marici-int-mul x d))
        (marici-int-mul y d))
      (marici-int-mul-add-right-distrib (marici-int-negate x) y d)
      (marici-int-add-congruent
        (marici-int-mul (marici-int-negate x) d)
        (marici-int-negate (marici-int-mul x d))
        (marici-int-mul y d) (marici-int-mul y d)
        (marici-int-mul-negate-left x d) refl)

#define marici-int-at-most-mul-nonnegative-right
  ( x y d : MariciInt)
  ( xy : MariciIntAtMost x y)
  ( d-nonnegative : MariciIntIsNonnegative d)
  : MariciIntAtMost (marici-int-mul x d) (marici-int-mul y d)
  := marici-int-nonnegative-transport
      (marici-int-mul (marici-int-add (marici-int-negate x) y) d)
      (marici-int-add
        (marici-int-negate (marici-int-mul x d))
        (marici-int-mul y d))
      (marici-int-scaled-difference-right x y d)
      (marici-int-nonnegative-mul
        (marici-int-add (marici-int-negate x) y) d
        xy d-nonnegative)
```

## Boundary

This proves right-scaling monotonicity for any nonnegative integer scale.
Rational transitivity additionally requires denominator-product reassociation.
