# Rational negation respects component equality

Negation factors through canonical raw components, so component equality is
sufficient for congruence. Combined with normalization retraction, this also
compares negating a canonical rational with normalizing its raw negation.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-negate-respects-component-equality
  ( p q : MariciRational)
  ( path : marici-rational-forget p
      =_{MariciRawFraction} marici-rational-forget q)
  : marici-rational-forget (marici-rational-negate p)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-negate q)
  := ap MariciRawFraction MariciRawFraction
      (marici-rational-forget p)
      (marici-rational-forget q)
      (\ raw → marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-negate raw)))
      path

#define marici-rational-negate-as-normalized-raw-negate-components
  ( q : MariciRational)
  : marici-rational-forget (marici-rational-negate q)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-fraction-negate
          (marici-rational-forget q)))
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-negate q))
      (marici-rational-forget
        (marici-rational-negate
          (marici-rational-from-raw (marici-rational-forget q))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-negate
            (marici-rational-forget q))))
      (marici-rational-negate-respects-component-equality
        q (marici-rational-from-raw (marici-rational-forget q))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-from-raw (marici-rational-forget q)))
          (marici-rational-forget q)
          (marici-rational-normalization-retraction-components q)))
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-negate
              (marici-rational-forget q))))
        (marici-rational-forget
          (marici-rational-negate
            (marici-rational-from-raw (marici-rational-forget q))))
        (marici-rational-negation-normalization-components
          (marici-rational-forget q)))
```

## Boundary

Negation is coherent with component equality and raw normalization. Absolute
value under normalized negation still requires absolute value to respect
raw-fraction equivalence, or an equivalent canonical sign lemma.
