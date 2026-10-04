{-# OPTIONS --safe --cubical --guardedness #-}
module CoherenceBadGlobalFiller where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import TypedGeneratorCoherence

-- Relative coherence must not be used as a filler for an arbitrary boundary.
bad : Cell 1 Bool Controls.incompatible
bad = refl
