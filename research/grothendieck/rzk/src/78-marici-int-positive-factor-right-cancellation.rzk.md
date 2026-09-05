# Positive canonical-integer right cancellation

Integer multiplication commutativity transports positive-factor injectivity to
the right multiplication orientation.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-positive-right-injective
  ( p : MariciNat)
  ( x y : MariciInt)
  ( e : marici-int-mul x (marici-int-pos p)
      =_{MariciInt} marici-int-mul y (marici-int-pos p))
  : x =_{MariciInt} y
  := marici-int-positive-left-injective p x y
      (concat MariciInt
        (marici-int-mul (marici-int-pos p) x)
        (marici-int-mul x (marici-int-pos p))
        (marici-int-mul (marici-int-pos p) y)
        (marici-int-mul-comm (marici-int-pos p) x)
        (concat MariciInt
          (marici-int-mul x (marici-int-pos p))
          (marici-int-mul y (marici-int-pos p))
          (marici-int-mul (marici-int-pos p) y)
          e
          (marici-int-mul-comm y (marici-int-pos p))))
```

## Boundary

Multiplication by every positive canonical integer is injective in both
orientations. The cancellation theorem is now available for the shared
positive denominator factor in raw-fraction relation transitivity.
