# Unit-denominator fractions are reduced

A nonunit common factor would have a successor factor predecessor bounded by
the zero denominator predecessor. The common-factor bound and zero-bound
uniqueness make that impossible.

```rzk
#lang rzk-1
```

```rzk
#define marici-at-most-successors-descend
  ( q n : MariciNat)
  ( bounded : MariciNatAtMost (marici-succ q) (marici-succ n))
  : MariciNatAtMost q n
  := match bounded
      ( marici-nat-at-most-witness gap equation ⇒
          marici-nat-at-most-witness q n gap
            (marici-succ-injective
              (marici-add gap q) n
              (concat MariciNat
                (marici-succ (marici-add gap q))
                (marici-add gap (marici-succ q))
                (marici-succ n)
                (rev MariciNat
                  (marici-add gap (marici-succ q))
                  (marici-succ (marici-add gap q))
                  (marici-add-succ-right gap q))
                equation)))

#define marici-unit-denominator-components-are-reduced
  ( a : MariciInt)
  : MariciRawComponentsAreReduced a marici-zero
  := \ nonunit → match nonunit
      ( marici-raw-components-nonunit-common-positive-factor f cert ⇒
          marici-succ-not-zero f
            (marici-at-most-zero-equal-zero (marici-succ f)
              (marici-common-positive-factor-at-most-denominator
                a marici-zero (marici-succ f) cert)))

#define marici-unit-denominator-reduced-fraction
  ( a : MariciInt)
  : MariciReducedRawFraction
  := marici-reduced-raw-fraction a marici-zero
      (marici-unit-denominator-components-are-reduced a)

#define marici-unit-denominator-normalization
  ( a : MariciInt)
  : MariciRawFractionNormalization (marici-raw-fraction a marici-zero)
  := marici-reduced-fraction-normalizes-itself
      (marici-unit-denominator-reduced-fraction a)
```

## Boundary

Every canonical integer over denominator one is now constructively reduced and
has a normalization witness. The successor-denominator selector remains to be
constructed by bounded search over nonunit factor predecessors.
