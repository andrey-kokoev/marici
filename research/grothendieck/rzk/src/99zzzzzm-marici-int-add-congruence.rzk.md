# Integer addition transports equality in both arguments

This packages the two path transports needed when raw-fraction addition
congruence substitutes its two input cross-product equalities.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-congruent
  ( x x-prime y y-prime : MariciInt)
  ( x-path : x =_{MariciInt} x-prime)
  ( y-path : y =_{MariciInt} y-prime)
  : marici-int-add x y
    =_{MariciInt}
    marici-int-add x-prime y-prime
  := concat MariciInt
      (marici-int-add x y)
      (marici-int-add x-prime y)
      (marici-int-add x-prime y-prime)
      (ap MariciInt MariciInt
        x x-prime
        (\ z → marici-int-add z y)
        x-path)
      (ap MariciInt MariciInt
        y y-prime
        (\ z → marici-int-add x-prime z)
        y-path)
```

## Boundary

The theorem transports two integer equalities through addition. It introduces
no algebraic axiom. The raw-fraction addition proof must still expose its two
summands using distributivity and reassociate denominator factors before this
transport applies.
