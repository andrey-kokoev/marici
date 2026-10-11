{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedTetrahedralPackage where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism using (Iso; iso)
open import Cubical.Foundations.GroupoidLaws using (assoc)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1)
import MarkedTetrahedronCoherence as Marked
import MarkedTriangleCoherence as Triangle
open import GradedBoundaryCoherence using (marked-fillers-distinct)

-- This is the path-coherence specialization, not arbitrary WG relations.
module Cells {ℓ : Level} (A : Type ℓ) where
  module T = Marked.Tetrahedra A
  module Tri = Triangle.Triangles A
  record Vertices : Type ℓ where
    constructor vertices
    field v0 v1 v2 v3 : A
  open Vertices

  record EdgePackage : Type ℓ where
    constructor edge-package
    field
      source target : A
      witness : source ≡ target

  record FacePackage : Type ℓ where
    constructor face-package
    field
      a b c : A
      ab : a ≡ b
      bc : b ≡ c
      ac : a ≡ c
      triangle : Tri.Triangle ab bc ac
  edge-ab edge-bc edge-ac : FacePackage → EdgePackage
  edge-ab f = edge-package (FacePackage.a f) (FacePackage.b f) (FacePackage.ab f)
  edge-bc f = edge-package (FacePackage.b f) (FacePackage.c f) (FacePackage.bc f)
  edge-ac f = edge-package (FacePackage.a f) (FacePackage.c f) (FacePackage.ac f)

  module Over (v : Vertices) where
    Edges = T.Edges (v0 v) (v1 v) (v2 v) (v3 v)
    record Surface : Type ℓ where
      constructor surface
      field
        edges : Edges
        face012 : T.Over.Face012 edges
        face123 : T.Over.Face123 edges
        face013 : T.Over.Face013 edges
        face023 : T.Over.Face023 edges
    Filler : Surface → Type ℓ
    Filler s = T.Over.Tetrahedron (Surface.edges s)
      (Surface.face012 s) (Surface.face123 s) (Surface.face013 s) (Surface.face023 s)
    Package : Type ℓ
    Package = Σ[ s ∈ Surface ] Filler s

    recover-surface : Package → Surface
    recover-surface = fst
    recover-filler : (p : Package) → Filler (recover-surface p)
    recover-filler = snd
    reassemble : (p : Package) → (recover-surface p , recover-filler p) ≡ p
    reassemble p = refl

    f012 f123 f013 f023 : Surface → FacePackage
    f012 s = face-package (v0 v) (v1 v) (v2 v)
      (T.Edges.e01 (Surface.edges s)) (T.Edges.e12 (Surface.edges s))
      (T.Edges.e02 (Surface.edges s)) (Surface.face012 s)
    f123 s = face-package (v1 v) (v2 v) (v3 v)
      (T.Edges.e12 (Surface.edges s)) (T.Edges.e23 (Surface.edges s))
      (T.Edges.e13 (Surface.edges s)) (Surface.face123 s)
    f013 s = face-package (v0 v) (v1 v) (v3 v)
      (T.Edges.e01 (Surface.edges s)) (T.Edges.e13 (Surface.edges s))
      (T.Edges.e03 (Surface.edges s)) (Surface.face013 s)
    f023 s = face-package (v0 v) (v2 v) (v3 v)
      (T.Edges.e02 (Surface.edges s)) (T.Edges.e23 (Surface.edges s))
      (T.Edges.e03 (Surface.edges s)) (Surface.face023 s)

    -- Six shared-edge checks include endpoint data AND the actual path.
    shared01 : (s : Surface) → edge-ab (f012 s) ≡ edge-ab (f013 s)
    shared01 s = refl
    shared12 : (s : Surface) → edge-bc (f012 s) ≡ edge-ab (f123 s)
    shared12 s = refl
    shared02 : (s : Surface) → edge-ac (f012 s) ≡ edge-ab (f023 s)
    shared02 s = refl
    shared23 : (s : Surface) → edge-bc (f123 s) ≡ edge-bc (f023 s)
    shared23 s = refl
    shared13 : (s : Surface) → edge-ac (f123 s) ≡ edge-bc (f013 s)
    shared13 s = refl
    shared03 : (s : Surface) → edge-ac (f013 s) ≡ edge-ac (f023 s)
    shared03 s = refl

    record Horn : Type ℓ where
      constructor horn
      field
        edges : Edges
        face012 : T.Over.Face012 edges
        face123 : T.Over.Face123 edges
        face013 : T.Over.Face013 edges
    complete : Horn → Package
    complete (horn e a b c) = surface e a b c (fst filling) , snd filling
      where filling = fst (T.Over.unique023 e a b c)
    forget : Package → Horn
    forget (surface e a b c d , t) = horn e a b c
    forget-complete : (h : Horn) → forget (complete h) ≡ h
    forget-complete h = refl
    complete-forget : (p : Package) → complete (forget p) ≡ p
    complete-forget (surface e a b c d , t) =
      cong {B = λ _ → Package} (λ dt → surface e a b c (fst dt) , snd dt)
        (snd (T.Over.unique023 e a b c) (d , t))
    horn-iso : Iso Horn Package
    horn-iso = iso complete forget complete-forget forget-complete

    -- Completion preserves the marked input, not merely its diagonal.
    edges-preserved : (h : Horn) → Surface.edges (fst (complete h)) ≡ Horn.edges h
    edges-preserved h = refl
    faces-preserved : (h : Horn)
      → forget (complete h) ≡ h
    faces-preserved = forget-complete

  -- The unindexed carrier explicitly retains the vertices as well.
  Full : Type ℓ
  Full = Σ[ v ∈ Vertices ] Over.Package v
  data Vertex : Type where
    zero one two three : Vertex
  vertex : Full → Vertex → A
  vertex (v , p) zero = v0 v
  vertex (v , p) one = v1 v
  vertex (v , p) two = v2 v
  vertex (v , p) three = v3 v

  Request : Type ℓ
  Request = Σ[ v ∈ Vertices ] Over.Horn v
  build : Request → Full
  build (v , h) = v , Over.complete v h
  recover-request : Full → Request
  recover-request (v , p) = v , Over.forget v p
  request-recovered : (q : Request) → recover-request (build q) ≡ q
  request-recovered q = refl
  package-recovered : (p : Full) → build (recover-request p) ≡ p
  package-recovered (v , p) = cong (λ q → v , q) (Over.complete-forget v p)

  WGState : Type ℓ
  WGState = Request ⊎ Full
  data WGRelation : WGState → WGState → Type ℓ where
    completed : (q : Request) → WGRelation (inl q) (inr (build q))
    retained : (p : Full) → WGRelation (inr p) (inr p)
  generate : (s : WGState) → Σ[ t ∈ WGState ] WGRelation s t
  generate (inl q) = inr (build q) , completed q
  generate (inr p) = inr p , retained p
  WG : Layer1 ℓ
  WG = record { State = WGState ; Witness = WGRelation ; generate = generate }

-- A vertex may itself retain a type and an inhabitant. A bare Type-valued
-- vertex would retain a type ONLY and could not supply an arbitrary inhabitant.
TypedValue : (ℓ : Level) → Type (ℓ-suc ℓ)
TypedValue ℓ = Σ[ T ∈ Type ℓ ] T
module Typed (ℓ : Level) where
  module C = Cells (TypedValue ℓ)
  recover-type : C.Full → C.Vertex → Type ℓ
  recover-type p i = fst (C.vertex p i)
  recover-term : (p : C.Full) (i : C.Vertex) → recover-type p i
  recover-term p i = snd (C.vertex p i)

module TypedFixture where
  module C = Typed ℓ-zero
  open C.C
  v : Vertices
  v = vertices (Bool , false) (Bool , true) (Bool , false) (Bool , true)
  p : Path (TypedValue ℓ-zero) (Bool , false) (Bool , true)
  p = ΣPathP (ua notEquiv , toPathP (uaβ notEquiv false))
  e : T.Edges (Bool , false) (Bool , true) (Bool , false) (Bool , true)
  e = record
    { e01 = p ; e12 = sym p ; e02 = p ∙ sym p
    ; e23 = p ; e13 = sym p ∙ p ; e03 = (p ∙ sym p) ∙ p }
  request : Request
  request = v , Over.horn e refl refl (assoc p (sym p) p)
  result : Full
  result = build request
  recovered-type : C.recover-type result one ≡ Bool
  recovered-type = refl
  recovered-term : C.recover-term result one ≡ true
  recovered-term = refl
  via-face-edge : EdgePackage.target (edge-ab (Over.f012 v (fst (snd result)))) ≡ (Bool , true)
  via-face-edge = refl
  same-request : recover-request result ≡ request
  same-request = request-recovered request

-- Fixed marks are essential in this hostile: do not allow an equality of
-- complete packages to move the four vertices while comparing their edges.
module LossyDiagonal where
  module C = Cells (Type ℓ-zero)
  v : C.Vertices
  v = C.vertices Bool Bool Bool Bool
  module O = C.Over v
  from-marked : Marked.Types.MarkedTetrahedron Bool Bool Bool Bool → O.Package
  from-marked (e , (a , b , c) , (d , t)) = O.surface e a b c d , t
  ordinary twisted : O.Package
  ordinary = from-marked Marked.ordinary
  twisted = from-marked Marked.twisted
  first-edge : O.Package → Bool ≡ Bool
  first-edge p = Marked.Types.Edges.e01 (O.Surface.edges (fst p))
  diagonal : O.Package → Bool ≡ Bool
  diagonal p = Marked.Types.Edges.e03 (O.Surface.edges (fst p))
  same-diagonal : diagonal ordinary ≡ diagonal twisted
  same-diagonal = refl
  distinct : ordinary ≡ twisted → ⊥
  distinct p = marked-fillers-distinct (cong first-edge p)
  no-recovery : (decode : (Bool ≡ Bool) → O.Package)
    → ((p : O.Package) → decode (diagonal p) ≡ p) → ⊥
  no-recovery decode law = distinct (sym (law ordinary) ∙ law twisted)
