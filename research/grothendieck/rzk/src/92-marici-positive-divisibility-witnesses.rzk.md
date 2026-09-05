# Positive divisibility witnesses

Normalization needs typed evidence that one positive factor occurs in both an
integer numerator and a positive denominator. These indexed witness types keep
the cofactors and exact multiplication equations rather than treating
numerical divisibility as an untyped proposition.

```rzk
#lang rzk-1
```

```rzk
#data MariciIntRightPositiveDivides
  ( factor-predecessor : MariciNat)
  ( value : MariciInt)
  := marici-int-right-positive-divides-witness
      ( cofactor : MariciInt)
      ( equation : marici-int-mul cofactor
          (marici-int-positive-denominator factor-predecessor)
        =_{MariciInt} value)

#data MariciPositiveNatRightDivides
  ( factor-predecessor value-predecessor : MariciNat)
  := marici-positive-nat-right-divides-witness
      ( cofactor-predecessor : MariciNat)
      ( equation : marici-mul
          (marici-succ cofactor-predecessor)
          (marici-succ factor-predecessor)
        =_{MariciNat} marici-succ value-predecessor)
```

The structurally positive unit factor divides every integer and every positive
natural.

```rzk
#define marici-int-positive-unit-right-divides
  ( z : MariciInt)
  : MariciIntRightPositiveDivides marici-zero z
  := marici-int-right-positive-divides-witness marici-zero z z
      (marici-int-mul-one-right z)

#define marici-positive-nat-unit-right-divides
  ( n : MariciNat)
  : MariciPositiveNatRightDivides marici-zero n
  := marici-positive-nat-right-divides-witness marici-zero n n
      (marici-mul-one-right (marici-succ n))
```

## Boundary

The two divisibility axes and their always-available unit witnesses are now
checked. A common-factor certificate must next pair these witnesses for the
numerator and denominator of one raw fraction; selection of a nonunit factor,
coprimality, and normalization remain open.
