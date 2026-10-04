{-# OPTIONS --safe --cubical --guardedness #-}
module BarycentricWitnessPacket where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import TypedGeneratorLayers using (Layer1; module GeneratedPaths)

-- Nonempty faces of the abstract tetrahedron. These mark occurrences,
-- even when several underlying state values coincide.
data Face : Type where
  v0 v1 v2 v3 : Face
  e01 e02 e03 e12 e13 e23 : Face
  f012 f013 f023 f123 : Face
  t0123 : Face

-- Literal occurrence supports are consumed and checked by the geometry audit.
support : Face → List ℕ
support v0 = 0 ∷ []
support v1 = 1 ∷ []
support v2 = 2 ∷ []
support v3 = 3 ∷ []
support e01 = 0 ∷ 1 ∷ []
support e02 = 0 ∷ 2 ∷ []
support e03 = 0 ∷ 3 ∷ []
support e12 = 1 ∷ 2 ∷ []
support e13 = 1 ∷ 3 ∷ []
support e23 = 2 ∷ 3 ∷ []
support f012 = 0 ∷ 1 ∷ 2 ∷ []
support f013 = 0 ∷ 1 ∷ 3 ∷ []
support f023 = 0 ∷ 2 ∷ 3 ∷ []
support f123 = 1 ∷ 2 ∷ 3 ∷ []
support t0123 = 0 ∷ 1 ∷ 2 ∷ 3 ∷ []

module Packet {ℓ : Level} (S : Type ℓ)
  (G : (s : S) → Σ[ t ∈ S ] (s ≡ t)) (s : S) where
  module P = GeneratedPaths S G
  module A = P.At s
  open Layer1 P.L using (next; edge)

  -- The type of the witness attached to each abstract face.
  CellType : Face → Type ℓ
  CellType v0 = S
  CellType v1 = S
  CellType v2 = S
  CellType v3 = S
  CellType e01 = s ≡ next s
  CellType e02 = s ≡ next (next s)
  CellType e03 = s ≡ next (next (next s))
  CellType e12 = next s ≡ next (next s)
  CellType e13 = next s ≡ next (next (next s))
  CellType e23 = next (next s) ≡ next (next (next s))
  CellType f012 = A.O.Face012
  CellType f013 = A.O.Face013
  CellType f023 = A.O.Face023
  CellType f123 = A.O.Face123
  CellType t0123 = A.O.Tetrahedron A.face012 A.face123 A.face013 A.face023

  -- Actual terms from Layer 2, including its certified tetrahedral witness.
  cell : (f : Face) → CellType f
  cell v0 = s
  cell v1 = next s
  cell v2 = next (next s)
  cell v3 = next (next (next s))
  cell e01 = edge s
  cell e02 = edge s ∙ edge (next s)
  cell e03 = (edge s ∙ edge (next s)) ∙ edge (next (next s))
  cell e12 = edge (next s)
  cell e13 = edge (next s) ∙ edge (next (next s))
  cell e23 = edge (next (next s))
  cell f012 = A.face012
  cell f013 = A.face013
  cell f023 = A.face023
  cell f123 = A.face123
  cell t0123 = A.tetrahedron

  TypedValue : Type (ℓ-suc ℓ)
  TypedValue = Σ[ T ∈ Type ℓ ] T

  -- The face mark distinguishes occurrences sharing the same typed value.
  Vertex : Type (ℓ-suc ℓ)
  Vertex = Σ[ f ∈ Face ] TypedValue

  vertex : Face → Vertex
  vertex f = f , CellType f , cell f

  face-recovered : (f : Face) → fst (vertex f) ≡ f
  face-recovered f = refl

  type-recovered : (f : Face) → fst (snd (vertex f)) ≡ CellType f
  type-recovered f = refl

  value-recovered : (f : Face) → snd (snd (vertex f)) ≡ cell f
  value-recovered f = refl

-- A type, or even a type together with its term, does not identify a face.
module Example = Packet Bool (λ b → b , refl) false

same-type : Example.CellType v0 ≡ Example.CellType v1
same-type = refl
same-typed-value : snd (Example.vertex v0) ≡ snd (Example.vertex v1)
same-typed-value = refl

is-first : Face → Bool
is-first v0 = true
is-first v1 = false
is-first v2 = false
is-first v3 = false
is-first e01 = false
is-first e02 = false
is-first e03 = false
is-first e12 = false
is-first e13 = false
is-first e23 = false
is-first f012 = false
is-first f013 = false
is-first f023 = false
is-first f123 = false
is-first t0123 = false

no-type-decoder : (decode : Type → Face)
  → ((f : Face) → decode (Example.CellType f) ≡ f) → ⊥
no-type-decoder decode recover = true≢false
  (cong is-first (sym (recover v0) ∙ recover v1))

no-typed-value-decoder : (decode : Example.TypedValue → Face)
  → ((f : Face) → decode (snd (Example.vertex f)) ≡ f) → ⊥
no-typed-value-decoder decode recover = true≢false
  (cong is-first (sym (recover v0) ∙ recover v1))
