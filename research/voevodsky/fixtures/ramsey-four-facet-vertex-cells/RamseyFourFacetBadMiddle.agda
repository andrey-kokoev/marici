{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFourFacetBadMiddle where
open import Cubical.Foundations.Prelude
open import RamseyFourFacetVertexCells
-- Same chart and vertex, but different retained parent faces.
bad : fst vp-1-2 ≡ fst vp-3-2
bad = refl
