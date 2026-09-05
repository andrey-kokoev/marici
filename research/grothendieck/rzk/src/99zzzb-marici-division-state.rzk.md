# Bounded-remainder natural division state

Division by the positive natural represented by predecessor `d` is carried by a
quotient, a remainder bounded by `d`, and an exact reconstruction equation.
The zero-value state and the two successor-update arithmetic identities are
constructed explicitly.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatDivisionState
  ( divisor-predecessor value : MariciNat)
  := marici-nat-division-state
      ( quotient remainder : MariciNat)
      ( remainder-bounded : MariciNatAtMost remainder divisor-predecessor)
      ( reconstruction : marici-add
          (marici-mul quotient (marici-succ divisor-predecessor))
          remainder
        =_{MariciNat} value)

#define marici-zero-at-most
  ( d : MariciNat)
  : MariciNatAtMost marici-zero d
  := marici-nat-at-most-witness marici-zero d d
      (marici-add-zero-right d)

#define marici-nat-division-zero-state
  ( d : MariciNat)
  : MariciNatDivisionState d marici-zero
  := marici-nat-division-state d marici-zero
      marici-zero marici-zero
      (marici-zero-at-most d) refl

#define marici-division-increment-remainder-equation
  ( q d r value : MariciNat)
  ( reconstruction : marici-add
      (marici-mul q (marici-succ d)) r =_{MariciNat} value)
  : marici-add (marici-mul q (marici-succ d)) (marici-succ r)
      =_{MariciNat} marici-succ value
  := concat MariciNat
      (marici-add (marici-mul q (marici-succ d)) (marici-succ r))
      (marici-succ
        (marici-add (marici-mul q (marici-succ d)) r))
      (marici-succ value)
      (marici-add-succ-right (marici-mul q (marici-succ d)) r)
      (ap MariciNat MariciNat
        (marici-add (marici-mul q (marici-succ d)) r)
        value marici-succ reconstruction)

#define marici-division-carry-product-equation
  ( q d : MariciNat)
  : marici-add
      (marici-mul (marici-succ q) (marici-succ d)) marici-zero
      =_{MariciNat}
    marici-succ
      (marici-add (marici-mul q (marici-succ d)) d)
  := concat MariciNat
      (marici-add
        (marici-mul (marici-succ q) (marici-succ d)) marici-zero)
      (marici-mul (marici-succ q) (marici-succ d))
      (marici-succ
        (marici-add (marici-mul q (marici-succ d)) d))
      (marici-add-zero-right
        (marici-mul (marici-succ q) (marici-succ d)))
      (concat MariciNat
        (marici-mul (marici-succ q) (marici-succ d))
        (marici-add (marici-succ d)
          (marici-mul q (marici-succ d)))
        (marici-succ
          (marici-add (marici-mul q (marici-succ d)) d))
        refl
        (concat MariciNat
          (marici-add (marici-succ d)
            (marici-mul q (marici-succ d)))
          (marici-add (marici-mul q (marici-succ d))
            (marici-succ d))
          (marici-succ
            (marici-add (marici-mul q (marici-succ d)) d))
          (marici-add-comm
            (marici-succ d) (marici-mul q (marici-succ d)))
          (marici-add-succ-right
            (marici-mul q (marici-succ d)) d)))
```

## Boundary

The Euclidean-division invariant and its successor algebra are checked. The
next construction must inspect whether the bounded remainder is at the divisor
predecessor: increment it below the endpoint, or reset it to zero and increment
the quotient at the endpoint.
