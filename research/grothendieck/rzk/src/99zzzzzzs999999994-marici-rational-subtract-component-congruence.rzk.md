# Rational subtraction respects component paths

Raw subtraction respects equality in each input. Canonical normalization lifts
those input paths to equality of the forgotten components of rational
subtractions.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-subtract-path-congruent
  ( p p-prime q q-prime : MariciRawFraction)
  ( left-path : p =_{MariciRawFraction} p-prime)
  ( right-path : q =_{MariciRawFraction} q-prime)
  : marici-raw-fraction-subtract p q
    =_{MariciRawFraction}
    marici-raw-fraction-subtract p-prime q-prime
  := concat MariciRawFraction
      (marici-raw-fraction-subtract p q)
      (marici-raw-fraction-subtract p-prime q)
      (marici-raw-fraction-subtract p-prime q-prime)
      (ap MariciRawFraction MariciRawFraction p p-prime
        (\ left → marici-raw-fraction-subtract left q) left-path)
      (ap MariciRawFraction MariciRawFraction q q-prime
        (\ right → marici-raw-fraction-subtract p-prime right) right-path)

#define marici-rational-subtract-component-congruent
  ( p p-prime q q-prime : MariciRational)
  ( left-path : marici-rational-forget p
      =_{MariciRawFraction} marici-rational-forget p-prime)
  ( right-path : marici-rational-forget q
      =_{MariciRawFraction} marici-rational-forget q-prime)
  : marici-rational-forget (marici-rational-subtract p q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-subtract p-prime q-prime)
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-subtract p q))
      (marici-normalized-raw-representative
        (marici-raw-fraction-subtract
          (marici-rational-forget p) (marici-rational-forget q)))
      (marici-rational-forget
        (marici-rational-subtract p-prime q-prime))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-subtract
          (marici-rational-forget p) (marici-rational-forget q)))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-subtract
            (marici-rational-forget p) (marici-rational-forget q)))
        (marici-normalized-raw-representative
          (marici-raw-fraction-subtract
            (marici-rational-forget p-prime)
            (marici-rational-forget q-prime)))
        (marici-rational-forget
          (marici-rational-subtract p-prime q-prime))
        (ap MariciRawFraction MariciRawFraction
          (marici-raw-fraction-subtract
            (marici-rational-forget p) (marici-rational-forget q))
          (marici-raw-fraction-subtract
            (marici-rational-forget p-prime)
            (marici-rational-forget q-prime))
          marici-normalized-raw-representative
          (marici-raw-fraction-subtract-path-congruent
            (marici-rational-forget p)
            (marici-rational-forget p-prime)
            (marici-rational-forget q)
            (marici-rational-forget q-prime)
            left-path right-path))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-subtract p-prime q-prime))
          (marici-normalized-raw-representative
            (marici-raw-fraction-subtract
              (marici-rational-forget p-prime)
              (marici-rational-forget q-prime)))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-subtract
              (marici-rational-forget p-prime)
              (marici-rational-forget q-prime)))))
```

## Boundary

Rational subtraction is now congruent under component equality. Flattening
subtraction of two normalized raw inputs still requires preservation of raw
equivalence by subtraction.
