{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPortObservationBadReferences where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyPortObservationGates
bad : references false ≡ references true
bad = refl
