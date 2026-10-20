{-# OPTIONS --safe --cubical --guardedness #-}
module MixedHistoryCertificates where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Maybe.Base using (just)
open import NativeExtensionFamilyAudit using (Seeds)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using (Mode; Body; prepared; package; derivation; reader; aligned)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import NativeComposeHistoryBridge as C
import NativeAttachmentHistoryBridge as A
import GeneratedReaderClassification as G
import InternalComparisonInterchange as Native
import RetainedPackageFeedback as Feedback
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

endClosure : {m : Mode} {a b : F.Object} → F.Full m a b → Closure Seeds
endClosure f = F.asPackage f , F.admitted f
record EndWitness {m : Mode} {a b : F.Object} (f : F.Full m a b) : Type₁ where
  field
    actual : Closure Seeds
    exact : actual ≡ endClosure f
endWitness : {m : Mode} {a b : F.Object} (f : F.Full m a b) → EndWitness f
EndWitness.actual (endWitness f) = endClosure f
EndWitness.exact (endWitness f) = refl

joinClosure : {m n : Mode} {a b c : F.Object} → F.Full m a b → F.Full n b c → Closure Seeds
joinClosure f g = C.Bridge.retainedPackage f g , C.Bridge.retained-native f g
joinBridge : {m n : Mode} {a b c : F.Object} → F.Full m a b → F.Full n b c → Closure Seeds
joinBridge f g = package (C.Bridge.bridgeBody f g) , C.Bridge.bridge-native f g
record JoinWitness {m n : Mode} {a b c : F.Object} (f : F.Full m a b) (g : F.Full n b c) : Type₁ where
  field
    history bridge : Closure Seeds
    historyExact : history ≡ joinClosure f g
    bridgeExact : bridge ≡ joinBridge f g
    inputsRecovered : C.composeOperands history ≡ just (endClosure f , endClosure g)
    bridgeRecovered : Native.comparisonOperands bridge ≡ just (history , endClosure (F.compose f g))
joinWitness : {m n : Mode} {a b c : F.Object} (f : F.Full m a b) (g : F.Full n b c) → JoinWitness f g
JoinWitness.history (joinWitness f g) = joinClosure f g
JoinWitness.bridge (joinWitness f g) = joinBridge f g
JoinWitness.historyExact (joinWitness f g) = refl
JoinWitness.bridgeExact (joinWitness f g) = refl
JoinWitness.inputsRecovered (joinWitness f g) = C.Bridge.premises-retained f g
JoinWitness.bridgeRecovered (joinWitness f g) = C.Bridge.both-histories-retained f g

attachClosure : {m : Mode} {a b : F.Object} (f : F.Full m a b) → Out (fst a) → Closure Seeds
attachClosure f o = A.Bridge.retainedPackage f o , A.Bridge.retained-native f o
attachBridge : {m : Mode} {a b : F.Object} (f : F.Full m a b) → Out (fst a) → Closure Seeds
attachBridge f o = package (A.Bridge.bridgeBody f o) , A.Bridge.bridge-native f o
record AttachWitness {m : Mode} {a b : F.Object} (f : F.Full m a b) (o : Out (fst a)) : Type₁ where
  field
    history bridge : Closure Seeds
    historyExact : history ≡ attachClosure f o
    bridgeExact : bridge ≡ attachBridge f o
    inputRecovered : Feedback.peel (Feedback.peel history) ≡ endClosure f
    bridgeRecovered : Native.comparisonOperands bridge ≡ just (endClosure (M.attachment f o) , history)
attachWitness : {m : Mode} {a b : F.Object} (f : F.Full m a b) (o : Out (fst a)) → AttachWitness f o
AttachWitness.history (attachWitness f o) = attachClosure f o
AttachWitness.bridge (attachWitness f o) = attachBridge f o
AttachWitness.historyExact (attachWitness f o) = refl
AttachWitness.bridgeExact (attachWitness f o) = refl
AttachWitness.inputRecovered (attachWitness f o) = A.Bridge.old-premise-recovered f o
AttachWitness.bridgeRecovered (attachWitness f o) = A.Bridge.both-orders-recovered f o

-- Evidence mirrors every node, INCLUDING composition inside imported core
-- trees. Parents consume compiled child outputs; the child retained history
-- and its comparison bridge remain separately present in the recursive data.
CoreEvidence : {m : Mode} {a b : F.Object} → F.Tree m a b → Type₁
CoreEvidence (F.cell f) = EndWitness f
CoreEvidence (F.unit a) = EndWitness (F.identity a)
CoreEvidence (F.then r s) = CoreEvidence r × CoreEvidence s × JoinWitness (F.fold r) (F.fold s)
coreEvidence : {m : Mode} {a b : F.Object} (t : F.Tree m a b) → CoreEvidence t
coreEvidence (F.cell f) = endWitness f
coreEvidence (F.unit a) = endWitness (F.identity a)
coreEvidence (F.then r s) = coreEvidence r , coreEvidence s , joinWitness (F.fold r) (F.fold s)
Evidence : {m : Mode} {a b : F.Object} → M.Tree m a b → Type₁
Evidence (M.old t) = CoreEvidence t
Evidence (M.join r s) = Evidence r × Evidence s × JoinWitness (M.fold r) (M.fold s)
Evidence (M.attach r o) = Evidence r × AttachWitness (M.fold r) o
nodeEvidence : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Evidence t
nodeEvidence (M.old t) = coreEvidence t
nodeEvidence (M.join r s) = nodeEvidence r , nodeEvidence s , joinWitness (M.fold r) (M.fold s)
nodeEvidence (M.attach r o) = nodeEvidence r , attachWitness (M.fold r) o

compiledView : {m : Mode} {a b : F.Object} → F.Full m a b → Body (fst b)
compiledView {b = b} f = prepared (fst b) (F.asPackage f) (F.admitted f)
  (λ z → F.readPort b (fst (snd z))) (aligned (G.body (snd b)))
coreRoot : {m : Mode} {a b : F.Object} → F.Tree m a b → Body (fst b)
coreRoot (F.cell f) = compiledView f
coreRoot (F.unit a) = compiledView (F.identity a)
coreRoot (F.then r s) = C.Bridge.retainedBody (F.fold r) (F.fold s)
root : {m : Mode} {a b : F.Object} → M.Tree m a b → Body (fst b)
root (M.old t) = coreRoot t
root (M.join r s) = C.Bridge.retainedBody (M.fold r) (M.fold s)
root (M.attach t o) = A.Bridge.retainedBody (M.fold t) o

record Certificate {m : Mode} {a b : F.Object} (t : M.Tree m a b) : Type₁ where
  field
    tree : M.Tree m a b
    treeRecovery : tree ≡ t
    nodes : Evidence tree
    endpoint : EndWitness (M.fold tree)
    rootHistory : Closure Seeds
    rootRecovery : rootHistory ≡ Native.closure (fst b , root tree)
certify : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Certificate t
Certificate.tree (certify t) = t
Certificate.treeRecovery (certify t) = refl
Certificate.nodes (certify t) = nodeEvidence t
Certificate.endpoint (certify t) = endWitness (M.fold t)
Certificate.rootHistory (certify {b = b} t) = Native.closure (fst b , root t)
Certificate.rootRecovery (certify t) = refl

endpoint-coherence : {m : Mode} {a b : F.Object} (r s : M.Tree m a b)
  → EndWitness.actual (Certificate.endpoint (certify r)) ≡ EndWitness.actual (Certificate.endpoint (certify s))
endpoint-coherence r s i = F.asPackage (M.coherence r s i) , F.admitted (M.coherence r s i)

-- Root-history boundary, constructed separately in MixedRootHistoryCoherence.
-- Endpoint-coherence alone does not inhabit it: retained root Codes can differ.
RootBoundary : {m : Mode} {a b : F.Object} → M.Tree m a b → M.Tree m a b → Type
RootBoundary r s = Σ[ e ∈ (El (expression (package (root r))) ≃ El (expression (package (root s)))) ]
  (equivFun e (value (package (root r))) ≡ value (package (root s)))
  × ((x : El (expression (package (root r)))) → reader (root r) x ≡ reader (root s) (equivFun e x))
