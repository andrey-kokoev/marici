# Normalized raw-fraction operations

Raw negation, addition, and multiplication can now be followed by total
normalization. Each operation computes a reduced representative and retains a
normalization witness for the corresponding raw operation.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-negation-witness
  ( p : MariciRawFraction)
  : MariciRawFractionNormalization
      (marici-raw-fraction-negate p)
  := marici-normalize-raw-fraction
      (marici-raw-fraction-negate p)

#define marici-normalized-addition-witness
  ( p q : MariciRawFraction)
  : MariciRawFractionNormalization
      (marici-raw-fraction-add p q)
  := marici-normalize-raw-fraction
      (marici-raw-fraction-add p q)

#define marici-normalized-multiplication-witness
  ( p q : MariciRawFraction)
  : MariciRawFractionNormalization
      (marici-raw-fraction-mul p q)
  := marici-normalize-raw-fraction
      (marici-raw-fraction-mul p q)

#define marici-normal-form-negate
  ( p : MariciRawFraction)
  : MariciRawFraction
  := marici-normalization-forget-representative
      (marici-raw-fraction-negate p)
      (marici-normalized-negation-witness p)

#define marici-normal-form-add
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := marici-normalization-forget-representative
      (marici-raw-fraction-add p q)
      (marici-normalized-addition-witness p q)

#define marici-normal-form-mul
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := marici-normalization-forget-representative
      (marici-raw-fraction-mul p q)
      (marici-normalized-multiplication-witness p q)
```

The constants are normalized from their canonical denominator-one raw forms.

```rzk
#define marici-normal-form-zero
  : MariciRawFraction
  := marici-normalized-raw-representative
      (marici-raw-fraction marici-int-zero marici-zero)

#define marici-normal-form-one
  : MariciRawFraction
  := marici-normalized-raw-representative
      (marici-raw-fraction marici-int-one marici-zero)
```

## Boundary

Negation, addition, multiplication, zero, and one now have executable normalized
representatives. These functions operate on raw presentations; proving that
they descend to presentation-independent canonical operations requires
normalization canonicality. Inversion additionally requires a typed nonzero
input and sign-aware numerator/denominator exchange.
