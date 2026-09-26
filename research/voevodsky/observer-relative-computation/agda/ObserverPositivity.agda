{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverPositivity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import IndexIdentityCoherence as Indexed
import IndexIdentityCoherenceRegression as Cover
module Ix = Indexed.Indexed ℓ-zero

-- These are different notions; no metric or temporal order is assumed.
module Positivity (O X : Type) (p : O → X) (F : X → Type) where
  Supported = O
  Participation = Σ O (λ o → F (p o))
  Observation = (o : O) → F (p o)
  PointwisePossible = (o : O) → ∥ F (p o) ∥₁
  SupportedObservation = Σ O (λ _ → Observation)
  Distinguishable = Σ Observation (λ s → Σ Observation (λ t → (s ≡ t → ⊥)))

  participation-has-support : Participation → Supported
  participation-has-support = fst

  coherent-participation : SupportedObservation → Participation
  coherent-participation (o , s) = o , s o

  observation-is-possible : Observation → PointwisePossible
  observation-is-possible s o = ∣ s o ∣₁

-- Nonempty support does not manufacture an accessible witness.
module EmptyContent where
  module P = Positivity Unit Unit (λ x → x) (λ _ → ⊥)
  supported : P.Supported
  supported = tt
  no-participation : P.Participation → ⊥
  no-participation = snd

-- Positive actual participation does not require distinguishable states.
module StaticContent where
  module P = Positivity Unit Unit (λ x → x) (λ _ → Unit)
  participates : P.Participation
  participates = tt , tt
  coherent : P.SupportedObservation
  coherent = tt , (λ _ → tt)
  no-distinction : P.Distinguishable → ⊥
  no-distinction (s , t , unequal) = unequal refl

module EverywherePossible where
  module P = Positivity (Ix.Index Cover.F) (Ix.Index Cover.F)
    (λ x → x) (Ix.Fibre Cover.F)

  participates : P.Participation
  participates = Cover.base-index , true

  -- Truncated existence is compatible around the loop even though
  -- choosing a witness coherently around it is impossible.
  locally-possible : P.PointwisePossible
  locally-possible (tt , Cover.base) = ∣ true ∣₁
  locally-possible (tt , Cover.loop i) =
    isProp→PathP {B = λ j → ∥ Ix.Fibre Cover.F (tt , Cover.loop j) ∥₁}
      (λ _ → squash₁) ∣ true ∣₁ ∣ true ∣₁ i

  no-observation : P.Observation → ⊥
  no-observation = Cover.no-section

  no-supported-observation : P.SupportedObservation → ⊥
  no-supported-observation (_ , s) = no-observation s

  -- This is not a claim about failure of effective search alone:
  -- the candidate coherent section itself cannot exist.
  pointwise-does-not-select : (P.PointwisePossible → P.Observation) → ⊥
  pointwise-does-not-select choose = no-observation (choose locally-possible)
