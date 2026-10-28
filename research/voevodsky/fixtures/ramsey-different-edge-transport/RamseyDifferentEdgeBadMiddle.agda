{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDifferentEdgeBadMiddle where
open import Cubical.Foundations.Prelude
import RamseyPermitEquivalence as M
import RamseyFourFacetVertexCells as F
bad : M.move-0-1 F.vp-2-1 ≡ M.move-0-1 F.vp-0-1
bad = refl
