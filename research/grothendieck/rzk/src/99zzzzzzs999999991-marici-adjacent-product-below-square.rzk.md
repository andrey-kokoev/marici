# Adjacent positive product is bounded by the larger square

The adjacent-denominator difference proves that the smaller positive
denominator is at most the larger. Positive scaling by the larger denominator
then compares their product with the larger square.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-denominator-at-most-successor
  ( n : MariciNat)
  : MariciIntAtMost
      (marici-int-positive-denominator n)
      (marici-int-positive-denominator (marici-succ n))
  := marici-int-nonnegative-transport
      marici-int-one
      (marici-int-add
        (marici-int-negate (marici-int-positive-denominator n))
        (marici-int-positive-denominator (marici-succ n)))
      (rev MariciInt
        (marici-int-add
          (marici-int-negate (marici-int-positive-denominator n))
          (marici-int-positive-denominator (marici-succ n)))
        marici-int-one
        (concat MariciInt
          (marici-int-add
            (marici-int-negate (marici-int-positive-denominator n))
            (marici-int-positive-denominator (marici-succ n)))
          (marici-int-add
            (marici-int-positive-denominator (marici-succ n))
            (marici-int-negate (marici-int-positive-denominator n)))
          marici-int-one
          (marici-int-add-comm
            (marici-int-negate (marici-int-positive-denominator n))
            (marici-int-positive-denominator (marici-succ n)))
          (marici-adjacent-positive-denominator-difference n)))
      marici-trivial

#define marici-adjacent-positive-product-at-most-larger-square
  ( n : MariciNat)
  : MariciIntAtMost
      (marici-int-mul
        (marici-int-positive-denominator n)
        (marici-int-positive-denominator (marici-succ n)))
      (marici-int-mul
        (marici-int-positive-denominator (marici-succ n))
        (marici-int-positive-denominator (marici-succ n)))
  := marici-int-at-most-mul-nonnegative-right
      (marici-int-positive-denominator n)
      (marici-int-positive-denominator (marici-succ n))
      (marici-int-positive-denominator (marici-succ n))
      (marici-positive-denominator-at-most-successor n)
      marici-trivial
```

## Boundary

The denominator inequality behind the exponent-two telescoping majorant is now
proved. It must next be transported through encoded denominator-product paths
to obtain the corresponding reciprocal raw-fraction order.
