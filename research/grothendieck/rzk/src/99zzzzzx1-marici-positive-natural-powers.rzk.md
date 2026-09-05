# Positive natural powers

A positive base raised to a natural exponent remains structurally positive.
The predecessor is computed recursively, avoiding an unproved use of truncated
predecessor on an arbitrary power.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-power-predecessor
  ( base-predecessor exponent : MariciNat)
  : MariciNat
  := match exponent
      ( marici-zero ⇒ marici-zero
      | marici-succ k ih ⇒
          marici-positive-product-predecessor base-predecessor ih)

#define marici-succ-positive-power-predecessor
  ( base-predecessor exponent : MariciNat)
  : marici-succ
      (marici-positive-power-predecessor base-predecessor exponent)
    =_{MariciNat}
    marici-nat-power (marici-succ base-predecessor) exponent
  := match exponent
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          concat MariciNat
            (marici-succ
              (marici-positive-product-predecessor base-predecessor
                (marici-positive-power-predecessor base-predecessor k)))
            (marici-mul
              (marici-succ base-predecessor)
              (marici-succ
                (marici-positive-power-predecessor base-predecessor k)))
            (marici-mul
              (marici-succ base-predecessor)
              (marici-nat-power (marici-succ base-predecessor) k))
            (marici-succ-positive-product base-predecessor
              (marici-positive-power-predecessor base-predecessor k))
            (ap MariciNat MariciNat
              (marici-succ
                (marici-positive-power-predecessor base-predecessor k))
              (marici-nat-power (marici-succ base-predecessor) k)
              (\ z → marici-mul (marici-succ base-predecessor) z)
              ih))
```

## Boundary

This proves the exact positivity witness needed for reciprocal-power
denominators. It does not assert growth, order monotonicity, or convergence of
Dirichlet sums.
