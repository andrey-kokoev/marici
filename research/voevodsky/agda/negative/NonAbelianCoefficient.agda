{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module NonAbelianCoefficient where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.Group
open import Cubical.Algebra.AbGroup
open import GenericPastingComplex

-- Deliberate failure: an arbitrary group does not supply the commutativity
-- required by the coefficient-generic cyclic complex.
module Invalid {ℓ : Level} (G : Group ℓ) where
  badCoefficient : AbGroup ℓ
  badCoefficient = Group→AbGroup G
