{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRetainedObservationExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import RamseyNativeRetainedObservation
module O = Observations Bool Unit Unit Bool Bool (λ _ → Unit) (λ _ → tt) (λ _ a → a) (λ _ s → s)
example : O.R.Resolve (O.package false tt tt)
example = O.native false tt tt
