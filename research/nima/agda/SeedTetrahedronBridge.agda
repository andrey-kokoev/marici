{-# OPTIONS --safe --cubical --guardedness #-}
module SeedTetrahedronBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc)
open import ActualSeedEndpointTable
import RetainedTetrahedralPackage as Retained

-- Explicit free geometric realization of the supplied directed graph.
-- This adds its six edges as paths but NO face relations. Original directed
-- occurrence records remain separate; BA is not declared the inverse of AB.
data Realization : Type where
  node : Vertex → Realization
  edge : (e : Occurrence) → node (source e) ≡ node (target e)

module C = Retained.Cells Realization
vertices : C.Vertices
vertices = C.vertices (node A) (node D) (node B) (node C)

-- The D->C diagonal is the witnessed composite DB BC. The A->C edge
-- uses reversal in this explicit path interpretation, not a primitive AC.
skeleton : C.Over.Edges vertices
skeleton = record
  { e01 = edge AD
  ; e12 = edge DB
  ; e02 = edge AB
  ; e23 = edge BC
  ; e13 = edge DB ∙ edge BC
  ; e03 = sym (edge CA)
  }

-- Two exact missing geometric comparisons. Neither is a supplied seed fact.
ForwardFace TriangleABC : Type
ForwardFace = (edge AD ∙ edge DB) ≡ edge AB
TriangleABC = (edge AB ∙ edge BC) ≡ sym (edge CA)

-- The fourth primitive BA is still retained as an independent edge.
-- Identifying it with the reversal of AB would need this separate witness.
ReverseAB : Type
ReverseAB = edge BA ≡ sym (edge AB)

-- A DBC face is already supplied by the composite diagonal definition.
face-DBC : C.T.Over.Face123 skeleton
face-DBC = refl

module WithFaces (forward : ForwardFace) (abc : TriangleABC) where
  -- ADC is not an independently supplied seed face. Complete that side
  -- together with its coherence, keeping the independently supplied ABC.
  side-completion : C.T.Over.Missing013 skeleton forward face-DBC abc
  side-completion = fst (C.T.Over.unique013 skeleton forward face-DBC abc)

  face-ADC : C.T.Over.Face013 skeleton
  face-ADC = fst side-completion

  supplied-bottom-filler : C.T.Over.Tetrahedron skeleton forward face-DBC face-ADC abc
  supplied-bottom-filler = snd side-completion

  horn : C.Over.Horn vertices
  horn = C.Over.horn skeleton forward face-DBC face-ADC
  completed : C.Full
  completed = C.build (vertices , horn)

  source-horn-recovered : C.recover-request completed ≡ (vertices , horn)
  source-horn-recovered = refl
  supplied-edges-preserved : C.Over.Surface.edges (fst (snd completed)) ≡ skeleton
  supplied-edges-preserved = refl

  -- The bottom face arrives WITH its filler. This is the actual pair
  -- returned inside Cells.build, not a face chosen separately afterward.
  bottom-and-filler : C.T.Over.Missing023 skeleton forward face-DBC face-ADC
  bottom-and-filler = C.Over.Surface.face023 (fst (snd completed)) , snd (snd completed)

  bottom-pair-agrees : bottom-and-filler ≡ (abc , supplied-bottom-filler)
  bottom-pair-agrees = snd (C.T.Over.unique023 skeleton forward face-DBC face-ADC)
    (abc , supplied-bottom-filler)

  bottom-agrees : fst bottom-and-filler ≡ abc
  bottom-agrees = cong fst bottom-pair-agrees

  -- Filler comparison is dependent on the compared bottom face.
  filler-agrees : PathP
    (λ i → C.T.Over.Tetrahedron skeleton forward face-DBC face-ADC (bottom-agrees i))
    (snd bottom-and-filler) supplied-bottom-filler
  filler-agrees i = snd (bottom-pair-agrees i)

  record BridgePacket : Type where
    constructor bridge-packet
    field
      retained-forward : ForwardFace
      retained-abc : TriangleABC
      full : C.Full
      paired-bottom : C.T.Over.Missing023 skeleton forward face-DBC face-ADC
      paired-agreement : paired-bottom ≡ (abc , supplied-bottom-filler)
  packet : BridgePacket
  packet = bridge-packet forward abc completed bottom-and-filler bottom-pair-agrees

-- Control: a tetrahedron can be filled on the three-edge spine alone by
-- defining every diagonal as a composite. That does NOT respect the seed's
-- independently supplied AB and CA edges and is not the requested bridge.
spine-edges : C.Over.Edges vertices
spine-edges = record
  { e01 = edge AD
  ; e12 = edge DB
  ; e02 = edge AD ∙ edge DB
  ; e23 = edge BC
  ; e13 = edge DB ∙ edge BC
  ; e03 = (edge AD ∙ edge DB) ∙ edge BC
  }
spine-horn : C.Over.Horn vertices
spine-horn = C.Over.horn spine-edges refl refl
  (assoc (edge AD) (edge DB) (edge BC))
spine-completed : C.Full
spine-completed = C.build (vertices , spine-horn)
