{-# OPTIONS --safe --cubical --guardedness #-}
module negative.WolframBadProof where
open import Cubical.Foundations.Prelude
module Bad {ℓ : Level} (A : Type ℓ) (_∣_ : A → A → A)
  (W : (a b c : A) → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c) where
  -- EXPECTED FAILURE: commutativity needs a derivation, not reflexivity.
  bad : (x y : A) → (x ∣ y) ≡ (y ∣ x)
  bad x y = refl
