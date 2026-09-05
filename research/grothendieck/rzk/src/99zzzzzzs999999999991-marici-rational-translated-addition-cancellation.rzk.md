# Rational translated addition cancels at canonical components

Normalization retraction replaces arbitrary rational inputs by normalization of
their forgotten raw components. The normalized cancellation theorem applies,
and retraction returns the surviving component to the original rational.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-to-normalized-forget-components
  ( p : MariciRational)
  : marici-rational-forget p
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw (marici-rational-forget p))
  := rev MariciRawFraction
      (marici-rational-forget
        (marici-rational-from-raw (marici-rational-forget p)))
      (marici-rational-forget p)
      (marici-rational-normalization-retraction-components p)

#define marici-rational-translated-addition-cancellation-components
  ( p q : MariciRational)
  : marici-rational-forget
      (marici-rational-subtract (marici-rational-add p q) p)
    =_{MariciRawFraction}
    marici-rational-forget q
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-subtract (marici-rational-add p q) p))
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-add
            (marici-rational-from-raw (marici-rational-forget p))
            (marici-rational-from-raw (marici-rational-forget q)))
          (marici-rational-from-raw (marici-rational-forget p))))
      (marici-rational-forget q)
      (marici-rational-subtract-component-congruent
        (marici-rational-add p q)
        (marici-rational-add
          (marici-rational-from-raw (marici-rational-forget p))
          (marici-rational-from-raw (marici-rational-forget q)))
        p (marici-rational-from-raw (marici-rational-forget p))
        (marici-rational-add-component-congruent
          p (marici-rational-from-raw (marici-rational-forget p))
          q (marici-rational-from-raw (marici-rational-forget q))
          (marici-rational-to-normalized-forget-components p)
          (marici-rational-to-normalized-forget-components q))
        (marici-rational-to-normalized-forget-components p))
      (concat MariciRawFraction
        (marici-rational-forget
          (marici-rational-subtract
            (marici-rational-add
              (marici-rational-from-raw (marici-rational-forget p))
              (marici-rational-from-raw (marici-rational-forget q)))
            (marici-rational-from-raw (marici-rational-forget p))))
        (marici-rational-forget
          (marici-rational-from-raw (marici-rational-forget q)))
        (marici-rational-forget q)
        (marici-normalized-translated-addition-cancellation-components
          (marici-rational-forget p) (marici-rational-forget q))
        (marici-rational-normalization-retraction-components q))
```

## Boundary

For arbitrary rationals, `(p + q) - p` now has exactly the canonical components
of `q`. Applying this to each shifted accumulator identifies the ordered
partial-sum difference with its independently folded tail.
