{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRetainedObservationBadReadout where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Unit.Base using (tt)
open import RamseyRetainedObservationExamples
bad : O.Index false
bad = tt , (false , (refl , (true , refl)))
