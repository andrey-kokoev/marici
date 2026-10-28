{-# OPTIONS --safe --cubical --guardedness #-}
module SourceActionObservationObstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; false; true; false≢true)
open import Cubical.Data.Empty using (⊥)
open import ActualSeedEndpointTable
open import SeedTetrahedronBridge using (Realization; node; edge)
import NativeExtensionFamilyAudit as N
import SourceGraphFreeRealization as G

-- Actual six-occurrence permutation, not a replacement filled source.
swap : Realization → Realization
swap (node A) = node B
swap (node B) = node A
swap (node C) = node D
swap (node D) = node C
swap (edge AB i) = edge BA i
swap (edge BC i) = edge AD i
swap (edge CA i) = edge DB i
swap (edge AD i) = edge BC i
swap (edge DB i) = edge CA i
swap (edge BA i) = edge AB i

swap² : (x : Realization) → swap (swap x) ≡ x
swap² (node A) = refl
swap² (node B) = refl
swap² (node C) = refl
swap² (node D) = refl
swap² (edge AB i) = refl
swap² (edge BC i) = refl
swap² (edge CA i) = refl
swap² (edge AD i) = refl
swap² (edge DB i) = refl
swap² (edge BA i) = refl

color : N.Vertex → Bool
color N.A = false
color N.B = true
color N.C = false
color N.D = true
no-fixed : (v : N.Vertex) → v ≡ N.sigma v → ⊥
no-fixed N.A p = false≢true (cong color p)
no-fixed N.B p = false≢true (sym (cong color p))
no-fixed N.C p = false≢true (cong color p)
no-fixed N.D p = false≢true (sym (cong color p))

-- Obstruction holds for ANY realization with the AB attachment path,
-- not just the selected free HIT or a particular native producer.
module AnyRealization {ℓ : Level} (X : Type ℓ) (points : Vertex → X)
  (ab : points A ≡ points B) where
  no-endpoint-decoder : (observe : X → N.Vertex)
    → ((v : Vertex) → observe (points v) ≡ G.nativeVertex v) → ⊥
  no-endpoint-decoder observe agrees = false≢true
    (cong color (sym (agrees A) ∙ cong observe ab ∙ agrees B))

  no-equivariant-decoder : (act : X → X) (on-A : act (points A) ≡ points B)
    (observe : X → N.Vertex)
    → ((x : X) → observe (act x) ≡ N.sigma (observe x)) → ⊥
  no-equivariant-decoder act on-A observe equivariant = no-fixed (observe (points A))
    (cong observe (ab ∙ sym on-A) ∙ equivariant (points A))

module Actual = AnyRealization Realization node (edge AB)

-- An involutive source action exists, but not the requested readout.
-- No endpoint-recovery assumption is needed for this stronger obstruction.
no-actual-equivariant-decoder : (observe : Realization → N.Vertex)
  → ((x : Realization) → observe (swap x) ≡ N.sigma (observe x)) → ⊥
no-actual-equivariant-decoder = Actual.no-equivariant-decoder swap refl
