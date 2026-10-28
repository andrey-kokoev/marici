{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPermitEquivalenceBadFacet where
open import Cubical.Foundations.Prelude
import RamseyFourFacetVertexCells as F
open import RamseyPermitEquivalence
bad : move-0-1 F.vp-2-1 ≡ F.vp-1-0
bad = refl
