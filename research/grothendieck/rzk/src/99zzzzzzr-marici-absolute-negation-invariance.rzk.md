# Absolute value is invariant under negation

Canonical integer magnitude forgets sign. Consequently raw-fraction absolute
value is unchanged by numerator negation.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-magnitude-negate
  ( z : MariciInt)
  : marici-int-magnitude (marici-int-negate z)
    =_{MariciNat}
    marici-int-magnitude z
  := match z
      ( marici-int-zero ⇒ refl
      | marici-int-pos n ⇒ refl
      | marici-int-neg n ⇒ refl)

#define marici-raw-fraction-absolute-negate
  ( p : MariciRawFraction)
  : marici-raw-fraction-absolute
      (marici-raw-fraction-negate p)
    =_{MariciRawFraction}
    marici-raw-fraction-absolute p
  := match p
      ( marici-raw-fraction numerator denominator-predecessor ⇒
          ap MariciNat MariciRawFraction
            (marici-int-magnitude (marici-int-negate numerator))
            (marici-int-magnitude numerator)
            (\ magnitude → marici-raw-fraction
              (marici-int-embed-nat magnitude)
              denominator-predecessor)
            (marici-int-magnitude-negate numerator))
```

## Boundary

Absolute value now ignores raw numerator sign. Distance symmetry still requires
the checked identification of one directed subtraction with the negation of the
opposite directed subtraction.
