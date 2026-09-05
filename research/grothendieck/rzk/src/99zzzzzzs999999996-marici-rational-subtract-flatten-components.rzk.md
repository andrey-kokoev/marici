# Rational subtraction flattens nested normalization

Subtracting two rationals constructed from raw fractions has the same forgotten
canonical components as directly normalizing their raw subtraction. Raw
subtraction congruence transports both source normalization equivalences.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-subtract-from-raw-components
  ( p q : MariciRawFraction)
  : marici-rational-forget
      (marici-rational-subtract
        (marici-rational-from-raw p)
        (marici-rational-from-raw q))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw (marici-raw-fraction-subtract p q))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-from-raw p)
          (marici-rational-from-raw q)))
      (marici-normalized-raw-representative
        (marici-raw-fraction-subtract
          (marici-rational-forget (marici-rational-from-raw p))
          (marici-rational-forget (marici-rational-from-raw q))))
      (marici-rational-forget
        (marici-rational-from-raw (marici-raw-fraction-subtract p q)))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-subtract
          (marici-rational-forget (marici-rational-from-raw p))
          (marici-rational-forget (marici-rational-from-raw q))))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-subtract
            (marici-rational-forget (marici-rational-from-raw p))
            (marici-rational-forget (marici-rational-from-raw q))))
        (marici-normalized-raw-representative
          (marici-raw-fraction-subtract p q))
        (marici-rational-forget
          (marici-rational-from-raw (marici-raw-fraction-subtract p q)))
        (marici-normalized-raw-representatives-respect-equivalence
          (marici-raw-fraction-subtract
            (marici-rational-forget (marici-rational-from-raw p))
            (marici-rational-forget (marici-rational-from-raw q)))
          (marici-raw-fraction-subtract p q)
          (marici-raw-fraction-subtract-congruent
            (marici-rational-forget (marici-rational-from-raw p)) p
            (marici-rational-forget (marici-rational-from-raw q)) q
            (marici-raw-fraction-equivalent-sym
              p (marici-rational-forget (marici-rational-from-raw p))
              (marici-raw-equivalent-forget-rational-from-raw p))
            (marici-raw-fraction-equivalent-sym
              q (marici-rational-forget (marici-rational-from-raw q))
              (marici-raw-equivalent-forget-rational-from-raw q))))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-from-raw (marici-raw-fraction-subtract p q)))
          (marici-normalized-raw-representative
            (marici-raw-fraction-subtract p q))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-subtract p q))))
```

## Boundary

Rational subtraction now commutes with canonicalization at the component level.
Together with simplified reciprocal paths and the adjacent raw subtraction
identity, this identifies the rational telescoping majorant endpoint.
