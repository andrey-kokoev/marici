# Adjacent swaps in four-factor integer scaling

Successive right-scale commutation lifts under one further scale. Together with
the existing three-factor swap, this permits arbitrary reordering of the three
positive denominator factors used in raw-addition monotonicity.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-four-scale-swap-first-two
  ( x a b c : MariciInt)
  : marici-int-mul
      (marici-int-mul (marici-int-mul x a) b) c
    =_{MariciInt}
    marici-int-mul
      (marici-int-mul (marici-int-mul x b) a) c
  := ap MariciInt MariciInt
      (marici-int-mul (marici-int-mul x a) b)
      (marici-int-mul (marici-int-mul x b) a)
      (\ scaled → marici-int-mul scaled c)
      (marici-int-commute-right-scales x a b)

#define marici-int-four-scale-swap-last-two
  ( x a b c : MariciInt)
  : marici-int-mul
      (marici-int-mul (marici-int-mul x a) b) c
    =_{MariciInt}
    marici-int-mul
      (marici-int-mul (marici-int-mul x a) c) b
  := marici-int-commute-right-scales
      (marici-int-mul x a) b c
```

## Boundary

The denominator factors in each scaled raw-addition inequality can now be
aligned by adjacent swaps. The next theorem uses those paths with integer
addition monotonicity to establish raw-fraction addition monotonicity.
