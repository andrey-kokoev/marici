# Marici simplicial pasting interface

This file defines the first Rzk projection of the Marici categorical shell. It
uses the directed simplices of simplicial HoTT. It does not import additive,
arithmetic, completion, or physical semantics.

```rzk
#lang rzk-1

#assume extext : ExtExt
```

A directed triangle consists of two composable edges together with the
canonical composite and its two-simplex witness. The witness is retained rather
than replacing composition by an untyped equality.

```rzk
#def marici-composite
  ( A : U)
  ( is-segal-A : is-segal A)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  : hom A x z
  := comp-is-segal A is-segal-A x y z f g

#def marici-triangle-witness
  ( A : U)
  ( is-segal-A : is-segal A)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  : hom2 A x y z f g
      (marici-composite A is-segal-A x y z f g)
  := witness-comp-is-segal A is-segal-A x y z f g
```

Three composable edges determine two parenthesized composites. Their equality
is derived from the Segal structure and the checked three-dimensional filling
argument in sHoTT.

```rzk
#def marici-left-associated
  ( A : U)
  ( is-segal-A : is-segal A)
  ( w x y z : A)
  ( f : hom A w x)
  ( g : hom A x y)
  ( h : hom A y z)
  : hom A w z
  := comp-is-segal A is-segal-A w y z
      (comp-is-segal A is-segal-A w x y f g) h

#def marici-right-associated
  ( A : U)
  ( is-segal-A : is-segal A)
  ( w x y z : A)
  ( f : hom A w x)
  ( g : hom A x y)
  ( h : hom A y z)
  : hom A w z
  := comp-is-segal A is-segal-A w x z f
      (comp-is-segal A is-segal-A x y z g h)

#def marici-associativity uses (extext)
  ( A : U)
  ( is-segal-A : is-segal A)
  ( w x y z : A)
  ( f : hom A w x)
  ( g : hom A x y)
  ( h : hom A y z)
  : (marici-left-associated A is-segal-A w x y z f g h)
  = (marici-right-associated A is-segal-A w x y z f g h)
  := associative-is-segal extext A is-segal-A w x y z f g h
```

For a Rezk type the Segal structure is extracted rather than separately
postulated. This is the entry point for the complete directed categorical
model.

```rzk
#def marici-composite-is-rezk
  ( A : U)
  ( is-rezk-A : is-rezk A)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  : hom A x z
  := marici-composite A (is-segal-is-rezk A is-rezk-A) x y z f g

#def marici-triangle-witness-is-rezk
  ( A : U)
  ( is-rezk-A : is-rezk A)
  ( x y z : A)
  ( f : hom A x y)
  ( g : hom A y z)
  : hom2 A x y z f g
      (marici-composite-is-rezk A is-rezk-A x y z f g)
  := marici-triangle-witness
      A (is-segal-is-rezk A is-rezk-A) x y z f g
```

## Boundary

This file establishes directed composition, its two-simplex filler, derived
associativity, and the Rezk entry point. It does not yet identify these arrows
with the additive boundary operators in the Cubical Agda
`GenericPastingComplex`; that comparison requires a separately typed
interpretation functor into an additive target.
