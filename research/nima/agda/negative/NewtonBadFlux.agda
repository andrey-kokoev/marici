{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NewtonBadFlux where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import NewtonRadialCoefficients
-- Radius 2 and slope numerator 3 imply flux numerator 12, not 11.
bad : normalizedFluxNumerator (pos 2) (pos 3) ≡ pos 11
bad = refl
