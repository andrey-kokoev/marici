{-# OPTIONS --safe --cubical --guardedness #-}
module RefinementBadWitness where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import BarycentricRefinementCoherence
-- Changing the annotation while claiming reflexive preservation fails.
bad : Preservation BoolSource.T BoolSource.w BoolSource.carrier
bad = (λ _ → true) , (λ _ → refl)
