{-# OPTIONS --safe --cubical --guardedness #-}
module ThreeWitnessRetainedCone where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Foundations.GroupoidLaws using (assoc)
import RetainedTetrahedralPackage as Retained

-- The three witnesses need not have the same type. Each focused view keeps
-- the WHOLE input packet, including its already supplied face witness.
module Focus {ℓ : Level} (P A : Type ℓ) (select : P → A) where
  View : Type ℓ
  View = Σ[ p ∈ P ] Σ[ a ∈ A ] (a ≡ select p)

  decorate : P → View
  decorate p = p , select p , refl
  recover : View → P
  recover = fst
  recover-decorate : (p : P) → recover (decorate p) ≡ p
  recover-decorate p = refl
  decorate-recover : (v : View) → decorate (recover v) ≡ v
  decorate-recover (p , a , e) i = p , e (~ i) , (λ j → e ((~ i) ∨ j))
  viewEquiv : P ≃ View
  viewEquiv = isoToEquiv (iso decorate recover decorate-recover recover-decorate)

  pointed-path : (p : P) → Path (Retained.TypedValue ℓ)
    (P , p) (View , decorate p)
  pointed-path p = ΣPathP (ua viewEquiv , toPathP (uaβ viewEquiv p))

module Cone {ℓ : Level} (P A B C : Type ℓ)
  (first : P → A) (second : P → B) (third : P → C) where
  module V1 = Focus P A first
  module V2 = Focus P B second
  module V3 = Focus P C third
  module Cell = Retained.Cells (Retained.TypedValue ℓ)

  module At (p : P) where
    vertices : Cell.Vertices
    vertices = Cell.vertices (P , p) (V1.View , V1.decorate p)
      (V2.View , V2.decorate p) (V3.View , V3.decorate p)
    module O = Cell.Over vertices

    -- Pairwise witness comparisons are transported through the common packet.
    -- They compare lossless presentations, not bare heterogeneous witnesses.
    a = V1.pointed-path p
    b = sym (V1.pointed-path p) ∙ V2.pointed-path p
    c = sym (V2.pointed-path p) ∙ V3.pointed-path p

    edges : O.Edges
    edges = record { e01 = a ; e12 = b ; e02 = a ∙ b
                   ; e23 = c ; e13 = b ∙ c ; e03 = (a ∙ b) ∙ c }
    horn : O.Horn
    horn = O.horn edges refl refl (assoc a b c)

    -- Existing WG horn completion supplies the fourth face AND the interior.
    request : Cell.Request
    request = vertices , horn
    tetrahedron : Cell.Full
    tetrahedron = Cell.build request
    surface : O.Surface
    surface = fst (snd tetrahedron)
    interior : O.Filler surface
    interior = snd (snd tetrahedron)

    input-horn-retained : Cell.recover-request tetrahedron ≡ request
    input-horn-retained = Cell.request-recovered request
    input-edges-retained : O.Surface.edges surface ≡ edges
    input-edges-retained = refl
    apex-retains-packet : Cell.vertex tetrahedron Cell.zero ≡ (P , p)
    apex-retains-packet = refl

    -- All three views reconstruct the same complete packet, not only a scalar.
    first-recovers : V1.recover (V1.decorate p) ≡ p
    first-recovers = refl
    second-recovers : V2.recover (V2.decorate p) ≡ p
    second-recovers = refl
    third-recovers : V3.recover (V3.decorate p) ≡ p
    third-recovers = refl

-- A specialization where the original three inputs really are the edges of
-- a filled path triangle. The old face is an INPUT, not generated from counts.
module PathWitnessTriangle {ℓ : Level} (X : Type ℓ) (x y z : X) where
  record Packet : Type ℓ where
    constructor packet
    field
      ab : x ≡ y
      bc : y ≡ z
      ac : x ≡ z
      face : ab ∙ bc ≡ ac
  module Raised = Cone Packet (x ≡ y) (y ≡ z) (x ≡ z)
    Packet.ab Packet.bc Packet.ac

  original-face-recovered : (p : Packet)
    → Packet.face (Raised.V1.recover (Raised.V1.decorate p)) ≡ Packet.face p
  original-face-recovered p = refl
