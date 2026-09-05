# Rational absolute value respects component equality

Absolute value is factored through an explicit raw-fraction operation. Equality
of canonical raw components therefore transports through absolute value without
requiring equality of reducedness proofs.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-absolute-respects-component-equality
  ( q r : MariciRational)
  ( components : marici-rational-forget q
      =_{MariciRawFraction} marici-rational-forget r)
  : marici-rational-forget (marici-rational-absolute q)
    =_{MariciRawFraction}
    marici-rational-forget (marici-rational-absolute r)
  := ap MariciRawFraction MariciRawFraction
      (marici-rational-forget q)
      (marici-rational-forget r)
      (\ p → marici-rational-forget
        (marici-rational-from-raw
          (marici-raw-fraction-absolute p)))
      components
```

## Boundary

This is congruence for canonical components. It does not identify packaged
reducedness witnesses or prove the triangle inequality.
