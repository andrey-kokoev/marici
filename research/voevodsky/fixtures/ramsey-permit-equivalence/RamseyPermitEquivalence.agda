{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPermitEquivalence where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Empty as Empty
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)
open import RamseyUniformRelative using (first; next)
open import RamseyNativeEdgeAttachments using (InFace)
open import RamseyPermitFibers using (same-facet)
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
import RamseyFourFacetVertexCells as F
Tag : ℕ → Type
Tag zero = Unit
Tag (suc zero) = Unit
Tag (suc (suc n)) = ⊥
wrong-count : 1 ≡ 2 → ⊥
wrong-count p = transport (cong Tag p) tt
Is : Vertex → Vertex → Type
Is c0 c0 = Unit
Is c0 m0 = ⊥
Is c0 c1 = ⊥
Is c0 m1 = ⊥
Is m0 c0 = ⊥
Is m0 m0 = Unit
Is m0 c1 = ⊥
Is m0 m1 = ⊥
Is c1 c0 = ⊥
Is c1 m0 = ⊥
Is c1 c1 = Unit
Is c1 m1 = ⊥
Is m1 c0 = ⊥
Is m1 m0 = ⊥
Is m1 c1 = ⊥
Is m1 m1 = Unit
self-free : (v : Vertex) → InFace v v → ⊥
self-free c0 (first , p) = transport (cong (Is c0) (sym p)) tt
self-free c0 ((next first) , p) = transport (cong (Is c0) (sym p)) tt
self-free c0 ((next (next first)) , p) = transport (cong (Is c0) (sym p)) tt
self-free c0 (next (next (next ())) , p)
self-free m0 (first , p) = transport (cong (Is m0) (sym p)) tt
self-free m0 ((next first) , p) = transport (cong (Is m0) (sym p)) tt
self-free m0 ((next (next first)) , p) = transport (cong (Is m0) (sym p)) tt
self-free m0 (next (next (next ())) , p)
self-free c1 (first , p) = transport (cong (Is c1) (sym p)) tt
self-free c1 ((next first) , p) = transport (cong (Is c1) (sym p)) tt
self-free c1 ((next (next first)) , p) = transport (cong (Is c1) (sym p)) tt
self-free c1 (next (next (next ())) , p)
self-free m1 (first , p) = transport (cong (Is m1) (sym p)) tt
self-free m1 ((next first) , p) = transport (cong (Is m1) (sym p)) tt
self-free m1 ((next (next first)) , p) = transport (cong (Is m1) (sym p)) tt
self-free m1 (next (next (next ())) , p)
data Code-0-0 : Type where
  k0-0-2 : Code-0-0
decode-0-0 : Code-0-0 → E.A.VertexPermit C.q0 c0
decode-0-0 k0-0-2 = F.vp-2-0
encode-0-0 : E.A.VertexPermit C.q0 c0 → Code-0-0
encode-0-0 (c0 , (permit , member)) = Empty.rec (self-free c0 member)
encode-0-0 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-0-0 (c1 , (permit , member)) = k0-0-2
encode-0-0 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-decode-0-0 : (k : Code-0-0) → encode-0-0 (decode-0-0 k) ≡ k
encode-decode-0-0 k0-0-2 = refl
decode-encode-0-0 : (p : E.A.VertexPermit C.q0 c0) → decode-0-0 (encode-0-0 p) ≡ p
decode-encode-0-0 (c0 , (permit , member)) = Empty.rec (self-free c0 member)
decode-encode-0-0 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-0-0 (c1 , (permit , member)) = sym (same-facet C.q0 c0 (c1 , (permit , member)) F.vp-2-0 refl)
decode-encode-0-0 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
classification-0-0 : E.A.VertexPermit C.q0 c0 ≃ Code-0-0
classification-0-0 = isoToEquiv (iso encode-0-0 decode-0-0 encode-decode-0-0 decode-encode-0-0)
data Code-0-1 : Type where
  k0-1-0 k0-1-2 : Code-0-1
decode-0-1 : Code-0-1 → E.A.VertexPermit C.q0 m0
decode-0-1 k0-1-0 = F.vp-0-1
decode-0-1 k0-1-2 = F.vp-2-1
encode-0-1 : E.A.VertexPermit C.q0 m0 → Code-0-1
encode-0-1 (c0 , (permit , member)) = k0-1-0
encode-0-1 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-0-1 (c1 , (permit , member)) = k0-1-2
encode-0-1 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-decode-0-1 : (k : Code-0-1) → encode-0-1 (decode-0-1 k) ≡ k
encode-decode-0-1 k0-1-0 = refl
encode-decode-0-1 k0-1-2 = refl
decode-encode-0-1 : (p : E.A.VertexPermit C.q0 m0) → decode-0-1 (encode-0-1 p) ≡ p
decode-encode-0-1 (c0 , (permit , member)) = sym (same-facet C.q0 m0 (c0 , (permit , member)) F.vp-0-1 refl)
decode-encode-0-1 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-0-1 (c1 , (permit , member)) = sym (same-facet C.q0 m0 (c1 , (permit , member)) F.vp-2-1 refl)
decode-encode-0-1 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
classification-0-1 : E.A.VertexPermit C.q0 m0 ≃ Code-0-1
classification-0-1 = isoToEquiv (iso encode-0-1 decode-0-1 encode-decode-0-1 decode-encode-0-1)
data Code-0-2 : Type where
  k0-2-0 : Code-0-2
decode-0-2 : Code-0-2 → E.A.VertexPermit C.q0 c1
decode-0-2 k0-2-0 = F.vp-0-2
encode-0-2 : E.A.VertexPermit C.q0 c1 → Code-0-2
encode-0-2 (c0 , (permit , member)) = k0-2-0
encode-0-2 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-0-2 (c1 , (permit , member)) = Empty.rec (self-free c1 member)
encode-0-2 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-decode-0-2 : (k : Code-0-2) → encode-0-2 (decode-0-2 k) ≡ k
encode-decode-0-2 k0-2-0 = refl
decode-encode-0-2 : (p : E.A.VertexPermit C.q0 c1) → decode-0-2 (encode-0-2 p) ≡ p
decode-encode-0-2 (c0 , (permit , member)) = sym (same-facet C.q0 c1 (c0 , (permit , member)) F.vp-0-2 refl)
decode-encode-0-2 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-0-2 (c1 , (permit , member)) = Empty.rec (self-free c1 member)
decode-encode-0-2 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
classification-0-2 : E.A.VertexPermit C.q0 c1 ≃ Code-0-2
classification-0-2 = isoToEquiv (iso encode-0-2 decode-0-2 encode-decode-0-2 decode-encode-0-2)
data Code-0-3 : Type where
  k0-3-0 k0-3-2 : Code-0-3
decode-0-3 : Code-0-3 → E.A.VertexPermit C.q0 m1
decode-0-3 k0-3-0 = F.vp-0-3
decode-0-3 k0-3-2 = F.vp-2-3
encode-0-3 : E.A.VertexPermit C.q0 m1 → Code-0-3
encode-0-3 (c0 , (permit , member)) = k0-3-0
encode-0-3 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-0-3 (c1 , (permit , member)) = k0-3-2
encode-0-3 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-decode-0-3 : (k : Code-0-3) → encode-0-3 (decode-0-3 k) ≡ k
encode-decode-0-3 k0-3-0 = refl
encode-decode-0-3 k0-3-2 = refl
decode-encode-0-3 : (p : E.A.VertexPermit C.q0 m1) → decode-0-3 (encode-0-3 p) ≡ p
decode-encode-0-3 (c0 , (permit , member)) = sym (same-facet C.q0 m1 (c0 , (permit , member)) F.vp-0-3 refl)
decode-encode-0-3 (m0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-0-3 (c1 , (permit , member)) = sym (same-facet C.q0 m1 (c1 , (permit , member)) F.vp-2-3 refl)
decode-encode-0-3 (m1 , (permit , member)) = Empty.rec (wrong-count permit)
classification-0-3 : E.A.VertexPermit C.q0 m1 ≃ Code-0-3
classification-0-3 = isoToEquiv (iso encode-0-3 decode-0-3 encode-decode-0-3 decode-encode-0-3)
data Code-7-0 : Type where
  k7-0-1 k7-0-3 : Code-7-0
decode-7-0 : Code-7-0 → E.A.VertexPermit C.q7 c0
decode-7-0 k7-0-1 = F.vp-1-0
decode-7-0 k7-0-3 = F.vp-3-0
encode-7-0 : E.A.VertexPermit C.q7 c0 → Code-7-0
encode-7-0 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-0 (m0 , (permit , member)) = k7-0-1
encode-7-0 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-0 (m1 , (permit , member)) = k7-0-3
encode-decode-7-0 : (k : Code-7-0) → encode-7-0 (decode-7-0 k) ≡ k
encode-decode-7-0 k7-0-1 = refl
encode-decode-7-0 k7-0-3 = refl
decode-encode-7-0 : (p : E.A.VertexPermit C.q7 c0) → decode-7-0 (encode-7-0 p) ≡ p
decode-encode-7-0 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-0 (m0 , (permit , member)) = sym (same-facet C.q7 c0 (m0 , (permit , member)) F.vp-1-0 refl)
decode-encode-7-0 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-0 (m1 , (permit , member)) = sym (same-facet C.q7 c0 (m1 , (permit , member)) F.vp-3-0 refl)
classification-7-0 : E.A.VertexPermit C.q7 c0 ≃ Code-7-0
classification-7-0 = isoToEquiv (iso encode-7-0 decode-7-0 encode-decode-7-0 decode-encode-7-0)
data Code-7-1 : Type where
  k7-1-3 : Code-7-1
decode-7-1 : Code-7-1 → E.A.VertexPermit C.q7 m0
decode-7-1 k7-1-3 = F.vp-3-1
encode-7-1 : E.A.VertexPermit C.q7 m0 → Code-7-1
encode-7-1 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-1 (m0 , (permit , member)) = Empty.rec (self-free m0 member)
encode-7-1 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-1 (m1 , (permit , member)) = k7-1-3
encode-decode-7-1 : (k : Code-7-1) → encode-7-1 (decode-7-1 k) ≡ k
encode-decode-7-1 k7-1-3 = refl
decode-encode-7-1 : (p : E.A.VertexPermit C.q7 m0) → decode-7-1 (encode-7-1 p) ≡ p
decode-encode-7-1 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-1 (m0 , (permit , member)) = Empty.rec (self-free m0 member)
decode-encode-7-1 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-1 (m1 , (permit , member)) = sym (same-facet C.q7 m0 (m1 , (permit , member)) F.vp-3-1 refl)
classification-7-1 : E.A.VertexPermit C.q7 m0 ≃ Code-7-1
classification-7-1 = isoToEquiv (iso encode-7-1 decode-7-1 encode-decode-7-1 decode-encode-7-1)
data Code-7-2 : Type where
  k7-2-1 k7-2-3 : Code-7-2
decode-7-2 : Code-7-2 → E.A.VertexPermit C.q7 c1
decode-7-2 k7-2-1 = F.vp-1-2
decode-7-2 k7-2-3 = F.vp-3-2
encode-7-2 : E.A.VertexPermit C.q7 c1 → Code-7-2
encode-7-2 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-2 (m0 , (permit , member)) = k7-2-1
encode-7-2 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-2 (m1 , (permit , member)) = k7-2-3
encode-decode-7-2 : (k : Code-7-2) → encode-7-2 (decode-7-2 k) ≡ k
encode-decode-7-2 k7-2-1 = refl
encode-decode-7-2 k7-2-3 = refl
decode-encode-7-2 : (p : E.A.VertexPermit C.q7 c1) → decode-7-2 (encode-7-2 p) ≡ p
decode-encode-7-2 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-2 (m0 , (permit , member)) = sym (same-facet C.q7 c1 (m0 , (permit , member)) F.vp-1-2 refl)
decode-encode-7-2 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-2 (m1 , (permit , member)) = sym (same-facet C.q7 c1 (m1 , (permit , member)) F.vp-3-2 refl)
classification-7-2 : E.A.VertexPermit C.q7 c1 ≃ Code-7-2
classification-7-2 = isoToEquiv (iso encode-7-2 decode-7-2 encode-decode-7-2 decode-encode-7-2)
data Code-7-3 : Type where
  k7-3-1 : Code-7-3
decode-7-3 : Code-7-3 → E.A.VertexPermit C.q7 m1
decode-7-3 k7-3-1 = F.vp-1-3
encode-7-3 : E.A.VertexPermit C.q7 m1 → Code-7-3
encode-7-3 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-3 (m0 , (permit , member)) = k7-3-1
encode-7-3 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
encode-7-3 (m1 , (permit , member)) = Empty.rec (self-free m1 member)
encode-decode-7-3 : (k : Code-7-3) → encode-7-3 (decode-7-3 k) ≡ k
encode-decode-7-3 k7-3-1 = refl
decode-encode-7-3 : (p : E.A.VertexPermit C.q7 m1) → decode-7-3 (encode-7-3 p) ≡ p
decode-encode-7-3 (c0 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-3 (m0 , (permit , member)) = sym (same-facet C.q7 m1 (m0 , (permit , member)) F.vp-1-3 refl)
decode-encode-7-3 (c1 , (permit , member)) = Empty.rec (wrong-count permit)
decode-encode-7-3 (m1 , (permit , member)) = Empty.rec (self-free m1 member)
classification-7-3 : E.A.VertexPermit C.q7 m1 ≃ Code-7-3
classification-7-3 = isoToEquiv (iso encode-7-3 decode-7-3 encode-decode-7-3 decode-encode-7-3)
code-move-0-0 : Code-0-0 → Code-7-1
code-move-0-0 k0-0-2 = k7-1-3
move-0-0 : E.A.VertexPermit C.q0 c0 → E.A.VertexPermit C.q7 m0
move-0-0 p = decode-7-1 (code-move-0-0 (encode-0-0 p))
code-move-0-1 : Code-0-1 → Code-7-0
code-move-0-1 k0-1-0 = k7-0-1
code-move-0-1 k0-1-2 = k7-0-3
move-0-1 : E.A.VertexPermit C.q0 m0 → E.A.VertexPermit C.q7 c0
move-0-1 p = decode-7-0 (code-move-0-1 (encode-0-1 p))
code-move-0-2 : Code-0-2 → Code-7-3
code-move-0-2 k0-2-0 = k7-3-1
move-0-2 : E.A.VertexPermit C.q0 c1 → E.A.VertexPermit C.q7 m1
move-0-2 p = decode-7-3 (code-move-0-2 (encode-0-2 p))
code-move-0-3 : Code-0-3 → Code-7-2
code-move-0-3 k0-3-0 = k7-2-1
code-move-0-3 k0-3-2 = k7-2-3
move-0-3 : E.A.VertexPermit C.q0 m1 → E.A.VertexPermit C.q7 c1
move-0-3 p = decode-7-2 (code-move-0-3 (encode-0-3 p))
code-move-7-0 : Code-7-0 → Code-0-1
code-move-7-0 k7-0-1 = k0-1-0
code-move-7-0 k7-0-3 = k0-1-2
move-7-0 : E.A.VertexPermit C.q7 c0 → E.A.VertexPermit C.q0 m0
move-7-0 p = decode-0-1 (code-move-7-0 (encode-7-0 p))
code-move-7-1 : Code-7-1 → Code-0-0
code-move-7-1 k7-1-3 = k0-0-2
move-7-1 : E.A.VertexPermit C.q7 m0 → E.A.VertexPermit C.q0 c0
move-7-1 p = decode-0-0 (code-move-7-1 (encode-7-1 p))
code-move-7-2 : Code-7-2 → Code-0-3
code-move-7-2 k7-2-1 = k0-3-0
code-move-7-2 k7-2-3 = k0-3-2
move-7-2 : E.A.VertexPermit C.q7 c1 → E.A.VertexPermit C.q0 m1
move-7-2 p = decode-0-3 (code-move-7-2 (encode-7-2 p))
code-move-7-3 : Code-7-3 → Code-0-2
code-move-7-3 k7-3-1 = k0-2-0
move-7-3 : E.A.VertexPermit C.q7 m1 → E.A.VertexPermit C.q0 c1
move-7-3 p = decode-0-2 (code-move-7-3 (encode-7-3 p))
code-square-0-0 : (k : Code-0-0) → code-move-7-1 (code-move-0-0 k) ≡ k
code-square-0-0 k0-0-2 = refl
square-0-0 : (p : E.A.VertexPermit C.q0 c0) → move-7-1 (move-0-0 p) ≡ p
square-0-0 p = cong (λ k → decode-0-0 (code-move-7-1 k)) (encode-decode-7-1 (code-move-0-0 (encode-0-0 p))) ∙ cong decode-0-0 (code-square-0-0 (encode-0-0 p)) ∙ decode-encode-0-0 p
code-square-0-1 : (k : Code-0-1) → code-move-7-0 (code-move-0-1 k) ≡ k
code-square-0-1 k0-1-0 = refl
code-square-0-1 k0-1-2 = refl
square-0-1 : (p : E.A.VertexPermit C.q0 m0) → move-7-0 (move-0-1 p) ≡ p
square-0-1 p = cong (λ k → decode-0-1 (code-move-7-0 k)) (encode-decode-7-0 (code-move-0-1 (encode-0-1 p))) ∙ cong decode-0-1 (code-square-0-1 (encode-0-1 p)) ∙ decode-encode-0-1 p
code-square-0-2 : (k : Code-0-2) → code-move-7-3 (code-move-0-2 k) ≡ k
code-square-0-2 k0-2-0 = refl
square-0-2 : (p : E.A.VertexPermit C.q0 c1) → move-7-3 (move-0-2 p) ≡ p
square-0-2 p = cong (λ k → decode-0-2 (code-move-7-3 k)) (encode-decode-7-3 (code-move-0-2 (encode-0-2 p))) ∙ cong decode-0-2 (code-square-0-2 (encode-0-2 p)) ∙ decode-encode-0-2 p
code-square-0-3 : (k : Code-0-3) → code-move-7-2 (code-move-0-3 k) ≡ k
code-square-0-3 k0-3-0 = refl
code-square-0-3 k0-3-2 = refl
square-0-3 : (p : E.A.VertexPermit C.q0 m1) → move-7-2 (move-0-3 p) ≡ p
square-0-3 p = cong (λ k → decode-0-3 (code-move-7-2 k)) (encode-decode-7-2 (code-move-0-3 (encode-0-3 p))) ∙ cong decode-0-3 (code-square-0-3 (encode-0-3 p)) ∙ decode-encode-0-3 p
code-square-7-0 : (k : Code-7-0) → code-move-0-1 (code-move-7-0 k) ≡ k
code-square-7-0 k7-0-1 = refl
code-square-7-0 k7-0-3 = refl
square-7-0 : (p : E.A.VertexPermit C.q7 c0) → move-0-1 (move-7-0 p) ≡ p
square-7-0 p = cong (λ k → decode-7-0 (code-move-0-1 k)) (encode-decode-0-1 (code-move-7-0 (encode-7-0 p))) ∙ cong decode-7-0 (code-square-7-0 (encode-7-0 p)) ∙ decode-encode-7-0 p
code-square-7-1 : (k : Code-7-1) → code-move-0-0 (code-move-7-1 k) ≡ k
code-square-7-1 k7-1-3 = refl
square-7-1 : (p : E.A.VertexPermit C.q7 m0) → move-0-0 (move-7-1 p) ≡ p
square-7-1 p = cong (λ k → decode-7-1 (code-move-0-0 k)) (encode-decode-0-0 (code-move-7-1 (encode-7-1 p))) ∙ cong decode-7-1 (code-square-7-1 (encode-7-1 p)) ∙ decode-encode-7-1 p
code-square-7-2 : (k : Code-7-2) → code-move-0-3 (code-move-7-2 k) ≡ k
code-square-7-2 k7-2-1 = refl
code-square-7-2 k7-2-3 = refl
square-7-2 : (p : E.A.VertexPermit C.q7 c1) → move-0-3 (move-7-2 p) ≡ p
square-7-2 p = cong (λ k → decode-7-2 (code-move-0-3 k)) (encode-decode-0-3 (code-move-7-2 (encode-7-2 p))) ∙ cong decode-7-2 (code-square-7-2 (encode-7-2 p)) ∙ decode-encode-7-2 p
code-square-7-3 : (k : Code-7-3) → code-move-0-2 (code-move-7-3 k) ≡ k
code-square-7-3 k7-3-1 = refl
square-7-3 : (p : E.A.VertexPermit C.q7 m1) → move-0-2 (move-7-3 p) ≡ p
square-7-3 p = cong (λ k → decode-7-3 (code-move-0-2 k)) (encode-decode-0-2 (code-move-7-3 (encode-7-3 p))) ∙ cong decode-7-3 (code-square-7-3 (encode-7-3 p)) ∙ decode-encode-7-3 p
equiv-0-0 : E.A.VertexPermit C.q0 c0 ≃ E.A.VertexPermit C.q7 m0
equiv-0-0 = isoToEquiv (iso move-0-0 move-7-1 square-7-1 square-0-0)
canonical-2-0 : move-0-0 F.vp-2-0 ≡ F.vp-3-1
canonical-2-0 = refl
equiv-0-1 : E.A.VertexPermit C.q0 m0 ≃ E.A.VertexPermit C.q7 c0
equiv-0-1 = isoToEquiv (iso move-0-1 move-7-0 square-7-0 square-0-1)
canonical-0-1 : move-0-1 F.vp-0-1 ≡ F.vp-1-0
canonical-0-1 = refl
canonical-2-1 : move-0-1 F.vp-2-1 ≡ F.vp-3-0
canonical-2-1 = refl
equiv-0-2 : E.A.VertexPermit C.q0 c1 ≃ E.A.VertexPermit C.q7 m1
equiv-0-2 = isoToEquiv (iso move-0-2 move-7-3 square-7-3 square-0-2)
canonical-0-2 : move-0-2 F.vp-0-2 ≡ F.vp-1-3
canonical-0-2 = refl
equiv-0-3 : E.A.VertexPermit C.q0 m1 ≃ E.A.VertexPermit C.q7 c1
equiv-0-3 = isoToEquiv (iso move-0-3 move-7-2 square-7-2 square-0-3)
canonical-0-3 : move-0-3 F.vp-0-3 ≡ F.vp-1-2
canonical-0-3 = refl
canonical-2-3 : move-0-3 F.vp-2-3 ≡ F.vp-3-2
canonical-2-3 = refl
equiv-7-0 : E.A.VertexPermit C.q7 c0 ≃ E.A.VertexPermit C.q0 m0
equiv-7-0 = isoToEquiv (iso move-7-0 move-0-1 square-0-1 square-7-0)
canonical-1-0 : move-7-0 F.vp-1-0 ≡ F.vp-0-1
canonical-1-0 = refl
canonical-3-0 : move-7-0 F.vp-3-0 ≡ F.vp-2-1
canonical-3-0 = refl
equiv-7-1 : E.A.VertexPermit C.q7 m0 ≃ E.A.VertexPermit C.q0 c0
equiv-7-1 = isoToEquiv (iso move-7-1 move-0-0 square-0-0 square-7-1)
canonical-3-1 : move-7-1 F.vp-3-1 ≡ F.vp-2-0
canonical-3-1 = refl
equiv-7-2 : E.A.VertexPermit C.q7 c1 ≃ E.A.VertexPermit C.q0 m1
equiv-7-2 = isoToEquiv (iso move-7-2 move-0-3 square-0-3 square-7-2)
canonical-1-2 : move-7-2 F.vp-1-2 ≡ F.vp-0-3
canonical-1-2 = refl
canonical-3-2 : move-7-2 F.vp-3-2 ≡ F.vp-2-3
canonical-3-2 = refl
equiv-7-3 : E.A.VertexPermit C.q7 m1 ≃ E.A.VertexPermit C.q0 c1
equiv-7-3 = isoToEquiv (iso move-7-3 move-0-2 square-0-2 square-7-3)
canonical-1-3 : move-7-3 F.vp-1-3 ≡ F.vp-0-2
canonical-1-3 = refl
