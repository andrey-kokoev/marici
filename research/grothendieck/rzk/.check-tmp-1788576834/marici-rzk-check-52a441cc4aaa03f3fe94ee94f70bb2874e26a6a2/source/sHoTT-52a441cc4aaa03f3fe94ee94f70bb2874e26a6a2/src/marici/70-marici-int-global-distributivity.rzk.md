# Global integer distributivity

The completed positive-plus-negative family is supplied to the single-family
reduction. Integer multiplication therefore distributes over integer addition
in both orientations for arbitrary integers.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-add-left-distrib
  ( x y z : MariciInt)
  : marici-int-mul x (marici-int-add y z)
    =_{MariciInt}
    marici-int-add (marici-int-mul x y) (marici-int-mul x z)
  := marici-int-mul-add-left-distrib-from-single-mixed-branch
      marici-all-factor-positive-negative-left-distrib x y z

#define marici-int-mul-add-right-distrib
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-add x y) z
    =_{MariciInt}
    marici-int-add (marici-int-mul x z) (marici-int-mul y z)
  := marici-int-mul-add-right-distrib-from-single-mixed-branch
      marici-all-factor-positive-negative-left-distrib z x y
```

## Boundary

Both distributive orientations are checked for arbitrary canonical integers.
Mixed-sign integer addition associativity remains open, so this establishes the
distributive laws without yet packaging the integers as a ring object.
