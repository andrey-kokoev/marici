{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardCertifiedPrograms where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool using (true; isSetBool)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; AB; BC; Seeds; pointQ; root; sigma)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using (Body; Mode; act; package)
import InternalComparisonInterchange as Native
import SourceCertifiedPrograms as Old
import GeneratedReaderClassification as G
import CanonicalComparisonSynthesis as Compile
import RetainedFeedbackCovariance as Move
import ForwardForwardBodyBinding as Forward
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero

-- A successor grammar, not a reinterpretation of the old root-only grammar.
-- The only new initial-proof operation is the EXISTING chosen forward lift.
data Initial : Vertex → Type where
  rootI : (v : Vertex) → Initial v
  forwardI : {v : Vertex} → Initial v → Initial (sigma v)
runInitial : {v : Vertex} → Initial v → Resolve Seeds (pointQ v)
runInitial (rootI v) = root v
runInitial (forwardI {v} p) = Move.moveInitial v (runInitial p)
record InitialCertificate (v : Vertex) (d : Resolve Seeds (pointQ v)) : Type₁ where
  constructor initial-certificate
  field
    initialProducer : Initial v
    initialMatches : runInitial initialProducer ≡ d
forward-certificate : {v : Vertex} {d : Resolve Seeds (pointQ v)}
  → InitialCertificate v d → InitialCertificate (sigma v) (Move.moveInitial v d)
forward-certificate {v} (initial-certificate p eq) =
  initial-certificate (forwardI p) (cong (Move.moveInitial v) eq)

mutual
  data Program : Vertex → Type₁ where
    initialP : {v : Vertex} → Initial v → Program v
    legacyP : {v : Vertex} → Old.Program v → Program v
    attachP : {v : Vertex} (p : Program v) (o : Out v) → Program (fst o)
    compareP : (m : Mode) {v : Vertex} (p : Program v) (q : Program (act m v))
      → Compile.Compile.accepted m (decode p) (decode q)
          (Compile.Compile.compile m (decode p) (decode q)) ≡ true
      → Program (act m v)
  decode : {v : Vertex} → Program v → G.Fragment v
  decode (initialP {v} p) = G.start v (runInitial p)
  decode (legacyP p) = Old.decode p
  decode (attachP p o) = G.attachF (decode p) o
  decode (compareP m p q ok) = K.next (K.require-success K.compile ok)
    where module K = Compile.Compile m (decode p) (decode q)
native : {v : Vertex} (p : Program v) → Resolve Seeds (package (G.body (decode p)))
native p = G.native (decode p)
legacy-native-match : {v : Vertex} (p : Old.Program v) → native (legacyP p) ≡ Old.native p
legacy-native-match p = refl
module Pair (m : Mode) {v : Vertex} (p : Program v) (q : Program (act m v)) where
  module K = Compile.Compile m (decode p) (decode q)
  Guard = K.accepted K.compile ≡ true
  guard-prop : isProp Guard
  guard-prop = isSetBool _ _
  guard-irrelevant : (u w : Guard) → compareP m p q u ≡ compareP m p q w
  guard-irrelevant u w = cong (compareP m p q) (guard-prop u w)
record Certificate {v : Vertex} (a : G.Fragment v) : Type₁ where
  constructor certificate
  field
    producer : Program v
    matches : decode producer ≡ a
native-closure-match : {v : Vertex} {a : G.Fragment v} (c : Certificate a)
  → Path (Closure Seeds)
    (package (G.body (decode (Certificate.producer c))) , native (Certificate.producer c))
    (package (G.body a) , G.native a)
native-closure-match c i = package (G.body (Certificate.matches c i)) , G.native (Certificate.matches c i)

-- Existing compatible cells are matched to computed canonical cells. The
-- producer stores ONLY the compiler's proposition-valued success guard,
-- not the supplied filler. This is producibility, not unique historical origin.
abstract
  compare-certificate : (m : Mode) {v : Vertex} {a : G.Fragment v} {b : G.Fragment (act m v)}
    → Certificate a → Certificate b → (f : G.Comparisons.Filler m a b)
    → Certificate (Forward.cmp m a b f)
  compare-certificate m {v} {a} {b} ca cb f = certificate generated (canonical ∙ endpoint)
    where
    pa : Program v
    pa = Certificate.producer ca
    pb : Program (act m v)
    pb = Certificate.producer cb
    ea : decode pa ≡ a
    ea = Certificate.matches ca
    eb : decode pb ≡ b
    eb = Certificate.matches cb
    Family : I → Type
    Family i = G.Comparisons.Filler m (ea (~ i)) (eb (~ i))
    initialFiller : G.Comparisons.Filler m (decode pa) (decode pb)
    initialFiller = transport (λ i → Family i) f
    module K = Compile.Compile m (decode pa) (decode pb)
    ok : K.accepted K.compile ≡ true
    ok = K.complete initialFiller
    generated : Program (act m v)
    generated = compareP m pa pb ok
    canonical : decode generated ≡ Forward.cmp m (decode pa) (decode pb) initialFiller
    canonical = cong K.next (K.C.filler-prop (K.require-success K.compile ok) initialFiller)
    endpoint : Forward.cmp m (decode pa) (decode pb) initialFiller ≡ Forward.cmp m a b f
    endpoint i = Forward.cmp m (ea i) (eb i) (transport-filler (λ j → Family j) f (~ i))

-- A precise origin obligation for every actual initial proof in a fragment.
-- There is no constructor/function giving this for arbitrary Resolve inputs.
Origins : {v : Vertex} → G.Fragment v → Type₁
Origins (G.start v d) = InitialCertificate v d
Origins (G.attachF a o) = Origins a
Origins (G.compareF m a b e p h) = Origins a × Origins b
legacy-origins : {v : Vertex} (p : Old.Program v) → Origins (Old.decode p)
legacy-origins (Old.seedP v) = initial-certificate (rootI v) refl
legacy-origins (Old.attachP p o) = legacy-origins p
legacy-origins (Old.compareP m p q ok) = legacy-origins p , legacy-origins q
producer-origins : {v : Vertex} (p : Program v) → Origins (decode p)
producer-origins (initialP p) = initial-certificate p refl
producer-origins (legacyP p) = legacy-origins p
producer-origins (attachP p o) = producer-origins p
producer-origins (compareP m p q ok) = producer-origins p , producer-origins q
origins-of-certificate : {v : Vertex} {a : G.Fragment v} → Certificate a → Origins a
origins-of-certificate c = subst Origins (Certificate.matches c) (producer-origins (Certificate.producer c))
certify : {v : Vertex} (a : G.Fragment v) → Origins a → Certificate a
certify (G.start v d) (initial-certificate p eq) = certificate (initialP p) (cong (G.start v) eq)
certify (G.attachF a o) origin = certificate (attachP (Certificate.producer c) o)
  (cong (λ a → G.attachF a o) (Certificate.matches c))
  where c = certify a origin
certify (G.compareF m a b e p h) (oa , ob) = compare-certificate m (certify a oa) (certify b ob) (e , p , h)

record Entry (original : Σ Vertex Body) : Type₁ where
  constructor entry
  field
    entryProgram : Program (fst original)
    entryMatches : Native.closure (fst original , G.body (decode entryProgram)) ≡ Native.closure original
asEntry : {v : Vertex} {a : G.Fragment v} → Certificate a → Entry (v , G.body a)
asEntry c = entry (Certificate.producer c) (native-closure-match c)
data AllCertified : List (Σ Vertex Body) → Type₁ where
  nilC : AllCertified []
  _∷C_ : {x : Σ Vertex Body} {xs : List (Σ Vertex Body)} → Entry x → AllCertified xs → AllCertified (x ∷ xs)
infixr 5 _∷C_

-- Bind the EXACT old d/d1/d2 diagram in an EXPLICIT certified input context.
-- There is no function supplying c0 for arbitrary d. Forward transports are
-- retained as originally defined, never reset to the old root proof.
module Diagram (d : Resolve Seeds (pointQ A)) (c0 : InitialCertificate A d) where
  module D = Forward.Diagram d
  c1 : InitialCertificate B D.d1
  c1 = forward-certificate c0
  c2 : InitialCertificate A D.d2
  c2 = forward-certificate c1
  sourceOrigins : Origins D.source
  sourceOrigins = (c0 , c1) , c2
  targetOrigins : Origins D.target
  targetOrigins = (c0 , c1) , c2
  source-certificate : Certificate D.source
  source-certificate = certify D.source sourceOrigins
  target-certificate : Certificate D.target
  target-certificate = certify D.target targetOrigins
  sequential-certificate : Certificate D.sequentialTerm
  sequential-certificate = certify D.sequentialTerm (sourceOrigins , targetOrigins)
  direct-certificate : Certificate D.directTerm
  direct-certificate = certify D.directTerm (sourceOrigins , targetOrigins)
  actual-second-forward : runInitial (forwardI (forwardI (InitialCertificate.initialProducer c0))) ≡ D.d2
  actual-second-forward = InitialCertificate.initialMatches c2
  certified-diagram : AllCertified D.diagram
  certified-diagram =
    asEntry (certify D.a0 c0) ∷C asEntry (certify D.a1 c1) ∷C asEntry (certify D.a2 c2)
    ∷C asEntry (certify D.q1 (c0 , c1)) ∷C asEntry (certify D.q2 ((c0 , c1) , c2))
    ∷C asEntry (certify D.FirstRow.firstCellTerm ((c0 , c1) , (c0 , c1)))
    ∷C asEntry (certify D.FirstRow.secondCellTerm ((c0 , c1) , (c0 , c1)))
    ∷C asEntry (certify D.SecondRow.firstCellTerm (sourceOrigins , targetOrigins))
    ∷C asEntry (certify D.SecondRow.secondCellTerm (sourceOrigins , targetOrigins))
    ∷C asEntry (certify D.FirstRow.source (c0 , c1))
    ∷C asEntry (certify D.FirstRow.target (c0 , c1))
    ∷C asEntry source-certificate ∷C asEntry (certify D.SecondRow.source sourceOrigins)
    ∷C asEntry target-certificate ∷C asEntry sequential-certificate ∷C asEntry direct-certificate ∷C nilC

module GeneratedDiagram (p : Initial A) = Diagram (runInitial p) (initial-certificate p refl)
