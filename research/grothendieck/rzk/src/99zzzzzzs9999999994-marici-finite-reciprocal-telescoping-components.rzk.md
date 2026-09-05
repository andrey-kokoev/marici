# Finite adjacent reciprocal sums telescope

Induction maintains a component path from the finite sum to the outer
reciprocal difference. The zero case is self-subtraction; the successor case
transports the induction path through addition and applies adjacent-difference
composition.

```rzk
#lang rzk-1
```

```rzk
#define marici-reciprocal-difference-successor-term
  ( n : MariciNat)
  : MariciRational
  := marici-rational-reciprocal-difference n (marici-succ n)

#define marici-finite-reciprocal-telescoping-components
  ( bound : MariciNat)
  : marici-rational-forget
      (marici-rational-finite-sum bound
        marici-reciprocal-difference-successor-term)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-reciprocal-difference marici-zero bound)
  := match bound
      ( marici-zero ⇒
          rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-reciprocal-difference
                marici-zero marici-zero))
            (marici-rational-forget marici-rational-zero)
            (marici-rational-subtract-self-components
              (marici-rational-positive-reciprocal-power
                marici-zero marici-one))
      | marici-succ k induction ⇒
          concat MariciRawFraction
            (marici-rational-forget
              (marici-rational-finite-sum (marici-succ k)
                marici-reciprocal-difference-successor-term))
            (marici-rational-forget
              (marici-rational-add
                (marici-rational-reciprocal-difference marici-zero k)
                (marici-rational-reciprocal-difference k (marici-succ k))))
            (marici-rational-forget
              (marici-rational-reciprocal-difference
                marici-zero (marici-succ k)))
            (marici-rational-add-component-congruent
              (marici-rational-finite-sum k
                marici-reciprocal-difference-successor-term)
              (marici-rational-reciprocal-difference marici-zero k)
              (marici-rational-reciprocal-difference k (marici-succ k))
              (marici-rational-reciprocal-difference k (marici-succ k))
              induction refl)
            (marici-rational-reciprocal-differences-compose-components
              marici-zero k (marici-succ k)))
```

## Boundary

The finite telescoping identity is complete at canonical components. It can now
transport the finite-sum majorant endpoint to the outer reciprocal difference,
which is bounded by the initial reciprocal tolerance.
