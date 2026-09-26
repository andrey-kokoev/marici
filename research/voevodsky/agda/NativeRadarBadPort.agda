{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRadarBadPort where
open import NativeRadarReadout
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
sample : Rows
sample before x3 = clocks (pos 0) (pos 1)
sample _ _ = clocks (pos 0) (pos 0)
-- Synthetic algebraic hostile, not a physically admitted clock schedule.
bad : native-read sample xx ≡ native-read sample yy
bad = refl
