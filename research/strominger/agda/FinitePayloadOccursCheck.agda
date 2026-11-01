{-# OPTIONS --safe --cubical --guardedness #-}
module FinitePayloadOccursCheck where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Nat.Order using (_<_; ¬m<m)
open import Cubical.Data.Empty.Base using (⊥)

-- A rank theorem, not a formalization of the JavaScript JSON representation.
-- The source audit supplies a strict rank increase from literal containment.
no-ranked-self-containment : ∀ {ℓ} {A : Type ℓ}
  (rank : A → ℕ) (inner outer : A)
  → rank inner < rank outer → outer ≡ inner → ⊥
no-ranked-self-containment rank inner outer rise same =
  ¬m<m (subst (λ n → rank inner < n) (cong rank same) rise)

-- Even a weaker proposed identification preserving only rank is obstructed.
no-rank-preserving-identification : (n m : ℕ) → n < m → m ≡ n → ⊥
no-rank-preserving-identification n m rise same =
  ¬m<m (subst (λ k → n < k) same rise)
