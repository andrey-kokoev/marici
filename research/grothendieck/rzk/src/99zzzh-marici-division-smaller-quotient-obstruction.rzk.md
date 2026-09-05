# Division uniqueness excludes a smaller state quotient

If the quotient stored by a bounded-remainder state is strictly below the
quotient of a pure divisibility witness, distributivity and additive prefix
cancellation identify the remainder with a positive full-divisor multiple.
The bounded-remainder obstruction then eliminates the branch.

```rzk
#lang rzk-1
```

```rzk
#define marici-division-smaller-quotient-remainder-product
  ( divisor-predecessor value quotient witness-quotient remainder
      gap-predecessor : MariciNat)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} value)
  ( witness-equation : marici-mul witness-quotient
      (marici-succ divisor-predecessor)
    =_{MariciNat} value)
  ( quotient-gap : marici-add (marici-succ gap-predecessor) quotient
    =_{MariciNat} witness-quotient)
  : remainder =_{MariciNat}
      marici-mul (marici-succ gap-predecessor)
        (marici-succ divisor-predecessor)
  := marici-add-prefix-injective
      (marici-mul quotient (marici-succ divisor-predecessor))
      remainder
      (marici-mul (marici-succ gap-predecessor)
        (marici-succ divisor-predecessor))
      (concat MariciNat
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor)) remainder)
        value
        (marici-add
          (marici-mul quotient (marici-succ divisor-predecessor))
          (marici-mul (marici-succ gap-predecessor)
            (marici-succ divisor-predecessor)))
        reconstruction
        (concat MariciNat
          value
          (marici-mul witness-quotient
            (marici-succ divisor-predecessor))
          (marici-add
            (marici-mul quotient (marici-succ divisor-predecessor))
            (marici-mul (marici-succ gap-predecessor)
              (marici-succ divisor-predecessor)))
          (rev MariciNat
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor))
            value witness-equation)
          (concat MariciNat
            (marici-mul witness-quotient
              (marici-succ divisor-predecessor))
            (marici-mul
              (marici-add (marici-succ gap-predecessor) quotient)
              (marici-succ divisor-predecessor))
            (marici-add
              (marici-mul quotient (marici-succ divisor-predecessor))
              (marici-mul (marici-succ gap-predecessor)
                (marici-succ divisor-predecessor)))
            (ap MariciNat MariciNat witness-quotient
              (marici-add (marici-succ gap-predecessor) quotient)
              (\ coefficient → marici-mul coefficient
                (marici-succ divisor-predecessor))
              (rev MariciNat
                (marici-add (marici-succ gap-predecessor) quotient)
                witness-quotient quotient-gap))
            (concat MariciNat
              (marici-mul
                (marici-add (marici-succ gap-predecessor) quotient)
                (marici-succ divisor-predecessor))
              (marici-add
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor))
                (marici-mul quotient
                  (marici-succ divisor-predecessor)))
              (marici-add
                (marici-mul quotient (marici-succ divisor-predecessor))
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor)))
              (marici-mul-add-left-distrib
                (marici-succ gap-predecessor) quotient
                (marici-succ divisor-predecessor))
              (marici-add-comm
                (marici-mul (marici-succ gap-predecessor)
                  (marici-succ divisor-predecessor))
                (marici-mul quotient
                  (marici-succ divisor-predecessor)))))))

#define marici-division-smaller-quotient-impossible
  ( divisor-predecessor value quotient witness-quotient remainder
      gap-predecessor : MariciNat)
  ( remainder-bounded : MariciNatAtMost remainder divisor-predecessor)
  ( reconstruction : marici-add
      (marici-mul quotient (marici-succ divisor-predecessor)) remainder
    =_{MariciNat} value)
  ( witness-equation : marici-mul witness-quotient
      (marici-succ divisor-predecessor)
    =_{MariciNat} value)
  ( quotient-gap : marici-add (marici-succ gap-predecessor) quotient
    =_{MariciNat} witness-quotient)
  : MariciEmpty
  := marici-full-positive-divisor-not-bounded-remainder
      divisor-predecessor gap-predecessor remainder
      (rev MariciNat remainder
        (marici-mul (marici-succ gap-predecessor)
          (marici-succ divisor-predecessor))
        (marici-division-smaller-quotient-remainder-product
          divisor-predecessor value quotient witness-quotient remainder
          gap-predecessor reconstruction witness-equation quotient-gap))
      remainder-bounded
```

## Boundary

The branch where the division-state quotient is strictly smaller than a pure
multiple's quotient is impossible. The symmetric greater-quotient branch
remains; unlike this branch, it contradicts reconstruction directly because a
larger full-divisor prefix cannot equal a smaller prefix plus a remainder.
