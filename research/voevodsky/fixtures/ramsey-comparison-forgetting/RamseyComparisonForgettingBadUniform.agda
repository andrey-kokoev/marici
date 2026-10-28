{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyComparisonForgettingBadUniform where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false)
open import RamseyComparisonForgetting
-- Constant reconstruction is not valid uniformly over independent targets.
bad : Factors {X = Bool × Bool} fst snd
bad = (λ _ → false) , (λ x → refl)
