{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedTetrahedronBadErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
open import MarkedTetrahedronCoherence

-- Identical return diagonals cannot erase the retained first-edge action.
erased : transport (Types.first-edge ordinary) false ≡ transport (Types.first-edge twisted) false
erased = refl
