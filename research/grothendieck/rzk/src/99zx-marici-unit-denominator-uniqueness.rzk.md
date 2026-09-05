# Uniqueness at unit denominators

For two denominator-one fractions, cross-product equivalence reduces to equality
of the canonical integer numerators by the right unit law. Component congruence
then gives equality of the raw representatives.

```rzk
#lang rzk-1
```

```rzk
#define marici-unit-denominator-equivalent-numerators-equal
  ( a b : MariciInt)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a marici-zero)
      (marici-raw-fraction b marici-zero))
  : a =_{MariciInt} b
  := concat MariciInt
      a
      (marici-int-mul a marici-int-one)
      b
      (rev MariciInt
        (marici-int-mul a marici-int-one) a
        (marici-int-mul-one-right a))
      (concat MariciInt
        (marici-int-mul a marici-int-one)
        (marici-int-mul b marici-int-one)
        b
        equivalent
        (marici-int-mul-one-right b))

#define marici-unit-denominator-equivalent-raw-fractions-equal
  ( a b : MariciInt)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction a marici-zero)
      (marici-raw-fraction b marici-zero))
  : marici-raw-fraction a marici-zero =_{MariciRawFraction}
      marici-raw-fraction b marici-zero
  := marici-raw-fraction-component-path
      a b marici-zero marici-zero
      (marici-unit-denominator-equivalent-numerators-equal
        a b equivalent)
      refl
```

## Boundary

Equivalent reduced representatives are unique when both denominators are one.
The general theorem requires the coprime cross-product argument showing that
each positive denominator divides the other before cancellation forces their
equality.
