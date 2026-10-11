{-# OPTIONS --safe --cubical --guardedness #-}
module WolframConstructedEquivalence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isPropΠ)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using ([])
open import RefutationConstructionWG
import GeneratedWolframConstruction as Generated

module Result {ℓ : Level} (A B C : Type ℓ) where
  atoms : ℕ → Type ℓ
  atoms zero = A
  atoms (suc zero) = B
  atoms (suc (suc n)) = C
  open Semantics atoms

  bottom-prop : isProp (Meaning bottom)
  bottom-prop x y = cong lift (isProp⊥ (lower x) (lower y))

  empty-environment : Environment []
  empty-environment ()

  -- These maps interpret the results of the individual WG rule calls.
  forward : Meaning Generated.W → Meaning Generated.D
  forward = evaluate (construct Generated.forward) empty-environment
  backward : Meaning Generated.D → Meaning Generated.W
  backward = evaluate (construct Generated.backward) empty-environment

  equivalence : Meaning Generated.W ≃ Meaning Generated.D
  equivalence = isoToEquiv record
    { fun = forward ; inv = backward
    ; rightInv = λ d → isPropΠ (λ _ → bottom-prop) _ d
    ; leftInv = λ w → isPropΠ (λ _ → bottom-prop) _ w }

  -- Recovering C additionally requires stability and propositionality.
  stable-equivalence : isProp C → (Meaning Generated.D → C)
    → Meaning Generated.W ≃ C
  stable-equivalence prop stable = isoToEquiv record
    { fun = λ w → stable (forward w)
    ; inv = λ c → backward (λ nc → nc c)
    ; rightInv = λ c → prop _ c
    ; leftInv = λ w → isPropΠ (λ _ → bottom-prop) _ w }
