{-# OPTIONS --safe --cubical --guardedness #-}
module CertifiedForwardHigherPackets where

open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using (List; []; _∷_; map)
open import NativeExtensionFamilyAudit using (Vertex; A; Seeds; pointQ)
open import InternalSourceComparisons using (Body; package)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
import ForwardForwardHigherAdmission as Higher
import WholePackageResolution as Resolution
import WholePackageSigmaPi as Whole
open Resolution.Generators ℓ-zero

-- The three EXACT existing higher outputs, not a caller-supplied family or
-- path. All decisive parameters are computed by the named forward diagram.
data Stage : Type where
  leftEnvelope rightEnvelope higherPath : Stage
higherClosure : (d : Resolve Seeds (pointQ A)) → Stage → Closure Seeds
higherClosure d leftEnvelope = H.envelope H.T.sequential , H.envelope-derived H.T.sequential
  where module H = Higher.Admit d
higherClosure d rightEnvelope = H.envelope H.T.direct , H.envelope-derived H.T.direct
  where module H = Higher.Admit d
higherClosure d higherPath = H.admittedPathPackage , H.admitted-higher
  where module H = Higher.Admit d

-- A closed sum of the prior certified Fragment grammar and these computed
-- higher producers. No arbitrary Resolve, Complete, Type, family or cell port.
data Program : Type₁ where
  fragmentP : {v : Vertex} → P.Program v → Program
  higherP : P.Initial A → Stage → Program
native : Program → Closure Seeds
native (fragmentP p) = package (G.body (P.decode p)) , P.native p
native (higherP p stage) = higherClosure (P.runInitial p) stage
-- This is a data package one universe up, not a new native admission claim.
reified : P.Initial A → Whole.Universe.Complete (ℓ-suc ℓ-zero)
reified p = Higher.Admit.reified (P.runInitial p)
record Certificate (original : Closure Seeds) : Type₁ where
  constructor certificate
  field
    producer : Program
    matches : native producer ≡ original
certify : (d : Resolve Seeds (pointQ A)) (c0 : P.InitialCertificate A d) (stage : Stage)
  → Certificate (higherClosure d stage)
certify d c0 stage = certificate (higherP (P.InitialCertificate.initialProducer c0) stage)
  (cong (λ d → higherClosure d stage) (P.InitialCertificate.initialMatches c0))

data AllCertified : List (Closure Seeds) → Type₁ where
  nilH : AllCertified []
  _∷H_ : {x : Closure Seeds} {xs : List (Closure Seeds)}
    → Certificate x → AllCertified xs → AllCertified (x ∷ xs)
infixr 5 _∷H_
compileList : {xs : List (Closure Seeds)} → AllCertified xs → List Program
compileList nilH = []
compileList (c ∷H cs) = Certificate.producer c ∷ compileList cs
list-match : {xs : List (Closure Seeds)} (cs : AllCertified xs) → map native (compileList cs) ≡ xs
list-match nilH = refl
list-match (c ∷H cs) = cong₂ _∷_ (Certificate.matches c) (list-match cs)

-- Bind the original nineteen-entry retained packet, not a newly chosen list
-- of lookalike outputs. The initial certificate is mandatory for arbitrary d.
module Context (d : Resolve Seeds (pointQ A)) (c0 : P.InitialCertificate A d) where
  module H = Higher.Admit d
  module D = P.Diagram d c0
  fromEntries : {xs : List (Σ Vertex Body)} → P.AllCertified xs → AllCertified (H.nativeDiagram xs)
  fromEntries P.nilC = nilH
  fromEntries (P._∷C_ e es) = certificate (fragmentP (P.Entry.entryProgram e))
    (P.Entry.entryMatches e) ∷H fromEntries es
  retained-certified : AllCertified H.retainedClosures
  retained-certified = certify d c0 leftEnvelope ∷H certify d c0 rightEnvelope
    ∷H certify d c0 higherPath ∷H fromEntries D.certified-diagram
  packet : List Program
  packet = compileList retained-certified
  packet-matches : map native packet ≡ H.retainedClosures
  packet-matches = list-match retained-certified
  reified-matches : reified (P.InitialCertificate.initialProducer c0) ≡ H.reified
  reified-matches = cong Higher.Admit.reified (P.InitialCertificate.initialMatches c0)

module Generated (p : P.Initial A) = Context (P.runInitial p) (P.initial-certificate p refl)
