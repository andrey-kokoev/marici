# Explicit proposition induction for the conditional set quotient

Nondependent quotient recursion cannot promote a representative proof whose
target depends on the quotient value. This module isolates proposition-valued
quotient induction as a seventh assumption and uses it to extend real-negation
involutivity from classes to arbitrary conditional real values.

```rzk
#lang rzk-1
```

```rzk
#assume marici-set-quotient-proposition-ind
  : ( A : U)
  → ( relation : A → A → U)
  → ( P : marici-set-quotient A relation → U)
  → (( z : marici-set-quotient A relation) → MariciIsProposition (P z))
  → (( x : A) → P (marici-set-quotient-class A relation x))
  → ( z : marici-set-quotient A relation)
  → P z

#define marici-real-negate-involutive
  ( real : MariciReal)
  : marici-real-negate (marici-real-negate real)
    =_{MariciReal}
    real
  := marici-set-quotient-proposition-ind
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent
      (\ value → marici-real-negate (marici-real-negate value)
        =_{MariciReal} value)
      (\ value → marici-real-is-set
        (marici-real-negate (marici-real-negate value)) value)
      marici-real-negate-involutive-on-cauchy-class
      real
```

## Boundary

Conditional real negation is now involutive for every `MariciReal`. The proof
depends on seven explicit quotient assumptions in total, including the recursor
computation and proposition-induction laws added after the initial five-law
interface. None is derived from Rzk or sHoTT in this development.
