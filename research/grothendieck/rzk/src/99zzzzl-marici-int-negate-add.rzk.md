# Integer negation preserves same-sign addition

Canonical sign reversal commutes definitionally with addition on both nonzero
same-sign faces. These paths isolate the remaining negation/addition
compatibility obligation to opposite-sign normalization.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-negate-add-positive
  ( a b : MariciNat)
  : marici-int-negate
      (marici-int-add (marici-int-pos a) (marici-int-pos b))
    =_{MariciInt}
    marici-int-add
      (marici-int-negate (marici-int-pos a))
      (marici-int-negate (marici-int-pos b))
  := refl

#define marici-int-negate-add-negative
  ( a b : MariciNat)
  : marici-int-negate
      (marici-int-add (marici-int-neg a) (marici-int-neg b))
    =_{MariciInt}
    marici-int-add
      (marici-int-negate (marici-int-neg a))
      (marici-int-negate (marici-int-neg b))
  := refl
```

## Boundary

Negation/addition compatibility is checked on both nonzero same-sign faces.
The attempted all-sign theorem exposed the exact residual: mixed-sign output is
an ordering-indexed normalizer, so its negation is not definitionally the
reversed mixed normalizer. A comparison-duality theorem is required before
negation can transport one mixed associativity face to its sign reverse.
