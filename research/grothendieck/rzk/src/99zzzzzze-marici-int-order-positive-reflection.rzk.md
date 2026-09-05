# Positive scaling reflects integer order

Multiplication by a structurally positive denominator preserves the sign of a
canonical integer. Nonnegativity, and hence order, can therefore be reflected
back through that scale.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-nonnegative-positive-product-reflects-left
  ( x : MariciInt)
  ( d : MariciNat)
  ( product-nonnegative : MariciIntIsNonnegative
      (marici-int-mul x (marici-int-positive-denominator d)))
  : MariciIntIsNonnegative x
  := (match x into
      (\ x-prime → MariciIntIsNonnegative
          (marici-int-mul x-prime (marici-int-positive-denominator d))
        → MariciIntIsNonnegative x-prime)
      ( marici-int-zero ⇒ \ witness → marici-trivial
      | marici-int-pos a ⇒ \ witness → marici-trivial
      | marici-int-neg a ⇒ \ witness →
          marici-empty-elim
            (MariciIntIsNonnegative (marici-int-neg a)) witness))
      product-nonnegative

#define marici-int-at-most-positive-scale-right-reflects
  ( x y : MariciInt)
  ( d : MariciNat)
  ( scaled : MariciIntAtMost
      (marici-int-mul x (marici-int-positive-denominator d))
      (marici-int-mul y (marici-int-positive-denominator d)))
  : MariciIntAtMost x y
  := marici-int-nonnegative-positive-product-reflects-left
      (marici-int-add (marici-int-negate x) y) d
      (marici-int-nonnegative-transport
        (marici-int-add
          (marici-int-negate
            (marici-int-mul x (marici-int-positive-denominator d)))
          (marici-int-mul y (marici-int-positive-denominator d)))
        (marici-int-mul
          (marici-int-add (marici-int-negate x) y)
          (marici-int-positive-denominator d))
        (rev MariciInt
          (marici-int-mul
            (marici-int-add (marici-int-negate x) y)
            (marici-int-positive-denominator d))
          (marici-int-add
            (marici-int-negate
              (marici-int-mul x (marici-int-positive-denominator d)))
            (marici-int-mul y (marici-int-positive-denominator d)))
          (marici-int-scaled-difference-right x y
            (marici-int-positive-denominator d)))
        scaled)
```

## Boundary

Order reflection is proved only for the structurally positive denominator
scales used by rational cross-products. This is the cancellation gate required
for rational-order transitivity.
