# Composing one reduction step with recursive normalization

If a nonunit factor removes to a cofactor fraction and that cofactor fraction
already has a normalization witness, relation transitivity reuses its reduced
representative as a normalization of the original fraction.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalization-after-nonunit-removal
  ( a : MariciInt)
  ( d : MariciNat)
  ( c : MariciRawComponentsNonunitCommonPositiveFactor a d)
  ( recursive : MariciRawFractionNormalization
      (marici-nonunit-common-factor-reduced-fraction a d c))
  : MariciRawFractionNormalization (marici-raw-fraction a d)
  := match recursive
      ( marici-raw-fraction-normalization representative preserves ⇒
          marici-raw-fraction-normalization
            (marici-raw-fraction a d)
            representative
            (marici-raw-fraction-equivalent-trans
              (marici-raw-fraction a d)
              (marici-nonunit-common-factor-reduced-fraction a d c)
              (marici-reduced-raw-fraction-forget representative)
              (marici-nonunit-common-factor-removal-preserves-equivalent
                a d c)
              preserves))
```

```rzk
#define marici-normalization-from-reduction-decision
  ( a : MariciInt)
  ( d : MariciNat)
  ( decision : MariciRawComponentsReductionDecision a d)
  ( reducible-recursive :
    (factor : MariciRawComponentsNonunitCommonPositiveFactor a d)
    → MariciRawFractionNormalization
        (marici-nonunit-common-factor-reduced-fraction a d factor))
  : MariciRawFractionNormalization (marici-raw-fraction a d)
  := match decision
      ( marici-raw-components-reducible factor ⇒
          marici-normalization-after-nonunit-removal
            a d factor (reducible-recursive factor)
      | marici-raw-components-reduced proof ⇒
          marici-reduced-fraction-normalizes-itself
            (marici-reduced-raw-fraction a d proof))
```

## Boundary

The recursive normalization algebra is now checked: reduced branches stop and
nonunit branches compose one equivalence-preserving removal with the recursive
result. A total decision function and a well-founded recursion principle are
still required to instantiate this algebra for every raw fraction.
