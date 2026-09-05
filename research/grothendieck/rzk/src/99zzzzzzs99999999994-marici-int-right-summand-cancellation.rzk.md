# Integer addition cancels its right summand

Associativity aligns the right summand with its inverse. Integer inverse and
right-zero laws then remove the pair. This is the direct cancellation shape
produced after distributing a translated raw-fraction numerator.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-then-subtract-right
  ( a b : MariciInt)
  : marici-int-add
      (marici-int-add a b)
      (marici-int-negate b)
    =_{MariciInt}
    a
  := concat MariciInt
      (marici-int-add
        (marici-int-add a b)
        (marici-int-negate b))
      (marici-int-add a marici-int-zero)
      a
      (concat MariciInt
        (marici-int-add
          (marici-int-add a b)
          (marici-int-negate b))
        (marici-int-add a
          (marici-int-add b (marici-int-negate b)))
        (marici-int-add a marici-int-zero)
        (marici-int-add-assoc a b (marici-int-negate b))
        (ap MariciInt MariciInt
          (marici-int-add b (marici-int-negate b))
          marici-int-zero
          (\ residual → marici-int-add a residual)
          (marici-int-add-inverse-right b)))
      (marici-int-add-zero-right a)
```

## Boundary

Both left- and right-summand integer cancellation forms are now available.
The next proof must distribute and reassociate the cross-products for
`((p + q) - p) ~ q`, then descend that raw equivalence through rational
normalization to identify accumulated partial-sum differences with shifted
tails.
