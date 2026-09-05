# Zero-factor mixed distributivity

The zero multiplier annihilates the mixed source sum and both summands. This
settles the zero constructor of the remaining multiplier case split.

```rzk
#lang rzk-1
```

```rzk
#define marici-zero-factor-mixed-left-distrib
  ( a b : MariciNat)
  : marici-int-mul marici-int-zero
      (marici-int-add (marici-int-pos a) (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-mul marici-int-zero (marici-int-pos a))
      (marici-int-mul marici-int-zero (marici-int-neg b))
  := refl
```

## Boundary

The zero and positive multiplier constructors now satisfy the unrestricted
positive-plus-negative family. The negative multiplier constructor remains.
