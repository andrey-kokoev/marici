# Explicit computation rule for conditional set-quotient recursion

The earlier quotient interface exposes a recursor but no rule describing its
value on a quotient class. This module isolates that missing computation law as
one additional assumption. It then derives the representative formula for
conditional real negation.

```rzk
#lang rzk-1
```

```rzk
#assume marici-set-quotient-rec-class
  : ( A : U)
  → ( relation : A → A → U)
  → ( B : U)
  → ( is-set-B : MariciIsSet B)
  → ( representative-map : A → B)
  → ( respects-relation : ( x y : A) → relation x y
      → representative-map x =_{B} representative-map y)
  → ( x : A)
  → marici-set-quotient-rec A relation B is-set-B
      representative-map respects-relation
      (marici-set-quotient-class A relation x)
    =_{B}
    representative-map x

#define marici-real-negate-from-cauchy-sequence
  ( sequence : MariciRationalCauchySequence)
  : marici-real-negate (marici-real-from-cauchy-sequence sequence)
    =_{MariciReal}
    marici-real-from-cauchy-sequence
      (marici-rational-cauchy-sequence-negate sequence)
  := marici-set-quotient-rec-class
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent
      MariciReal
      marici-real-is-set
      (\ representative → marici-real-from-cauchy-sequence
        (marici-rational-cauchy-sequence-negate representative))
      marici-real-negate-representatives-respect-equivalence
      sequence
```

## Boundary

The representative computation formula is conditional on this sixth explicit
set-quotient assumption. It is not derived from Rzk or sHoTT. A concrete
set-quotient implementation must provide and typecheck this law before
conditional real arithmetic becomes unconditional.
