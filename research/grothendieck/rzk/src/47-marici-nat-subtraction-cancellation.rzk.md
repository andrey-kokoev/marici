# Natural subtraction cancellation laws

These laws provide the exact arithmetic needed when mixed-sign normalization
reaches a residual branch. Truncated subtraction cancels either summand from a
known additive decomposition, and cancels one multiplicative copy from a
successor factor.

```rzk
#lang rzk-1
```

```rzk
#define marici-sub-add-prefix
  ( n k : MariciNat)
  : marici-sub (marici-add n k) n =_{MariciNat} k
  := match n
      ( marici-zero ⇒ marici-sub-zero-right k
      | marici-succ j ih ⇒ ih)

#define marici-sub-add-suffix
  ( n k : MariciNat)
  : marici-sub (marici-add n k) k =_{MariciNat} n
  := concat MariciNat
      (marici-sub (marici-add n k) k)
      (marici-sub (marici-add k n) k)
      n
      (ap MariciNat MariciNat
        (marici-add n k) (marici-add k n)
        (\ z → marici-sub z k)
        (marici-add-comm n k))
      (marici-sub-add-prefix k n)
```

```rzk
#define marici-sub-mul-successor-right
  ( n k : MariciNat)
  : marici-sub (marici-mul n (marici-succ k)) n
    =_{MariciNat} marici-mul n k
  := concat MariciNat
      (marici-sub (marici-mul n (marici-succ k)) n)
      (marici-sub (marici-add n (marici-mul n k)) n)
      (marici-mul n k)
      (ap MariciNat MariciNat
        (marici-mul n (marici-succ k))
        (marici-add n (marici-mul n k))
        (\ z → marici-sub z n)
        (marici-mul-succ-right n k))
      (marici-sub-add-prefix n (marici-mul n k))
```

## Boundary

Cancellation is proved only when an additive decomposition is supplied by the
source expression. This is not arbitrary subtraction cancellation, order
reflection, or positive-factor multiplicative cancellation.
