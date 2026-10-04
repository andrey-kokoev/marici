{-# OPTIONS --safe --cubical --guardedness #-}
module CoherenceBadScoreLift where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import TypedGeneratorCoherence
open Controls

-- A shared score comparison does not lift to a comparison of the original
-- history observations. The required source comparison would imply true/false.
bad-lift : Cell 1 Bool (boundaryMap 1 C.score separated)
  → C.MB.is-empty (fst C.idle) ≡ C.MB.is-empty (fst C.twice)
bad-lift p = refl
