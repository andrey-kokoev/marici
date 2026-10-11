{-# OPTIONS --safe --cubical --guardedness #-}
module TetrahedralReturnTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (rCancel)
import RetainedTetrahedralPackage as Retained

-- Ordinary path transport in the EXISTING filled-tetrahedron specialization.
-- This theorem does not erase the retained route or higher filler records.
module Return {ℓ ℓ' : Level} (X : Type ℓ) (F : X → Type ℓ') where
  module C = Retained.Cells X
  root : C.Full → X
  root p = C.Vertices.v0 (fst p)
  edges : (p : C.Full) → C.Over.Edges (fst p)
  edges p = C.Over.Surface.edges (fst (snd p))
  diagonal : (p : C.Full) → root p ≡ C.Vertices.v3 (fst p)
  diagonal p = C.T.Edges.e03 (edges p)
  spine : (p : C.Full) → root p ≡ C.Vertices.v3 (fst p)
  spine p = (C.T.Edges.e01 (edges p) ∙ C.T.Edges.e12 (edges p))
    ∙ C.T.Edges.e23 (edges p)
  spine-to-diagonal : (p : C.Full) → spine p ≡ diagonal p
  spine-to-diagonal p = C.T.Over.left-route (edges p)
    (C.Over.Surface.face012 (fst (snd p)))
    (C.Over.Surface.face023 (fst (snd p)))

  cycle : (p : C.Full) → root p ≡ root p
  cycle p = spine p ∙ sym (diagonal p)
  cycle-null : (p : C.Full) → cycle p ≡ refl
  cycle-null p = cong (λ q → q ∙ sym (diagonal p)) (spine-to-diagonal p)
    ∙ rCancel (diagonal p)

  reference-return : (p : C.Full) (reference : F (root p))
    → subst F (cycle p) reference ≡ reference
  reference-return p reference = cong (λ q → subst F q reference) (cycle-null p)
    ∙ transportRefl reference
