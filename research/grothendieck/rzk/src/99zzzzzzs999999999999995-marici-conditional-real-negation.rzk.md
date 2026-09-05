# Conditional negation on the completed real carrier

Pointwise Cauchy-sequence negation respects the completion relation. Applying
set-quotient soundness therefore makes its class map constant on equivalent
representatives, which supplies the compatibility argument required by the
set-quotient recursor.

```rzk
#lang rzk-1
```

```rzk
#define marici-real-negate-representatives-respect-equivalence
  ( x y : MariciRationalCauchySequence)
  ( equivalent : MariciRationalCauchySequencesEquivalent x y)
  : marici-real-from-cauchy-sequence
      (marici-rational-cauchy-sequence-negate x)
    =_{MariciReal}
    marici-real-from-cauchy-sequence
      (marici-rational-cauchy-sequence-negate y)
  := marici-real-equivalent-sequences-equal
      (marici-rational-cauchy-sequence-negate x)
      (marici-rational-cauchy-sequence-negate y)
      (marici-rational-cauchy-equivalence-negate x y equivalent)

#define marici-real-negate
  : MariciReal → MariciReal
  := marici-set-quotient-rec
      MariciRationalCauchySequence
      MariciRationalCauchySequencesEquivalent
      MariciReal
      marici-real-is-set
      (\ sequence → marici-real-from-cauchy-sequence
        (marici-rational-cauchy-sequence-negate sequence))
      marici-real-negate-representatives-respect-equivalence
```

## Boundary

This defines conditional real negation through the assumed set-quotient
recursor and proves the representative map respects the quotient relation. The
interface currently has no computation law for that recursor, so no theorem
identifying `marici-real-negate (marici-real-from-cauchy-sequence x)` with the
class of the pointwise-negated representative is claimed. Such a theorem needs
an explicit recursor computation rule from the quotient implementation.
