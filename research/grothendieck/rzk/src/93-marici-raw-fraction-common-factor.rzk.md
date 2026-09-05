# Raw-fraction common positive factors

A common-factor certificate pairs an integer numerator cofactor with a
structurally positive denominator cofactor. Both exact right-factor equations
share one positive factor, so the object records the compatibility needed for
factor removal rather than two unrelated divisibility claims.

```rzk
#lang rzk-1
```

```rzk
#data MariciRawComponentsCommonPositiveFactor
  ( numerator : MariciInt)
  ( denominator-predecessor factor-predecessor : MariciNat)
  := marici-raw-components-common-positive-factor
      ( numerator-cofactor : MariciInt)
      ( denominator-cofactor-predecessor : MariciNat)
      ( numerator-equation : marici-int-mul numerator-cofactor
          (marici-int-positive-denominator factor-predecessor)
        =_{MariciInt} numerator)
      ( denominator-equation : marici-mul
          (marici-succ denominator-cofactor-predecessor)
          (marici-succ factor-predecessor)
        =_{MariciNat} marici-succ denominator-predecessor)
```

Every pair of raw-fraction components has the unit common positive factor.

```rzk
#define marici-raw-components-unit-common-positive-factor
  ( a : MariciInt)
  ( d : MariciNat)
  : MariciRawComponentsCommonPositiveFactor a d marici-zero
  := marici-raw-components-common-positive-factor
      a d marici-zero a d
      (marici-int-mul-one-right a)
      (marici-mul-one-right (marici-succ d))
```

## Boundary

Common-factor data now shares one factor across numerator and denominator and
retains both cofactors. Extracting the reduced raw fraction, proving it related
to the original using scaling reflection, selecting nonunit factors, and
certifying coprimality remain open.
