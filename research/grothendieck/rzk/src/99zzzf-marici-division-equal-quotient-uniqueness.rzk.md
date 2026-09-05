# Division uniqueness at equal quotients

When a bounded-remainder division state reconstructs the same value as a pure
multiple with the same quotient, additive prefix cancellation forces the
remainder to be zero. This closes the equal branch of quotient comparison in
the divisibility-to-zero-remainder theorem.

```rzk
#lang rzk-1
```

```rzk
#define marici-division-equal-quotient-remainder-zero
  ( divisor-predecessor value quotient witness-quotient remainder : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} value)
  ( witness-equation : marici-mul witness-quotient
      (marici-succ divisor-predecessor)
    =_{MariciNat} value)
  ( quotients-equal : quotient =_{MariciNat} witness-quotient)
  : remainder =_{MariciNat} marici-zero
  := marici-add-prefix-injective
      (marici-mul quotient (marici-succ divisor-predecessor))
      remainder marici-zero
      (concat MariciNat
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
        value
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor)) marici-zero)
        reconstruction
        (concat MariciNat
          value
          (marici-mul witness-quotient
            (marici-succ divisor-predecessor))
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor)) marici-zero)
          (rev MariciNat
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor))
            value witness-equation)
          (concat MariciNat
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor))
            (marici-mul quotient (marici-succ divisor-predecessor))
            (marici-add
              (marici-mul quotient (marici-succ divisor-predecessor))
              marici-zero)
            (ap MariciNat MariciNat witness-quotient quotient
              (\ quotient-prime → marici-mul quotient-prime
                (marici-succ divisor-predecessor))
              (rev MariciNat quotient witness-quotient quotients-equal))
            (rev MariciNat
              (marici-add
                (marici-mul quotient (marici-succ divisor-predecessor))
                marici-zero)
              (marici-mul quotient (marici-succ divisor-predecessor))
              (marici-add-zero-right
                (marici-mul quotient
                  (marici-succ divisor-predecessor)))))))
```

## Boundary

The equal-quotient division-uniqueness branch is complete. The two strict
quotient-gap branches must next be rewritten into a bounded remainder equal to
a positive full-divisor multiple, where the established order obstruction
eliminates them.
