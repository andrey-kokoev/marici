# Right-factor swaps in a sum of products

After transporting the two raw-fraction equivalences, the target normal form
differs only by commuted denominator pairs. This theorem performs both swaps.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-sum-product-right-swaps
  ( a b c d e f g h : MariciInt)
  : marici-int-add
      (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-mul (marici-int-mul e f) (marici-int-mul g h))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-mul a b) (marici-int-mul d c))
      (marici-int-mul (marici-int-mul e f) (marici-int-mul h g))
  := marici-int-add-congruent
      (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-mul (marici-int-mul a b) (marici-int-mul d c))
      (marici-int-mul (marici-int-mul e f) (marici-int-mul g h))
      (marici-int-mul (marici-int-mul e f) (marici-int-mul h g))
      (ap MariciInt MariciInt
        (marici-int-mul c d) (marici-int-mul d c)
        (\ z → marici-int-mul (marici-int-mul a b) z)
        (marici-int-mul-comm c d))
      (ap MariciInt MariciInt
        (marici-int-mul g h) (marici-int-mul h g)
        (\ z → marici-int-mul (marici-int-mul e f) z)
        (marici-int-mul-comm g h))
```

## Boundary

This is only the final denominator-order normalization. It assumes no fraction
cancellation and will be composed with the two input equivalence transports.
