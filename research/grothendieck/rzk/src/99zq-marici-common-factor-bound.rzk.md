# Common positive factors are bounded by the denominator

The denominator equation also bounds the factor predecessor, not only its
cofactor. Multiplication commutativity swaps the two roles before applying the
positive-cofactor bound.

```rzk
#lang rzk-1
```

```rzk
#define marici-common-positive-factor-at-most-denominator
  ( a : MariciInt)
  ( d f : MariciNat)
  ( c : MariciRawComponentsCommonPositiveFactor a d f)
  : MariciNatAtMost f d
  := match c
      ( marici-raw-components-common-positive-factor q r eq-num eq-den ⇒
          marici-positive-cofactor-at-most-target f r d
            (concat MariciNat
              (marici-mul (marici-succ f) (marici-succ r))
              (marici-mul (marici-succ r) (marici-succ f))
              (marici-succ d)
              (marici-mul-comm (marici-succ f) (marici-succ r))
              eq-den))

#define marici-nonunit-common-factor-at-most-denominator
  ( a : MariciInt)
  ( d : MariciNat)
  ( c : MariciRawComponentsNonunitCommonPositiveFactor a d)
  : match c into (\ _ → U)
      ( marici-raw-components-nonunit-common-positive-factor f cert ⇒
          MariciNatAtMost (marici-succ f) d)
  := match c
      ( marici-raw-components-nonunit-common-positive-factor f cert ⇒
          marici-common-positive-factor-at-most-denominator
            a d (marici-succ f) cert)
```

## Boundary

Every nonunit factor predecessor lies within the denominator-predecessor bound.
This is the completeness bound for factor enumeration. A bounded common-factor
decision must still accumulate fixed-factor refutations and convert total
absence into reducedness.
