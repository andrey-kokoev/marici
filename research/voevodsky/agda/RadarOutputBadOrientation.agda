{-# OPTIONS --safe --cubical --guardedness #-}
module RadarOutputBadOrientation where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos; -_)
open import RadarOutputEnclosure
open IntegerBounds
-- Negation must exchange the lower and upper endpoint.
bad : lower (neg-I (interval (pos 1) (pos 2))) ≡ - (pos 1)
bad = refl
