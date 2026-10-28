{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPermitFibersBadCollapse where
open import Cubical.Foundations.Prelude
import RamseyFourFacetVertexCells as F
open import RamseyPermitFibers
bad : F.vp-0-3 ≡ F.vp-2-3
bad = refl
