# Symmetry and unit bases for natural Bézout differences

Swapping the two naturals exchanges the two difference orientations and swaps
their coefficients. A unit in either coordinate has a canonical certificate
using coefficients zero and one. These are the transport and terminal cases
needed by bounded Euclidean recursion.

```rzk
#lang rzk-1
```

```rzk
#define marici-natural-bezout-difference-symmetric
  ( x y : MariciNat)
  ( bezout : MariciNatBezoutDifference x y)
  : MariciNatBezoutDifference y x
  := match bezout
      ( marici-nat-bezout-left u v equation ⇒
          marici-nat-bezout-right y x v u equation
      | marici-nat-bezout-right u v equation ⇒
          marici-nat-bezout-left y x v u equation)

#define marici-natural-bezout-unit-right
  ( x : MariciNat)
  : MariciNatBezoutDifference x (marici-succ marici-zero)
  := marici-nat-bezout-left x (marici-succ marici-zero)
      marici-zero (marici-succ marici-zero) refl

#define marici-natural-bezout-unit-left
  ( y : MariciNat)
  : MariciNatBezoutDifference (marici-succ marici-zero) y
  := marici-nat-bezout-right (marici-succ marici-zero) y
      (marici-succ marici-zero) marici-zero refl
```

## Boundary

Natural Bézout differences now transport across coordinate exchange and stop
at a unit second coordinate. In the nonunit Euclidean step, a zero remainder
is excluded by coprimality, a unit remainder uses this base, and a nonunit
remainder recursively obtains a certificate after swapping the coprime pair.
The bounded recursion itself remains to be assembled.
