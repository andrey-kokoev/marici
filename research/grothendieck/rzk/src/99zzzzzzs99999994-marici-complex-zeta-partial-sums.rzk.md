# Complex-valued finite zeta approximants

The conditional real and complex embeddings lift each executable rational
Dirichlet partial sum to the complex real axis. This provides a typed sequence
of finite approximants before any convergence claim.

```rzk
#lang rzk-1
```

```rzk
#define marici-real-zero
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  : MariciReal set-quotient
  := marici-rational-to-real set-quotient quotient-class
      marici-rational-zero

#define marici-real-one
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  : MariciReal set-quotient
  := marici-rational-to-real set-quotient quotient-class
      marici-rational-one

#define marici-complex-zero
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  : MariciComplex set-quotient
  := marici-complex set-quotient
      (marici-real-zero set-quotient quotient-class)
      (marici-real-zero set-quotient quotient-class)

#define marici-complex-one
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  : MariciComplex set-quotient
  := marici-complex set-quotient
      (marici-real-one set-quotient quotient-class)
      (marici-real-zero set-quotient quotient-class)

#define marici-zeta-complex-partial-sum
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  ( bound exponent : MariciNat)
  : MariciComplex set-quotient
  := marici-rational-to-complex set-quotient quotient-class
      (marici-zeta-dirichlet-partial-sum bound exponent)

#define marici-zeta-complex-partial-sum-zero
  ( set-quotient : ( A : U) → (A → A → U) → U)
  ( quotient-class : ( A : U)
    → ( relation : A → A → U)
    → A
    → set-quotient A relation)
  ( exponent : MariciNat)
  : marici-zeta-complex-partial-sum
      set-quotient quotient-class marici-zero exponent
    =_{MariciComplex set-quotient}
    marici-complex-zero set-quotient quotient-class
  := ap MariciRational (MariciComplex set-quotient)
      (marici-zeta-dirichlet-partial-sum marici-zero exponent)
      marici-rational-zero
      (marici-rational-to-complex set-quotient quotient-class)
      (marici-zeta-dirichlet-partial-sum-zero exponent)
```

## Boundary

This constructs complex-valued finite approximants only. It does not prove that
the partial-sum sequence is Cauchy for any exponent, define a complex limit, or
supply analytic continuation. Those require quantitative tail estimates and
completed complex arithmetic.
