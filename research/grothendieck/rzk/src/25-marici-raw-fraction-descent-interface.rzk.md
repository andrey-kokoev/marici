# Conditional multiplicative descent interface for raw fractions

The previously separate relation proofs are packaged into the exact interface
needed before constructing quotient-level multiplication. The package remains
conditional only on positive integer cancellation.

```rzk
#lang rzk-1

#data MariciRawFractionMultiplicativeDescentLaws
  := marici-raw-fraction-multiplicative-descent-laws
      ( raw-relation-reflexive
        : ( p : MariciRawFraction)
        → marici-raw-fraction-equivalent p p)
      ( raw-relation-symmetric
        : ( p q : MariciRawFraction)
        → marici-raw-fraction-equivalent p q
        → marici-raw-fraction-equivalent q p)
      ( raw-relation-transitive
        : ( p q r : MariciRawFraction)
        → marici-raw-fraction-equivalent p q
        → marici-raw-fraction-equivalent q r
        → marici-raw-fraction-equivalent p r)
      ( raw-multiplication-congruent
        : ( p p-prime q q-prime : MariciRawFraction)
        → marici-raw-fraction-equivalent p p-prime
        → marici-raw-fraction-equivalent q q-prime
        → marici-raw-fraction-equivalent
            (marici-raw-fraction-mul p q)
            (marici-raw-fraction-mul p-prime q-prime))
```

```rzk
#define marici-raw-fraction-multiplicative-descent-if-positive-cancellative
  ( cancel-positive : MariciPositiveRightCancellation)
  : MariciRawFractionMultiplicativeDescentLaws
  := marici-raw-fraction-multiplicative-descent-laws
      marici-raw-fraction-equivalent-refl
      marici-raw-fraction-equivalent-sym
      (marici-raw-fraction-equivalent-trans-if-positive-cancellative
        cancel-positive)
      marici-raw-fraction-mul-congruent
```

## Boundary

This package establishes only an equivalence relation and compatibility of raw
multiplication, conditional on positive cancellation. It does not construct a
quotient, effective quotient eliminator, canonical normalization, sethood, or
an equality-reflection principle. Raw addition is absent because its
congruence remains downstream of integer distributivity.
