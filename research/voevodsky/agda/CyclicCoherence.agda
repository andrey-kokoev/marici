{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CyclicCoherence where

open import Cubical.Foundations.Prelude

record Vertex : Type₁ where
  field
    P O R : Type
    generate : P → O
    cohere : O → R

record LaxCycle : Type₁ where
  field
    A B C : Vertex
    T-A : Vertex.R A → Vertex.P B
    T-B : Vertex.R B → Vertex.P C
    T-C : Vertex.R C → Vertex.P A

module CommonFiber {X : Type} (x : X) where

  edge : x ≡ x
  edge = refl

  face : Square edge edge edge edge
  face i j = x

  omega : Cube face face face face face face
  omega i j k = x

  fillerType : Type
  fillerType = Cube face face face face face face

  fillerInhabited : fillerType
  fillerInhabited = omega
