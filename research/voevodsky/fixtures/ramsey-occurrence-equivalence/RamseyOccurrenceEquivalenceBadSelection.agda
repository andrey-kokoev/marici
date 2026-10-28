{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyOccurrenceEquivalenceBadSelection where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (m0; c1)
import RamseyFourFacetVertexCells as F
open import RamseyExternalPEExamples
open import RamseyOccurrenceEquivalence
bad : move-0-1-2 (P.S.AB , ((m0 , (F.vp-0-1 , F.vp-3-1)) , (P.S.source-leg , tt)))
  ≡ (P.S.AB , ((c1 , (F.vp-1-2 , F.vp-0-2)) , (P.S.source-leg , tt)))
bad = refl
