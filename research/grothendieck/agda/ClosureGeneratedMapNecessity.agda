{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGeneratedMapNecessity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Function using (_∘_) 
open import Cubical.Data.Sigma
open import Cubical.HITs.Pushout.Base

-- A map from a closure is exactly its two piece maps AND attachment paths.
-- No independently selected global comparison is an input.
module Generated {A B S T : Type} (f : S → A) (g : S → B) where
  P : Type
  P = Pushout f g

  Cocone : Type
  Cocone = Σ (A → T) (λ l → Σ (B → T)
    (λ r → (s : S) → l (f s) ≡ r (g s)))

  assemble : Cocone → P → T
  assemble (l , r , h) (inl a) = l a
  assemble (l , r , h) (inr b) = r b
  assemble (l , r , h) (push s i) = h s i

  restrict : (P → T) → Cocone
  restrict F = (λ a → F (inl a)) , (λ b → F (inr b)) ,
    (λ s → cong F (push s))

  restrict-assemble : (c : Cocone) → restrict (assemble c) ≡ c
  restrict-assemble (l , r , h) = refl

  assemble-restrict-point : (F : P → T) (x : P) → assemble (restrict F) x ≡ F x
  assemble-restrict-point F (inl a) = refl
  assemble-restrict-point F (inr b) = refl
  assemble-restrict-point F (push s i) = refl

  assemble-restrict : (F : P → T) → assemble (restrict F) ≡ F
  assemble-restrict F = funExt (assemble-restrict-point F)

  generatedMapIso : Iso (P → T) Cocone
  Iso.fun generatedMapIso = restrict
  Iso.inv generatedMapIso = assemble
  Iso.rightInv generatedMapIso = restrict-assemble
  Iso.leftInv generatedMapIso = assemble-restrict

  -- Equality is forced by equality of COMPLETE constructor data.
  -- An equality of just l and r does not satisfy this premise.
  determined-by-constructors : (F G : P → T) → restrict F ≡ restrict G → F ≡ G
  determined-by-constructors F G h =
    sym (assemble-restrict F) ∙ cong assemble h ∙ assemble-restrict G

-- Readout commutation follows by checking its full local cocone.
module Comparison {A B S T U : Type} (f : S → A) (g : S → B) where
  module Target = Generated {T = U} f g
  comparison-square : (readout : T → U)
    (F : Pushout f g → T) (G : Pushout f g → U)
    (local : Target.restrict (readout ∘ F) ≡ Target.restrict G) →
    readout ∘ F ≡ G
  comparison-square readout F G local =
    Target.determined-by-constructors (readout ∘ F) G local
