{-# OPTIONS --safe --cubical --guardedness #-}
module GradedBoundaryBadErasure where
open import Cubical.Foundations.Prelude
open import GradedBoundaryCoherence

-- Must reject: higher reflexive expansion does not identify different answers.
erased : false-cycle ≡ true-cycle
erased = refl
