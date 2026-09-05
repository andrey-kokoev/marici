# Sign-aware normalized reciprocal

A raw fraction is nonzero when its canonical integer numerator is not zero.
For a positive numerator, reciprocal swaps the positive numerator magnitude
with the denominator. For a negative numerator it also retains the negative
sign. The impossible zero branch is eliminated by the supplied evidence.

```rzk
#lang rzk-1
```

```rzk
#define MariciRawFractionNumeratorNonzero
  ( p : MariciRawFraction)
  : U
  := (marici-raw-fraction-numerator p =_{MariciInt} marici-int-zero)
    → MariciEmpty

#define marici-raw-components-reciprocal
  ( a : MariciInt)
  ( d : MariciNat)
  ( nonzero : (a =_{MariciInt} marici-int-zero) → MariciEmpty)
  : MariciRawFraction
  := (match a into
      (\ a-prime → ((a-prime =_{MariciInt} marici-int-zero)
        → MariciEmpty) → MariciRawFraction)
      ( marici-int-zero ⇒ \ component-nonzero →
          marici-empty-elim MariciRawFraction (component-nonzero refl)
      | marici-int-pos n ⇒ \ component-nonzero →
          marici-raw-fraction (marici-int-pos d) n
      | marici-int-neg n ⇒ \ component-nonzero →
          marici-raw-fraction (marici-int-neg d) n)) nonzero

#define marici-raw-fraction-reciprocal
  ( p : MariciRawFraction)
  ( nonzero : MariciRawFractionNumeratorNonzero p)
  : MariciRawFraction
  := (match p into
      (\ p-prime → MariciRawFractionNumeratorNonzero p-prime
        → MariciRawFraction)
      ( marici-raw-fraction a d ⇒ \ component-nonzero →
          marici-raw-components-reciprocal a d component-nonzero))
      nonzero

#define marici-normalized-reciprocal-witness
  ( p : MariciRawFraction)
  ( nonzero : MariciRawFractionNumeratorNonzero p)
  : MariciRawFractionNormalization
      (marici-raw-fraction-reciprocal p nonzero)
  := marici-normalize-raw-fraction
      (marici-raw-fraction-reciprocal p nonzero)

#define marici-normal-form-reciprocal
  ( p : MariciRawFraction)
  ( nonzero : MariciRawFractionNumeratorNonzero p)
  : MariciRawFraction
  := marici-normalization-forget-representative
      (marici-raw-fraction-reciprocal p nonzero)
      (marici-normalized-reciprocal-witness p nonzero)
```

## Boundary

Reciprocal is now total on the typed nonzero domain and computes a normalized
representative. Proving its multiplication law and presentation independence
requires normalization canonicality plus the existing integer sign and
positive-product laws. The nonzero evidence is attached to the raw numerator;
descent of nonzeroness across equivalent presentations remains to be proved.
