{-# OPTIONS --safe --cubical --guardedness #-}
module PeriodFourWitness where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Path using (compPath→Square)
open import Cubical.Data.Sigma using (ΣPathP)

module General {ℓ : Level} {S : Type ℓ} (F : S → S) where
  Fix : Type ℓ
  Fix = Σ S (λ a → F a ≡ a)

  advance : Fix → Fix
  advance (a , p) = F a , cong F p

  -- Both boundary composites are literally cong F p ∙ p.
  return-square : (a : S) (p : F a ≡ a)
    → PathP (λ i → F (p i) ≡ p i) (cong F p) p
  return-square a p = compPath→Square refl

  fixpoint-shift-homotopy : (x : Fix) → advance x ≡ x
  fixpoint-shift-homotopy (a , p) = ΣPathP (p , return-square a p)

module PeriodFour {ℓ : Level} {S : Type ℓ} (G : S → S) where
  fourth : S → S
  fourth a = G (G (G (G a)))

  open General fourth
  Per4 = Fix

  shift : Per4 → Per4
  shift (a , p) = G a , cong G p

  shift-four-return : (x : Per4)
    → shift (shift (shift (shift x))) ≡ x
  shift-four-return = fixpoint-shift-homotopy
