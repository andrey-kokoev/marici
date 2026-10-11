{-# OPTIONS --safe --cubical --guardedness #-}
module PathUnitCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit; rUnit; assoc)
open import Cubical.Foundations.Path using (Square→compPath; compPathlEquiv)
open import Cubical.Foundations.Equiv using (invEq)
open import Cubical.Foundations.Equiv.Properties using (congEquiv)

-- In the reflexive case both units compute to h. The associator is the
-- antidiagonal of the square obtained by composing h with itself.
-- Its boundary equation, followed by unit naturality and cancellation,
-- proves the base case without assuming that higher paths are propositions.
module _ {ℓ : Level} {A : Type ℓ} (x : A) where
  private
    h : refl {x = x} ≡ refl ∙ refl
    h = rUnit refl
    unit-at-refl : lUnit (refl {x = x}) ≡ h
    unit-at-refl = refl
    assoc-at-refl : assoc (refl {x = x}) refl refl ≡ (λ i → h i ∙ h (~ i))
    assoc-at-refl = refl

    square : Square (cong (_∙ refl) h) refl (cong (refl ∙_) h) (sym (assoc refl refl refl))
    square i j = h (j ∧ ~ i) ∙ h i

    unit-naturality : cong (refl ∙_) h ≡ lUnit (refl ∙ refl)
    unit-naturality = invEq (congEquiv (compPathlEquiv h))
      (Square→compPath (λ i j → lUnit (h j) i))

  left-unit-assoc-refl :
    cong (_∙ refl {x = x}) (lUnit refl) ∙ sym (assoc refl refl refl)
      ≡ lUnit (refl ∙ refl)
  left-unit-assoc-refl = sym (Square→compPath square)
    ∙ sym (rUnit (cong (refl ∙_) h)) ∙ unit-naturality

-- Generalize both endpoints during induction; no fixed-boundary path is
-- erased or replaced by proof irrelevance.
left-unit-assoc : ∀ {ℓ} {A : Type ℓ} {x y z : A}
  (p : x ≡ y) (q : y ≡ z)
  → cong (_∙ q) (lUnit p) ∙ sym (assoc refl p q) ≡ lUnit (p ∙ q)
left-unit-assoc {x = x} p q = J
  (λ y p → ∀ {z} (q : y ≡ z)
    → cong (_∙ q) (lUnit p) ∙ sym (assoc refl p q) ≡ lUnit (p ∙ q))
  (J (λ z q → cong (_∙ q) (lUnit refl) ∙ sym (assoc refl refl q)
       ≡ lUnit (refl ∙ q)) (left-unit-assoc-refl x)) p q
