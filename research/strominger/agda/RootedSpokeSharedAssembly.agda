{-# OPTIONS --safe --cubical --guardedness #-}
module RootedSpokeSharedAssembly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sum.Base using (inl; inr)
open import TypedGeneratorLayers using (Layer1)
import TableFibrationCycle as Table
import RetainedTetrahedralPackage as Retained
import RootedSpokePathCompletion as Paths
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv)

-- Adapter only: the package constructor and WG transition are shared code.
module Assemble {ℓ : Level} {X : Type ℓ} {a b c d : X}
  (ab : a ≡ b) (ac : a ≡ c) (ad : a ≡ d) where
  module P = Paths.FromSpokes ab ac ad
  module C = Retained.Cells X
  vertices : C.Vertices
  vertices = C.vertices a b c d
  module O = C.Over vertices

  request : C.Request
  request = vertices , O.horn P.edges P.faceABC P.faceBCD P.faceABD
  completed : C.Full
  completed = C.build request
  surface : O.Surface
  surface = fst (snd completed)

  -- The actual shared WG generator executes precisely this build request.
  generated : fst (Layer1.generate C.WG (inl request)) ≡ inr completed
  generated = refl
  recovered : C.recover-request completed ≡ request
  recovered = C.request-recovered request
  edges-retained : O.Surface.edges surface ≡ P.edges
  edges-retained = refl
  spoke-AB : C.T.Edges.e01 (O.Surface.edges surface) ≡ ab
  spoke-AB = refl
  spoke-AC : C.T.Edges.e02 (O.Surface.edges surface) ≡ ac
  spoke-AC = refl
  spoke-AD : C.T.Edges.e03 (O.Surface.edges surface) ≡ ad
  spoke-AD = refl
  branch-BC : C.T.Edges.e12 (O.Surface.edges surface) ≡ sym ab ∙ ac
  branch-BC = refl
  branch-BD : C.T.Edges.e13 (O.Surface.edges surface) ≡ sym ab ∙ ad
  branch-BD = refl
  branch-CD : C.T.Edges.e23 (O.Surface.edges surface) ≡ sym ac ∙ ad
  branch-CD = refl

  -- The retained assembler fills ACD, paired with its filler. Compare that
  -- actual output to the independently constructed cancellation face/filler.
  paired-output : P.O.Missing023 P.faceABC P.faceBCD P.faceABD
  paired-output = O.Surface.face023 surface , snd (snd completed)
  paired-agreement : paired-output ≡ (P.faceACD , P.tetrahedron)
  paired-agreement = snd (P.O.unique023 P.faceABC P.faceBCD P.faceABD)
    (P.faceACD , P.tetrahedron)
  face-ACD-retained : O.Surface.face023 surface ≡ P.faceACD
  face-ACD-retained = cong fst paired-agreement
  filler-retained : PathP
    (λ i → P.O.Tetrahedron P.faceABC P.faceBCD P.faceABD (face-ACD-retained i))
    (snd (snd completed)) P.tetrahedron
  filler-retained i = snd (paired-agreement i)

  -- Shared edges include their endpoints and paths, not just edge counts.
  shared-AB = O.shared01 surface
  shared-BC = O.shared12 surface
  shared-AC = O.shared02 surface
  shared-CD = O.shared23 surface
  shared-BD = O.shared13 surface
  shared-AD = O.shared03 surface

module Seed where
  data Vertex : Type where
    A B C D : Vertex
  data Occurrence : Type where
    AB AC AD : Occurrence
  source target : Occurrence → Vertex
  source AB = A
  source AC = A
  source AD = A
  target AB = B
  target AC = C
  target AD = D
  seed : Table.Table Occurrence Vertex Vertex
  seed = Table.table Occurrence (λ e → e) source target
  grouped-recovery : Table.TableIso (Table.unpack (Table.group-from seed)) seed
  grouped-recovery = Table.unpack-correct seed
  four-recovery : Table.TableIso (Table.four seed) seed
  four-recovery = Table.four-correct seed

  -- Explicit path interpretation, following the existing seed bridge.
  -- Only three primitive edge constructors; NO primitive face constructor,
  -- branch comparison, coordinate, phase, or cyclic leaf action is supplied.
  data Realization : Type where
    node : Vertex → Realization
    edge : (e : Occurrence) → node (source e) ≡ node (target e)
  module S = Assemble (edge AB) (edge AC) (edge AD)
  assembled : S.C.Full
  assembled = S.completed

  -- Keep the original table alongside the geometric output. Derived reverse
  -- paths are not new primitive rows or free directed protocol traversals.
  record AssemblyPacket : Type₁ where
    constructor packet
    field
      primitive-table : Table.Table Occurrence Vertex Vertex
      full : S.C.Full
      table-retained : primitive-table ≡ seed
      request-retained : S.C.recover-request full ≡ S.request
  result : AssemblyPacket
  result = packet seed assembled refl S.recovered

-- Nontrivial payload-action control of the generic shared adapter.
-- These marks are deliberately distinct from the free seed realization.
module Twisted where
  module S = Assemble (ua notEquiv) (refl {x = Bool}) (refl {x = Bool})
  first-edge : Bool ≡ Bool
  first-edge = S.C.T.Edges.e01 (S.O.Surface.edges S.surface)
  action : transport first-edge false ≡ true
  action = uaβ notEquiv false
