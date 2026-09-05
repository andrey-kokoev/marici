# Normalized adjacent raw differences compose

Raw adjacent-difference equivalence descends through rational normalization.
Thus addition of the two normalized adjacent differences has the same canonical
components as normalization of the outer difference.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-adjacent-differences-compose-components
  ( a b c : MariciInt)
  ( d e f : MariciNat)
  : marici-rational-forget
      (marici-rational-add
        (marici-rational-from-raw
          (marici-raw-difference-fraction a d b e))
        (marici-rational-from-raw
          (marici-raw-difference-fraction b e c f)))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw
        (marici-raw-difference-fraction a d c f))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-add
          (marici-rational-from-raw
            (marici-raw-difference-fraction a d b e))
          (marici-rational-from-raw
            (marici-raw-difference-fraction b e c f))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-add
            (marici-raw-difference-fraction a d b e)
            (marici-raw-difference-fraction b e c f))))
      (marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-difference-fraction a d c f)))
      (marici-rational-add-from-raw-components
        (marici-raw-difference-fraction a d b e)
        (marici-raw-difference-fraction b e c f))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-fraction-add
              (marici-raw-difference-fraction a d b e)
              (marici-raw-difference-fraction b e c f))))
        (marici-normalized-raw-representative
          (marici-raw-fraction-add
            (marici-raw-difference-fraction a d b e)
            (marici-raw-difference-fraction b e c f)))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-difference-fraction a d c f)))
        (marici-rational-from-raw-forget-normalized
          (marici-raw-fraction-add
            (marici-raw-difference-fraction a d b e)
            (marici-raw-difference-fraction b e c f)))
        (concat MariciRawFraction
          (marici-normalized-raw-representative
            (marici-raw-fraction-add
              (marici-raw-difference-fraction a d b e)
              (marici-raw-difference-fraction b e c f)))
          (marici-normalized-raw-representative
            (marici-raw-difference-fraction a d c f))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-difference-fraction a d c f)))
          (marici-normalized-raw-representatives-respect-equivalence
            (marici-raw-fraction-add
              (marici-raw-difference-fraction a d b e)
              (marici-raw-difference-fraction b e c f))
            (marici-raw-difference-fraction a d c f)
            (marici-raw-adjacent-differences-compose a b c d e f))
          (rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw
                (marici-raw-difference-fraction a d c f)))
            (marici-normalized-raw-representative
              (marici-raw-difference-fraction a d c f))
            (marici-rational-from-raw-forget-normalized
              (marici-raw-difference-fraction a d c f)))))
```

## Boundary

The normalized successor algebra for telescoping is now proved generically.
Transporting simplified reciprocal-tolerance components into this identity
provides the rational adjacent-difference composition step.
