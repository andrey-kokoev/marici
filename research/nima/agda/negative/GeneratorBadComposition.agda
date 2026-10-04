{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratorBadComposition where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
open import TypedGeneratorLayers
-- Two flips form a history, but not one edge of the original flip relation.
bad : Layer1.Witness flip-layer false false
bad = refl
