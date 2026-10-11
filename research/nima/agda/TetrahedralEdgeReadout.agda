{-# OPTIONS --safe --cubical --guardedness #-}
module TetrahedralEdgeReadout where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (isoToEquiv)
open import Cubical.Foundations.Univalence using (uaβ; ~uaβ)
open import Cubical.Data.Bool.Base using (Bool)
import RetainedTetrahedralPackage as Retained
import GradedBoundaryCoherence as Source

module L = Retained.LossyDiagonal
edge12 : L.O.Package → Bool ≡ Bool
edge12 p = L.C.T.Edges.e12 (L.O.Surface.edges (fst p))

-- Exact truth-table contract for the existing filled packages, rather than
-- independent Boolean maps guessed to make the feedback example work.
ordinary01 : (b : Bool) → transport (L.first-edge L.ordinary) b ≡ b
ordinary01 b = transportRefl b
ordinary12 : (b : Bool) → transport (edge12 L.ordinary) b ≡ b
ordinary12 b = transportRefl b
twisted01 : (b : Bool) → transport (L.first-edge L.twisted) b ≡ Source.flip b
twisted01 b = uaβ (isoToEquiv Source.flip-iso) b
twisted12 : (b : Bool) → transport (edge12 L.twisted) b ≡ Source.flip b
twisted12 b = ~uaβ (isoToEquiv Source.flip-iso) b

ordinary-composite : (b : Bool)
  → transport (edge12 L.ordinary) (transport (L.first-edge L.ordinary) b) ≡ b
ordinary-composite b = cong (transport (edge12 L.ordinary)) (ordinary01 b) ∙ ordinary12 b
twisted-composite : (b : Bool)
  → transport (edge12 L.twisted) (transport (L.first-edge L.twisted) b) ≡ b
twisted-composite b = cong (transport (edge12 L.twisted)) (twisted01 b)
  ∙ (twisted12 (Source.flip b) ∙ Source.flip-twice b)

same-mark : L.C.vertex (L.v , L.ordinary) L.C.zero
  ≡ L.C.vertex (L.v , L.twisted) L.C.zero
same-mark = refl
same-diagonal = L.same-diagonal
