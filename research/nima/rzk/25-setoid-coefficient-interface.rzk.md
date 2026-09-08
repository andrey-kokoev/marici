# Setoid-native coefficient and chain-map interface

This module does not identify evaluation equality with Rzk identity.  It packages
maps together with the exact congruence required by the coefficient
presentations, and instantiates the loaded differentials and endpoint quotient.

```rzk
#lang rzk-1

#define NimaSetoidMorphism
  (A B : U) (eqA : A -> A -> U) (eqB : B -> B -> U) : U
  := Sigma (f : A -> B), (x y : A) -> eqA x y -> eqB (f x) (f y)

#define nima-setoid-identity
  (A : U) (eqA : A -> A -> U) : NimaSetoidMorphism A A eqA eqA
  := (\ x -> x, \ x y p -> p)

#define nima-setoid-compose
  (A B C : U) (eqA : A -> A -> U) (eqB : B -> B -> U) (eqC : C -> C -> U)
  (g : NimaSetoidMorphism B C eqB eqC)
  (f : NimaSetoidMorphism A B eqA eqB)
  : NimaSetoidMorphism A C eqA eqC
  := (\ x -> first g (first f x),
      \ x y p -> second g (first f x) (first f y) (second f x y p))

#define nima-setoid-morphism-equal
  (A B : U) (eqB : B -> B -> U)
  (f g : A -> B) : U
  := (x : A) -> eqB (f x) (g x)

#define nima-zsum-setoid-morphism
  (A B : U) (column : A -> NimaZSum B)
  : NimaSetoidMorphism (NimaZSum A) (NimaZSum B) (nima-sum-equal A) (nima-sum-equal B)
  := (nima-sum-bind A B column,
      \ p q equal -> nima-sum-bind-cong A B column p q equal)

#define nima-finite-loaded-d-setoid
  : NimaSetoidMorphism NimaFiniteLoadedCoefficients NimaFiniteLoadedCoefficients
      (nima-sum-equal NimaFiniteLoadedBasis) (nima-sum-equal NimaFiniteLoadedBasis)
  := nima-zsum-setoid-morphism NimaFiniteLoadedBasis NimaFiniteLoadedBasis nima-finite-loaded-column

#define nima-cech-loaded-d-setoid
  : NimaSetoidMorphism NimaCechLoadedCoefficients NimaCechLoadedCoefficients
      (nima-sum-equal NimaCechLoadedBasis) (nima-sum-equal NimaCechLoadedBasis)
  := nima-zsum-setoid-morphism NimaCechLoadedBasis NimaCechLoadedBasis nima-cech-loaded-column

#define nima-relative-cech-d-setoid
  : NimaSetoidMorphism NimaRelativeCechCoefficients NimaRelativeCechCoefficients
      (nima-sum-equal NimaRelativeCechBasis) (nima-sum-equal NimaRelativeCechBasis)
  := nima-zsum-setoid-morphism NimaRelativeCechBasis NimaRelativeCechBasis nima-relative-cech-column

#define nima-finite-cech-comparison-setoid
  : NimaSetoidMorphism NimaFiniteLoadedCoefficients NimaCechLoadedCoefficients
      (nima-sum-equal NimaFiniteLoadedBasis) (nima-sum-equal NimaCechLoadedBasis)
  := nima-zsum-setoid-morphism NimaFiniteLoadedBasis NimaCechLoadedBasis
       (\ a -> nima-sum-atom NimaCechLoadedBasis (nima-finite-cech-monomial a))

#define nima-cech-relative-projection-setoid
  : NimaSetoidMorphism NimaCechLoadedCoefficients NimaRelativeCechCoefficients
      (nima-sum-equal NimaCechLoadedBasis) (nima-sum-equal NimaRelativeCechBasis)
  := nima-zsum-setoid-morphism NimaCechLoadedBasis NimaRelativeCechBasis nima-cech-relative-basis-column

```

The resulting objects are setoid complexes and setoid chain maps.  Any later
identity-based or derived interface must consume this structure through an
explicit completion functor; no coercion to identity is present here.
