# Reduced uniqueness and normalization canonicality are closed

The checked reduced cross-product denominator divisibility theorem plugs into
the existing order/antisymmetry bridge, producing unconditional uniqueness of
equivalent reduced representatives. The canonicality interface then shows
computed normalization agrees with every equivalent reduced target and fixes
already reduced inputs.

```rzk
#lang rzk-1
```

```rzk
#define marici-reduced-representative-uniqueness
  : MariciReducedRepresentativeUniqueness
  := marici-reduced-representative-uniqueness-from-euclid
      marici-reduced-cross-product-denominator-divisibility

#define marici-normalization-representative-canonical
  ( source : MariciRawFraction)
  ( normalization : MariciRawFractionNormalization source)
  ( target : MariciReducedRawFraction)
  ( equivalent : marici-raw-fraction-equivalent source
      (marici-reduced-raw-fraction-forget target))
  : marici-normalization-forget-representative source normalization
      =_{MariciRawFraction}
    marici-reduced-raw-fraction-forget target
  := marici-normalization-representative-canonical-if-unique
      marici-reduced-representative-uniqueness
      source normalization target equivalent

#define marici-normalized-representative-canonical
  ( source : MariciRawFraction)
  ( target : MariciReducedRawFraction)
  ( equivalent : marici-raw-fraction-equivalent source
      (marici-reduced-raw-fraction-forget target))
  : marici-normalized-raw-representative source
      =_{MariciRawFraction}
    marici-reduced-raw-fraction-forget target
  := marici-normalized-representative-canonical-if-unique
      marici-reduced-representative-uniqueness
      source target equivalent

#define marici-normalization-fixes-reduced
  ( target : MariciReducedRawFraction)
  : marici-normalized-raw-representative
      (marici-reduced-raw-fraction-forget target)
      =_{MariciRawFraction}
    marici-reduced-raw-fraction-forget target
  := marici-normalization-fixes-reduced-if-unique
      marici-reduced-representative-uniqueness target
```

## Boundary

Normalization is now canonical at the raw representative level: equivalent
reduced fractions have identical numerators and denominator predecessors, and
total normalization returns that unique representative. Presentation-
independent rational operations may now be proved by normalizing raw operation
results and using this canonicality theorem; their algebraic laws remain
separate obligations.
