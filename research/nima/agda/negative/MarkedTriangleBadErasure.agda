{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedTriangleBadErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
open import MarkedTriangleCoherence

-- Same diagonal does not identify the effects of the retained first edges.
erased : transport (Types.first-edge ordinary) false ≡ transport (Types.first-edge twisted) false
erased = refl
