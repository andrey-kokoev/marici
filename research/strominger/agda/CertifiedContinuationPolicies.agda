{-# OPTIONS --safe --cubical --guardedness #-}
module CertifiedContinuationPolicies where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Maybe.Base using (just)
open import NativeExtensionFamilyAudit using (Vertex; A; Seeds; pointQ)
open import InternalSourceComparisons using (Body; Mode; stay; act)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
import CanonicalComparisonSynthesis as Compile
import ContinuationPolicyFamily as Policy
import InternalComparisonInterchange as Native
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero hiding (output)

-- Two declared outputs of the existing policy family, not new native rules.
data Stage : Type where
  output comparison : Stage
module Model (m : Mode) {v : Vertex} (a : G.Fragment v) (b : G.Fragment (act m v))
  (f : G.Comparisons.Filler m a b) where
  module F = Policy.Family m (G.body a) (G.body b) (fst f) (fst (snd f)) (snd (snd f))
  Request = F.S.Request
  Control = F.S.S.Request
  synchronize : Control → Request
  synchronize = invEq (F.S.S.P.synchronized-source F.S.S.z)
  request-match : (r : Request) → synchronize (fst r) ≡ r
  request-match = F.S.request-recovered
  body : (r : Request) → Policy.Presentation → Stage → Body (fst (F.S.route r))
  body r k output = F.output r k
  body r k comparison = F.policyComparison r k
  value : Request → Policy.Presentation → Stage → Σ Vertex Body
  value r k op = fst (F.S.route r) , body r k op
  targetFragment : (r : Request) → G.Fragment (fst (F.S.route r))
  targetFragment r = G.attachF (G.compareF m a b (fst f) (fst (snd f)) (snd (snd f))) (F.S.route r)
  target-binding : (r : Request) → G.body (targetFragment r) ≡ F.output r Policy.target
  target-binding r = refl
module Compiled (m : Mode) {v : Vertex} (p : P.Program v) (q : P.Program (act m v))
  (ok : P.Pair.Guard m p q) where
  module K = Compile.Compile m (P.decode p) (P.decode q)
  filler = K.require-success K.compile ok
  module R = Model m (P.decode p) (P.decode q) filler
  Control = R.Control
  value : Control → Policy.Presentation → Stage → Σ Vertex Body
  value s = R.value (R.synchronize s)

-- No Body, Resolve, full filler, reader, family or synchronization path import.
-- Control is exactly the source-derived outgoing request of the computed cell.
data Program : Type₁ where
  policyP : (m : Mode) {v : Vertex} (p : P.Program v) (q : P.Program (act m v))
    (ok : P.Pair.Guard m p q) → Compiled.Control m p q ok
    → Policy.Presentation → Stage → Program
decode : Program → Σ Vertex Body
decode (policyP m p q ok s k op) = Compiled.value m p q ok s k op
native : (p : Program) → Closure Seeds
native p = Native.closure (decode p)
record Certificate (original : Σ Vertex Body) : Type₁ where
  constructor certificate
  field
    producer : Program
    matches : decode producer ≡ original
native-match : {original : Σ Vertex Body} (c : Certificate original)
  → native (Certificate.producer c) ≡ Native.closure original
native-match c = cong Native.closure (Certificate.matches c)

-- Existing parameterized presentations are matched to the closed evaluator.
-- First transport operand/cell/request data together, then match the full
-- filler to the computed one, then recover the original synchronized tuple.
abstract
  certify : (m : Mode) {v : Vertex} {a : G.Fragment v} {b : G.Fragment (act m v)}
    (ca : P.Certificate a) (cb : P.Certificate b) (f : G.Comparisons.Filler m a b)
    (r : Model.Request m a b f) (k : Policy.Presentation) (op : Stage)
    → Certificate (Model.value m a b f r k op)
  certify m {v} {a} {b} ca cb f r k op = certificate generated (request-path ∙ cell-path ∙ operand-path)
    where
    pa : P.Program v
    pa = P.Certificate.producer ca
    pb : P.Program (act m v)
    pb = P.Certificate.producer cb
    ea : P.decode pa ≡ a
    ea = P.Certificate.matches ca
    eb : P.decode pb ≡ b
    eb = P.Certificate.matches cb
    Data : (a : G.Fragment v) (b : G.Fragment (act m v)) → Type
    Data a b = Σ[ f ∈ G.Comparisons.Filler m a b ] Model.Request m a b f
    back : I → Type
    back i = Data (ea (~ i)) (eb (~ i))
    initial : Data (P.decode pa) (P.decode pb)
    initial = transport (λ i → back i) (f , r)
    f0 : G.Comparisons.Filler m (P.decode pa) (P.decode pb)
    f0 = fst initial
    r0 : Model.Request m (P.decode pa) (P.decode pb) f0
    r0 = snd initial
    module K = Compile.Compile m (P.decode pa) (P.decode pb)
    ok : P.Pair.Guard m pa pb
    ok = K.complete f0
    module C = Compiled m pa pb ok
    cell-eq : C.filler ≡ f0
    cell-eq = K.C.filler-prop C.filler f0
    request-back : I → Type
    request-back i = Model.Request m (P.decode pa) (P.decode pb) (cell-eq (~ i))
    rc : C.R.Request
    rc = transport (λ i → request-back i) r0
    generated : Program
    generated = policyP m pa pb ok (fst rc) k op
    request-path : decode generated ≡ C.R.value rc k op
    request-path = cong (λ r → C.R.value r k op) (C.R.request-match rc)
    cell-path : C.R.value rc k op ≡ Model.value m (P.decode pa) (P.decode pb) f0 r0 k op
    cell-path i = Model.value m (P.decode pa) (P.decode pb) (cell-eq i)
      (transport-filler (λ j → request-back j) r0 (~ i)) k op
    operand-path : Model.value m (P.decode pa) (P.decode pb) f0 r0 k op
      ≡ Model.value m a b f r k op
    operand-path i = Model.value m (ea i) (eb i)
      (fst (transport-filler (λ j → back j) (f , r) (~ i)))
      (snd (transport-filler (λ j → back j) (f , r) (~ i))) k op

-- The common target really is a certified generated endpoint. Source and
-- synchronized raw outputs are connected to it by the retained native policy
-- comparisons, NOT silently equated with it or reclassified as Fragments.
target-certificate : (m : Mode) {v : Vertex} {a : G.Fragment v} {b : G.Fragment (act m v)}
  (ca : P.Certificate a) (cb : P.Certificate b) (f : G.Comparisons.Filler m a b)
  (r : Model.Request m a b f) → P.Certificate (Model.targetFragment m a b f r)
target-certificate m ca cb f r = P.certify (Model.targetFragment m _ _ f r)
  (P.origins-of-certificate ca , P.origins-of-certificate cb)

comparison-operands : (m : Mode) {v : Vertex} {a : G.Fragment v} {b : G.Fragment (act m v)}
  (ca : P.Certificate a) (cb : P.Certificate b) (f : G.Comparisons.Filler m a b)
  (r : Model.Request m a b f) (k : Policy.Presentation)
  → Native.comparisonOperands (native (Certificate.producer (certify m ca cb f r k comparison)))
    ≡ just (Native.closure (Model.value m a b f r k output)
           , Native.closure (Model.value m a b f r Policy.target output))
comparison-operands m ca cb f r k = cong Native.comparisonOperands
  (native-match (certify m ca cb f r k comparison))

-- Exact common witnesses from the unchanged named forward diagram.
module Forward (d : Resolve Seeds (pointQ A)) (c0 : P.InitialCertificate A d) where
  module D = P.Diagram d c0
  module Sequential = Model stay D.D.source D.D.target D.D.sequential
  module Direct = Model stay D.D.source D.D.target D.D.direct
  sequential : (r : Sequential.Request) (k : Policy.Presentation) (op : Stage)
    → Certificate (Sequential.value r k op)
  sequential = certify stay D.source-certificate D.target-certificate D.D.sequential
  direct : (r : Direct.Request) (k : Policy.Presentation) (op : Stage)
    → Certificate (Direct.value r k op)
  direct = certify stay D.source-certificate D.target-certificate D.D.direct
