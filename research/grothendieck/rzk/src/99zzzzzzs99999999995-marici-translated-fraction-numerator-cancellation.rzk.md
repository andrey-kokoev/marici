# Translated-fraction numerator cancellation

Right distributivity exposes the two scaled summands in a translated fraction.
Multiplication associativity identifies the subtracted scaled numerator with
the first summand, and additive cancellation leaves the second summand.

```rzk
#lang rzk-1
```

```rzk
#define marici-translated-fraction-numerator-cancellation
  ( a b d e : MariciInt)
  : marici-int-add
      (marici-int-mul
        (marici-int-add
          (marici-int-mul a e)
          (marici-int-mul b d))
        d)
      (marici-int-negate
        (marici-int-mul a (marici-int-mul e d)))
    =_{MariciInt}
    marici-int-mul (marici-int-mul b d) d
  := concat MariciInt
      (marici-int-add
        (marici-int-mul
          (marici-int-add
            (marici-int-mul a e)
            (marici-int-mul b d)) d)
        (marici-int-negate
          (marici-int-mul a (marici-int-mul e d))))
      (marici-int-add
        (marici-int-add
          (marici-int-mul (marici-int-mul a e) d)
          (marici-int-mul (marici-int-mul b d) d))
        (marici-int-negate
          (marici-int-mul (marici-int-mul a e) d)))
      (marici-int-mul (marici-int-mul b d) d)
      (concat MariciInt
        (marici-int-add
          (marici-int-mul
            (marici-int-add
              (marici-int-mul a e)
              (marici-int-mul b d)) d)
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d))))
        (marici-int-add
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) d)
            (marici-int-mul (marici-int-mul b d) d))
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d))))
        (marici-int-add
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) d)
            (marici-int-mul (marici-int-mul b d) d))
          (marici-int-negate
            (marici-int-mul (marici-int-mul a e) d)))
        (marici-int-add-congruent
          (marici-int-mul
            (marici-int-add
              (marici-int-mul a e)
              (marici-int-mul b d)) d)
          (marici-int-add
            (marici-int-mul (marici-int-mul a e) d)
            (marici-int-mul (marici-int-mul b d) d))
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d)))
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d)))
          (marici-int-mul-add-right-distrib
            (marici-int-mul a e) (marici-int-mul b d) d)
          refl)
        (ap MariciInt MariciInt
          (marici-int-negate
            (marici-int-mul a (marici-int-mul e d)))
          (marici-int-negate
            (marici-int-mul (marici-int-mul a e) d))
          (\ negative → marici-int-add
            (marici-int-add
              (marici-int-mul (marici-int-mul a e) d)
              (marici-int-mul (marici-int-mul b d) d)) negative)
          (ap MariciInt MariciInt
            (marici-int-mul a (marici-int-mul e d))
            (marici-int-mul (marici-int-mul a e) d)
            marici-int-negate
            (rev MariciInt
              (marici-int-mul (marici-int-mul a e) d)
              (marici-int-mul a (marici-int-mul e d))
              (marici-int-mul-assoc a e d)))))
      (marici-int-add-then-subtract-left
        (marici-int-mul (marici-int-mul a e) d)
        (marici-int-mul (marici-int-mul b d) d))
```

## Boundary

The numerator cancellation for `((p + q) - p)` is now explicit. Completing the
raw-fraction equivalence requires the corresponding denominator-product
associativity paths and final cross-product reassociation.
