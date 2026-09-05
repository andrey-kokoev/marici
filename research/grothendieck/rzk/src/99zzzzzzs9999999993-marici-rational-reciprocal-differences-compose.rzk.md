# Rational reciprocal differences compose

Each rational reciprocal difference is transported to normalization of its raw
directed-difference fraction. Generic normalized composition then cancels the
shared middle reciprocal at the component level.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-reciprocal-difference
  ( i j : MariciNat)
  : MariciRational
  := marici-rational-subtract
      (marici-rational-positive-reciprocal-power i marici-one)
      (marici-rational-positive-reciprocal-power j marici-one)

#define marici-rational-reciprocal-difference-raw-components
  ( i j : MariciNat)
  : marici-rational-forget
      (marici-rational-reciprocal-difference i j)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-difference-fraction
          marici-int-one i marici-int-one j))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-reciprocal-difference i j))
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-from-raw (marici-raw-reciprocal-tolerance i))
          (marici-rational-from-raw (marici-raw-reciprocal-tolerance j))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-difference-fraction
            marici-int-one i marici-int-one j)))
      (marici-rational-subtract-component-congruent
        (marici-rational-positive-reciprocal-power i marici-one)
        (marici-rational-from-raw (marici-raw-reciprocal-tolerance i))
        (marici-rational-positive-reciprocal-power j marici-one)
        (marici-rational-from-raw (marici-raw-reciprocal-tolerance j))
        (marici-rational-reciprocal-tolerance-simplified-components i)
        (marici-rational-reciprocal-tolerance-simplified-components j))
      (marici-rational-subtract-from-raw-components
        (marici-raw-reciprocal-tolerance i)
        (marici-raw-reciprocal-tolerance j))

#define marici-rational-reciprocal-differences-compose-components
  ( i j k : MariciNat)
  : marici-rational-forget
      (marici-rational-add
        (marici-rational-reciprocal-difference i j)
        (marici-rational-reciprocal-difference j k))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-reciprocal-difference i k)
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-reciprocal-difference i j)
          (marici-rational-reciprocal-difference j k)))
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw
            (marici-raw-difference-fraction
              marici-int-one i marici-int-one j))
          (marici-rational-from-raw
            (marici-raw-difference-fraction
              marici-int-one j marici-int-one k))))
      (marici-rational-forget
        (marici-rational-reciprocal-difference i k))
      (marici-rational-add-component-congruent
        (marici-rational-reciprocal-difference i j)
        (marici-rational-from-raw
          (marici-raw-difference-fraction
            marici-int-one i marici-int-one j))
        (marici-rational-reciprocal-difference j k)
        (marici-rational-from-raw
          (marici-raw-difference-fraction
            marici-int-one j marici-int-one k))
        (marici-rational-reciprocal-difference-raw-components i j)
        (marici-rational-reciprocal-difference-raw-components j k))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-add
            (marici-rational-from-raw
              (marici-raw-difference-fraction
                marici-int-one i marici-int-one j))
            (marici-rational-from-raw
              (marici-raw-difference-fraction
                marici-int-one j marici-int-one k))))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-difference-fraction
              marici-int-one i marici-int-one k)))
        (marici-rational-forget
          (marici-rational-reciprocal-difference i k))
        (marici-normalized-adjacent-differences-compose-components
          marici-int-one marici-int-one marici-int-one i j k)
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-reciprocal-difference i k))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-difference-fraction
                marici-int-one i marici-int-one k)))
          (marici-rational-reciprocal-difference-raw-components i k)))
```

## Boundary

Rational reciprocal differences now compose at canonical components. This is
the algebraic successor step needed to collapse finite adjacent-difference
sums; converting component equality into rational equality is unnecessary for
order transport.
