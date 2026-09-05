# Explicit set-quotient interface and real completion carrier

Rzk's checked inductive fragment does not provide higher path constructors.
This module therefore isolates the missing set-quotient capability as explicit
assumptions rather than disguising it as a proved construction. The completed
real carrier is defined only relative to this interface.

```rzk
#lang rzk-1
```

```rzk
#define MariciIsProposition
  ( A : U)
  : U
  := ( x y : A) → x =_{A} y

#define MariciIsSet
  ( A : U)
  : U
  := ( x y : A) → MariciIsProposition (x =_{A} y)

#assume marici-set-quotient
  : ( A : U) → (A → A → U) → U

#assume marici-set-quotient-class
  : ( A : U)
  → ( relation : A → A → U)
  → A
  → marici-set-quotient A relation

#assume marici-set-quotient-sound
  : ( A : U)
  → ( relation : A → A → U)
  → ( x y : A)
  → relation x y
  → marici-set-quotient-class A relation x
    =_{marici-set-quotient A relation}
    marici-set-quotient-class A relation y

#assume marici-set-quotient-is-set
  : ( A : U)
  → ( relation : A → A → U)
  → MariciIsSet (marici-set-quotient A relation)

#define MariciReal uses (marici-set-quotient)
  : U
  := marici-set-quotient
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent

#define marici-real-from-cauchy-sequence uses (marici-set-quotient marici-set-quotient-class)
  ( sequence : MariciRationalCauchySequence)
  : marici-set-quotient
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent
  := marici-set-quotient-class
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent
      sequence

#define marici-real-equivalent-sequences-equal uses (marici-set-quotient marici-set-quotient-class marici-set-quotient-sound)
  ( x y : MariciRationalCauchySequence)
  ( equivalent : MariciRationalCauchySequencesEquivalent x y)
  : marici-set-quotient-class
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent x
    =_{marici-set-quotient
        MariciRationalCauchySequence
        MariciRationalCauchySequencesEquivalent}
    marici-set-quotient-class
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent y
  := marici-set-quotient-sound
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent
      x y equivalent

#define marici-real-is-set uses (marici-set-quotient marici-set-quotient-is-set)
  : MariciIsSet
      (marici-set-quotient
        MariciRationalCauchySequence
        MariciRationalCauchySequencesEquivalent)
  := marici-set-quotient-is-set
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent


```

## Boundary

`MariciReal` is now a typed completion carrier conditional on the five explicit
set-quotient assumptions above. This module does not claim that those
assumptions were derived from simplicial type theory or from sHoTT. A complete
formalization must replace them with an admitted library primitive or a checked
higher-inductive construction before the carrier is unconditional.
