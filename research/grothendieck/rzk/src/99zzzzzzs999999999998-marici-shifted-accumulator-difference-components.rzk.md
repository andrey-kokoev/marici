# Shifted accumulator difference is the folded tail

The accumulator split transports subtraction to `(prefix + tail) - prefix`.
Translated-addition cancellation then removes the prefix and leaves the
independently folded shifted tail at canonical components.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-shifted-accumulator-difference-components
  ( prefix length : MariciNat)
  ( term : MariciNat → MariciRational)
  : marici-rational-forget
      (marici-rational-subtract
        (marici-rational-shifted-accumulate prefix length term)
        (marici-rational-finite-sum prefix term))
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-finite-sum length
        (marici-rational-shifted-tail-term prefix term))
  := concat MariciRawFraction
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-shifted-accumulate prefix length term)
          (marici-rational-finite-sum prefix term)))
      (marici-rational-forget
        (marici-rational-subtract
          (marici-rational-add
            (marici-rational-finite-sum prefix term)
            (marici-rational-finite-sum length
              (marici-rational-shifted-tail-term prefix term)))
          (marici-rational-finite-sum prefix term)))
      (marici-rational-forget
        (marici-rational-finite-sum length
          (marici-rational-shifted-tail-term prefix term)))
      (marici-rational-subtract-component-congruent
        (marici-rational-shifted-accumulate prefix length term)
        (marici-rational-add
          (marici-rational-finite-sum prefix term)
          (marici-rational-finite-sum length
            (marici-rational-shifted-tail-term prefix term)))
        (marici-rational-finite-sum prefix term)
        (marici-rational-finite-sum prefix term)
        (marici-rational-shifted-accumulate-split-components
          prefix length term)
        refl)
      (marici-rational-translated-addition-cancellation-components
        (marici-rational-finite-sum prefix term)
        (marici-rational-finite-sum length
          (marici-rational-shifted-tail-term prefix term)))
```

## Boundary

The difference between a shifted accumulator and its prefix now has exactly the
folded-tail components. Transporting the longer initial sum through the shifted-
accumulation equality gives the corresponding ordered partial-sum difference.
For the exponent-two bound, the prefix is the successor of the tolerance
cutoff; aligning `index + succ cutoff` with `succ (index + cutoff)` remains an
explicit natural-addition path.
