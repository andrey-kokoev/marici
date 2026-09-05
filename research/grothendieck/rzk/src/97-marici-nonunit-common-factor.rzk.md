# Nonunit common positive factors

A nonunit common-factor witness requires the factor predecessor itself to be a
successor. Hence its represented positive factor has magnitude at least two by
construction, rather than by an external inequality proposition.

```rzk
#lang rzk-1
```

```rzk
#data MariciRawComponentsNonunitCommonPositiveFactor
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  := marici-raw-components-nonunit-common-positive-factor
      ( nonunit-predecessor : MariciNat)
      ( certificate : MariciRawComponentsCommonPositiveFactor
          numerator denominator-predecessor
          (marici-succ nonunit-predecessor))

#define marici-nonunit-common-factor-reduced-fraction
  ( a : MariciInt)
  ( d : MariciNat)
  ( c : MariciRawComponentsNonunitCommonPositiveFactor a d)
  : MariciRawFraction
  := match c
      ( marici-raw-components-nonunit-common-positive-factor f cert ⇒
          marici-common-factor-reduced-fraction a d (marici-succ f) cert)

#define marici-nonunit-common-factor-removal-preserves-equivalent
  ( a : MariciInt)
  ( d : MariciNat)
  ( c : MariciRawComponentsNonunitCommonPositiveFactor a d)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction a d)
      (marici-nonunit-common-factor-reduced-fraction a d c)
  := match c
      ( marici-raw-components-nonunit-common-positive-factor f cert ⇒
          marici-common-factor-removal-preserves-equivalent
            a d (marici-succ f) cert)
```

## Boundary

Nonunit common factors are now separated structurally from the always-present
unit witness, and their removal preserves equivalence. A decision procedure
selecting such a witness or certifying its absence, a decreasing measure for
iteration, and coprimality-based uniqueness remain open.
