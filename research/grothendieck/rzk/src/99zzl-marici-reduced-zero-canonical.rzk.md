# Reduced zero has denominator one

If a zero numerator had denominator at least two, the whole denominator would
be a structurally nonunit common positive factor: it divides zero with zero
cofactor and divides itself with unit cofactor. Reducedness rules this out.

```rzk
#lang rzk-1
```

```rzk
#define marici-reduced-zero-denominator-is-one
  ( d : MariciNat)
  ( reduced : MariciRawComponentsAreReduced marici-int-zero d)
  : d =_{MariciNat} marici-zero
  := (match d into
      (\ d-prime → MariciRawComponentsAreReduced marici-int-zero d-prime
        → d-prime =_{MariciNat} marici-zero)
      ( marici-zero ⇒ \ reduced-prime → refl
      | marici-succ n induction ⇒ \ reduced-prime →
          marici-empty-elim
            ((marici-succ n) =_{MariciNat} marici-zero)
            (reduced-prime
              (marici-raw-components-nonunit-common-positive-factor
                marici-int-zero (marici-succ n) n
                (marici-raw-components-common-positive-factor
                  marici-int-zero (marici-succ n) (marici-succ n)
                  marici-int-zero marici-zero
                  (marici-int-mul-zero-left
                    (marici-int-positive-denominator (marici-succ n)))
                  (marici-mul-one-left
                    (marici-succ (marici-succ n)))))))) reduced

#define marici-reduced-zero-raw-representative-canonical
  ( d : MariciNat)
  ( reduced : MariciRawComponentsAreReduced marici-int-zero d)
  : marici-raw-fraction marici-int-zero d =_{MariciRawFraction}
      marici-raw-fraction marici-int-zero marici-zero
  := marici-raw-fraction-component-path
      marici-int-zero marici-int-zero d marici-zero
      refl
      (marici-reduced-zero-denominator-is-one d reduced)
```

## Boundary

Zero now has a unique underlying reduced raw presentation without using the
general Euclid theorem. Consequently the reduced carrier's numerator-zero test
has the intended canonical representative in its zero branch. Nonzero reduced
uniqueness still requires the magnitude Euclid argument.
