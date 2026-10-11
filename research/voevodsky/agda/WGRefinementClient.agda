{-# OPTIONS --safe --cubical --guardedness #-}
module WGRefinementClient where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1)
open import ComposableWitnessSpecialization

-- INPUT: independently stated; not importing ProofDependentFixture's solutions.
base : Layer1 ℓ-zero
base = record { State = Bool ; Witness = λ s t → t ≡ not s ; generate = λ s → not s , refl }
first : Refinement base
first = record
  { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift true
  ; Admit = λ _ → Bool ; advance = λ s p → not p
  ; Extra = λ x y r → Bool ; certify = snd }
second : Refinement (compile first)
second = record
  { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift false
  ; Admit = λ _ → Bool ; advance = λ x q → not q
  ; Extra = λ x y w → snd w ≡ snd (fst x)
  ; certify = λ x → refl }
third : Refinement (compile second)
third = record
  { Source = Lift {j = ℓ-suc ℓ-zero} Bool ; source = lift true
  ; Admit = λ _ → Bool ; advance = λ x z → not z
  ; Extra = λ x y w → snd (fst w) ≡ snd (fst (fst x))
  ; certify = λ x → refl }

-- TWO LAYERS: generic composition supplies the full-step certificate.
composite : Refinement base
composite = compose first second
module C = Composite first second
correct : Realization (compile second) (compile composite)
correct = C.correct
recover₁ : fst (Refinement.source composite) ≡ Refinement.source first
recover₁ = C.recover-first-source
recover₂ : snd (Refinement.source composite) ≡ Refinement.source second
recover₂ = C.recover-second-source
rejectsErasure : Refinement.Extra second
  ((false , true) , false) ((true , false) , true) (refl , false) → ⊥
rejectsErasure = false≢true

-- THIRD LAYER: generic rebasing and associativity replace local tuple maps.
module A = Associativity first second third
reused : Refinement base
reused = compose composite (C.rebase third)
associated : Realization (compile reused) (compile A.right)
associated = A.associator
sourcePreserved : Iso.fun A.source-associator (Refinement.source reused)
  ≡ Refinement.source A.right
sourcePreserved = A.source-preserved
