# Reduction decision interface

A constructive reduction decision must either exhibit a structurally nonunit
common factor or certify that no such factor exists. The two branches are kept
as data, so failure to find a factor cannot silently become reducedness.

```rzk
#lang rzk-1
```

```rzk
#data MariciRawComponentsReductionDecision
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  := marici-raw-components-reducible
      ( factor : MariciRawComponentsNonunitCommonPositiveFactor
          numerator denominator-predecessor)
  | marici-raw-components-reduced
      ( proof : MariciRawComponentsAreReduced
          numerator denominator-predecessor)

#define marici-reduction-decision-from-factor
  ( a : MariciInt)
  ( d : MariciNat)
  ( f : MariciRawComponentsNonunitCommonPositiveFactor a d)
  : MariciRawComponentsReductionDecision a d
  := marici-raw-components-reducible a d f

#define marici-reduction-decision-from-reduced
  ( a : MariciInt)
  ( d : MariciNat)
  ( r : MariciRawComponentsAreReduced a d)
  : MariciRawComponentsReductionDecision a d
  := marici-raw-components-reduced a d r

#define marici-reduction-decision-next-fraction
  ( a : MariciInt)
  ( d : MariciNat)
  ( decision : MariciRawComponentsReductionDecision a d)
  : MariciRawFraction
  := match decision
      ( marici-raw-components-reducible factor ⇒
          marici-nonunit-common-factor-reduced-fraction a d factor
      | marici-raw-components-reduced proof ⇒
          marici-raw-fraction a d)
```

## Boundary

The exact output contract for constructive factor selection is now checked. A
selector must return evidence in one of these branches. No selector is yet
constructed. The reducible branch also needs a denominator-decrease theorem
before recursive normalization is justified.
