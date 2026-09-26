{-# OPTIONS --safe --cubical --guardedness #-}
module negative.AmplitudeResolveBadReadout where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import ScalarAmplitudeResolveFixture
-- EXPECTED FAILURE: the selected native expression does not read out 145.
bad : E.readout expression (snd (E.package expression)) ≡ pos 145
bad = refl
