# Raw reciprocal preserves nonzeroness and is involutive

The reciprocal numerator is the original positive denominator with the input
sign, so it is structurally nonzero. Applying the sign-aware exchange twice
returns the original raw presentation.

```rzk
#lang rzk-1
```

```rzk
#define marici-components-reciprocal-numerator-nonzero
  ( a : MariciInt)
  ( d : MariciNat)
  ( nonzero : (a =_{MariciInt} marici-int-zero) → MariciEmpty)
  : MariciRawFractionNumeratorNonzero
      (marici-raw-components-reciprocal a d nonzero)
  := (match a into
      (\ a-prime → (nonzero-prime :
          (a-prime =_{MariciInt} marici-int-zero) → MariciEmpty)
        → MariciRawFractionNumeratorNonzero
          (marici-raw-components-reciprocal
            a-prime d nonzero-prime))
      ( marici-int-zero ⇒ \ nonzero-prime →
          marici-empty-elim
            (MariciRawFractionNumeratorNonzero
              (marici-raw-components-reciprocal
                marici-int-zero d nonzero-prime))
            (nonzero-prime refl)
      | marici-int-pos n ⇒ \ nonzero-prime →
          marici-int-pos-not-zero d
      | marici-int-neg n ⇒ \ nonzero-prime →
          marici-int-neg-not-zero d)) nonzero

#define marici-reciprocal-numerator-nonzero
  ( p : MariciRawFraction)
  ( nonzero : MariciRawFractionNumeratorNonzero p)
  : MariciRawFractionNumeratorNonzero
      (marici-raw-fraction-reciprocal p nonzero)
  := (match p into
      (\ p-prime → (nonzero-prime :
          MariciRawFractionNumeratorNonzero p-prime)
        → MariciRawFractionNumeratorNonzero
          (marici-raw-fraction-reciprocal p-prime nonzero-prime))
      ( marici-raw-fraction a d ⇒ \ nonzero-prime →
          marici-components-reciprocal-numerator-nonzero
            a d nonzero-prime)) nonzero

#define marici-components-reciprocal-involutive
  ( a : MariciInt)
  ( d : MariciNat)
  ( nonzero : (a =_{MariciInt} marici-int-zero) → MariciEmpty)
  : marici-raw-fraction-reciprocal
      (marici-raw-components-reciprocal a d nonzero)
      (marici-components-reciprocal-numerator-nonzero a d nonzero)
      =_{MariciRawFraction} marici-raw-fraction a d
  := (match a into
      (\ a-prime → (nonzero-prime :
          (a-prime =_{MariciInt} marici-int-zero) → MariciEmpty)
        → marici-raw-fraction-reciprocal
            (marici-raw-components-reciprocal
              a-prime d nonzero-prime)
            (marici-components-reciprocal-numerator-nonzero
              a-prime d nonzero-prime)
            =_{MariciRawFraction} marici-raw-fraction a-prime d)
      ( marici-int-zero ⇒ \ nonzero-prime →
          marici-empty-elim
            (marici-raw-fraction-reciprocal
              (marici-raw-components-reciprocal
                marici-int-zero d nonzero-prime)
              (marici-components-reciprocal-numerator-nonzero
                marici-int-zero d nonzero-prime)
              =_{MariciRawFraction}
            marici-raw-fraction marici-int-zero d)
            (nonzero-prime refl)
      | marici-int-pos n ⇒ \ nonzero-prime → refl
      | marici-int-neg n ⇒ \ nonzero-prime → refl)) nonzero

#define marici-raw-fraction-reciprocal-involutive
  ( p : MariciRawFraction)
  ( nonzero : MariciRawFractionNumeratorNonzero p)
  : marici-raw-fraction-reciprocal
      (marici-raw-fraction-reciprocal p nonzero)
      (marici-reciprocal-numerator-nonzero p nonzero)
      =_{MariciRawFraction} p
  := (match p into
      (\ p-prime → (nonzero-prime :
          MariciRawFractionNumeratorNonzero p-prime)
        → marici-raw-fraction-reciprocal
            (marici-raw-fraction-reciprocal p-prime nonzero-prime)
            (marici-reciprocal-numerator-nonzero
              p-prime nonzero-prime)
            =_{MariciRawFraction} p-prime)
      ( marici-raw-fraction a d ⇒ \ nonzero-prime →
          marici-components-reciprocal-involutive
            a d nonzero-prime)) nonzero
```

## Boundary

Raw reciprocal is a checked-form involution on its typed nonzero domain and
constructively preserves that domain. This is a presentation-level theorem;
normalized reciprocal involution requires canonicality to identify the
normalizations inserted between applications.
