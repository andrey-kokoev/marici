{-# OPTIONS --safe --cubical --guardedness #-}
module FixedBoundaryBadErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import GradedBoundaryCoherence using (twisted-filler)
open import FixedTetrahedralBoundary

-- Same source and target type, but the retained path acts differently.
erased : false-section Bool refl ≡ false-section Bool twisted-filler
erased = refl
