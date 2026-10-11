{-# OPTIONS --safe --cubical --guardedness #-}
module FourSimplexHorn where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; compEquiv; equivFun; invEq; secEq; retEq)
open import Cubical.Foundations.Isomorphism using (Iso; iso; isoToEquiv)
open import Cubical.Foundations.Path using (symIso; compPathlEquiv; PathP≃Path; PathP≡doubleCompPathʳ; Square→compPath)
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Foundations.GroupoidLaws using (lUnit; rUnit; assoc; rCancel)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorLayers using (Layer1)
import MarkedTetrahedronCoherence as Marked
import RetainedTetrahedralPackage as Retained

module Simplex {ℓ : Level} (A : Type ℓ) where
  module M = Marked.Tetrahedra A
  module R = Retained.Cells A

  -- A triangular square with its last side degenerate. This is a cubical
  -- presentation of a simplex, not the ordinary four-sided square boundary.
  Triangle : {x y z : A} → x ≡ y → y ≡ z → x ≡ z → Type ℓ
  Triangle {z = z} p q r = PathP (λ i → p i ≡ z) r q
  triangle-comparison-J : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ (p ∙ q ≡ r)
  triangle-comparison-J {x} {y} {z} p =
    J (λ y p → (q : y ≡ z) (r : x ≡ z) → Triangle p q r ≃ (p ∙ q ≡ r))
      (λ q r → compEquiv (isoToEquiv symIso) (compPathlEquiv (sym (lUnit q)))) p

  -- A second comparison built by pasting the dependent square to a double
  -- path composite, then normalizing its final reflexive edge.
  triangle-comparison-by-pasting : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ (p ∙ q ≡ r)
  triangle-comparison-by-pasting {x} {y} {z} p q r =
    compEquiv (pathToEquiv (PathP≡doubleCompPathʳ p r q refl))
      (compEquiv (pathToEquiv (cong (λ u → r ≡ u) normalize)) (isoToEquiv symIso))
    where
      normalize : p ∙∙ q ∙∙ refl ≡ p ∙ q
      normalize = doubleCompPath≡compPath p q refl
        ∙ sym (cong (p ∙_) (rUnit q))

  -- Retain the original J-based triangle bridge. Its sweep coherence is
  -- proved below; the exploratory pasting equivalence is a separate choice.
  triangle-comparison : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ (p ∙ q ≡ r)
  triangle-comparison = triangle-comparison-J

  -- A direct sweep of the triangle witness after composing with the initial
  -- segment of p. This is the boundary formula needed for comparison
  -- naturality across moving first vertices.
  triangle-sweep : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    (t : Triangle p q r) → (refl ∙ r) ≡ (p ∙ q)
  triangle-sweep p q r t i = (λ j → p (i ∧ j)) ∙ t i

  -- The reflexive case of J computes propositionally, not definitionally.
  -- After exposing that computation, the base coherence is the square
  -- expressing naturality of the inverse left-unit homotopy.
  triangle-comparison-J-sweep : {x y z : A}
    (p : x ≡ y) (q : y ≡ z) (r : x ≡ z) (t : Triangle p q r)
    → equivFun (triangle-comparison-J p q r) t
      ≡ sym (triangle-sweep p q r t) ∙ sym (lUnit r)
  triangle-comparison-J-sweep {x} {y} {z} = J
    (λ y p → (q : y ≡ z) (r : x ≡ z) (t : Triangle p q r)
      → equivFun (triangle-comparison-J p q r) t
        ≡ sym (triangle-sweep p q r t) ∙ sym (lUnit r))
    (λ q r t →
      cong (λ f → equivFun (f q r) t)
        (JRefl
          (λ y p → (q : y ≡ z) (r : x ≡ z) → Triangle p q r ≃ (p ∙ q ≡ r))
          (λ q r → compEquiv (isoToEquiv symIso) (compPathlEquiv (sym (lUnit q)))))
      ∙ Square→compPath (λ i j → lUnit (t (~ j)) (~ i)))

  triangle-comparison-sweep : {x y z : A}
    (p : x ≡ y) (q : y ≡ z) (r : x ≡ z) (t : Triangle p q r)
    → equivFun (triangle-comparison p q r) t
      ≡ sym (triangle-sweep p q r t) ∙ sym (lUnit r)
  triangle-comparison-sweep = triangle-comparison-J-sweep

  triangle-sweep-cancel : {x y z : A}
    (p : x ≡ y) (q : y ≡ z) (r : x ≡ z) (t : Triangle p q r)
    → triangle-sweep p q r t ∙ equivFun (triangle-comparison p q r) t
      ≡ sym (lUnit r)
  triangle-sweep-cancel p q r t =
    cong (s ∙_) (triangle-comparison-sweep p q r t)
    ∙ assoc s (sym s) (sym (lUnit r))
    ∙ cong (_∙ sym (lUnit r)) (rCancel s)
    ∙ sym (lUnit (sym (lUnit r)))
    where
      s = triangle-sweep p q r t

  module OnEdges {x0 x1 x2 x3 : A} (e : M.Edges x0 x1 x2 x3) where
    open M.Edges e
    record Surface : Type ℓ where
      constructor surface
      field
        a012 : Triangle e01 e12 e02
        a123 : Triangle e12 e23 e13
        a013 : Triangle e01 e13 e03
        a023 : Triangle e02 e23 e03
    Tetrahedron : Surface → Type ℓ
    Tetrahedron s = PathP
      (λ i → Triangle (Surface.a012 s i) e23 (Surface.a013 s i))
      (Surface.a023 s) (Surface.a123 s)

  record TrianglePackage : Type ℓ where
    constructor triangle-package
    field
      x y z : A
      xy : x ≡ y
      yz : y ≡ z
      xz : x ≡ z
      face : Triangle xy yz xz

  triangle-ab triangle-bc triangle-ac : TrianglePackage → R.EdgePackage
  triangle-ab (triangle-package a b c p q r f) = R.edge-package a b p
  triangle-bc (triangle-package a b c p q r f) = R.edge-package b c q
  triangle-ac (triangle-package a b c p q r f) = R.edge-package a c r

  -- Exact bridge to the earlier retained triangle representation, including
  -- endpoints and edges. A corresponding tetrahedron-level bridge is not
  -- assumed by the four-dimensional completion below.
  face-to-previous : TrianglePackage → R.FacePackage
  face-to-previous (triangle-package a b c p q r f) =
    R.face-package a b c p q r (equivFun (triangle-comparison p q r) f)
  face-from-previous : R.FacePackage → TrianglePackage
  face-from-previous (R.face-package a b c p q r f) =
    triangle-package a b c p q r (invEq (triangle-comparison p q r) f)
  previous-roundtrip : (f : R.FacePackage) → face-to-previous (face-from-previous f) ≡ f
  previous-roundtrip (R.face-package a b c p q r f) =
    cong (R.face-package a b c p q r) (secEq (triangle-comparison p q r) f)
  cubical-roundtrip : (f : TrianglePackage) → face-from-previous (face-to-previous f) ≡ f
  cubical-roundtrip (triangle-package a b c p q r f) =
    cong (triangle-package a b c p q r) (retEq (triangle-comparison p q r) f)
  triangle-package-iso : Iso TrianglePackage R.FacePackage
  triangle-package-iso = iso face-to-previous face-from-previous previous-roundtrip cubical-roundtrip

  record TetraPackage : Type ℓ where
    constructor tetra-package
    field
      vertices : R.Vertices
      edges : M.Edges (R.Vertices.v0 vertices) (R.Vertices.v1 vertices)
        (R.Vertices.v2 vertices) (R.Vertices.v3 vertices)
      surface : OnEdges.Surface edges
      filler : OnEdges.Tetrahedron edges surface

  face012 face123 face013 face023 : TetraPackage → TrianglePackage
  face012 (tetra-package (R.vertices a b c d) e s t) =
    triangle-package a b c (M.Edges.e01 e) (M.Edges.e12 e) (M.Edges.e02 e) (OnEdges.Surface.a012 s)
  face123 (tetra-package (R.vertices a b c d) e s t) =
    triangle-package b c d (M.Edges.e12 e) (M.Edges.e23 e) (M.Edges.e13 e) (OnEdges.Surface.a123 s)
  face013 (tetra-package (R.vertices a b c d) e s t) =
    triangle-package a b d (M.Edges.e01 e) (M.Edges.e13 e) (M.Edges.e03 e) (OnEdges.Surface.a013 s)
  face023 (tetra-package (R.vertices a b c d) e s t) =
    triangle-package a c d (M.Edges.e02 e) (M.Edges.e23 e) (M.Edges.e03 e) (OnEdges.Surface.a023 s)

  record Vertices : Type ℓ where
    constructor vertices
    field x0 x1 x2 x3 x4 : A
  module At (v : Vertices) where
    open Vertices v
    record Edges : Type ℓ where
      field
        e01 : x0 ≡ x1
        e02 : x0 ≡ x2
        e03 : x0 ≡ x3
        e04 : x0 ≡ x4
        e12 : x1 ≡ x2
        e13 : x1 ≡ x3
        e14 : x1 ≡ x4
        e23 : x2 ≡ x3
        e24 : x2 ≡ x4
        e34 : x3 ≡ x4

    module WithEdges (e : Edges) where
      open Edges e
      record Faces : Type ℓ where
        field
          a012 : Triangle e01 e12 e02
          a013 : Triangle e01 e13 e03
          a014 : Triangle e01 e14 e04
          a023 : Triangle e02 e23 e03
          a024 : Triangle e02 e24 e04
          a034 : Triangle e03 e34 e04
          a123 : Triangle e12 e23 e13
          a124 : Triangle e12 e24 e14
          a134 : Triangle e13 e34 e14
          a234 : Triangle e23 e34 e24

      edges0123 : M.Edges x0 x1 x2 x3
      edges0123 = record { e01 = e01 ; e12 = e12 ; e02 = e02 ; e23 = e23 ; e13 = e13 ; e03 = e03 }
      edges0124 : M.Edges x0 x1 x2 x4
      edges0124 = record { e01 = e01 ; e12 = e12 ; e02 = e02 ; e23 = e24 ; e13 = e14 ; e03 = e04 }
      edges0134 : M.Edges x0 x1 x3 x4
      edges0134 = record { e01 = e01 ; e12 = e13 ; e02 = e03 ; e23 = e34 ; e13 = e14 ; e03 = e04 }
      edges0234 : M.Edges x0 x2 x3 x4
      edges0234 = record { e01 = e02 ; e12 = e23 ; e02 = e03 ; e23 = e34 ; e13 = e24 ; e03 = e04 }
      edges1234 : M.Edges x1 x2 x3 x4
      edges1234 = record { e01 = e12 ; e12 = e23 ; e02 = e13 ; e23 = e34 ; e13 = e24 ; e03 = e14 }

      module WithFaces (a : Faces) where
        open Faces a
        s0123 : OnEdges.Surface edges0123
        s0123 = OnEdges.surface a012 a123 a013 a023
        s0124 : OnEdges.Surface edges0124
        s0124 = OnEdges.surface a012 a124 a014 a024
        s0134 : OnEdges.Surface edges0134
        s0134 = OnEdges.surface a013 a134 a014 a034
        s0234 : OnEdges.Surface edges0234
        s0234 = OnEdges.surface a023 a234 a024 a034
        s1234 : OnEdges.Surface edges1234
        s1234 = OnEdges.surface a123 a234 a124 a134
        T0123 = OnEdges.Tetrahedron edges0123 s0123
        T0124 = OnEdges.Tetrahedron edges0124 s0124
        T0134 = OnEdges.Tetrahedron edges0134 s0134
        T0234 = OnEdges.Tetrahedron edges0234 s0234
        T1234 = OnEdges.Tetrahedron edges1234 s1234

        -- Outer horn opposite vertex 0. All ten edges and ten faces are
        -- already fixed, as are the four supplied tetrahedral cells.
        record Horn : Type ℓ where
          constructor horn
          field
            t0123 : T0123
            t0124 : T0124
            t0134 : T0134
            t0234 : T0234

        Family : Horn → I → Type ℓ
        Family h i = PathP
          (λ j → Triangle (Horn.t0123 h i j) e34 (Horn.t0124 h i j))
          (Horn.t0134 h i) a234
        family-start : (h : Horn) → Family h i0 ≡ T0234
        family-start h = refl
        family-end : (h : Horn) → Family h i1 ≡ T1234
        family-end h = refl
        FourCell : (h : Horn) → T1234 → Type ℓ
        FourCell h t = PathP (Family h) (Horn.t0234 h) t
        fixed-face-gate : (h : Horn) (t : T1234)
          → FourCell h t ≃ (transport (λ i → Family h i) (Horn.t0234 h) ≡ t)
        fixed-face-gate h t = PathP≃Path (Family h) (Horn.t0234 h) t
        incompatible-fixed-face : (h : Horn) (t : T1234)
          → ((transport (λ i → Family h i) (Horn.t0234 h) ≡ t) → ⊥) → FourCell h t → ⊥
        incompatible-fixed-face h t neq fill = neq (equivFun (fixed-face-gate h t) fill)
        Missing : Horn → Type ℓ
        Missing h = Σ[ t ∈ T1234 ] FourCell h t
        unique : (h : Horn) → isContr (Missing h)
        unique h = isContrSinglP (Family h) (Horn.t0234 h)

        Filled : Type ℓ
        Filled = Σ[ h ∈ Horn ] Missing h
        complete : Horn → Filled
        complete h = h , fst (unique h)
        forget : Filled → Horn
        forget = fst
        horn-recovered : (h : Horn) → forget (complete h) ≡ h
        horn-recovered h = refl
        package-recovered : (p : Filled) → complete (forget p) ≡ p
        package-recovered (h , t) i = h , snd (unique h) t i
        horn-fixed : (p : Filled) → cong forget (package-recovered p) ≡ refl
        horn-fixed p = refl
        completion-iso : Iso Horn Filled
        completion-iso = iso complete forget package-recovered horn-recovered

        -- All five tetrahedral faces of the four-cell are boundary equations.
        boundary0234 : (p : Filled) → (λ j k l → snd (snd p) i0 j k l) ≡ Horn.t0234 (fst p)
        boundary0234 p = refl
        boundary1234 : (p : Filled) → (λ j k l → snd (snd p) i1 j k l) ≡ fst (snd p)
        boundary1234 p = refl
        boundary0134 : (p : Filled) → (λ i k l → snd (snd p) i i0 k l) ≡ Horn.t0134 (fst p)
        boundary0134 p = refl
        boundary0124 : (p : Filled) → (λ i j l → snd (snd p) i j i0 l) ≡ Horn.t0124 (fst p)
        boundary0124 p = refl
        boundary0123 : (p : Filled) → (λ i j k → snd (snd p) i j k i0) ≡ Horn.t0123 (fst p)
        boundary0123 p = refl
        -- The other cubical sides are the collapsed lower-dimensional sides.
        collapsed234 : (p : Filled) → (λ i k l → snd (snd p) i i1 k l) ≡ (λ (i k l : I) → a234 k l)
        collapsed234 p = refl
        collapsed34 : (p : Filled) → (λ i j l → snd (snd p) i j i1 l) ≡ (λ (i j l : I) → e34 l)
        collapsed34 p = refl
        collapsed4 : (p : Filled) → (λ i j k → snd (snd p) i j k i1) ≡ (λ (i j k : I) → x4)
        collapsed4 p = refl

        p0123 p0124 p0134 p0234 p1234 : Filled → TetraPackage
        p0123 p = tetra-package (R.vertices x0 x1 x2 x3) edges0123 s0123 (Horn.t0123 (fst p))
        p0124 p = tetra-package (R.vertices x0 x1 x2 x4) edges0124 s0124 (Horn.t0124 (fst p))
        p0134 p = tetra-package (R.vertices x0 x1 x3 x4) edges0134 s0134 (Horn.t0134 (fst p))
        p0234 p = tetra-package (R.vertices x0 x2 x3 x4) edges0234 s0234 (Horn.t0234 (fst p))
        p1234 p = tetra-package (R.vertices x1 x2 x3 x4) edges1234 s1234 (fst (snd p))

        shared012 : (p : Filled) → face012 (p0123 p) ≡ face012 (p0124 p)
        shared012 p = refl
        shared013 : (p : Filled) → face013 (p0123 p) ≡ face012 (p0134 p)
        shared013 p = refl
        shared023 : (p : Filled) → face023 (p0123 p) ≡ face012 (p0234 p)
        shared023 p = refl
        shared123 : (p : Filled) → face123 (p0123 p) ≡ face012 (p1234 p)
        shared123 p = refl
        shared014 : (p : Filled) → face013 (p0124 p) ≡ face013 (p0134 p)
        shared014 p = refl
        shared024 : (p : Filled) → face023 (p0124 p) ≡ face013 (p0234 p)
        shared024 p = refl
        shared124 : (p : Filled) → face123 (p0124 p) ≡ face013 (p1234 p)
        shared124 p = refl
        shared034 : (p : Filled) → face023 (p0134 p) ≡ face023 (p0234 p)
        shared034 p = refl
        shared134 : (p : Filled) → face123 (p0134 p) ≡ face023 (p1234 p)
        shared134 p = refl
        shared234 : (p : Filled) → face123 (p0234 p) ≡ face123 (p1234 p)
        shared234 p = refl

  Request : Type ℓ
  Request = Σ[ v ∈ Vertices ] Σ[ e ∈ At.Edges v ] Σ[ a ∈ At.WithEdges.Faces v e ]
    At.WithEdges.WithFaces.Horn v e a
  Full : Type ℓ
  Full = Σ[ v ∈ Vertices ] Σ[ e ∈ At.Edges v ] Σ[ a ∈ At.WithEdges.Faces v e ]
    At.WithEdges.WithFaces.Filled v e a
  build : Request → Full
  build (v , e , a , h) = v , e , a , At.WithEdges.WithFaces.complete v e a h
  recover : Full → Request
  recover (v , e , a , p) = v , e , a , fst p
  recover-build : (q : Request) → recover (build q) ≡ q
  recover-build q = refl
  State = Request ⊎ Full
  data Witness : State → State → Type ℓ where
    completed : (q : Request) → Witness (inl q) (inr (build q))
    retained : (p : Full) → Witness (inr p) (inr p)
  generate : (x : State) → Σ[ y ∈ State ] Witness x y
  generate (inl q) = inr (build q) , completed q
  generate (inr p) = inr p , retained p
  WG : Layer1 ℓ
  WG = record { State = State ; Witness = Witness ; generate = generate }

-- A nonconstant type-and-term edge; higher faces are coherent cone cells.
module TypedFixture where
  module S = Simplex (Retained.TypedValue ℓ-zero)
  a b : Retained.TypedValue ℓ-zero
  a = Bool , false
  b = Bool , true
  p : a ≡ b
  p = Retained.TypedFixture.p
  v : S.Vertices
  v = S.vertices a b b b b
  e : S.At.Edges v
  e = record
    { e01 = p ; e02 = p ; e03 = p ; e04 = p
    ; e12 = refl ; e13 = refl ; e14 = refl ; e23 = refl ; e24 = refl ; e34 = refl }
  faces : S.At.WithEdges.Faces v e
  faces = record
    { a012 = λ i j → p (i ∨ j) ; a013 = λ i j → p (i ∨ j)
    ; a014 = λ i j → p (i ∨ j) ; a023 = λ i j → p (i ∨ j)
    ; a024 = λ i j → p (i ∨ j) ; a034 = λ i j → p (i ∨ j)
    ; a123 = refl ; a124 = refl ; a134 = refl ; a234 = refl }
  module H = S.At.WithEdges.WithFaces v e faces
  horn : H.Horn
  horn = H.horn (λ i j k → p (i ∨ j ∨ k)) (λ i j k → p (i ∨ j ∨ k))
    (λ i j k → p (i ∨ j ∨ k)) (λ i j k → p (i ∨ j ∨ k))
  explicit : H.Missing horn
  explicit = refl , λ i j k l → p (i ∨ j ∨ k ∨ l)
  generated : H.Filled
  generated = H.complete horn
  agrees-with-explicit : snd generated ≡ explicit
  agrees-with-explicit = snd (H.unique horn) explicit
  supplied-horn-fixed : fst generated ≡ horn
  supplied-horn-fixed = refl
  recovered-vertex : S.R.Vertices.v0 (S.TetraPackage.vertices (H.p1234 generated)) ≡ (Bool , true)
  recovered-vertex = refl
