# Adjacent positive denominators differ by one

Embedding preservation of natural addition rewrites the larger adjacent
positive denominator as one plus the smaller. Integer associativity and inverse
cancellation then compute their difference exactly.

```rzk
#lang rzk-1
```

```rzk
#define marici-adjacent-positive-denominator-difference
  ( n : MariciNat)
  : marici-int-add
      (marici-int-positive-denominator (marici-succ n))
      (marici-int-negate (marici-int-positive-denominator n))
    =_{MariciInt}
    marici-int-one
  := concat MariciInt
      (marici-int-add
        (marici-int-positive-denominator (marici-succ n))
        (marici-int-negate (marici-int-positive-denominator n)))
      (marici-int-add
        (marici-int-add marici-int-one
          (marici-int-positive-denominator n))
        (marici-int-negate (marici-int-positive-denominator n)))
      marici-int-one
      (marici-int-add-congruent
        (marici-int-positive-denominator (marici-succ n))
        (marici-int-add marici-int-one
          (marici-int-positive-denominator n))
        (marici-int-negate (marici-int-positive-denominator n))
        (marici-int-negate (marici-int-positive-denominator n))
        (marici-int-embed-add marici-one (marici-succ n))
        refl)
      (concat MariciInt
        (marici-int-add
          (marici-int-add marici-int-one
            (marici-int-positive-denominator n))
          (marici-int-negate (marici-int-positive-denominator n)))
        (marici-int-add marici-int-one marici-int-zero)
        marici-int-one
        (concat MariciInt
          (marici-int-add
            (marici-int-add marici-int-one
              (marici-int-positive-denominator n))
            (marici-int-negate (marici-int-positive-denominator n)))
          (marici-int-add marici-int-one
            (marici-int-add
              (marici-int-positive-denominator n)
              (marici-int-negate (marici-int-positive-denominator n))))
          (marici-int-add marici-int-one marici-int-zero)
          (marici-int-add-assoc marici-int-one
            (marici-int-positive-denominator n)
            (marici-int-negate (marici-int-positive-denominator n)))
          (ap MariciInt MariciInt
            (marici-int-add
              (marici-int-positive-denominator n)
              (marici-int-negate (marici-int-positive-denominator n)))
            marici-int-zero
            (\ residual → marici-int-add marici-int-one residual)
            (marici-int-add-inverse-right
              (marici-int-positive-denominator n))))
        (marici-int-add-zero-right marici-int-one))
```

## Boundary

The numerator of the difference between adjacent reciprocal tolerances now
reduces to one. Packaging this identity as raw-fraction equivalence supplies the
pointwise telescoping term used by the exponent-two majorant.
