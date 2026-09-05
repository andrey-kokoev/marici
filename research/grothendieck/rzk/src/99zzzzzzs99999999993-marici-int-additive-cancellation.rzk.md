# Integer addition cancels a translated summand

Commutativity moves the retained summand left, associativity aligns the added
integer with its inverse, and the inverse and zero laws remove that pair. This
is the numerator identity required to identify an accumulated partial-sum
difference with its shifted tail.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-then-subtract-left
  ( a b : MariciInt)
  : marici-int-add
      (marici-int-add a b)
      (marici-int-negate a)
    =_{MariciInt}
    b
  := concat MariciInt
      (marici-int-add
        (marici-int-add a b)
        (marici-int-negate a))
      (marici-int-add
        (marici-int-add b a)
        (marici-int-negate a))
      b
      (marici-int-add-congruent
        (marici-int-add a b) (marici-int-add b a)
        (marici-int-negate a) (marici-int-negate a)
        (marici-int-add-comm a b) refl)
      (concat MariciInt
        (marici-int-add
          (marici-int-add b a)
          (marici-int-negate a))
        (marici-int-add b marici-int-zero)
        b
        (concat MariciInt
          (marici-int-add
            (marici-int-add b a)
            (marici-int-negate a))
          (marici-int-add b
            (marici-int-add a (marici-int-negate a)))
          (marici-int-add b marici-int-zero)
          (marici-int-add-assoc b a (marici-int-negate a))
          (ap MariciInt MariciInt
            (marici-int-add a (marici-int-negate a))
            marici-int-zero
            (\ residual → marici-int-add b residual)
            (marici-int-add-inverse-right a)))
        (marici-int-add-zero-right b))
```

## Boundary

The additive numerator cancellation needed by shifted-tail extraction is now
proved. Denominator alignment and normalization transport remain before the
partial-sum distance can be identified with the independently folded tail.
