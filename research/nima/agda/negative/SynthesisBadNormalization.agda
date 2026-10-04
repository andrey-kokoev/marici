{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisBadNormalization where
open import Cubical.Foundations.Prelude
open import AlgebraSynthesisSpecification
-- Raw variable names are not an admissible canonical source coordinate.
bad : Formula
bad = (var 1 , var 1) , refl
