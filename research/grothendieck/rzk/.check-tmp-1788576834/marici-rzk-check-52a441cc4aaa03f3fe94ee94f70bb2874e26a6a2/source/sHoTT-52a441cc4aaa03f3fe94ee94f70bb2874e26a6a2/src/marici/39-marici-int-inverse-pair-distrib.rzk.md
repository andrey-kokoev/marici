# Distributivity over exact inverse pairs

The first opposite-sign family does not require comparison: an element plus its
exact negation is zero. Both distributive orientations therefore hold for an
arbitrary integer multiplier and arbitrary integer summand.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-inverse-pair-left-distrib
  ( x y : MariciInt)
  : marici-int-mul x
      (marici-int-add y (marici-int-negate y))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x y)
      (marici-int-mul x (marici-int-negate y))
  := concat MariciInt
      (marici-int-mul x
        (marici-int-add y (marici-int-negate y)))
      marici-int-zero
      (marici-int-add
        (marici-int-mul x y)
        (marici-int-mul x (marici-int-negate y)))
      (concat MariciInt
        (marici-int-mul x
          (marici-int-add y (marici-int-negate y)))
        (marici-int-mul x marici-int-zero)
        marici-int-zero
        (ap MariciInt MariciInt
          (marici-int-add y (marici-int-negate y))
          marici-int-zero
          (\ z → marici-int-mul x z)
          (marici-int-add-inverse-right y))
        (marici-int-mul-zero-right x))
      (rev MariciInt
        (marici-int-add
          (marici-int-mul x y)
          (marici-int-mul x (marici-int-negate y)))
        marici-int-zero
        (concat MariciInt
          (marici-int-add
            (marici-int-mul x y)
            (marici-int-mul x (marici-int-negate y)))
          (marici-int-add
            (marici-int-mul x y)
            (marici-int-negate (marici-int-mul x y)))
          marici-int-zero
          (ap MariciInt MariciInt
            (marici-int-mul x (marici-int-negate y))
            (marici-int-negate (marici-int-mul x y))
            (\ z → marici-int-add (marici-int-mul x y) z)
            (marici-int-mul-negate-right x y))
          (marici-int-add-inverse-right (marici-int-mul x y))))

#define marici-int-mul-add-inverse-pair-right-distrib
  ( x y : MariciInt)
  : marici-int-mul
      (marici-int-add y (marici-int-negate y)) x
    =_{MariciInt}
    marici-int-add
      (marici-int-mul y x)
      (marici-int-mul (marici-int-negate y) x)
  := marici-int-right-distrib-from-left x y (marici-int-negate y)
      (marici-int-mul-add-inverse-pair-left-distrib x y)
```

## Boundary

This is a global theorem for exact inverse pairs, not a finite test. Unequal
opposite-sign addends still require comparison/subtraction coherence.
