# Rational adjacent reciprocal difference has the unit-product components

Component congruence replaces each reciprocal tolerance by its simplified raw
presentation. Flattening rational subtraction and the exact raw subtraction
path then identify the canonical components of the telescoping difference.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-adjacent-reciprocal-difference
  ( n : MariciNat)
  : MariciRational
  := marici-rational-subtract
      (marici-rational-positive-reciprocal-power n marici-one)
      (marici-rational-positive-reciprocal-power
        (marici-succ n) marici-one)

#define marici-rational-adjacent-reciprocal-difference-components
  ( n : MariciNat)
  : marici-rational-forget
      (marici-rational-adjacent-reciprocal-difference n)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-adjacent-reciprocal-difference n))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-adjacent-reciprocal-difference n))
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance n))
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance (marici-succ n)))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-adjacent-reciprocal-difference n)))
      (marici-rational-subtract-component-congruent
        (marici-rational-positive-reciprocal-power n marici-one)
        (marici-rational-from-raw (marici-raw-reciprocal-tolerance n))
        (marici-rational-positive-reciprocal-power
          (marici-succ n) marici-one)
        (marici-rational-from-raw
          (marici-raw-reciprocal-tolerance (marici-succ n)))
        (marici-rational-reciprocal-tolerance-simplified-components n)
        (marici-rational-reciprocal-tolerance-simplified-components
          (marici-succ n)))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-subtract
            (marici-rational-from-raw
              (marici-raw-reciprocal-tolerance n))
            (marici-rational-from-raw
              (marici-raw-reciprocal-tolerance (marici-succ n)))))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-subtract
              (marici-raw-reciprocal-tolerance n)
              (marici-raw-reciprocal-tolerance (marici-succ n)))))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-adjacent-reciprocal-difference n)))
        (marici-rational-subtract-from-raw-components
          (marici-raw-reciprocal-tolerance n)
          (marici-raw-reciprocal-tolerance (marici-succ n)))
        (ap MariciRawFraction MariciRawFraction
          (marici-raw-fraction-subtract
            (marici-raw-reciprocal-tolerance n)
            (marici-raw-reciprocal-tolerance (marici-succ n)))
          (marici-raw-adjacent-reciprocal-difference n)
          (\ raw → marici-rational-forget
            (marici-rational-from-raw raw))
          (marici-raw-adjacent-reciprocal-subtraction-path n)))
```

## Boundary

Both endpoints of the exponent-two pointwise majorant now have canonical
component paths to the raw fractions compared by the raw majorant theorem. A
single order-transport step yields the rational inequality.
