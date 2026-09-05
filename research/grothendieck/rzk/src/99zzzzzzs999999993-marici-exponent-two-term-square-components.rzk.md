# Exponent-two Dirichlet term has the square raw denominator

The positive-power-two predecessor path identifies the actual Dirichlet term at
index `n+1` with normalization of the unit fraction whose denominator is the
encoded square of `n+2`.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-square-reciprocal
  ( n : MariciNat)
  : MariciRawFraction
  := marici-raw-fraction marici-int-one
      (marici-positive-product-predecessor n n)

#define marici-exponent-two-term-square-input-path
  ( n : MariciNat)
  : marici-raw-fraction marici-int-one
      (marici-positive-power-predecessor n marici-two)
    =_{MariciRawFraction}
    marici-raw-square-reciprocal n
  := marici-raw-fraction-denominator-path
      marici-int-one
      (marici-positive-power-predecessor n marici-two)
      (marici-positive-product-predecessor n n)
      (marici-positive-power-predecessor-two n)

#define marici-exponent-two-dirichlet-term-square
  ( n : MariciNat)
  : marici-rational-dirichlet-term marici-two n
    =_{MariciRational}
    marici-rational-from-raw (marici-raw-square-reciprocal n)
  := ap MariciRawFraction MariciRational
      (marici-raw-fraction marici-int-one
        (marici-positive-power-predecessor n marici-two))
      (marici-raw-square-reciprocal n)
      marici-rational-from-raw
      (marici-exponent-two-term-square-input-path n)

#define marici-exponent-two-dirichlet-term-square-components
  ( n : MariciNat)
  : marici-rational-forget
      (marici-rational-dirichlet-term marici-two n)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw (marici-raw-square-reciprocal n))
  := ap MariciRational MariciRawFraction
      (marici-rational-dirichlet-term marici-two n)
      (marici-rational-from-raw (marici-raw-square-reciprocal n))
      marici-rational-forget
      (marici-exponent-two-dirichlet-term-square n)
```

## Boundary

The left endpoint of the pointwise telescoping majorant now matches the raw
square reciprocal. The right endpoint still requires flattening rational
subtraction of the two adjacent simplified reciprocal tolerances.
