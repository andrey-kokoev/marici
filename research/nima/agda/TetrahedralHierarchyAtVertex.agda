{-# OPTIONS --safe --cubical --guardedness #-}
module TetrahedralHierarchyAtVertex where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Empty.Base using (⊥)
import RetainedTetrahedralPackage as Retained

-- Arity levels in the existing filled tetrahedral package, not powers of
-- an energy variable and not a requirement on every WG constructor.
module Hierarchy {ℓ : Level} (X : Type ℓ) where
  module C = Retained.Cells X

  vertices : C.Full → C.Vertices
  vertices = fst
  surface : (p : C.Full) → C.Over.Surface (vertices p)
  surface p = fst (snd p)
  edges : (p : C.Full) → C.Over.Edges (vertices p)
  edges p = C.Over.Surface.edges (surface p)
  filler : (p : C.Full) → C.Over.Filler (vertices p) (surface p)
  filler p = snd (snd p)

  -- Surface retains all four named triangular faces and their shared edges.
  reassemble : (p : C.Full) → (vertices p , surface p , filler p) ≡ p
  reassemble p = refl

  -- Explicit lossless view adapter. The original vertex projection alone
  -- is not this view: here the complete hierarchy remains in the package.
  module At (mark : C.Vertex) where
    View : Type ℓ
    View = Σ[ x ∈ X ] Σ[ p ∈ C.Full ] (C.vertex p mark ≡ x)

    decorate : C.Full → View
    decorate p = C.vertex p mark , p , refl
    recover : View → C.Full
    recover v = fst (snd v)

    recover-decorate : (p : C.Full) → recover (decorate p) ≡ p
    recover-decorate p = refl
    decorate-recover : (v : View) → decorate (recover v) ≡ v
    decorate-recover (x , p , w) i = w i , p , (λ j → w (i ∧ j))

    active-unchanged : (p : C.Full) → fst (decorate p) ≡ C.vertex p mark
    active-unchanged p = refl
    all-tiers-recovered : (p : C.Full)
      → (vertices (recover (decorate p)) , surface (recover (decorate p)) , filler (recover (decorate p))) ≡ p
    all-tiers-recovered p = refl

-- Existing hostile: same fixed four vertices, even the same diagonal, but
-- different edge witnesses and hence different retained packages.
module VertexProjectionControl where
  module L = Retained.LossyDiagonal
  active : L.O.Package → Type
  active p = L.C.vertex (L.v , p) L.C.zero
  active-agrees : active L.ordinary ≡ active L.twisted
  active-agrees = refl

  no-vertex-only-recovery : (decode : Type → L.O.Package)
    → ((p : L.O.Package) → decode (active p) ≡ p) → ⊥
  no-vertex-only-recovery decode law = L.distinct
    (sym (law L.ordinary) ∙ law L.twisted)
