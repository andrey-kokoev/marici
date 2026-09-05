# Reduced raw fractions

Reducedness is the constructive absence of a structurally nonunit common
positive factor. A reduced raw fraction packages canonical integer numerator
components, a positive denominator predecessor, and that absence proof.

```rzk
#lang rzk-1
```

```rzk
#define MariciRawComponentsAreReduced
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  : U
  := MariciRawComponentsNonunitCommonPositiveFactor
      numerator denominator-predecessor
    → MariciEmpty

#data MariciReducedRawFraction
  := marici-reduced-raw-fraction
      ( numerator : MariciInt)
      ( denominator-predecessor : MariciNat)
      ( reduced : MariciRawComponentsAreReduced
          numerator denominator-predecessor)

#define marici-reduced-raw-fraction-forget
  ( p : MariciReducedRawFraction)
  : MariciRawFraction
  := match p
      ( marici-reduced-raw-fraction a d reduced ⇒
          marici-raw-fraction a d)

#define marici-reduced-raw-fraction-no-nonunit-common-factor
  ( p : MariciReducedRawFraction)
  : match p into (\ q → U)
      ( marici-reduced-raw-fraction a d reduced ⇒
          MariciRawComponentsAreReduced a d)
  := match p
      ( marici-reduced-raw-fraction a d reduced ⇒ reduced)
```

## Boundary

The target type for normalized representatives is now explicit: a raw fraction
plus constructive evidence excluding every nonunit common positive factor.
No inhabitant is manufactured without that evidence. Existence requires a
factor-selection and decreasing-removal theorem; representative uniqueness
requires a coprime cross-product argument.
