{-# OPTIONS --safe --cubical --guardedness #-}
module negative.DSCBadStationarity where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import DSCActionCountermodels
-- EXPECTED FAILURE: legal DSC execution need not be stationary.
bad : Output.residual (run (quadratic , pos 2)) ≡ pos 0
bad = refl
