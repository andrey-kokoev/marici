# Decidable zero and reciprocal on reduced normal forms

A reduced normal form is zero exactly when its canonical numerator is zero at
the presentation level. Integer decidable equality therefore selects either a
zero path or the evidence required by sign-aware reciprocal.

```rzk
#lang rzk-1
```

```rzk
#define MariciReducedNormalFormNonzero
  ( p : MariciReducedRawFraction)
  : U
  := MariciRawFractionNumeratorNonzero
      (marici-reduced-raw-fraction-forget p)

#data MariciReducedNormalFormZeroDecision
  ( p : MariciReducedRawFraction)
  := marici-reduced-normal-form-zero-case
      ( numerator-zero : marici-raw-fraction-numerator
          (marici-reduced-raw-fraction-forget p)
        =_{MariciInt} marici-int-zero)
  | marici-reduced-normal-form-nonzero-case
      ( numerator-nonzero : MariciReducedNormalFormNonzero p)

#define marici-reduced-normal-form-decide-zero
  ( p : MariciReducedRawFraction)
  : MariciReducedNormalFormZeroDecision p
  := match (marici-int-decide-equality
      (marici-raw-fraction-numerator
        (marici-reduced-raw-fraction-forget p))
      marici-int-zero)
      ( marici-int-equal path ⇒
          marici-reduced-normal-form-zero-case p path
      | marici-int-unequal refutation ⇒
          marici-reduced-normal-form-nonzero-case p refutation)

#define marici-reduced-normal-form-reciprocal
  ( p : MariciReducedRawFraction)
  ( nonzero : MariciReducedNormalFormNonzero p)
  : MariciReducedRawFraction
  := marici-normalize-to-reduced
      (marici-raw-fraction-reciprocal
        (marici-reduced-raw-fraction-forget p)
        nonzero)
```

## Boundary

The reduced normal-form carrier now has decidable zero testing and a total
reciprocal on the selected nonzero branch. This is an executable partial-field
interface. Proving that numerator-zero agrees with rational zero across all
presentations and that reciprocal satisfies its field law still requires
canonicality and the Euclid theorem.
