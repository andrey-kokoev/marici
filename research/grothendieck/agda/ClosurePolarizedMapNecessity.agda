{-# OPTIONS --safe --cubical --guardedness #-}
module ClosurePolarizedMapNecessity where

open import Cubical.Foundations.Prelude
open import Cubical.HITs.Pushout.Base
open import ClosureGeneratedMapNecessity

-- The quadratic comparison is tested in BOTH slots. Its complete local data
-- contains four piece-pair maps, attachment paths in each slot, and their
-- mixed compatibility. No bilinearity or positivity is assumed or fabricated.
module Polarized {A B S U : Type} (f : S → A) (g : S → B) where
  P = Pushout f g
  module Inner = Generated {T = U} f g
  module Outer = Generated {T = Inner.Cocone} f g

  localData : (P → P → U) → Outer.Cocone
  localData Q = Outer.restrict (λ x → Inner.restrict (Q x))

  reconstruct : Outer.Cocone → P → P → U
  reconstruct c x = Inner.assemble (Outer.assemble c x)

  reconstruct-localData : (Q : P → P → U) → reconstruct (localData Q) ≡ Q
  reconstruct-localData Q = funExt λ x →
    cong Inner.assemble (Outer.assemble-restrict-point
      (λ y → Inner.restrict (Q y)) x)
    ∙ Inner.assemble-restrict (Q x)

  forced-polarized-comparison : (Q R : P → P → U) →
    localData Q ≡ localData R → Q ≡ R
  forced-polarized-comparison Q R h =
    sym (reconstruct-localData Q) ∙ cong reconstruct h ∙ reconstruct-localData R
