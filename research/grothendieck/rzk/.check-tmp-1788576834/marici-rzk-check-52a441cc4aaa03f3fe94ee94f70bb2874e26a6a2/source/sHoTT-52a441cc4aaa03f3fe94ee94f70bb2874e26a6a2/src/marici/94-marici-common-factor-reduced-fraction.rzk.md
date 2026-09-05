# Extracting a reduced candidate from common-factor data

A common-factor certificate carries the two cofactors needed to form a raw
fraction. Extraction forgets the factorization equations only after using their
indexed certificate as the source of the cofactors.

```rzk
#lang rzk-1
```

```rzk
#define marici-common-factor-reduced-fraction
  ( a : MariciInt)
  ( d f : MariciNat)
  ( c : MariciRawComponentsCommonPositiveFactor a d f)
  : MariciRawFraction
  := match c
      ( marici-raw-components-common-positive-factor
          q r eq-num eq-den ⇒ marici-raw-fraction q r)

#define marici-unit-common-factor-reduces-trivially
  ( a : MariciInt)
  ( d : MariciNat)
  : marici-common-factor-reduced-fraction a d marici-zero
      (marici-raw-components-unit-common-positive-factor a d)
    =_{MariciRawFraction} marici-raw-fraction a d
  := refl
```

## Boundary

Every common-factor certificate now determines a raw-fraction candidate, and
unit-factor extraction computes to the original fraction. Proving the candidate
related to the original, selecting a nonunit factor when one exists, and
certifying coprimality remain open.
