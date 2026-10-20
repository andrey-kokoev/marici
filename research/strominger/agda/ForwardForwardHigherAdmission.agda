{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardForwardHigherAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism using (isoToEquiv)
open import Cubical.Data.Bool using (false≢true)
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.List using (List; []; _∷_)
open import Cubical.Relation.Nullary using (¬_)
open import NativeExtensionFamilyAudit using (Vertex; A; C; Seeds; pointQ; root)
open import InternalSourceComparisons using (Body; stay; package; derivation)
open import GeneratedReaderClassification using (body; normal; carrier-set; native)
import ForwardForwardBodyBinding as Binding
import CoherentDependentExtensions as General
import HigherWitnessAdmission as Prior
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

module Admit (d : Resolve Seeds (pointQ A)) where
  module T = Binding.Diagram d
  Filler : Type
  Filler = T.Final.C.Filler
  term : Filler → Body C
  term f = body (Binding.cmp stay T.source T.target f)
  branch : Filler → Complete
  branch f = path-package (expression (package (term f)))
    (value (package (term f))) (value (package (term f))) refl
  branch-derived : (f : Filler) → Resolve Seeds (branch f)
  branch-derived f = apply
    (reflexivity-rule (expression (package (term f))) (value (package (term f))))
    (λ _ → derivation (term f))
  EnvelopeCode : Code
  EnvelopeCode = E Filler (λ f → retained (branch f))
  envelope : Filler → Complete
  envelope f = E-package Filler branch f
  envelope-derived : (f : Filler) → Resolve Seeds (envelope f)
  envelope-derived f = apply (E-rule Filler branch f) (λ { (lift g) → branch-derived g })
  branch-contractible : (f : Filler) → isContr (El (retained (branch f)))
  branch-contractible f = refl , (λ p → carrier-set
    (normal (Binding.cmp stay T.source T.target f)) _ _ refl p)
  module Projection = General.Projection Filler (λ f → El (retained (branch f)))
  envelopeEquiv : El EnvelopeCode ≃ Filler
  envelopeEquiv = isoToEquiv (Projection.contractible-projection branch-contractible)
  left right : El EnvelopeCode
  left = value (envelope T.sequential)
  right = value (envelope T.direct)
  envelopePath : left ≡ right
  envelopePath i = T.filler-coherence i , refl
  path-recovery : cong fst envelopePath ≡ T.filler-coherence
  path-recovery = refl
  admittedPathPackage : Complete
  admittedPathPackage = path-package EnvelopeCode left right envelopePath
  module H = Prior.PathAdmission Seeds
  admitted-higher : Resolve Seeds admittedPathPackage
  admitted-higher = H.from-derived-point EnvelopeCode left
    (envelope-derived T.sequential) envelopePath

  -- Faithful envelope admission still does not admit the bare atomic Code.
  barePackage : Complete
  barePackage = path-package (atom Filler) T.sequential T.direct T.filler-coherence
  bare-not-admitted : ¬ (Resolve Seeds barePackage)
  bare-not-admitted proof = false≢true (sym (Prior.resolution-spine proof))

  nativeDiagram : List (Σ Vertex Body) → List (Closure Seeds)
  nativeDiagram [] = []
  nativeDiagram ((v , b) ∷ bs) = (package b , derivation b) ∷ nativeDiagram bs
  retainedClosures : List (Closure Seeds)
  retainedClosures = (envelope T.sequential , envelope-derived T.sequential)
    ∷ (envelope T.direct , envelope-derived T.direct)
    ∷ (admittedPathPackage , admitted-higher) ∷ nativeDiagram T.diagram
  Payload : Type₁
  Payload = List (Σ Vertex Body) × List (Closure Seeds)
  certificate : Payload
  certificate = T.diagram , retainedClosures
  reified : Whole.Universe.Complete (ℓ-suc ℓ-zero)
  reified = Whole.Universe.pack (Whole.Universe.atom Payload) certificate
  recovery : Whole.Universe.value reified ≡ certificate
  recovery = refl

module Regression = Admit (root A)
