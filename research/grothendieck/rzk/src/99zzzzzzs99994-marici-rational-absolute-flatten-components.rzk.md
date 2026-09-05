# Rational absolute value flattens nested normalization

Taking rational absolute value after constructing a rational from a raw
fraction has the same canonical raw components as normalizing the raw absolute
value directly. Preservation of raw equivalence by absolute value supplies the
comparison between the nested and direct normalization inputs.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-absolute-from-raw-components
  ( p : MariciRawFraction)
  : marici-rational-forget
      (marici-rational-absolute (marici-rational-from-raw p))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw (marici-raw-fraction-absolute p))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-absolute (marici-rational-from-raw p)))
      (marici-normalized-raw-representative
        (marici-raw-fraction-absolute
          (marici-rational-forget (marici-rational-from-raw p))))
      (marici-rational-forget
        (marici-rational-from-raw (marici-raw-fraction-absolute p)))
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-absolute
          (marici-rational-forget (marici-rational-from-raw p))))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-absolute
            (marici-rational-forget (marici-rational-from-raw p))))
        (marici-normalized-raw-representative
          (marici-raw-fraction-absolute p))
        (marici-rational-forget
          (marici-rational-from-raw (marici-raw-fraction-absolute p)))
        (marici-normalized-raw-representatives-respect-equivalence
          (marici-raw-fraction-absolute
            (marici-rational-forget (marici-rational-from-raw p)))
          (marici-raw-fraction-absolute p)
          (marici-raw-fraction-absolute-respects-equivalence
            (marici-rational-forget (marici-rational-from-raw p)) p
            (marici-raw-fraction-equivalent-sym
              p
              (marici-rational-forget (marici-rational-from-raw p))
              (marici-raw-equivalent-forget-rational-from-raw p))))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-from-raw (marici-raw-fraction-absolute p)))
          (marici-normalized-raw-representative
            (marici-raw-fraction-absolute p))
          (marici-rational-from-raw-forget-normalized
            (marici-raw-fraction-absolute p))))
```

## Boundary

Absolute value now commutes with canonicalization at the forgotten-component
level. Applying this to raw subtraction will identify rational distance with
the direct normalization of the raw absolute directed difference.
