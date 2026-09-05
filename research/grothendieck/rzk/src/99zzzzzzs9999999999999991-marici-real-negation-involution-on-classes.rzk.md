# Conditional real negation is involutive on quotient classes

The recursor computation rule is applied first under real negation and then to
the resulting pointwise-negated representative. Quotient soundness identifies
the twice-negated representative with the original Cauchy sequence.

```rzk
#lang rzk-1
```

```rzk
#define marici-real-negate-involutive-on-cauchy-class
  ( sequence : MariciRationalCauchySequence)
  : marici-real-negate
      (marici-real-negate
        (marici-real-from-cauchy-sequence sequence))
    =_{MariciReal}
    marici-real-from-cauchy-sequence sequence
  := concat MariciReal
      (marici-real-negate
        (marici-real-negate
          (marici-real-from-cauchy-sequence sequence)))
      (marici-real-negate
        (marici-real-from-cauchy-sequence
          (marici-rational-cauchy-sequence-negate sequence)))
      (marici-real-from-cauchy-sequence sequence)
      (ap MariciReal MariciReal
        (marici-real-negate
          (marici-real-from-cauchy-sequence sequence))
        (marici-real-from-cauchy-sequence
          (marici-rational-cauchy-sequence-negate sequence))
        marici-real-negate
        (marici-real-negate-from-cauchy-sequence sequence))
      (concat MariciReal
        (marici-real-negate
          (marici-real-from-cauchy-sequence
            (marici-rational-cauchy-sequence-negate sequence)))
        (marici-real-from-cauchy-sequence
          (marici-rational-cauchy-sequence-negate
            (marici-rational-cauchy-sequence-negate sequence)))
        (marici-real-from-cauchy-sequence sequence)
        (marici-real-negate-from-cauchy-sequence
          (marici-rational-cauchy-sequence-negate sequence))
        (marici-real-equivalent-sequences-equal
          (marici-rational-cauchy-sequence-negate
            (marici-rational-cauchy-sequence-negate sequence))
          sequence
          (marici-rational-cauchy-sequence-double-negate-equivalent
            sequence)))
```

## Boundary

Involutivity is proved for every explicitly represented quotient class,
conditional on set-quotient soundness and the assumed recursor computation law.
The present interface lacks dependent quotient induction, so this module does
not promote the statement to an arbitrary opaque `MariciReal` input.
