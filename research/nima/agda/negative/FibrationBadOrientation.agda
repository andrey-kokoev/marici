{-# OPTIONS --safe --cubical --guardedness #-}
module negative.FibrationBadOrientation where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import TableFibrationCycle
-- EXPECTED FAILURE: keeping a row is not enough to preserve its endpoint roles.
bad : TableIso example (transpose example)
TableIso.rows bad = idIso
TableIso.preserves-label bad r = refl
TableIso.preserves-from bad r = refl
TableIso.preserves-to bad r = refl
