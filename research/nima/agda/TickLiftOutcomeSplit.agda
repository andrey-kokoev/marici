{-# OPTIONS --safe --cubical --guardedness #-}
module TickLiftOutcomeSplit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.Data.Empty using (⊥)

-- Logical schemas. No candidate type or source-derived predicate is supplied.
module Split {ℓ : Level} (Candidate : Type ℓ)
  (LocalLift ReturnInterpretation : Candidate → Type ℓ) where

  FullLift : Type ℓ
  FullLift = Σ Candidate (λ f → LocalLift f × ReturnInterpretation f)

  LocalCore : Type ℓ
  LocalCore = Σ Candidate LocalLift

  positive-branch : FullLift → LocalCore
  positive-branch (f , local , returned) = f , local

  negative-branch : (FullLift → ⊥)
    → (f : Candidate) → LocalLift f → ReturnInterpretation f → ⊥
  negative-branch noFull f local returned = noFull (f , local , returned)

  -- A standalone rejection of the weaker claim refutes the full lift.
  local-core-rejection-refutes-full : (LocalCore → ⊥) → FullLift → ⊥
  local-core-rejection-refutes-full noLocal full = noLocal (positive-branch full)

  -- A positive local witness leaves precisely its own return obligation.
  extend-local-witness : (local : LocalCore) → ReturnInterpretation (fst local) → FullLift
  extend-local-witness (f , local) returned = f , local , returned
