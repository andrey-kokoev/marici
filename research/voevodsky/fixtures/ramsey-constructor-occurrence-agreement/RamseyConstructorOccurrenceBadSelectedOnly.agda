{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyConstructorOccurrenceBadSelectedOnly where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces using (m0; c1)
open import RamseyExternalPEExamples
import RamseyFourFacetVertexCells as Ports
import RamseyFourFacetConstructor as F
open import RamseyConstructorOccurrenceAgreement
bad : L.map-occurrence F.comparison-0-1-2 (P.S.AB , ((m0 , (Ports.vp-0-1 , Ports.vp-3-1)) , (P.S.source-leg , tt)))
  ≡ (P.S.AB , ((c1 , (Ports.vp-1-2 , Ports.vp-0-2)) , (P.S.source-leg , tt)))
bad = refl
