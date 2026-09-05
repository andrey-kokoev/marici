# Division uniqueness excludes a greater state quotient

If the quotient stored by a division state strictly exceeds a pure divisibility
quotient, distributivity exposes the common smaller quotient prefix. Additive
prefix cancellation then makes a positive divisor-gap product plus the
remainder equal zero, contradicting successor disjointness.

```rzk
#lang rzk-1
```

```rzk
#define marici-division-greater-quotient-zero-sum
  ( divisor-predecessor value quotient witness-quotient remainder
      gap-predecessor : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} value)
  ( witness-equation : marici-mul witness-quotient
      (marici-succ divisor-predecessor)
    =_{MariciNat} value)
  ( quotient-gap : marici-add (marici-succ gap-predecessor) witness-quotient
    =_{MariciNat} quotient)
  : marici-add
      (marici-mul (marici-succ gap-predecessor)
        (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} marici-zero
  := marici-add-prefix-injective
      (marici-mul witness-quotient (marici-succ divisor-predecessor))
      (marici-add
        (marici-mul (marici-succ gap-predecessor)
          (marici-succ divisor-predecessor)) remainder)
      marici-zero
      (concat MariciNat
        (marici-add
          (marici-mul witness-quotient
            (marici-succ divisor-predecessor))
          (marici-add
            (marici-mul (marici-succ gap-predecessor)
              (marici-succ divisor-predecessor)) remainder))
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
        (marici-add
          (marici-mul witness-quotient
            (marici-succ divisor-predecessor)) marici-zero)
        (concat MariciNat
          (marici-add
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor))
            (marici-add
              (marici-mul (marici-succ gap-predecessor)
                (marici-succ divisor-predecessor)) remainder))
          (marici-add
            (marici-add
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor))
              (marici-mul (marici-succ gap-predecessor)
                (marici-succ divisor-predecessor))) remainder)
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
          (rev MariciNat
            (marici-add
              (marici-add
                (marici-mul witness-quotient
                  (marici-succ divisor-predecessor))
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor))) remainder)
            (marici-add
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor))
              (marici-add
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor)) remainder))
            (marici-add-assoc
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor))
              (marici-mul (marici-succ gap-predecessor)
                (marici-succ divisor-predecessor)) remainder))
          (ap MariciNat MariciNat
            (marici-add
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor))
              (marici-mul (marici-succ gap-predecessor)
                (marici-succ divisor-predecessor)))
            (marici-mul quotient (marici-succ divisor-predecessor))
            (\ prefix → marici-add prefix remainder)
            (concat MariciNat
              (marici-add
                (marici-mul witness-quotient
                  (marici-succ divisor-predecessor))
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor)))
              (marici-add
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor))
                (marici-mul witness-quotient
                  (marici-succ divisor-predecessor)))
              (marici-mul quotient (marici-succ divisor-predecessor))
              (marici-add-comm
                (marici-mul witness-quotient
                  (marici-succ divisor-predecessor))
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor)))
              (concat MariciNat
                (marici-add
                  (marici-mul (marici-succ gap-predecessor)
                    (marici-succ divisor-predecessor))
                  (marici-mul witness-quotient
                    (marici-succ divisor-predecessor)))
                (marici-mul
                  (marici-add (marici-succ gap-predecessor)
                    witness-quotient)
                  (marici-succ divisor-predecessor))
                (marici-mul quotient
                  (marici-succ divisor-predecessor))
                (rev MariciNat
                  (marici-mul
                    (marici-add (marici-succ gap-predecessor)
                      witness-quotient)
                    (marici-succ divisor-predecessor))
                  (marici-add
                    (marici-mul (marici-succ gap-predecessor)
                      (marici-succ divisor-predecessor))
                    (marici-mul witness-quotient
                      (marici-succ divisor-predecessor)))
                  (marici-mul-add-left-distrib
                    (marici-succ gap-predecessor) witness-quotient
                    (marici-succ divisor-predecessor)))
                (ap MariciNat MariciNat
                  (marici-add (marici-succ gap-predecessor)
                    witness-quotient) quotient
                  (\ coefficient → marici-mul coefficient
                    (marici-succ divisor-predecessor))
                  quotient-gap)))))
        (concat MariciNat
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
          value
          (marici-add
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor)) marici-zero)
          reconstruction
          (concat MariciNat
            value
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor))
            (marici-add
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor)) marici-zero)
            (rev MariciNat
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor))
              value witness-equation)
            (rev MariciNat
              (marici-add
                (marici-mul witness-quotient
                  (marici-succ divisor-predecessor)) marici-zero)
              (marici-mul witness-quotient
                (marici-succ divisor-predecessor))
              (marici-add-zero-right
                (marici-mul witness-quotient
                  (marici-succ divisor-predecessor)))))))

#define marici-division-greater-quotient-impossible
  ( divisor-predecessor value quotient witness-quotient remainder
      gap-predecessor : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} value)
  ( witness-equation : marici-mul witness-quotient
      (marici-succ divisor-predecessor)
    =_{MariciNat} value)
  ( quotient-gap : marici-add (marici-succ gap-predecessor) witness-quotient
    =_{MariciNat} quotient)
  : MariciEmpty
  := marici-positive-product-plus-not-zero
      gap-predecessor divisor-predecessor remainder
      (marici-division-greater-quotient-zero-sum
        divisor-predecessor value quotient witness-quotient remainder
        gap-predecessor reconstruction witness-equation quotient-gap)
```

## Boundary

Both strict quotient branches of division uniqueness are now impossible. The
next theorem can match explicit quotient trichotomy: equality yields zero
remainder, while either strict branch eliminates into the zero-remainder type.
