{-# OPTIONS --safe --cubical --guardedness #-}
module RadarOutputBadSquare where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos; negsuc)
open import RadarOutputEnclosure
open IntegerBounds
-- A zero-crossing interval cannot use the nonnegative-endpoint square rule.
bad : Inside (square-I (interval (negsuc 0) (pos 1))) (pos 0)
bad = (0 , refl) , (1 , refl)
