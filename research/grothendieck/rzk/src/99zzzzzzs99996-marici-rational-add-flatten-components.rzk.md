# Rational addition flattens nested normalization

Adding two rationals constructed from raw fractions has the same forgotten
canonical components as directly normalizing the raw sum. Addition congruence
transports the two source-to-normal-form equivalences through raw addition.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-add-from-raw-components
  ( p q : MariciRawFraction)
  : marici-rational-forget
      (marici-rational-add
        (marici-rational-from-raw p)
        (marici-rational-from-raw q))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw (marici-raw-fraction-add p q))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw p)
          (marici-rational-from-raw q)))
      (marici-normalized-raw-representative
        (marici-raw-fraction-add
          (marici-rational-forget (marici-rational-from-raw p))
          (marici-rational-forget (marici-rational-from-raw q))))
      (marici-rational-forget
        (marici-rational-from-raw (marici-raw-fraction-add p q)))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-add
          (marici-rational-forget (marici-rational-from-raw p))
          (marici-rational-forget (marici-rational-from-raw q))))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-add
            (marici-rational-forget (marici-rational-from-raw p))
            (marici-rational-forget (marici-rational-from-raw q))))
        (marici-normalized-raw-representative
          (marici-raw-fraction-add p q))
        (marici-rational-forget
          (marici-rational-from-raw (marici-raw-fraction-add p q)))
        (marici-normalized-raw-representatives-respect-equivalence
          (marici-raw-fraction-add
            (marici-rational-forget (marici-rational-from-raw p))
            (marici-rational-forget (marici-rational-from-raw q)))
          (marici-raw-fraction-add p q)
          (marici-raw-fraction-add-congruent
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
            (marici-rational-from-raw (marici-raw-fraction-add p q)))
          (marici-normalized-raw-representative
            (marici-raw-fraction-add p q))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-add p q))))
```

## Boundary

Rational addition now commutes with canonicalization at the forgotten-component
level. Combining this with the distance flattening paths makes the full rational
triangle endpoint comparison available.
