# Normalization from a certified common factor and reduced cofactors

Exact common-factor equations construct the factor certificate. If the
resulting cofactors are independently certified reduced, relation-preserving
factor removal packages them as a normalization witness for the original raw
fraction.

```rzk
#lang rzk-1
```

```rzk
#define marici-certified-factor-normalization
  ( a q : MariciInt)
  ( d f r : MariciNat)
  ( numerator-equation : marici-int-mul q
      (marici-int-positive-denominator f)
    =_{MariciInt} a)
  ( denominator-equation : marici-mul
      (marici-succ r) (marici-succ f)
    =_{MariciNat} marici-succ d)
  ( reduced : MariciRawComponentsAreReduced q r)
  : MariciRawFractionNormalization (marici-raw-fraction a d)
  := marici-raw-fraction-normalization
      (marici-raw-fraction a d)
      (marici-reduced-raw-fraction q r reduced)
      (marici-common-factor-removal-preserves-equivalent
        a d f
        (marici-raw-components-common-positive-factor
          a d f q r numerator-equation denominator-equation))
```

## Boundary

The checked normalization pipeline is complete once a common factor, both
cofactors, their exact equations, and reducedness of those cofactors are
supplied. The theorem does not select those data. Universal normalization still
requires constructive selection and termination; representative uniqueness
still requires a coprime cross-product theorem.
