{-# OPTIONS --safe --cubical --guardedness #-}
module CertifiedFramedCells where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isPropΣ)
open import Cubical.Data.Bool using (true; isSetBool)
open import Cubical.Data.Maybe.Base using (just)
open import NativeExtensionFamilyAudit using (Seeds)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons using (Mode; act)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
import CanonicalComparisonSynthesis as Compile
import FiniteComparisonTrees as F
import MixedHistoryCertificates as History
import MixedComparisonTrees as M
import InternalComparisonInterchange as Native
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero

Frame : Mode → F.Object → F.Object → Type
Frame m a b = act m (fst a) ≡ fst b
frame-prop : (m : Mode) (a b : F.Object) → isProp (Frame m a b)
frame-prop m a b = vertex-is-set _ _

-- The compiler works on a reindexed target, but the emitted full cell and
-- native compare-rule derivation have the ORIGINAL actual target endpoint.
module Synthesis (m : Mode) (a b : F.Object) (frame : Frame m a b) where
  moved : G.Fragment (act m (fst a))
  moved = transport (λ i → G.Fragment (frame (~ i))) (snd b)
  target-path : (act m (fst a) , moved) ≡ b
  target-path i = frame i , transport-filler (λ j → G.Fragment (frame (~ j))) (snd b) (~ i)
  module K = Compile.Compile m (snd a) moved
  Guard = K.accepted K.compile ≡ true
  guard-prop : isProp Guard
  guard-prop = isSetBool _ _
  generate : Guard → F.Full m a b
  generate ok = transport (λ i → F.Full m a (target-path i))
    (F.from-generated m (snd a) moved (K.require-success K.compile ok))
  complete : F.Full m a b → Guard
  complete f = K.complete (F.Full.payload
    (transport (λ i → F.Full m a (target-path (~ i))) f))

Admission : Mode → F.Object → F.Object → Type
Admission m a b = Σ[ frame ∈ Frame m a b ] Synthesis.Guard m a b frame
admission-prop : (m : Mode) (a b : F.Object) → isProp (Admission m a b)
admission-prop m a b = isPropΣ (frame-prop m a b) (Synthesis.guard-prop m a b)

-- A certified-input producer interface, not an unchecked Fragment import.
-- Actual endpoint histories are retained together with their existing source
-- producer certificates. Only proposition-valued frame/success guards follow.
-- No Full value, equivalence, selected-value path or reader function field.
record Program (m : Mode) (a b : F.Object) : Type₁ where
  constructor program
  field
    leftOrigin : P.Certificate (snd a)
    rightOrigin : P.Certificate (snd b)
    admitted : Admission m a b
evaluate : {m : Mode} {a b : F.Object} → Program m a b → F.Full m a b
evaluate {m} {a} {b} p = Synthesis.generate m a b (fst (Program.admitted p)) (snd (Program.admitted p))
native : {m : Mode} {a b : F.Object} → Program m a b → Closure Seeds
native p = History.endClosure (evaluate p)
record Certificate {m : Mode} {a b : F.Object} (f : F.Full m a b) : Type₁ where
  constructor certificate
  field
    producer : Program m a b
    matches : evaluate producer ≡ f
certify : {m : Mode} {a b : F.Object}
  → P.Certificate (snd a) → P.Certificate (snd b) → (f : F.Full m a b) → Certificate f
certify {m} {a} {b} ca cb f = certificate script (F.full-prop m a b (evaluate script) f)
  where
  script : Program m a b
  script = program ca cb (F.frame f , Synthesis.complete m a b (F.frame f) f)
native-match : {m : Mode} {a b : F.Object} {f : F.Full m a b} (c : Certificate f)
  → native (Certificate.producer c) ≡ History.endClosure f
native-match c = cong History.endClosure (Certificate.matches c)
operands-recovered : {m : Mode} {a b : F.Object} (p : Program m a b)
  → Native.comparisonOperands (native p)
    ≡ just (Native.closure (fst a , G.body (snd a)) , Native.closure (fst b , G.body (snd b)))
operands-recovered p = refl

-- Closure of evaluated CELL certification, not raw native-history assembly.
identity-certificate : (a : F.Object) → P.Certificate (snd a) → Certificate (F.identity a)
identity-certificate a ca = certify ca ca (F.identity a)
compose-certificate : {m n : Mode} {a b c : F.Object}
  {f : F.Full m a b} {g : F.Full n b c}
  → Certificate f → Certificate g → Certificate (F.compose f g)
compose-certificate {f = f} {g} cf cg = certify
  (Program.leftOrigin (Certificate.producer cf))
  (Program.rightOrigin (Certificate.producer cg)) (F.compose f g)
origin-attach : {a : F.Object} (ca : P.Certificate (snd a)) (o : Out (fst a))
  → P.Certificate (G.attachF (snd a) o)
origin-attach ca o = P.certificate (P.attachP (P.Certificate.producer ca) o)
  (cong (λ a → G.attachF a o) (P.Certificate.matches ca))
attach-certificate : {m : Mode} {a b : F.Object} {f : F.Full m a b}
  → Certificate f → (o : Out (fst a)) → Certificate (M.attachment f o)
attach-certificate {a = a} {b} {f} cf o = certify
  (origin-attach {a} (Program.leftOrigin (Certificate.producer cf)) o)
  (origin-attach {b} (Program.rightOrigin (Certificate.producer cf)) (M.route f o))
  (M.attachment f o)

-- Guard proofs do not add hidden choices; origin certificates themselves
-- are not erased or declared proposition-valued.
guards-irrelevant : {m : Mode} {a b : F.Object}
  (ca : P.Certificate (snd a)) (cb : P.Certificate (snd b)) (u w : Admission m a b)
  → program ca cb u ≡ program ca cb w
guards-irrelevant {m} {a} {b} ca cb u w = cong (program ca cb) (admission-prop m a b u w)
