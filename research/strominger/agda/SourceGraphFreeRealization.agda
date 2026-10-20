{-# OPTIONS --safe --cubical --guardedness #-}
module SourceGraphFreeRealization where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.GroupoidLaws using (cong-∙∙)
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.Bool using (Bool; false; true; false≢true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.Bouquet.Base
open import ActualSeedEndpointTable
open import SeedTetrahedronBridge using (Realization; node; edge)
import SeedFaceObstruction as Prior
import NativeExtensionFamilyAudit as N

-- Reuse the predecessor, and bind its occurrence table to the audited source.
nativeVertex : Vertex → N.Vertex
nativeVertex A = N.A
nativeVertex B = N.B
nativeVertex C = N.C
nativeVertex D = N.D
nativeEdge : (e : Occurrence) → N.Edge (nativeVertex (source e)) (nativeVertex (target e))
nativeEdge AB = N.AB
nativeEdge BC = N.BC
nativeEdge CA = N.CA
nativeEdge AD = N.AD
nativeEdge DB = N.DB
nativeEdge BA = N.BA
NativeOccurrence = Σ[ s ∈ N.Vertex ] Σ[ t ∈ N.Vertex ] N.Edge s t
intoNative : Occurrence → NativeOccurrence
intoNative e = nativeVertex (source e) , nativeVertex (target e) , nativeEdge e
outOfNative : NativeOccurrence → Occurrence
outOfNative (_ , _ , N.AB) = AB
outOfNative (_ , _ , N.BC) = BC
outOfNative (_ , _ , N.CA) = CA
outOfNative (_ , _ , N.AD) = AD
outOfNative (_ , _ , N.DB) = DB
outOfNative (_ , _ , N.BA) = BA
occurrence-section : (e : Occurrence) → outOfNative (intoNative e) ≡ e
occurrence-section AB = refl
occurrence-section BC = refl
occurrence-section CA = refl
occurrence-section AD = refl
occurrence-section DB = refl
occurrence-section BA = refl
occurrence-retract : (e : NativeOccurrence) → intoNative (outOfNative e) ≡ e
occurrence-retract (_ , _ , N.AB) = refl
occurrence-retract (_ , _ , N.BC) = refl
occurrence-retract (_ , _ , N.CA) = refl
occurrence-retract (_ , _ , N.AD) = refl
occurrence-retract (_ , _ , N.DB) = refl
occurrence-retract (_ , _ , N.BA) = refl
source-occurrence-equivalence : Occurrence ≃ NativeOccurrence
source-occurrence-equivalence = isoToEquiv
  (iso intoNative outOfNative occurrence-retract occurrence-section)

-- Exact mapping property of the DECLARED path interpretation, not a claim
-- that the original directed rows were already paths or that WG selects it.
module Universal {ℓ : Level} (X : Type ℓ) where
  Diagram = Σ[ points ∈ (Vertex → X) ]
    ((e : Occurrence) → points (source e) ≡ points (target e))
  restrict : (Realization → X) → Diagram
  restrict f = (λ v → f (node v)) , (λ e → cong f (edge e))
  extend : Diagram → Realization → X
  extend (points , paths) (node v) = points v
  extend (points , paths) (edge e i) = paths e i
  extension-unique : (f : Realization → X) → extend (restrict f) ≡ f
  extension-unique f i (node v) = f (node v)
  extension-unique f i (edge e j) = f (edge e j)
  universal : (Realization → X) ≃ Diagram
  universal = isoToEquiv (iso restrict extend (λ _ → refl) extension-unique)

-- Tree: AB, AD, reverse CA. The three remaining edges are independent chords.
data Chord : Type where
  bc db ba : Chord
ThreeCircles = Bouquet Chord
collapse : Realization → ThreeCircles
collapse (node _) = base
collapse (edge AB i) = base
collapse (edge AD i) = base
collapse (edge CA i) = base
collapse (edge BC i) = loop bc i
collapse (edge DB i) = loop db i
collapse (edge BA i) = loop ba i

rootPath : (v : Vertex) → node A ≡ node v
rootPath A = refl
rootPath B = edge AB
rootPath C = sym (edge CA)
rootPath D = edge AD
chordEdge : Chord → Occurrence
chordEdge bc = BC
chordEdge db = DB
chordEdge ba = BA
-- Named legs make the inverse and its computation theorem share exact paths.
leftPath : (c : Chord) → node A ≡ node (source (chordEdge c))
leftPath c = rootPath (source (chordEdge c))
rightPath : (c : Chord) → node (target (chordEdge c)) ≡ node A
rightPath c = sym (rootPath (target (chordEdge c)))
expand : ThreeCircles → Realization
expand base = node A
expand (loop c i) = (leftPath c ∙∙ edge (chordEdge c) ∙∙ rightPath c) i

expand-collapse : (x : Realization) → expand (collapse x) ≡ x
expand-collapse (node v) = rootPath v
expand-collapse (edge AB i) j = edge AB (i ∧ j)
expand-collapse (edge AD i) j = edge AD (i ∧ j)
expand-collapse (edge CA i) j = edge CA (i ∨ ~ j)
expand-collapse (edge BC i) j = doubleCompPath-filler (leftPath bc) (edge BC) (rightPath bc) (~ j) i
expand-collapse (edge DB i) j = doubleCompPath-filler (leftPath db) (edge DB) (rightPath db) (~ j) i
expand-collapse (edge BA i) j = doubleCompPath-filler (leftPath ba) (edge BA) (rightPath ba) (~ j) i

collapse-loop : (c : Chord) → cong collapse (cong expand (loop c)) ≡ loop c
collapse-loop bc = cong-∙∙ collapse (leftPath bc) (edge BC) (rightPath bc)
  ∙ (λ j i → doubleCompPath-filler refl (loop bc) refl (~ j) i)
collapse-loop db = cong-∙∙ collapse (leftPath db) (edge DB) (rightPath db)
  ∙ (λ j i → doubleCompPath-filler refl (loop db) refl (~ j) i)
collapse-loop ba = cong-∙∙ collapse (leftPath ba) (edge BA) (rightPath ba)
  ∙ (λ j i → doubleCompPath-filler refl (loop ba) refl (~ j) i)
collapse-expand : (x : ThreeCircles) → collapse (expand x) ≡ x
collapse-expand base = refl
collapse-expand (loop c i) j = collapse-loop c j i
free-source-three-circles : Realization ≃ ThreeCircles
free-source-three-circles = isoToEquiv
  (iso collapse expand collapse-expand expand-collapse)

-- Labels remain construction data, not a discrete retract of the space.
isB : Vertex → Bool
isB A = false
isB B = true
isB C = false
isB D = false
no-discrete-retraction : (read : Realization → Vertex)
  → ((v : Vertex) → read (node v) ≡ v) → ⊥
no-discrete-retraction read preserves = false≢true
  (cong isB (sym (preserves A) ∙ cong read (edge AB) ∙ preserves B))

-- Existing face obstructions remain imported, not re-proved or generalized.
no-forward-face = Prior.no-forward-face
no-abc-face = Prior.no-abc-face
