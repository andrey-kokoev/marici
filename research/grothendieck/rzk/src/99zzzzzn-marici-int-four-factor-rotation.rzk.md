# Four-factor cross rotation

Raw-fraction addition congruence repeatedly rotates a product of two binary
products. This orientation exposes the input cross-product equalities directly.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-four-factor-rotate
  ( a b c d : MariciInt)
  : marici-int-mul (marici-int-mul a b) (marici-int-mul c d)
    =_{MariciInt}
    marici-int-mul (marici-int-mul a c) (marici-int-mul b d)
  := rev MariciInt
      (marici-int-mul (marici-int-mul a c) (marici-int-mul b d))
      (marici-int-mul (marici-int-mul a b) (marici-int-mul c d))
      (marici-int-four-factor-cross a b c d)
```

## Boundary

The theorem is the reverse orientation of the checked four-factor interchange.
It supplies no cancellation or fraction quotient. Its role is to rotate each
distributed summand before transporting raw-fraction equivalences.
