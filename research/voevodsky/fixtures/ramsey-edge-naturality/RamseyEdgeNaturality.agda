{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEdgeNaturality where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Data.Nat.Properties using (isSetℕ)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Bool.Base using (false; true)
import Cubical.Data.Empty as Empty
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1)
open import RamseyNativeEdgeAttachments using (Edge; e01; e02; e03; e12; e13; e23; InFace; endpoint)
open import RamseyPermitFibers using (membership-prop)
import RamseyPermitEquivalence as M
import RamseyRequestedPortExamples as C
import RamseyEdgeAttachmentsExamples as E
edge-fiber-prop : (c : C.Chart) (e : Edge) (f : Vertex) → isProp (Σ (C.Permit c f) (λ _ → Σ (InFace (endpoint false e) f) (λ _ → InFace (endpoint true e) f)))
edge-fiber-prop c e f = isPropΣ (isSetℕ _ _) (λ _ → isPropΣ (membership-prop (endpoint false e) f) (λ _ → membership-prop (endpoint true e) f))
same-edge-facet : (c : C.Chart) (e : Edge) (p q : E.A.EdgePermit c e) → fst p ≡ fst q → p ≡ q
same-edge-facet c e p q = Σ≡Prop (edge-fiber-prop c e)
vertex-map : Vertex → Vertex
vertex-map c0 = m0
vertex-map m0 = c0
vertex-map c1 = m1
vertex-map m1 = c1
data Code-0-0 : Type where
  k0-0-2 : Code-0-0
decode-0-0 : Code-0-0 → E.A.EdgePermit C.q0 e01
decode-0-0 k0-0-2 = E.att-0-2-0
encode-0-0 : E.A.EdgePermit C.q0 e01 → Code-0-0
encode-0-0 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
encode-0-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-0-0 (c1 , (permit , (left , right))) = k0-0-2
encode-0-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-decode-0-0 : (k : Code-0-0) → encode-0-0 (decode-0-0 k) ≡ k
encode-decode-0-0 k0-0-2 = refl
decode-encode-0-0 : (p : E.A.EdgePermit C.q0 e01) → decode-0-0 (encode-0-0 p) ≡ p
decode-encode-0-0 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
decode-encode-0-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-0-0 (c1 , (permit , (left , right))) = sym (same-edge-facet C.q0 e01 (c1 , (permit , (left , right))) E.att-0-2-0 refl)
decode-encode-0-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
data Code-0-1 : Type where
decode-0-1 : Code-0-1 → E.A.EdgePermit C.q0 e02
decode-0-1 ()
encode-0-1 : E.A.EdgePermit C.q0 e02 → Code-0-1
encode-0-1 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
encode-0-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-0-1 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
encode-0-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-decode-0-1 : (k : Code-0-1) → encode-0-1 (decode-0-1 k) ≡ k
encode-decode-0-1 ()
decode-encode-0-1 : (p : E.A.EdgePermit C.q0 e02) → decode-0-1 (encode-0-1 p) ≡ p
decode-encode-0-1 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
decode-encode-0-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-0-1 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
decode-encode-0-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
data Code-0-2 : Type where
  k0-2-2 : Code-0-2
decode-0-2 : Code-0-2 → E.A.EdgePermit C.q0 e03
decode-0-2 k0-2-2 = E.att-0-2-2
encode-0-2 : E.A.EdgePermit C.q0 e03 → Code-0-2
encode-0-2 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
encode-0-2 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-0-2 (c1 , (permit , (left , right))) = k0-2-2
encode-0-2 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-decode-0-2 : (k : Code-0-2) → encode-0-2 (decode-0-2 k) ≡ k
encode-decode-0-2 k0-2-2 = refl
decode-encode-0-2 : (p : E.A.EdgePermit C.q0 e03) → decode-0-2 (encode-0-2 p) ≡ p
decode-encode-0-2 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
decode-encode-0-2 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-0-2 (c1 , (permit , (left , right))) = sym (same-edge-facet C.q0 e03 (c1 , (permit , (left , right))) E.att-0-2-2 refl)
decode-encode-0-2 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
data Code-0-3 : Type where
  k0-3-0 : Code-0-3
decode-0-3 : Code-0-3 → E.A.EdgePermit C.q0 e12
decode-0-3 k0-3-0 = E.att-0-0-3
encode-0-3 : E.A.EdgePermit C.q0 e12 → Code-0-3
encode-0-3 (c0 , (permit , (left , right))) = k0-3-0
encode-0-3 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-0-3 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
encode-0-3 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-decode-0-3 : (k : Code-0-3) → encode-0-3 (decode-0-3 k) ≡ k
encode-decode-0-3 k0-3-0 = refl
decode-encode-0-3 : (p : E.A.EdgePermit C.q0 e12) → decode-0-3 (encode-0-3 p) ≡ p
decode-encode-0-3 (c0 , (permit , (left , right))) = sym (same-edge-facet C.q0 e12 (c0 , (permit , (left , right))) E.att-0-0-3 refl)
decode-encode-0-3 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-0-3 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
decode-encode-0-3 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
data Code-0-4 : Type where
  k0-4-0 k0-4-2 : Code-0-4
decode-0-4 : Code-0-4 → E.A.EdgePermit C.q0 e13
decode-0-4 k0-4-0 = E.att-0-0-4
decode-0-4 k0-4-2 = E.att-0-2-4
encode-0-4 : E.A.EdgePermit C.q0 e13 → Code-0-4
encode-0-4 (c0 , (permit , (left , right))) = k0-4-0
encode-0-4 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-0-4 (c1 , (permit , (left , right))) = k0-4-2
encode-0-4 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-decode-0-4 : (k : Code-0-4) → encode-0-4 (decode-0-4 k) ≡ k
encode-decode-0-4 k0-4-0 = refl
encode-decode-0-4 k0-4-2 = refl
decode-encode-0-4 : (p : E.A.EdgePermit C.q0 e13) → decode-0-4 (encode-0-4 p) ≡ p
decode-encode-0-4 (c0 , (permit , (left , right))) = sym (same-edge-facet C.q0 e13 (c0 , (permit , (left , right))) E.att-0-0-4 refl)
decode-encode-0-4 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-0-4 (c1 , (permit , (left , right))) = sym (same-edge-facet C.q0 e13 (c1 , (permit , (left , right))) E.att-0-2-4 refl)
decode-encode-0-4 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
data Code-0-5 : Type where
  k0-5-0 : Code-0-5
decode-0-5 : Code-0-5 → E.A.EdgePermit C.q0 e23
decode-0-5 k0-5-0 = E.att-0-0-5
encode-0-5 : E.A.EdgePermit C.q0 e23 → Code-0-5
encode-0-5 (c0 , (permit , (left , right))) = k0-5-0
encode-0-5 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-0-5 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 left)
encode-0-5 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-decode-0-5 : (k : Code-0-5) → encode-0-5 (decode-0-5 k) ≡ k
encode-decode-0-5 k0-5-0 = refl
decode-encode-0-5 : (p : E.A.EdgePermit C.q0 e23) → decode-0-5 (encode-0-5 p) ≡ p
decode-encode-0-5 (c0 , (permit , (left , right))) = sym (same-edge-facet C.q0 e23 (c0 , (permit , (left , right))) E.att-0-0-5 refl)
decode-encode-0-5 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-0-5 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 left)
decode-encode-0-5 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
data Code-7-0 : Type where
  k7-0-3 : Code-7-0
decode-7-0 : Code-7-0 → E.A.EdgePermit C.q7 e01
decode-7-0 k7-0-3 = E.att-7-3-0
encode-7-0 : E.A.EdgePermit C.q7 e01 → Code-7-0
encode-7-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-0 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 right)
encode-7-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-0 (m1 , (permit , (left , right))) = k7-0-3
encode-decode-7-0 : (k : Code-7-0) → encode-7-0 (decode-7-0 k) ≡ k
encode-decode-7-0 k7-0-3 = refl
decode-encode-7-0 : (p : E.A.EdgePermit C.q7 e01) → decode-7-0 (encode-7-0 p) ≡ p
decode-encode-7-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-0 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 right)
decode-encode-7-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-0 (m1 , (permit , (left , right))) = sym (same-edge-facet C.q7 e01 (m1 , (permit , (left , right))) E.att-7-3-0 refl)
data Code-7-1 : Type where
  k7-1-1 k7-1-3 : Code-7-1
decode-7-1 : Code-7-1 → E.A.EdgePermit C.q7 e02
decode-7-1 k7-1-1 = E.att-7-1-1
decode-7-1 k7-1-3 = E.att-7-3-1
encode-7-1 : E.A.EdgePermit C.q7 e02 → Code-7-1
encode-7-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-1 (m0 , (permit , (left , right))) = k7-1-1
encode-7-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-1 (m1 , (permit , (left , right))) = k7-1-3
encode-decode-7-1 : (k : Code-7-1) → encode-7-1 (decode-7-1 k) ≡ k
encode-decode-7-1 k7-1-1 = refl
encode-decode-7-1 k7-1-3 = refl
decode-encode-7-1 : (p : E.A.EdgePermit C.q7 e02) → decode-7-1 (encode-7-1 p) ≡ p
decode-encode-7-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-1 (m0 , (permit , (left , right))) = sym (same-edge-facet C.q7 e02 (m0 , (permit , (left , right))) E.att-7-1-1 refl)
decode-encode-7-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-1 (m1 , (permit , (left , right))) = sym (same-edge-facet C.q7 e02 (m1 , (permit , (left , right))) E.att-7-3-1 refl)
data Code-7-2 : Type where
  k7-2-1 : Code-7-2
decode-7-2 : Code-7-2 → E.A.EdgePermit C.q7 e03
decode-7-2 k7-2-1 = E.att-7-1-2
encode-7-2 : E.A.EdgePermit C.q7 e03 → Code-7-2
encode-7-2 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-2 (m0 , (permit , (left , right))) = k7-2-1
encode-7-2 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-2 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
encode-decode-7-2 : (k : Code-7-2) → encode-7-2 (decode-7-2 k) ≡ k
encode-decode-7-2 k7-2-1 = refl
decode-encode-7-2 : (p : E.A.EdgePermit C.q7 e03) → decode-7-2 (encode-7-2 p) ≡ p
decode-encode-7-2 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-2 (m0 , (permit , (left , right))) = sym (same-edge-facet C.q7 e03 (m0 , (permit , (left , right))) E.att-7-1-2 refl)
decode-encode-7-2 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-2 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
data Code-7-3 : Type where
  k7-3-3 : Code-7-3
decode-7-3 : Code-7-3 → E.A.EdgePermit C.q7 e12
decode-7-3 k7-3-3 = E.att-7-3-3
encode-7-3 : E.A.EdgePermit C.q7 e12 → Code-7-3
encode-7-3 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-3 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
encode-7-3 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-3 (m1 , (permit , (left , right))) = k7-3-3
encode-decode-7-3 : (k : Code-7-3) → encode-7-3 (decode-7-3 k) ≡ k
encode-decode-7-3 k7-3-3 = refl
decode-encode-7-3 : (p : E.A.EdgePermit C.q7 e12) → decode-7-3 (encode-7-3 p) ≡ p
decode-encode-7-3 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-3 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
decode-encode-7-3 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-3 (m1 , (permit , (left , right))) = sym (same-edge-facet C.q7 e12 (m1 , (permit , (left , right))) E.att-7-3-3 refl)
data Code-7-4 : Type where
decode-7-4 : Code-7-4 → E.A.EdgePermit C.q7 e13
decode-7-4 ()
encode-7-4 : E.A.EdgePermit C.q7 e13 → Code-7-4
encode-7-4 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-4 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
encode-7-4 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-4 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
encode-decode-7-4 : (k : Code-7-4) → encode-7-4 (decode-7-4 k) ≡ k
encode-decode-7-4 ()
decode-encode-7-4 : (p : E.A.EdgePermit C.q7 e13) → decode-7-4 (encode-7-4 p) ≡ p
decode-encode-7-4 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-4 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
decode-encode-7-4 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-4 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
data Code-7-5 : Type where
  k7-5-1 : Code-7-5
decode-7-5 : Code-7-5 → E.A.EdgePermit C.q7 e23
decode-7-5 k7-5-1 = E.att-7-1-5
encode-7-5 : E.A.EdgePermit C.q7 e23 → Code-7-5
encode-7-5 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-5 (m0 , (permit , (left , right))) = k7-5-1
encode-7-5 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
encode-7-5 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
encode-decode-7-5 : (k : Code-7-5) → encode-7-5 (decode-7-5 k) ≡ k
encode-decode-7-5 k7-5-1 = refl
decode-encode-7-5 : (p : E.A.EdgePermit C.q7 e23) → decode-7-5 (encode-7-5 p) ≡ p
decode-encode-7-5 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-5 (m0 , (permit , (left , right))) = sym (same-edge-facet C.q7 e23 (m0 , (permit , (left , right))) E.att-7-1-5 refl)
decode-encode-7-5 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
decode-encode-7-5 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
code-move-0-0 : Code-0-0 → Code-7-0
code-move-0-0 k0-0-2 = k7-0-3
move-0-0 : E.A.EdgePermit C.q0 e01 → E.A.EdgePermit C.q7 e01
move-0-0 p = decode-7-0 (code-move-0-0 (encode-0-0 p))
code-move-0-1 : Code-0-1 → Code-7-4
code-move-0-1 ()
move-0-1 : E.A.EdgePermit C.q0 e02 → E.A.EdgePermit C.q7 e13
move-0-1 p = decode-7-4 (code-move-0-1 (encode-0-1 p))
code-move-0-2 : Code-0-2 → Code-7-3
code-move-0-2 k0-2-2 = k7-3-3
move-0-2 : E.A.EdgePermit C.q0 e03 → E.A.EdgePermit C.q7 e12
move-0-2 p = decode-7-3 (code-move-0-2 (encode-0-2 p))
code-move-0-3 : Code-0-3 → Code-7-2
code-move-0-3 k0-3-0 = k7-2-1
move-0-3 : E.A.EdgePermit C.q0 e12 → E.A.EdgePermit C.q7 e03
move-0-3 p = decode-7-2 (code-move-0-3 (encode-0-3 p))
code-move-0-4 : Code-0-4 → Code-7-1
code-move-0-4 k0-4-0 = k7-1-1
code-move-0-4 k0-4-2 = k7-1-3
move-0-4 : E.A.EdgePermit C.q0 e13 → E.A.EdgePermit C.q7 e02
move-0-4 p = decode-7-1 (code-move-0-4 (encode-0-4 p))
code-move-0-5 : Code-0-5 → Code-7-5
code-move-0-5 k0-5-0 = k7-5-1
move-0-5 : E.A.EdgePermit C.q0 e23 → E.A.EdgePermit C.q7 e23
move-0-5 p = decode-7-5 (code-move-0-5 (encode-0-5 p))
code-move-7-0 : Code-7-0 → Code-0-0
code-move-7-0 k7-0-3 = k0-0-2
move-7-0 : E.A.EdgePermit C.q7 e01 → E.A.EdgePermit C.q0 e01
move-7-0 p = decode-0-0 (code-move-7-0 (encode-7-0 p))
code-move-7-1 : Code-7-1 → Code-0-4
code-move-7-1 k7-1-1 = k0-4-0
code-move-7-1 k7-1-3 = k0-4-2
move-7-1 : E.A.EdgePermit C.q7 e02 → E.A.EdgePermit C.q0 e13
move-7-1 p = decode-0-4 (code-move-7-1 (encode-7-1 p))
code-move-7-2 : Code-7-2 → Code-0-3
code-move-7-2 k7-2-1 = k0-3-0
move-7-2 : E.A.EdgePermit C.q7 e03 → E.A.EdgePermit C.q0 e12
move-7-2 p = decode-0-3 (code-move-7-2 (encode-7-2 p))
code-move-7-3 : Code-7-3 → Code-0-2
code-move-7-3 k7-3-3 = k0-2-2
move-7-3 : E.A.EdgePermit C.q7 e12 → E.A.EdgePermit C.q0 e03
move-7-3 p = decode-0-2 (code-move-7-3 (encode-7-3 p))
code-move-7-4 : Code-7-4 → Code-0-1
code-move-7-4 ()
move-7-4 : E.A.EdgePermit C.q7 e13 → E.A.EdgePermit C.q0 e02
move-7-4 p = decode-0-1 (code-move-7-4 (encode-7-4 p))
code-move-7-5 : Code-7-5 → Code-0-5
code-move-7-5 k7-5-1 = k0-5-0
move-7-5 : E.A.EdgePermit C.q7 e23 → E.A.EdgePermit C.q0 e23
move-7-5 p = decode-0-5 (code-move-7-5 (encode-7-5 p))
code-square-0-0 : (k : Code-0-0) → code-move-7-0 (code-move-0-0 k) ≡ k
code-square-0-0 k0-0-2 = refl
square-0-0 : (p : E.A.EdgePermit C.q0 e01) → move-7-0 (move-0-0 p) ≡ p
square-0-0 p = cong (λ k → decode-0-0 (code-move-7-0 k)) (encode-decode-7-0 (code-move-0-0 (encode-0-0 p))) ∙ cong decode-0-0 (code-square-0-0 (encode-0-0 p)) ∙ decode-encode-0-0 p
code-square-0-1 : (k : Code-0-1) → code-move-7-4 (code-move-0-1 k) ≡ k
code-square-0-1 ()
square-0-1 : (p : E.A.EdgePermit C.q0 e02) → move-7-4 (move-0-1 p) ≡ p
square-0-1 p = cong (λ k → decode-0-1 (code-move-7-4 k)) (encode-decode-7-4 (code-move-0-1 (encode-0-1 p))) ∙ cong decode-0-1 (code-square-0-1 (encode-0-1 p)) ∙ decode-encode-0-1 p
code-square-0-2 : (k : Code-0-2) → code-move-7-3 (code-move-0-2 k) ≡ k
code-square-0-2 k0-2-2 = refl
square-0-2 : (p : E.A.EdgePermit C.q0 e03) → move-7-3 (move-0-2 p) ≡ p
square-0-2 p = cong (λ k → decode-0-2 (code-move-7-3 k)) (encode-decode-7-3 (code-move-0-2 (encode-0-2 p))) ∙ cong decode-0-2 (code-square-0-2 (encode-0-2 p)) ∙ decode-encode-0-2 p
code-square-0-3 : (k : Code-0-3) → code-move-7-2 (code-move-0-3 k) ≡ k
code-square-0-3 k0-3-0 = refl
square-0-3 : (p : E.A.EdgePermit C.q0 e12) → move-7-2 (move-0-3 p) ≡ p
square-0-3 p = cong (λ k → decode-0-3 (code-move-7-2 k)) (encode-decode-7-2 (code-move-0-3 (encode-0-3 p))) ∙ cong decode-0-3 (code-square-0-3 (encode-0-3 p)) ∙ decode-encode-0-3 p
code-square-0-4 : (k : Code-0-4) → code-move-7-1 (code-move-0-4 k) ≡ k
code-square-0-4 k0-4-0 = refl
code-square-0-4 k0-4-2 = refl
square-0-4 : (p : E.A.EdgePermit C.q0 e13) → move-7-1 (move-0-4 p) ≡ p
square-0-4 p = cong (λ k → decode-0-4 (code-move-7-1 k)) (encode-decode-7-1 (code-move-0-4 (encode-0-4 p))) ∙ cong decode-0-4 (code-square-0-4 (encode-0-4 p)) ∙ decode-encode-0-4 p
code-square-0-5 : (k : Code-0-5) → code-move-7-5 (code-move-0-5 k) ≡ k
code-square-0-5 k0-5-0 = refl
square-0-5 : (p : E.A.EdgePermit C.q0 e23) → move-7-5 (move-0-5 p) ≡ p
square-0-5 p = cong (λ k → decode-0-5 (code-move-7-5 k)) (encode-decode-7-5 (code-move-0-5 (encode-0-5 p))) ∙ cong decode-0-5 (code-square-0-5 (encode-0-5 p)) ∙ decode-encode-0-5 p
code-square-7-0 : (k : Code-7-0) → code-move-0-0 (code-move-7-0 k) ≡ k
code-square-7-0 k7-0-3 = refl
square-7-0 : (p : E.A.EdgePermit C.q7 e01) → move-0-0 (move-7-0 p) ≡ p
square-7-0 p = cong (λ k → decode-7-0 (code-move-0-0 k)) (encode-decode-0-0 (code-move-7-0 (encode-7-0 p))) ∙ cong decode-7-0 (code-square-7-0 (encode-7-0 p)) ∙ decode-encode-7-0 p
code-square-7-1 : (k : Code-7-1) → code-move-0-4 (code-move-7-1 k) ≡ k
code-square-7-1 k7-1-1 = refl
code-square-7-1 k7-1-3 = refl
square-7-1 : (p : E.A.EdgePermit C.q7 e02) → move-0-4 (move-7-1 p) ≡ p
square-7-1 p = cong (λ k → decode-7-1 (code-move-0-4 k)) (encode-decode-0-4 (code-move-7-1 (encode-7-1 p))) ∙ cong decode-7-1 (code-square-7-1 (encode-7-1 p)) ∙ decode-encode-7-1 p
code-square-7-2 : (k : Code-7-2) → code-move-0-3 (code-move-7-2 k) ≡ k
code-square-7-2 k7-2-1 = refl
square-7-2 : (p : E.A.EdgePermit C.q7 e03) → move-0-3 (move-7-2 p) ≡ p
square-7-2 p = cong (λ k → decode-7-2 (code-move-0-3 k)) (encode-decode-0-3 (code-move-7-2 (encode-7-2 p))) ∙ cong decode-7-2 (code-square-7-2 (encode-7-2 p)) ∙ decode-encode-7-2 p
code-square-7-3 : (k : Code-7-3) → code-move-0-2 (code-move-7-3 k) ≡ k
code-square-7-3 k7-3-3 = refl
square-7-3 : (p : E.A.EdgePermit C.q7 e12) → move-0-2 (move-7-3 p) ≡ p
square-7-3 p = cong (λ k → decode-7-3 (code-move-0-2 k)) (encode-decode-0-2 (code-move-7-3 (encode-7-3 p))) ∙ cong decode-7-3 (code-square-7-3 (encode-7-3 p)) ∙ decode-encode-7-3 p
code-square-7-4 : (k : Code-7-4) → code-move-0-1 (code-move-7-4 k) ≡ k
code-square-7-4 ()
square-7-4 : (p : E.A.EdgePermit C.q7 e13) → move-0-1 (move-7-4 p) ≡ p
square-7-4 p = cong (λ k → decode-7-4 (code-move-0-1 k)) (encode-decode-0-1 (code-move-7-4 (encode-7-4 p))) ∙ cong decode-7-4 (code-square-7-4 (encode-7-4 p)) ∙ decode-encode-7-4 p
code-square-7-5 : (k : Code-7-5) → code-move-0-5 (code-move-7-5 k) ≡ k
code-square-7-5 k7-5-1 = refl
square-7-5 : (p : E.A.EdgePermit C.q7 e23) → move-0-5 (move-7-5 p) ≡ p
square-7-5 p = cong (λ k → decode-7-5 (code-move-0-5 k)) (encode-decode-0-5 (code-move-7-5 (encode-7-5 p))) ∙ cong decode-7-5 (code-square-7-5 (encode-7-5 p)) ∙ decode-encode-7-5 p
equiv-0-0 : E.A.EdgePermit C.q0 e01 ≃ E.A.EdgePermit C.q7 e01
equiv-0-0 = isoToEquiv (iso move-0-0 move-7-0 square-7-0 square-0-0)
canonical-0-2-0 : move-0-0 E.att-0-2-0 ≡ E.att-7-3-0
canonical-0-2-0 = refl
restrict-0-0-0 : (p : E.A.EdgePermit C.q0 e01) → M.move-0-0 (E.A.restrict false C.q0 e01 p) ≡ E.A.restrict true C.q7 e01 (move-0-0 p)
restrict-0-0-0 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
restrict-0-0-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-0-0 (c1 , (permit , (left , right))) = refl
restrict-0-0-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-0-1 : (p : E.A.EdgePermit C.q0 e01) → M.move-0-1 (E.A.restrict true C.q0 e01 p) ≡ E.A.restrict false C.q7 e01 (move-0-0 p)
restrict-0-0-1 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
restrict-0-0-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-0-1 (c1 , (permit , (left , right))) = refl
restrict-0-0-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
equiv-0-1 : E.A.EdgePermit C.q0 e02 ≃ E.A.EdgePermit C.q7 e13
equiv-0-1 = isoToEquiv (iso move-0-1 move-7-4 square-7-4 square-0-1)
restrict-0-1-0 : (p : E.A.EdgePermit C.q0 e02) → M.move-0-0 (E.A.restrict false C.q0 e02 p) ≡ E.A.restrict false C.q7 e13 (move-0-1 p)
restrict-0-1-0 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
restrict-0-1-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-1-0 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
restrict-0-1-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-1-1 : (p : E.A.EdgePermit C.q0 e02) → M.move-0-2 (E.A.restrict true C.q0 e02 p) ≡ E.A.restrict true C.q7 e13 (move-0-1 p)
restrict-0-1-1 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
restrict-0-1-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-1-1 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
restrict-0-1-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
equiv-0-2 : E.A.EdgePermit C.q0 e03 ≃ E.A.EdgePermit C.q7 e12
equiv-0-2 = isoToEquiv (iso move-0-2 move-7-3 square-7-3 square-0-2)
canonical-0-2-2 : move-0-2 E.att-0-2-2 ≡ E.att-7-3-3
canonical-0-2-2 = refl
restrict-0-2-0 : (p : E.A.EdgePermit C.q0 e03) → M.move-0-0 (E.A.restrict false C.q0 e03 p) ≡ E.A.restrict false C.q7 e12 (move-0-2 p)
restrict-0-2-0 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
restrict-0-2-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-2-0 (c1 , (permit , (left , right))) = refl
restrict-0-2-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-2-1 : (p : E.A.EdgePermit C.q0 e03) → M.move-0-3 (E.A.restrict true C.q0 e03 p) ≡ E.A.restrict true C.q7 e12 (move-0-2 p)
restrict-0-2-1 (c0 , (permit , (left , right))) = Empty.rec (M.self-free c0 left)
restrict-0-2-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-2-1 (c1 , (permit , (left , right))) = refl
restrict-0-2-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
equiv-0-3 : E.A.EdgePermit C.q0 e12 ≃ E.A.EdgePermit C.q7 e03
equiv-0-3 = isoToEquiv (iso move-0-3 move-7-2 square-7-2 square-0-3)
canonical-0-0-3 : move-0-3 E.att-0-0-3 ≡ E.att-7-1-2
canonical-0-0-3 = refl
restrict-0-3-0 : (p : E.A.EdgePermit C.q0 e12) → M.move-0-1 (E.A.restrict false C.q0 e12 p) ≡ E.A.restrict false C.q7 e03 (move-0-3 p)
restrict-0-3-0 (c0 , (permit , (left , right))) = refl
restrict-0-3-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-3-0 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
restrict-0-3-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-3-1 : (p : E.A.EdgePermit C.q0 e12) → M.move-0-2 (E.A.restrict true C.q0 e12 p) ≡ E.A.restrict true C.q7 e03 (move-0-3 p)
restrict-0-3-1 (c0 , (permit , (left , right))) = refl
restrict-0-3-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-3-1 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 right)
restrict-0-3-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
equiv-0-4 : E.A.EdgePermit C.q0 e13 ≃ E.A.EdgePermit C.q7 e02
equiv-0-4 = isoToEquiv (iso move-0-4 move-7-1 square-7-1 square-0-4)
canonical-0-0-4 : move-0-4 E.att-0-0-4 ≡ E.att-7-1-1
canonical-0-0-4 = refl
canonical-0-2-4 : move-0-4 E.att-0-2-4 ≡ E.att-7-3-1
canonical-0-2-4 = refl
restrict-0-4-0 : (p : E.A.EdgePermit C.q0 e13) → M.move-0-1 (E.A.restrict false C.q0 e13 p) ≡ E.A.restrict false C.q7 e02 (move-0-4 p)
restrict-0-4-0 (c0 , (permit , (left , right))) = refl
restrict-0-4-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-4-0 (c1 , (permit , (left , right))) = refl
restrict-0-4-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-4-1 : (p : E.A.EdgePermit C.q0 e13) → M.move-0-3 (E.A.restrict true C.q0 e13 p) ≡ E.A.restrict true C.q7 e02 (move-0-4 p)
restrict-0-4-1 (c0 , (permit , (left , right))) = refl
restrict-0-4-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-4-1 (c1 , (permit , (left , right))) = refl
restrict-0-4-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
equiv-0-5 : E.A.EdgePermit C.q0 e23 ≃ E.A.EdgePermit C.q7 e23
equiv-0-5 = isoToEquiv (iso move-0-5 move-7-5 square-7-5 square-0-5)
canonical-0-0-5 : move-0-5 E.att-0-0-5 ≡ E.att-7-1-5
canonical-0-0-5 = refl
restrict-0-5-0 : (p : E.A.EdgePermit C.q0 e23) → M.move-0-2 (E.A.restrict false C.q0 e23 p) ≡ E.A.restrict true C.q7 e23 (move-0-5 p)
restrict-0-5-0 (c0 , (permit , (left , right))) = refl
restrict-0-5-0 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-5-0 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 left)
restrict-0-5-0 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-5-1 : (p : E.A.EdgePermit C.q0 e23) → M.move-0-3 (E.A.restrict true C.q0 e23 p) ≡ E.A.restrict false C.q7 e23 (move-0-5 p)
restrict-0-5-1 (c0 , (permit , (left , right))) = refl
restrict-0-5-1 (m0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-0-5-1 (c1 , (permit , (left , right))) = Empty.rec (M.self-free c1 left)
restrict-0-5-1 (m1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
equiv-7-0 : E.A.EdgePermit C.q7 e01 ≃ E.A.EdgePermit C.q0 e01
equiv-7-0 = isoToEquiv (iso move-7-0 move-0-0 square-0-0 square-7-0)
canonical-7-3-0 : move-7-0 E.att-7-3-0 ≡ E.att-0-2-0
canonical-7-3-0 = refl
restrict-7-0-0 : (p : E.A.EdgePermit C.q7 e01) → M.move-7-0 (E.A.restrict false C.q7 e01 p) ≡ E.A.restrict true C.q0 e01 (move-7-0 p)
restrict-7-0-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-0-0 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 right)
restrict-7-0-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-0-0 (m1 , (permit , (left , right))) = refl
restrict-7-0-1 : (p : E.A.EdgePermit C.q7 e01) → M.move-7-1 (E.A.restrict true C.q7 e01 p) ≡ E.A.restrict false C.q0 e01 (move-7-0 p)
restrict-7-0-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-0-1 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 right)
restrict-7-0-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-0-1 (m1 , (permit , (left , right))) = refl
equiv-7-1 : E.A.EdgePermit C.q7 e02 ≃ E.A.EdgePermit C.q0 e13
equiv-7-1 = isoToEquiv (iso move-7-1 move-0-4 square-0-4 square-7-1)
canonical-7-1-1 : move-7-1 E.att-7-1-1 ≡ E.att-0-0-4
canonical-7-1-1 = refl
canonical-7-3-1 : move-7-1 E.att-7-3-1 ≡ E.att-0-2-4
canonical-7-3-1 = refl
restrict-7-1-0 : (p : E.A.EdgePermit C.q7 e02) → M.move-7-0 (E.A.restrict false C.q7 e02 p) ≡ E.A.restrict false C.q0 e13 (move-7-1 p)
restrict-7-1-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-1-0 (m0 , (permit , (left , right))) = refl
restrict-7-1-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-1-0 (m1 , (permit , (left , right))) = refl
restrict-7-1-1 : (p : E.A.EdgePermit C.q7 e02) → M.move-7-2 (E.A.restrict true C.q7 e02 p) ≡ E.A.restrict true C.q0 e13 (move-7-1 p)
restrict-7-1-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-1-1 (m0 , (permit , (left , right))) = refl
restrict-7-1-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-1-1 (m1 , (permit , (left , right))) = refl
equiv-7-2 : E.A.EdgePermit C.q7 e03 ≃ E.A.EdgePermit C.q0 e12
equiv-7-2 = isoToEquiv (iso move-7-2 move-0-3 square-0-3 square-7-2)
canonical-7-1-2 : move-7-2 E.att-7-1-2 ≡ E.att-0-0-3
canonical-7-1-2 = refl
restrict-7-2-0 : (p : E.A.EdgePermit C.q7 e03) → M.move-7-0 (E.A.restrict false C.q7 e03 p) ≡ E.A.restrict false C.q0 e12 (move-7-2 p)
restrict-7-2-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-2-0 (m0 , (permit , (left , right))) = refl
restrict-7-2-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-2-0 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
restrict-7-2-1 : (p : E.A.EdgePermit C.q7 e03) → M.move-7-3 (E.A.restrict true C.q7 e03 p) ≡ E.A.restrict true C.q0 e12 (move-7-2 p)
restrict-7-2-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-2-1 (m0 , (permit , (left , right))) = refl
restrict-7-2-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-2-1 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
equiv-7-3 : E.A.EdgePermit C.q7 e12 ≃ E.A.EdgePermit C.q0 e03
equiv-7-3 = isoToEquiv (iso move-7-3 move-0-2 square-0-2 square-7-3)
canonical-7-3-3 : move-7-3 E.att-7-3-3 ≡ E.att-0-2-2
canonical-7-3-3 = refl
restrict-7-3-0 : (p : E.A.EdgePermit C.q7 e12) → M.move-7-1 (E.A.restrict false C.q7 e12 p) ≡ E.A.restrict false C.q0 e03 (move-7-3 p)
restrict-7-3-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-3-0 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
restrict-7-3-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-3-0 (m1 , (permit , (left , right))) = refl
restrict-7-3-1 : (p : E.A.EdgePermit C.q7 e12) → M.move-7-2 (E.A.restrict true C.q7 e12 p) ≡ E.A.restrict true C.q0 e03 (move-7-3 p)
restrict-7-3-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-3-1 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
restrict-7-3-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-3-1 (m1 , (permit , (left , right))) = refl
equiv-7-4 : E.A.EdgePermit C.q7 e13 ≃ E.A.EdgePermit C.q0 e02
equiv-7-4 = isoToEquiv (iso move-7-4 move-0-1 square-0-1 square-7-4)
restrict-7-4-0 : (p : E.A.EdgePermit C.q7 e13) → M.move-7-1 (E.A.restrict false C.q7 e13 p) ≡ E.A.restrict false C.q0 e02 (move-7-4 p)
restrict-7-4-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-4-0 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
restrict-7-4-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-4-0 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
restrict-7-4-1 : (p : E.A.EdgePermit C.q7 e13) → M.move-7-3 (E.A.restrict true C.q7 e13 p) ≡ E.A.restrict true C.q0 e02 (move-7-4 p)
restrict-7-4-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-4-1 (m0 , (permit , (left , right))) = Empty.rec (M.self-free m0 left)
restrict-7-4-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-4-1 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
equiv-7-5 : E.A.EdgePermit C.q7 e23 ≃ E.A.EdgePermit C.q0 e23
equiv-7-5 = isoToEquiv (iso move-7-5 move-0-5 square-0-5 square-7-5)
canonical-7-1-5 : move-7-5 E.att-7-1-5 ≡ E.att-0-0-5
canonical-7-1-5 = refl
restrict-7-5-0 : (p : E.A.EdgePermit C.q7 e23) → M.move-7-2 (E.A.restrict false C.q7 e23 p) ≡ E.A.restrict true C.q0 e23 (move-7-5 p)
restrict-7-5-0 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-5-0 (m0 , (permit , (left , right))) = refl
restrict-7-5-0 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-5-0 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
restrict-7-5-1 : (p : E.A.EdgePermit C.q7 e23) → M.move-7-3 (E.A.restrict true C.q7 e23 p) ≡ E.A.restrict false C.q0 e23 (move-7-5 p)
restrict-7-5-1 (c0 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-5-1 (m0 , (permit , (left , right))) = refl
restrict-7-5-1 (c1 , (permit , (left , right))) = Empty.rec (M.wrong-count permit)
restrict-7-5-1 (m1 , (permit , (left , right))) = Empty.rec (M.self-free m1 right)
endpoint-0-0 : vertex-map (endpoint false e01) ≡ endpoint true e01
endpoint-0-0 = refl
endpoint-0-1 : vertex-map (endpoint true e01) ≡ endpoint false e01
endpoint-0-1 = refl
endpoint-1-0 : vertex-map (endpoint false e02) ≡ endpoint false e13
endpoint-1-0 = refl
endpoint-1-1 : vertex-map (endpoint true e02) ≡ endpoint true e13
endpoint-1-1 = refl
endpoint-2-0 : vertex-map (endpoint false e03) ≡ endpoint false e12
endpoint-2-0 = refl
endpoint-2-1 : vertex-map (endpoint true e03) ≡ endpoint true e12
endpoint-2-1 = refl
endpoint-3-0 : vertex-map (endpoint false e12) ≡ endpoint false e03
endpoint-3-0 = refl
endpoint-3-1 : vertex-map (endpoint true e12) ≡ endpoint true e03
endpoint-3-1 = refl
endpoint-4-0 : vertex-map (endpoint false e13) ≡ endpoint false e02
endpoint-4-0 = refl
endpoint-4-1 : vertex-map (endpoint true e13) ≡ endpoint true e02
endpoint-4-1 = refl
endpoint-5-0 : vertex-map (endpoint false e23) ≡ endpoint true e23
endpoint-5-0 = refl
endpoint-5-1 : vertex-map (endpoint true e23) ≡ endpoint false e23
endpoint-5-1 = refl
