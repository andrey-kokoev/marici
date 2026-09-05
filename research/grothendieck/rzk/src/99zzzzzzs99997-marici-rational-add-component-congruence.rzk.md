# Rational addition respects component paths

Raw addition respects paths in each input. Applying canonical normalization and
its accessor path lifts those input paths to equality of the forgotten
components of rational sums.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-path-congruent
  ( p p-prime q q-prime : MariciRawFraction)
  ( left-path : p =_{MariciRawFraction} p-prime)
  ( right-path : q =_{MariciRawFraction} q-prime)
  : marici-raw-fraction-add p q
    =_{MariciRawFraction}
    marici-raw-fraction-add p-prime q-prime
  := concat MariciRawFraction
      (marici-raw-fraction-add p q)
      (marici-raw-fraction-add p-prime q)
      (marici-raw-fraction-add p-prime q-prime)
      (ap MariciRawFraction MariciRawFraction p p-prime
        (\ left → marici-raw-fraction-add left q) left-path)
      (ap MariciRawFraction MariciRawFraction q q-prime
        (\ right → marici-raw-fraction-add p-prime right) right-path)

#define marici-rational-add-component-congruent
  ( p p-prime q q-prime : MariciRational)
  ( left-path : marici-rational-forget p
      =_{MariciRawFraction} marici-rational-forget p-prime)
  ( right-path : marici-rational-forget q
      =_{MariciRawFraction} marici-rational-forget q-prime)
  : marici-rational-forget (marici-rational-add p q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-add p-prime q-prime)
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-add p q))
      (marici-normalized-raw-representative
        (marici-raw-fraction-add
          (marici-rational-forget p) (marici-rational-forget q)))
      (marici-rational-forget (marici-rational-add p-prime q-prime))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-add
          (marici-rational-forget p) (marici-rational-forget q)))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-add
            (marici-rational-forget p) (marici-rational-forget q)))
        (marici-normalized-raw-representative
          (marici-raw-fraction-add
            (marici-rational-forget p-prime)
            (marici-rational-forget q-prime)))
        (marici-rational-forget (marici-rational-add p-prime q-prime))
        (ap MariciRawFraction MariciRawFraction
          (marici-raw-fraction-add
            (marici-rational-forget p) (marici-rational-forget q))
          (marici-raw-fraction-add
            (marici-rational-forget p-prime)
            (marici-rational-forget q-prime))
          marici-normalized-raw-representative
          (marici-raw-fraction-add-path-congruent
            (marici-rational-forget p)
            (marici-rational-forget p-prime)
            (marici-rational-forget q)
            (marici-rational-forget q-prime)
            left-path right-path))
        (rev MariciRawFraction
          (marici-rational-forget (marici-rational-add p-prime q-prime))
          (marici-normalized-raw-representative
            (marici-raw-fraction-add
              (marici-rational-forget p-prime)
              (marici-rational-forget q-prime)))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-add
              (marici-rational-forget p-prime)
              (marici-rational-forget q-prime)))))
```

## Boundary

Component equality is now congruent under rational addition. Distance component
paths can therefore replace both normalized raw summands by the actual rational
distances in the final triangle endpoint.
