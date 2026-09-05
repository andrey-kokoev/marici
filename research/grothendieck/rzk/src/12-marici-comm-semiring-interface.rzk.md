# Marici equational commutative-semiring interface

This file packages the equational laws independently of any carrier. Sethood is
kept separate: an inhabitant certifies the displayed operations and equations,
not uniqueness of identity proofs.

```rzk
#lang rzk-1

#data MariciCommSemiringLaws
  ( A : U)
  ( zero one : A)
  ( add mul : A → A → A)
  :=
    marici-make-comm-semiring-laws
      ( add-zero-left : (x : A) → add zero x =_{A} x)
      ( add-zero-right : (x : A) → add x zero =_{A} x)
      ( add-assoc : (x : A) → (y : A) → (z : A)
          → add (add x y) z =_{A} add x (add y z))
      ( add-comm : (x : A) → (y : A) → add x y =_{A} add y x)
      ( mul-zero-left : (x : A) → mul zero x =_{A} zero)
      ( mul-zero-right : (x : A) → mul x zero =_{A} zero)
      ( mul-one-left : (x : A) → mul one x =_{A} x)
      ( mul-one-right : (x : A) → mul x one =_{A} x)
      ( mul-assoc : (x : A) → (y : A) → (z : A)
          → mul (mul x y) z =_{A} mul x (mul y z))
      ( mul-comm : (x : A) → (y : A) → mul x y =_{A} mul y x)
      ( mul-add-left-distrib : (x : A) → (y : A) → (z : A)
          → mul (add x y) z =_{A} add (mul x z) (mul y z))
      ( mul-add-right-distrib : (x : A) → (y : A) → (z : A)
          → mul x (add y z) =_{A} add (mul x y) (mul x z))
```

The natural-number instance contains only previously checked theorems.

```rzk
#define marici-nat-comm-semiring-laws
  : MariciCommSemiringLaws
      MariciNat marici-zero marici-one marici-add marici-mul
  := marici-make-comm-semiring-laws
      MariciNat marici-zero marici-one marici-add marici-mul
      marici-add-zero-left
      marici-add-zero-right
      marici-add-assoc
      marici-add-comm
      marici-mul-zero-left
      marici-mul-zero-right
      marici-mul-one-left
      marici-mul-one-right
      marici-mul-assoc
      marici-mul-comm
      marici-mul-add-left-distrib
      marici-mul-add-right-distrib
```

Operation-preserving maps are packaged separately from carrier laws.

```rzk
#data MariciSemiringMapLaws
  ( A B : U)
  ( zero-A one-A : A)
  ( add-A mul-A : A → A → A)
  ( zero-B one-B : B)
  ( add-B mul-B : B → B → B)
  ( f : A → B)
  :=
    marici-make-semiring-map-laws
      ( preserves-zero : f zero-A =_{B} zero-B)
      ( preserves-one : f one-A =_{B} one-B)
      ( preserves-add : (x : A) → (y : A)
          → f (add-A x y) =_{B} add-B (f x) (f y))
      ( preserves-mul : (x : A) → (y : A)
          → f (mul-A x y) =_{B} mul-B (f x) (f y))

#define marici-nat-int-map-laws
  : MariciSemiringMapLaws
      MariciNat MariciInt
      marici-zero marici-one marici-add marici-mul
      marici-int-zero marici-int-one marici-int-add marici-int-mul
      marici-int-embed-nat
  := marici-make-semiring-map-laws
      MariciNat MariciInt
      marici-zero marici-one marici-add marici-mul
      marici-int-zero marici-int-one marici-int-add marici-int-mul
      marici-int-embed-nat
      marici-int-embed-zero
      marici-int-embed-one
      marici-int-embed-add
      marici-int-embed-mul
```

## Boundary

`marici-nat-comm-semiring-laws` packages all equational laws, and
`marici-nat-int-map-laws` packages operation preservation. Neither implies that
`MariciNat` or `MariciInt` is a set. The integer target is not yet packaged as a
commutative ring because its associativity and distributivity proofs remain
open.
