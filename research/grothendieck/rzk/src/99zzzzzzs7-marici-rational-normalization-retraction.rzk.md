# Normalization retracts canonical rationals

Re-normalizing the forgotten raw presentation of a reduced rational preserves
its canonical numerator and denominator.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-normalization-retraction-components
  ( q : MariciRational)
  : marici-rational-forget
      (marici-rational-from-raw (marici-rational-forget q))
    =_{MariciRawFraction}
    marici-rational-forget q
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-from-raw (marici-rational-forget q)))
      (marici-normalized-raw-representative
        (marici-rational-forget q))
      (marici-rational-forget q)
      (marici-rational-from-raw-forget-normalized
        (marici-rational-forget q))
      (marici-normalized-representative-canonical
        (marici-rational-forget q) q
        (marici-raw-fraction-equivalent-refl
          (marici-rational-forget q)))
```

## Boundary

This is a retraction on canonical raw components. It does not identify the
reducedness proof fields of the packaged rationals.
