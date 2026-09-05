# First positive power preserves its predecessor

The predecessor encoding of a positive base raised to exponent one reduces to
the original base predecessor. The residual multiplication by zero and addition
of zero are discharged explicitly.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-power-predecessor-one
  ( k : MariciNat)
  : marici-positive-power-predecessor k marici-one
    =_{MariciNat} k
  := concat MariciNat
      (marici-positive-power-predecessor k marici-one)
      (marici-add k marici-zero)
      k
      (ap MariciNat MariciNat
        (marici-mul k marici-zero) marici-zero
        (\ residual → marici-add k residual)
        (marici-mul-zero-right k))
      (marici-add-zero-right k)
```

## Boundary

The reciprocal tolerance indexed by `k` now has a denominator predecessor equal
to `k` after explicit transport. Combining two tightened tolerances still
requires a raw-fraction addition equivalence using the doubled-denominator
identity.
