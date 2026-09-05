# Raw order descends to canonical rationals

A raw fraction is equivalent to the forgotten canonical rational obtained by
total normalization. Raw-order equivalence transport therefore sends every raw
order witness to an order witness between the corresponding rationals.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-equivalent-forget-rational-from-raw
  ( p : MariciRawFraction)
  : marici-raw-fraction-equivalent p
      (marici-rational-forget (marici-rational-from-raw p))
  := marici-raw-fraction-equivalent-trans
      p
      (marici-normalized-raw-representative p)
      (marici-rational-forget (marici-rational-from-raw p))
      (marici-normalized-raw-representative-preserves-equivalence p)
      (marici-raw-fraction-path-implies-equivalent
        (marici-normalized-raw-representative p)
        (marici-rational-forget (marici-rational-from-raw p))
        (rev MariciRawFraction
          (marici-rational-forget (marici-rational-from-raw p))
          (marici-normalized-raw-representative p)
          (marici-forget-normalize-to-reduced p)))

#define marici-raw-at-most-to-rational-at-most
  ( p q : MariciRawFraction)
  ( witness : MariciRawFractionAtMost p q)
  : MariciRationalAtMost
      (marici-rational-from-raw p)
      (marici-rational-from-raw q)
  := marici-raw-fraction-at-most-respects-equivalence
      p
      (marici-rational-forget (marici-rational-from-raw p))
      q
      (marici-rational-forget (marici-rational-from-raw q))
      (marici-raw-equivalent-forget-rational-from-raw p)
      (marici-raw-equivalent-forget-rational-from-raw q)
      witness
```

## Boundary

Raw inequalities now descend to canonical rational order without assuming that
normalization is judgmentally transparent. The rational triangle theorem still
requires paths identifying its nested subtraction, absolute-value, and addition
results with `rational-from-raw` applied to the raw triangle expressions.
