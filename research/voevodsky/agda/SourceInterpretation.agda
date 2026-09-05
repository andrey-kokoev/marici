{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SourceInterpretation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import RHGeneratedFixture

record SourceVertex : Type₁ where
  field
    Parameter Object Residue : Type
    generator : Parameter → Object
    coherencer : Object → Residue
open SourceVertex public

record VertexInterpretation (source : SourceVertex) : Type₁ where
  field
    parameter-coordinate : Parameter source → ℤ
    object-coordinate : Object source → ℤ
    residue-coordinate : Residue source → ℤ
    generator-natural :
      (p : Parameter source) →
      object-coordinate (generator source p) ≡ parameter-coordinate p
    coherencer-natural :
      (o : Object source) →
      residue-coordinate (coherencer source o) ≡ object-coordinate o
open VertexInterpretation public

record SourceCycle : Type₁ where
  field
    A B C : SourceVertex
    T-A : Residue A → Parameter B
    T-B : Residue B → Parameter C
    T-C : Residue C → Parameter A
open SourceCycle public

record CycleInterpretation (source : SourceCycle) : Type₁ where
  field
    interpret-A : VertexInterpretation (A source)
    interpret-B : VertexInterpretation (B source)
    interpret-C : VertexInterpretation (C source)
    T-A-natural :
      (r : Residue (A source)) →
      parameter-coordinate interpret-B (T-A source r) ≡ residue-coordinate interpret-A r
    T-B-natural :
      (r : Residue (B source)) →
      parameter-coordinate interpret-C (T-B source r) ≡ residue-coordinate interpret-B r
    T-C-natural :
      (r : Residue (C source)) →
      parameter-coordinate interpret-A (T-C source r) ≡ residue-coordinate interpret-C r
open CycleInterpretation public

record SourceCompletion : Type₁ where
  field
    Base Completed : Type
    inject : Base → Completed
open SourceCompletion public

record CompletionInterpretation (source : SourceCompletion) : Type₁ where
  field
    base-coordinate : Base source → ℤ
    completed-coordinate : Completed source → ℤ
    completion-natural :
      (x : Base source) →
      completed-coordinate (inject source x) ≡ base-coordinate x
open CompletionInterpretation public

record FillerInterpretation : Type₁ where
  field
    SourceFiller : Type
    source-discrepancy : SourceFiller → ℤ
    edge-coordinate : SourceFiller → Generatedℤ³
    boundary-natural :
      (f : SourceFiller) → generated∂₂ (edge-coordinate f) ≡ source-discrepancy f
open FillerInterpretation public

record SourceInterpretationContract
  (source-cycle : SourceCycle)
  (source-completion : SourceCompletion)
  (filler-interpretation : FillerInterpretation) : Type₁ where
  field
    cycle-interpretation : CycleInterpretation source-cycle
    completion-interpretation : CompletionInterpretation source-completion

-- The source objects are parameters, not fields chosen by an inhabitant.
-- Agda checks naturality relative to those supplied objects; external source
-- authority for supplying them remains outside this formal contract.
