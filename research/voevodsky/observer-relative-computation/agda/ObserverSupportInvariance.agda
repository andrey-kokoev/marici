{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverSupportInvariance where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd; Σ-cong-equiv-fst)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)

-- A support equivalence ALONE is insufficient: retain the comparison
-- of the access maps as well. Its action need not be the identity.
module Presentation (O Q X : Type) (F : X → Type)
  (p : O → X) (q : Q → X) (e : O ≃ Q)
  (h : (o : O) → p o ≡ q (equivFun e o)) where

  fibre-equiv : (o : O) → F (p o) ≃ F (q (equivFun e o))
  fibre-equiv o = pathToEquiv (cong F (h o))

  participation-equiv : Σ O (λ o → F (p o)) ≃ Σ Q (λ a → F (q a))
  participation-equiv = compEquiv (Σ-cong-equiv-snd fibre-equiv) (Σ-cong-equiv-fst e)

  observation-equiv : ((o : O) → F (p o)) ≃ ((a : Q) → F (q a))
  observation-equiv = equivΠ e fibre-equiv

  -- An observation obstruction is preserved, not hidden by relabelling.
  obstruction-preserved : (((o : O) → F (p o)) → ⊥)
    → (((a : Q) → F (q a)) → ⊥)
  obstruction-preserved impossible s = impossible (invEq observation-equiv s)

-- Duplicating a point as two independent accesses is NOT an equivalent
-- presentation. Without compatibility it admits new disagreement.
module Duplication where
  restrict : (Unit → Bool) → Bool → Bool
  restrict s _ = s tt

  disagree : Bool → Bool
  disagree true = true
  disagree false = false

  disagreement-not-restricted : (s : Unit → Bool) → restrict s ≡ disagree → ⊥
  disagreement-not-restricted s eq = true≢false
    (sym (cong (λ f → f true) eq) ∙ cong (λ f → f false) eq)

  -- Agreement recovers descent to the single original access.
  descend : (t : Bool → Bool) → t true ≡ t false → Unit → Bool
  descend t agreement _ = t true

  descent-recovers : (t : Bool → Bool) (agreement : t true ≡ t false)
    → restrict (descend t agreement) ≡ t
  descent-recovers t agreement i true = t true
  descent-recovers t agreement i false = agreement i
