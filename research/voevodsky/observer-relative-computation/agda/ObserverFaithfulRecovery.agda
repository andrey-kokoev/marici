{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverFaithfulRecovery where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc

-- Generic recovery does not depend on any concrete indexed machine.
module Faithful {A : Type} where
  necessary : (recover : ∥ A ∥₁ → A)
    → ((a : A) → recover ∣ a ∣₁ ≡ a) → isProp A
  necessary recover exact a b = sym (exact a)
    ∙ cong recover (squash₁ ∣ a ∣₁ ∣ b ∣₁) ∙ exact b

  reconstruct : isProp A → ∥ A ∥₁ → A
  reconstruct unique = Trunc.rec unique (λ a → a)

  equivalence : isProp A → ∥ A ∥₁ ≃ A
  equivalence unique = isoToEquiv (iso (reconstruct unique) ∣_∣₁
    (λ _ → refl) (λ t → squash₁ _ t))
