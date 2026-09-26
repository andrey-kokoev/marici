{-# OPTIONS --safe --cubical --guardedness #-}
module negative.DSCBadQuadraticity where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import DSCActionCountermodels
-- EXPECTED FAILURE: the typed quartic action has a nonzero fourth coefficient.
bad : fourthCoefficient (polynomial quartic) ≡ pos 0
bad = refl
