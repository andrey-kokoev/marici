# Lifting the left Bézout orientation through division

Given `x=qy+r`, a certificate `ur+1=vy` lifts to
`ux+1=(v+uq)y`. This is one constructor step of the subtraction-free extended
Euclidean algorithm.

```rzk
#lang rzk-1
```

```rzk
#define marici-bezout-left-lifts-through-division
  ( x y quotient remainder u v : MariciNat)
  ( reconstruction : marici-add (marici-mul quotient y) remainder
    =_{MariciNat} x)
  ( residue-bezout : marici-add (marici-mul u remainder)
      (marici-succ marici-zero)
    =_{MariciNat} marici-mul v y)
  : marici-add (marici-mul u x) (marici-succ marici-zero)
      =_{MariciNat}
    marici-mul (marici-add v (marici-mul u quotient)) y
  := concat MariciNat
      (marici-add (marici-mul u x) (marici-succ marici-zero))
      (marici-add
        (marici-mul u
          (marici-add (marici-mul quotient y) remainder))
        (marici-succ marici-zero))
      (marici-mul (marici-add v (marici-mul u quotient)) y)
      (ap MariciNat MariciNat x
        (marici-add (marici-mul quotient y) remainder)
        (\ value → marici-add (marici-mul u value)
          (marici-succ marici-zero))
        (rev MariciNat
          (marici-add (marici-mul quotient y) remainder)
          x reconstruction))
      (concat MariciNat
        (marici-add
          (marici-mul u
            (marici-add (marici-mul quotient y) remainder))
          (marici-succ marici-zero))
        (marici-add
          (marici-add
            (marici-mul (marici-mul u quotient) y)
            (marici-mul u remainder))
          (marici-succ marici-zero))
        (marici-mul (marici-add v (marici-mul u quotient)) y)
        (ap MariciNat MariciNat
          (marici-mul u
            (marici-add (marici-mul quotient y) remainder))
          (marici-add
            (marici-mul (marici-mul u quotient) y)
            (marici-mul u remainder))
          (\ value → marici-add value (marici-succ marici-zero))
          (concat MariciNat
            (marici-mul u
              (marici-add (marici-mul quotient y) remainder))
            (marici-add
              (marici-mul u (marici-mul quotient y))
              (marici-mul u remainder))
            (marici-add
              (marici-mul (marici-mul u quotient) y)
              (marici-mul u remainder))
            (marici-mul-add-right-distrib
              u (marici-mul quotient y) remainder)
            (ap MariciNat MariciNat
              (marici-mul u (marici-mul quotient y))
              (marici-mul (marici-mul u quotient) y)
              (\ value → marici-add value (marici-mul u remainder))
              (rev MariciNat
                (marici-mul (marici-mul u quotient) y)
                (marici-mul u (marici-mul quotient y))
                (marici-mul-assoc u quotient y)))))
        (concat MariciNat
          (marici-add
            (marici-add
              (marici-mul (marici-mul u quotient) y)
              (marici-mul u remainder))
            (marici-succ marici-zero))
          (marici-add
            (marici-mul (marici-mul u quotient) y)
            (marici-mul v y))
          (marici-mul (marici-add v (marici-mul u quotient)) y)
          (concat MariciNat
            (marici-add
              (marici-add
                (marici-mul (marici-mul u quotient) y)
                (marici-mul u remainder))
              (marici-succ marici-zero))
            (marici-add
              (marici-mul (marici-mul u quotient) y)
              (marici-add (marici-mul u remainder)
                (marici-succ marici-zero)))
            (marici-add
              (marici-mul (marici-mul u quotient) y)
              (marici-mul v y))
            (marici-add-assoc
              (marici-mul (marici-mul u quotient) y)
              (marici-mul u remainder) (marici-succ marici-zero))
            (ap MariciNat MariciNat
              (marici-add (marici-mul u remainder)
                (marici-succ marici-zero))
              (marici-mul v y)
              (\ value → marici-add
                (marici-mul (marici-mul u quotient) y) value)
              residue-bezout))
          (concat MariciNat
            (marici-add
              (marici-mul (marici-mul u quotient) y)
              (marici-mul v y))
            (marici-add
              (marici-mul v y)
              (marici-mul (marici-mul u quotient) y))
            (marici-mul (marici-add v (marici-mul u quotient)) y)
            (marici-add-comm
              (marici-mul (marici-mul u quotient) y)
              (marici-mul v y))
            (rev MariciNat
              (marici-mul (marici-add v (marici-mul u quotient)) y)
              (marici-add
                (marici-mul v y)
                (marici-mul (marici-mul u quotient) y))
              (marici-mul-add-left-distrib
                v (marici-mul u quotient) y)))))
```

## Boundary

The left-oriented residue certificate now lifts through one Euclidean division
step with explicit transformed coefficients. The symmetric residue orientation
must be lifted next; assembling both gives closure of
`MariciNatBezoutDifference` under `x=qy+r`.
