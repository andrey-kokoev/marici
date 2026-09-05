# Lifting the right Bézout orientation through division

Given `x=qy+r`, a residue certificate `vy+1=ur` lifts to
`(uq+v)y+1=ux`. This is the second coefficient update of the
subtraction-free extended Euclidean algorithm.

```rzk
#lang rzk-1
```

```rzk
#define marici-bezout-right-lifts-through-division
  ( x y quotient remainder u v : MariciNat)
  ( reconstruction : marici-add (marici-mul quotient y) remainder
    =_{MariciNat} x)
  ( residue-bezout : marici-add (marici-mul v y)
      (marici-succ marici-zero)
    =_{MariciNat} marici-mul u remainder)
  : marici-add
      (marici-mul (marici-add (marici-mul u quotient) v) y)
      (marici-succ marici-zero)
      =_{MariciNat} marici-mul u x
  := concat MariciNat
      (marici-add
        (marici-mul (marici-add (marici-mul u quotient) v) y)
        (marici-succ marici-zero))
      (marici-add
        (marici-mul (marici-mul u quotient) y)
        (marici-add (marici-mul v y) (marici-succ marici-zero)))
      (marici-mul u x)
      (concat MariciNat
        (marici-add
          (marici-mul (marici-add (marici-mul u quotient) v) y)
          (marici-succ marici-zero))
        (marici-add
          (marici-add
            (marici-mul (marici-mul u quotient) y)
            (marici-mul v y))
          (marici-succ marici-zero))
        (marici-add
          (marici-mul (marici-mul u quotient) y)
          (marici-add (marici-mul v y) (marici-succ marici-zero)))
        (ap MariciNat MariciNat
          (marici-mul (marici-add (marici-mul u quotient) v) y)
          (marici-add
            (marici-mul (marici-mul u quotient) y)
            (marici-mul v y))
          (\ value → marici-add value (marici-succ marici-zero))
          (marici-mul-add-left-distrib
            (marici-mul u quotient) v y))
        (marici-add-assoc
          (marici-mul (marici-mul u quotient) y)
          (marici-mul v y) (marici-succ marici-zero)))
      (concat MariciNat
        (marici-add
          (marici-mul (marici-mul u quotient) y)
          (marici-add (marici-mul v y) (marici-succ marici-zero)))
        (marici-add
          (marici-mul (marici-mul u quotient) y)
          (marici-mul u remainder))
        (marici-mul u x)
        (ap MariciNat MariciNat
          (marici-add (marici-mul v y) (marici-succ marici-zero))
          (marici-mul u remainder)
          (\ value → marici-add
            (marici-mul (marici-mul u quotient) y) value)
          residue-bezout)
        (concat MariciNat
          (marici-add
            (marici-mul (marici-mul u quotient) y)
            (marici-mul u remainder))
          (marici-mul u
            (marici-add (marici-mul quotient y) remainder))
          (marici-mul u x)
          (concat MariciNat
            (marici-add
              (marici-mul (marici-mul u quotient) y)
              (marici-mul u remainder))
            (marici-add
              (marici-mul u (marici-mul quotient y))
              (marici-mul u remainder))
            (marici-mul u
              (marici-add (marici-mul quotient y) remainder))
            (ap MariciNat MariciNat
              (marici-mul (marici-mul u quotient) y)
              (marici-mul u (marici-mul quotient y))
              (\ value → marici-add value (marici-mul u remainder))
              (marici-mul-assoc u quotient y))
            (rev MariciNat
              (marici-mul u
                (marici-add (marici-mul quotient y) remainder))
              (marici-add
                (marici-mul u (marici-mul quotient y))
                (marici-mul u remainder))
              (marici-mul-add-right-distrib
                u (marici-mul quotient y) remainder)))
          (ap MariciNat MariciNat
            (marici-add (marici-mul quotient y) remainder) x
            (\ value → marici-mul u value) reconstruction)))

#define marici-natural-bezout-lifts-through-division
  ( x y quotient remainder : MariciNat)
  ( reconstruction : marici-add (marici-mul quotient y) remainder
    =_{MariciNat} x)
  ( residue-bezout : MariciNatBezoutDifference remainder y)
  : MariciNatBezoutDifference x y
  := match residue-bezout
      ( marici-nat-bezout-left u v equation ⇒
          marici-nat-bezout-left x y u
            (marici-add v (marici-mul u quotient))
            (marici-bezout-left-lifts-through-division
              x y quotient remainder u v reconstruction equation)
      | marici-nat-bezout-right u v equation ⇒
          marici-nat-bezout-right x y u
            (marici-add (marici-mul u quotient) v)
            (marici-bezout-right-lifts-through-division
              x y quotient remainder u v reconstruction equation))
```

## Boundary

Both orientations of a residue Bézout difference now lift through
`x=qy+r`. The remaining construction is well-founded iteration of this update
along Euclidean division until the coprime base certificate is reached.
