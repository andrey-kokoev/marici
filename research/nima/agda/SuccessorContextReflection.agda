{-# OPTIONS --safe --cubical --guardedness #-}
module SuccessorContextReflection where

open import Cubical.Foundations.Prelude

-- Representative witnesses express that every key being classified is a
-- populated incoming fibre. Empty ports are not accidentally constrained.
module Context {ℓR ℓK ℓT : Level}
  (R : Type ℓR) (K : Type ℓK) (T : Type ℓT)
  (key : R → K) (representative : K → R)
  (rep-key : (k : K) → key (representative k) ≡ k)
  (successor : K → T) where

  Reflects : Type _
  Reflects = (a b : R) → successor (key a) ≡ successor (key b) → key a ≡ key b

  Injective : Type _
  Injective = (k l : K) → successor k ≡ successor l → k ≡ l

  preserves : (a b : R) → key a ≡ key b
    → successor (key a) ≡ successor (key b)
  preserves a b = cong successor

  injective-reflects : Injective → Reflects
  injective-reflects injective a b = injective (key a) (key b)

  reflects-injective : Reflects → Injective
  reflects-injective reflects k l p = sym (rep-key k)
    ∙ reflects (representative k) (representative l)
      (cong successor (rep-key k) ∙ p ∙ sym (cong successor (rep-key l)))
    ∙ rep-key l

-- Thus exact preservation/reflection picks the discrete kernel partition,
-- irrespective of generated port names. It does NOT select that contract,
-- specify a response metric, or identify all possible constructors with T9.
