# Reduced normal forms as an operational carrier

Normalization already contains a reduced representative, not merely its raw
projection. Extracting that representative makes the reduced-fraction type
closed under normalize-after-raw negation, addition, and multiplication.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalization-representative
  ( p : MariciRawFraction)
  ( normalization : MariciRawFractionNormalization p)
  : MariciReducedRawFraction
  := match normalization
      ( marici-raw-fraction-normalization representative preserves ⇒
          representative)

#define marici-normalize-to-reduced
  ( p : MariciRawFraction)
  : MariciReducedRawFraction
  := marici-normalization-representative p
      (marici-normalize-raw-fraction p)

#define marici-reduced-normal-form-negate
  ( p : MariciReducedRawFraction)
  : MariciReducedRawFraction
  := marici-normalize-to-reduced
      (marici-raw-fraction-negate
        (marici-reduced-raw-fraction-forget p))

#define marici-reduced-normal-form-add
  ( p q : MariciReducedRawFraction)
  : MariciReducedRawFraction
  := marici-normalize-to-reduced
      (marici-raw-fraction-add
        (marici-reduced-raw-fraction-forget p)
        (marici-reduced-raw-fraction-forget q))

#define marici-reduced-normal-form-mul
  ( p q : MariciReducedRawFraction)
  : MariciReducedRawFraction
  := marici-normalize-to-reduced
      (marici-raw-fraction-mul
        (marici-reduced-raw-fraction-forget p)
        (marici-reduced-raw-fraction-forget q))

#define marici-reduced-normal-form-zero
  : MariciReducedRawFraction
  := marici-normalize-to-reduced
      (marici-raw-fraction marici-int-zero marici-zero)

#define marici-reduced-normal-form-one
  : MariciReducedRawFraction
  := marici-normalize-to-reduced
      (marici-raw-fraction marici-int-one marici-zero)
```

Structural equality of the underlying canonical components remains executable.
This avoids requiring identity of reducedness proofs.

```rzk
#define marici-reduced-normal-forms-decide-component-equality
  ( p q : MariciReducedRawFraction)
  : MariciRawFractionEqualityDecision
      (marici-reduced-raw-fraction-forget p)
      (marici-reduced-raw-fraction-forget q)
  := marici-raw-fraction-decide-equality
      (marici-reduced-raw-fraction-forget p)
      (marici-reduced-raw-fraction-forget q)
```

## Boundary

`MariciReducedRawFraction` is now an executable normal-form carrier closed under
zero, one, negation, addition, and multiplication, with decidable component
equality. It is not yet a proved presentation-independent rational carrier:
Euclid/uniqueness must show equivalent reduced forms have equal components,
and field laws still require the outstanding integer additive laws.
