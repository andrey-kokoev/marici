# Absolute-value triangle at a common denominator

The integer triangle inequality scales by the shared positive denominator,
producing the raw-fraction order inequality for two numerators represented over
one denominator.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-common-denominator-absolute-triangle
  ( x y : MariciInt)
  ( denominator-predecessor : MariciNat)
  : MariciRawFractionAtMost
      (marici-raw-fraction-absolute
        (marici-raw-fraction
          (marici-int-add x y) denominator-predecessor))
      (marici-raw-fraction
        (marici-int-add
          (marici-int-absolute x) (marici-int-absolute y))
        denominator-predecessor)
  := marici-int-at-most-mul-nonnegative-right
      (marici-int-absolute (marici-int-add x y))
      (marici-int-add (marici-int-absolute x) (marici-int-absolute y))
      (marici-int-positive-denominator denominator-predecessor)
      (marici-int-absolute-triangle x y)
      marici-trivial
```

## Boundary

The triangle inequality is proved for raw fractions already expressed over a
shared denominator. The general rational triangle requires explicit common-
denominator presentations for the three directed differences and equivalence
transport into their normalized forms.
