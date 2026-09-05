# Conditional completed complex carrier

A complex value is an ordered pair in a real completion parameterized by one
set-quotient operation. A compatible quotient-class operation embeds rationals
on its real axis through constant Cauchy sequences recording zero imaginary
part.

```rzk
#lang rzk-1
```

```rzk
#data MariciComplex
  ( set-quotient : ( A : U) → (A → A → U) → U)
  := marici-complex
      ( real-part : MariciReal set-quotient)
      ( imaginary-part : MariciReal set-quotient)

#define marici-complex-real-part
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( z : MariciComplex set-quotient)
  : MariciReal set-quotient
  := match z
      ( marici-complex real-part imaginary-part ⇒ real-part)

#define marici-complex-imaginary-part
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( z : MariciComplex set-quotient)
  : MariciReal set-quotient
  := match z
      ( marici-complex real-part imaginary-part ⇒ imaginary-part)

#define marici-rational-to-complex
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  ( q : MariciRational)
  : MariciComplex set-quotient
  := marici-complex set-quotient
      (marici-rational-to-real set-quotient quotient-class q)
      (marici-rational-to-real set-quotient quotient-class
        marici-rational-zero)
```

## Boundary

The complex carrier and rational embedding now expose their quotient parameters.
They remain conditional on those supplied operations. Complex addition,
multiplication, exponentiation, convergence, and analytic structure remain
unconstructed.
