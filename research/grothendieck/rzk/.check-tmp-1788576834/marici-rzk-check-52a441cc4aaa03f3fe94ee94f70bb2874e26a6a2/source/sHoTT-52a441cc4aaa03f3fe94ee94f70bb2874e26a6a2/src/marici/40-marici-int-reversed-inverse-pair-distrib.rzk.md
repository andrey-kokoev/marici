# Distributivity over reversed exact inverse pairs

The opposite ordering of an exact inverse pair is handled independently through
the left-inverse law. This closes both orderings of the equal-magnitude
opposite-sign frontier.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-reversed-inverse-pair-left-distrib
  ( x y : MariciInt)
  : marici-int-mul x
      (marici-int-add (marici-int-negate y) y)
    =_{MariciInt}
    marici-int-add
      (marici-int-mul x (marici-int-negate y))
      (marici-int-mul x y)
  := concat MariciInt
      (marici-int-mul x
        (marici-int-add (marici-int-negate y) y))
      marici-int-zero
      (marici-int-add
        (marici-int-mul x (marici-int-negate y))
        (marici-int-mul x y))
      (concat MariciInt
        (marici-int-mul x
          (marici-int-add (marici-int-negate y) y))
        (marici-int-mul x marici-int-zero)
        marici-int-zero
        (ap MariciInt MariciInt
          (marici-int-add (marici-int-negate y) y)
          marici-int-zero
          (\ z → marici-int-mul x z)
          (marici-int-add-inverse-left y))
        (marici-int-mul-zero-right x))
      (rev MariciInt
        (marici-int-add
          (marici-int-mul x (marici-int-negate y))
          (marici-int-mul x y))
        marici-int-zero
        (concat MariciInt
          (marici-int-add
            (marici-int-mul x (marici-int-negate y))
            (marici-int-mul x y))
          (marici-int-add
            (marici-int-negate (marici-int-mul x y))
            (marici-int-mul x y))
          marici-int-zero
          (ap MariciInt MariciInt
            (marici-int-mul x (marici-int-negate y))
            (marici-int-negate (marici-int-mul x y))
            (\ z → marici-int-add z (marici-int-mul x y))
            (marici-int-mul-negate-right x y))
          (marici-int-add-inverse-left (marici-int-mul x y))))

#define marici-int-mul-add-reversed-inverse-pair-right-distrib
  ( x y : MariciInt)
  : marici-int-mul
      (marici-int-add (marici-int-negate y) y) x
    =_{MariciInt}
    marici-int-add
      (marici-int-mul (marici-int-negate y) x)
      (marici-int-mul y x)
  := marici-int-right-distrib-from-left
      x (marici-int-negate y) y
      (marici-int-mul-add-reversed-inverse-pair-left-distrib x y)
```

## Boundary

Both orderings of exact inverse pairs now satisfy both distributive
orientations for arbitrary integers. The remaining opposite-sign frontier has
unequal magnitudes and requires comparison/subtraction coherence.
