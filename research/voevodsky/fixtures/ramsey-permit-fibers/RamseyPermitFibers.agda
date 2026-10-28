{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPermitFibers where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1; face)
open import RamseyUniformRelative using (Slot; first; next)
open import RamseyNativeEdgeAttachments using (InFace)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
number : Vertex → ℕ
number c0 = 0
number m0 = 1
number c1 = 2
number m1 = 3
vertex : ℕ → Vertex
vertex zero = c0
vertex (suc zero) = m0
vertex (suc (suc zero)) = c1
vertex (suc (suc (suc n))) = m1
retract : (v : Vertex) → vertex (number v) ≡ v
retract c0 = refl
retract m0 = refl
retract c1 = refl
retract m1 = refl
vertex-set : isSet Vertex
vertex-set = isSetRetract number vertex retract isSetℕ
position : Vertex → Vertex → Slot 3
position c0 c0 = first
position c0 m0 = first
position c0 c1 = (next first)
position c0 m1 = (next (next first))
position m0 c0 = first
position m0 m0 = first
position m0 c1 = (next first)
position m0 m1 = (next (next first))
position c1 c0 = first
position c1 m0 = (next first)
position c1 c1 = first
position c1 m1 = (next (next first))
position m1 c0 = first
position m1 m0 = (next first)
position m1 c1 = (next (next first))
position m1 m1 = first
position-face : (f : Vertex) (i : Slot 3) → position f (face f i) ≡ i
position-face c0 first = refl
position-face c0 (next first) = refl
position-face c0 (next (next first)) = refl
position-face c0 (next (next (next ())))
position-face m0 first = refl
position-face m0 (next first) = refl
position-face m0 (next (next first)) = refl
position-face m0 (next (next (next ())))
position-face c1 first = refl
position-face c1 (next first) = refl
position-face c1 (next (next first)) = refl
position-face c1 (next (next (next ())))
position-face m1 first = refl
position-face m1 (next first) = refl
position-face m1 (next (next first)) = refl
position-face m1 (next (next (next ())))
face-injective : (f : Vertex) {i j : Slot 3} → face f i ≡ face f j → i ≡ j
face-injective f {i} {j} p = sym (position-face f i) ∙ cong (position f) p ∙ position-face f j
membership-prop : (v f : Vertex) → isProp (InFace v f)
membership-prop v f (i , p) (j , q) = Σ≡Prop (λ k → vertex-set (face f k) v) (face-injective f (p ∙ sym q))
facet-fiber-prop : (c : C.Chart) (v f : Vertex) → isProp (Σ (C.Permit c f) (λ _ → InFace v f))
facet-fiber-prop c v f = isPropΣ (isSetℕ _ _) (λ _ → membership-prop v f)
same-facet : (c : C.Chart) (v : Vertex) (p q : E.A.VertexPermit c v) → fst p ≡ fst q → p ≡ q
same-facet c v p q = Σ≡Prop (facet-fiber-prop c v)
facet-projection : (c : C.Chart) (v : Vertex) (p q : E.A.VertexPermit c v) → p ≡ q → fst p ≡ fst q
facet-projection c v p q = cong fst
canonical-0-1 : (p : E.A.VertexPermit C.q0 m0) → fst p ≡ c0 → p ≡ F.vp-0-1
canonical-0-1 p = same-facet C.q0 m0 p F.vp-0-1
canonical-0-2 : (p : E.A.VertexPermit C.q0 c1) → fst p ≡ c0 → p ≡ F.vp-0-2
canonical-0-2 p = same-facet C.q0 c1 p F.vp-0-2
canonical-0-3 : (p : E.A.VertexPermit C.q0 m1) → fst p ≡ c0 → p ≡ F.vp-0-3
canonical-0-3 p = same-facet C.q0 m1 p F.vp-0-3
canonical-1-0 : (p : E.A.VertexPermit C.q7 c0) → fst p ≡ m0 → p ≡ F.vp-1-0
canonical-1-0 p = same-facet C.q7 c0 p F.vp-1-0
canonical-1-2 : (p : E.A.VertexPermit C.q7 c1) → fst p ≡ m0 → p ≡ F.vp-1-2
canonical-1-2 p = same-facet C.q7 c1 p F.vp-1-2
canonical-1-3 : (p : E.A.VertexPermit C.q7 m1) → fst p ≡ m0 → p ≡ F.vp-1-3
canonical-1-3 p = same-facet C.q7 m1 p F.vp-1-3
canonical-2-0 : (p : E.A.VertexPermit C.q0 c0) → fst p ≡ c1 → p ≡ F.vp-2-0
canonical-2-0 p = same-facet C.q0 c0 p F.vp-2-0
canonical-2-1 : (p : E.A.VertexPermit C.q0 m0) → fst p ≡ c1 → p ≡ F.vp-2-1
canonical-2-1 p = same-facet C.q0 m0 p F.vp-2-1
canonical-2-3 : (p : E.A.VertexPermit C.q0 m1) → fst p ≡ c1 → p ≡ F.vp-2-3
canonical-2-3 p = same-facet C.q0 m1 p F.vp-2-3
canonical-3-0 : (p : E.A.VertexPermit C.q7 c0) → fst p ≡ m1 → p ≡ F.vp-3-0
canonical-3-0 p = same-facet C.q7 c0 p F.vp-3-0
canonical-3-1 : (p : E.A.VertexPermit C.q7 m0) → fst p ≡ m1 → p ≡ F.vp-3-1
canonical-3-1 p = same-facet C.q7 m0 p F.vp-3-1
canonical-3-2 : (p : E.A.VertexPermit C.q7 c1) → fst p ≡ m1 → p ≡ F.vp-3-2
canonical-3-2 p = same-facet C.q7 c1 p F.vp-3-2
