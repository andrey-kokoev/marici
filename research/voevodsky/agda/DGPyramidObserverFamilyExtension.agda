{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidObserverFamilyExtension where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sigma
open import Cubical.Data.Sum using (_⊎_; inl; inr)

-- Pointed observer families; joint faithfulness is stated by equality of all
-- readings, avoiding any illicit identification of distinct observer targets.
record ObserverFamily {ℓ : Level} (Source : Type ℓ) : Type (ℓ-suc ℓ) where
  field
    Index : Type ℓ
    Reading : Index → Type ℓ
    observe : (i : Index) → Source → Reading i

open ObserverFamily public

JointlyFaithful : {ℓ : Level} {S : Type ℓ} → ObserverFamily S → Type ℓ
JointlyFaithful F = (x y : _) →
  ((i : Index F) → observe F i x ≡ observe F i y) → x ≡ y

-- Adding any lawful family to an already jointly faithful family preserves
-- joint faithfulness.  This is the exact categorical content available when
-- adjoining the six normal observers to the full Fourier family.
extendObserverFamily : {ℓ : Level} {S : Type ℓ} →
  ObserverFamily S → ObserverFamily S → ObserverFamily S
extendObserverFamily F G = record
  { Index = Index F ⊎ Index G
  ; Reading = λ where
      (inl i) → Reading F i
      (inr j) → Reading G j
  ; observe = λ where
      (inl i) → observe F i
      (inr j) → observe G j
  }

extensionPreservesJointFaithfulness : {ℓ : Level} {S : Type ℓ} →
  (F G : ObserverFamily S) → JointlyFaithful F →
  JointlyFaithful (extendObserverFamily F G)
extensionPreservesJointFaithfulness F G faithful x y same =
  faithful x y (λ i → same (inl i))

-- Transport is required before two families on differently presented source
-- types can be combined.  This record prevents mere target-level incidence
-- from being mistaken for a common-source observer theorem.
record SourceTransport {ℓ : Level} (A B : Type ℓ) : Type ℓ where
  field
    forward : A → B
    backward : B → A
    backwardForward : (x : A) → backward (forward x) ≡ x

open SourceTransport public

pullObserverFamily : {ℓ : Level} {A B : Type ℓ} →
  SourceTransport A B → ObserverFamily B → ObserverFamily A
pullObserverFamily T F = record
  { Index = Index F
  ; Reading = Reading F
  ; observe = λ i x → observe F i (forward T x)
  }

pullbackPreservesJointFaithfulness : {ℓ : Level} {A B : Type ℓ} →
  (T : SourceTransport A B) → (F : ObserverFamily B) →
  JointlyFaithful F → JointlyFaithful (pullObserverFamily T F)
pullbackPreservesJointFaithfulness T F faithful x y same =
  sym (backwardForward T x) ∙
  cong (backward T) (faithful (forward T x) (forward T y) same) ∙
  backwardForward T y
