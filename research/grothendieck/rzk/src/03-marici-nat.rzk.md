# Marici natural-number substrate

This file begins the ordinary set-level arithmetic lane. It uses Rzk 0.11.3
recursive inductive types and introduces no simplicial semantics.

```rzk
#lang rzk-1

#data MariciNat
  := marici-zero
  | marici-succ (n : MariciNat)
```

Addition and multiplication recurse on their first argument.

```rzk
#define marici-add
  ( n m : MariciNat)
  : MariciNat
  := match n
      ( marici-zero ⇒ m
      | marici-succ k ih ⇒ marici-succ ih)

#define marici-mul
  ( n m : MariciNat)
  : MariciNat
  := match n
      ( marici-zero ⇒ marici-zero
      | marici-succ k ih ⇒ marici-add m ih)
```

The following equalities test the generated recursion and computation rules.

```rzk
#define marici-add-zero-left
  ( n : MariciNat)
  : marici-add marici-zero n =_{MariciNat} n
  := refl

#define marici-add-zero-right
  ( n : MariciNat)
  : marici-add n marici-zero =_{MariciNat} n
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          idJ
            ( MariciNat , marici-add k marici-zero
            , \ z q →
                marici-succ (marici-add k marici-zero)
                =_{MariciNat} marici-succ z
            , refl , k , ih))

#define marici-add-succ-right
  ( n m : MariciNat)
  : marici-add n (marici-succ m)
    =_{MariciNat} marici-succ (marici-add n m)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒
          ap MariciNat MariciNat
            (marici-add k (marici-succ m))
            (marici-succ (marici-add k m))
            marici-succ ih)

#define marici-add-comm
  ( n m : MariciNat)
  : marici-add n m =_{MariciNat} marici-add m n
  := match n
      ( marici-zero ⇒ rev MariciNat
          (marici-add m marici-zero) m
          (marici-add-zero-right m)
      | marici-succ k ih ⇒
          concat MariciNat
            (marici-succ (marici-add k m))
            (marici-succ (marici-add m k))
            (marici-add m (marici-succ k))
            (ap MariciNat MariciNat
              (marici-add k m) (marici-add m k) marici-succ ih)
            (rev MariciNat
              (marici-add m (marici-succ k))
              (marici-succ (marici-add m k))
              (marici-add-succ-right m k)))
```

Closed computations provide deliberate normalization tests.

```rzk
#define marici-one : MariciNat := marici-succ marici-zero
#define marici-two : MariciNat := marici-succ marici-one
#define marici-four : MariciNat := marici-succ (marici-succ marici-two)

#define marici-two-plus-two
  : marici-add marici-two marici-two =_{MariciNat} marici-four
  := refl

#define marici-two-times-two
  : marici-mul marici-two marici-two =_{MariciNat} marici-four
  := refl
```

## Boundary

This increment establishes constructors, induction-backed recursion, addition,
multiplication, additive zero laws, successor compatibility, commutativity, and
closed normalization tests. It does not yet prove that `MariciNat` is a set or
supply order and the remaining semiring laws.
