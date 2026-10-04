{-# OPTIONS --safe --cubical --guardedness #-}
module GradedBoundaryBadFiller where
open import Cubical.Foundations.Prelude
open import GradedBoundaryCoherence

-- Must reject: a well-formed boundary is not automatically filled.
answer : BoolTower.Fill 1 incompatible-boundary
answer = refl
