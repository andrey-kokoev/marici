{-# OPTIONS --safe --cubical --guardedness #-}
module PresentationBadCompletion where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit)
open import TypedGeneratorPresentation

-- A certificate for forgetting an arbitrary Boolean cannot be supplied.
bad : Reduction {ℓF = ℓ-zero} (Σ[ u ∈ Unit ] Bool) Unit
bad = contractRemainder (λ _ → Bool)
  (λ _ → false , λ { false → refl ; true → refl })
