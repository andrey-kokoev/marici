{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRealizationHolonomy where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence
open import ClosureTypedRealization using (TypedRealization)

-- Summarize a closed typed-realization path by its type automorphism and
-- the witness that its selected value returns. Keeping BOTH components is
-- necessary; the bare fact that the endpoint types match loses information.
PointedAction : (T : Type) → T → Type
PointedAction T v = Σ[ e ∈ (T ≃ T) ] (equivFun e v ≡ v)

residual : {T : Type} {v : T} →
  Path TypedRealization (T , v) (T , v) → PointedAction T v
residual p = pathToEquiv (cong fst p) , fromPathP (λ i → snd (p i))

residualAction : {T : Type} {v : T} →
  Path TypedRealization (T , v) (T , v) → T → T
residualAction p = equivFun (fst (residual p))

residualFixesValue : {T : Type} {v : T}
  (p : Path TypedRealization (T , v) (T , v)) → residualAction p v ≡ v
residualFixesValue p = snd (residual p)

-- This extracts a residual invariant. No complete classification of loops
-- by PointedAction, or sufficiency of point-fixing for null-homotopy, is
-- asserted here. The regression explicitly refutes the latter sufficiency.
