# Integer and natural embeddings into the rational carrier

Integers enter the reduced rational carrier through denominator one and total
normalization. Naturals use the checked integer embedding. Rational negation is
the existing normalize-after-raw operation.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-embed-int
  ( z : MariciInt)
  : MariciRational
  := marici-rational-from-raw
      (marici-raw-fraction z marici-zero)

#define marici-rational-embed-nat
  ( n : MariciNat)
  : MariciRational
  := marici-rational-embed-int
      (marici-int-embed-nat n)

#define marici-rational-negate
  ( q : MariciRational)
  : MariciRational
  := marici-reduced-normal-form-negate q

#define marici-rational-two
  : MariciRational
  := marici-rational-embed-nat marici-two

#define marici-rational-three
  : MariciRational
  := marici-rational-embed-nat marici-three
```

## Boundary

These are executable embeddings into canonical reduced components. Preservation
of addition and multiplication at the reduced-carrier identity level remains a
separate theorem; no field structure or analytic completion is asserted.
