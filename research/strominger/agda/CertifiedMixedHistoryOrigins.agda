{-# OPTIONS --safe --cubical --guardedness #-}
module CertifiedMixedHistoryOrigins where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map)
open import NativeExtensionFamilyAudit using (Vertex; A; C; Seeds; pointQ)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using (Body; Mode; stay)
import ForwardCertifiedPrograms as P
import CertifiedFramedCells as Cell
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import MixedHistoryCertificates as H
import NativeComposeHistoryBridge as Join
import NativeAttachmentHistoryBridge as Attach
import InternalComparisonInterchange as Native
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero

-- Obligations cover EVERY original node, not merely the outer endpoints.
-- Leaf certificates match computed full parameters; units require origins too.
CoreOrigins : {m : Mode} {a b : F.Object} → F.Tree m a b → Type₁
CoreOrigins (F.cell f) = Cell.Certificate f
CoreOrigins (F.unit a) = P.Certificate (snd a)
CoreOrigins (F.then r s) = CoreOrigins r × CoreOrigins s
coreCell : {m : Mode} {a b : F.Object} (t : F.Tree m a b) → CoreOrigins t → Cell.Certificate (F.fold t)
coreCell (F.cell f) c = c
coreCell (F.unit a) c = Cell.identity-certificate a c
coreCell (F.then r s) (cr , cs) = Cell.compose-certificate (coreCell r cr) (coreCell s cs)
Origins : {m : Mode} {a b : F.Object} → M.Tree m a b → Type₁
Origins (M.old t) = CoreOrigins t
Origins (M.join r s) = Origins r × Origins s
Origins (M.attach t o) = Origins t
foldCell : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Origins t → Cell.Certificate (M.fold t)
foldCell (M.old t) c = coreCell t c
foldCell (M.join r s) (cr , cs) = Cell.compose-certificate (foldCell r cr) (foldCell s cs)
foldCell (M.attach t o) c = Cell.attach-certificate (foldCell t c) o

-- Native operations on certified full-cell inputs. Parameters are EVALUATED
-- from their framed producers, not taken unchecked from the original cells.
data Kind : Type where
  history bridge : Kind
joinValue : {m n : Mode} {a b c : F.Object}
  → F.Full m a b → F.Full n b c → Kind → Σ Vertex Body
joinValue {c = c} f g history = fst c , Join.Bridge.retainedBody f g
joinValue {c = c} f g bridge = fst c , Join.Bridge.bridgeBody f g
attachValue : {m : Mode} {a b : F.Object} → F.Full m a b → Out (fst a) → Kind → Σ Vertex Body
attachValue f o history = fst (M.route f o) , Attach.Bridge.retainedBody f o
attachValue f o bridge = fst (M.route f o) , Attach.Bridge.bridgeBody f o
data Program : Type₁ where
  endP : {m : Mode} {a b : F.Object} {f : F.Full m a b} → Cell.Certificate f → Program
  joinP : {m n : Mode} {a b c : F.Object} {f : F.Full m a b} {g : F.Full n b c}
    → Cell.Certificate f → Cell.Certificate g → Kind → Program
  attachP : {m : Mode} {a b : F.Object} {f : F.Full m a b}
    → Cell.Certificate f → Out (fst a) → Kind → Program
value : {m : Mode} {a b : F.Object} {f : F.Full m a b} → Cell.Certificate f → F.Full m a b
value c = Cell.evaluate (Cell.Certificate.producer c)
decode : Program → Σ Vertex Body
decode (endP {b = b} c) = fst b , H.compiledView (value c)
decode (joinP cf cg k) = joinValue (value cf) (value cg) k
decode (attachP cf o k) = attachValue (value cf) o k
native : Program → Closure Seeds
native p = Native.closure (decode p)
record Certificate (original : Σ Vertex Body) : Type₁ where
  constructor certificate
  field
    producer : Program
    matches : decode producer ≡ original
native-match : {original : Σ Vertex Body} (c : Certificate original)
  → native (Certificate.producer c) ≡ Native.closure original
native-match c = cong Native.closure (Certificate.matches c)
endCertificate : {m : Mode} {a b : F.Object} {f : F.Full m a b}
  → Cell.Certificate f → Certificate (fst b , H.compiledView f)
endCertificate {b = b} cf = certificate (endP cf)
  (cong (λ f → fst b , H.compiledView f) (Cell.Certificate.matches cf))
joinCertificate : {m n : Mode} {a b c : F.Object} {f : F.Full m a b} {g : F.Full n b c}
  → Cell.Certificate f → Cell.Certificate g → (k : Kind) → Certificate (joinValue f g k)
joinCertificate cf cg k = certificate (joinP cf cg k)
  (cong₂ (λ f g → joinValue f g k) (Cell.Certificate.matches cf) (Cell.Certificate.matches cg))
attachCertificate : {m : Mode} {a b : F.Object} {f : F.Full m a b}
  → Cell.Certificate f → (o : Out (fst a)) (k : Kind) → Certificate (attachValue f o k)
attachCertificate cf o k = certificate (attachP cf o k)
  (cong (λ f → attachValue f o k) (Cell.Certificate.matches cf))

coreRoot : {m : Mode} {a b : F.Object} (t : F.Tree m a b) → CoreOrigins t
  → Certificate (fst b , H.coreRoot t)
coreRoot (F.cell f) c = endCertificate c
coreRoot (F.unit a) c = endCertificate (Cell.identity-certificate a c)
coreRoot (F.then r s) (cr , cs) = joinCertificate (coreCell r cr) (coreCell s cs) history
root : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Origins t
  → Certificate (fst b , H.root t)
root (M.old t) c = coreRoot t c
root (M.join r s) (cr , cs) = joinCertificate (foldCell r cr) (foldCell s cs) history
root (M.attach t o) c = attachCertificate (foldCell t c) o history

-- An exact traversal retains both subtrees, each local raw history, bridge
-- and compiled endpoint output. Parents continue to consume compiled cells.
corePacket : {m : Mode} {a b : F.Object} → F.Tree m a b → List (Σ Vertex Body)
corePacket (F.cell f) = (_ , H.compiledView f) ∷ []
corePacket (F.unit a) = (fst a , H.compiledView (F.identity a)) ∷ []
corePacket (F.then r s) = corePacket r ++ (corePacket s ++
  (joinValue (F.fold r) (F.fold s) history ∷ joinValue (F.fold r) (F.fold s) bridge
  ∷ (_ , H.compiledView (F.compose (F.fold r) (F.fold s))) ∷ []))
packet : {m : Mode} {a b : F.Object} → M.Tree m a b → List (Σ Vertex Body)
packet (M.old t) = corePacket t
packet (M.join r s) = packet r ++ (packet s ++
  (joinValue (M.fold r) (M.fold s) history ∷ joinValue (M.fold r) (M.fold s) bridge
  ∷ (_ , H.compiledView (F.compose (M.fold r) (M.fold s))) ∷ []))
packet (M.attach t o) = packet t ++ (attachValue (M.fold t) o history
  ∷ attachValue (M.fold t) o bridge ∷ (_ , H.compiledView (M.attachment (M.fold t) o)) ∷ [])
data AllCertified : List (Σ Vertex Body) → Type₁ where
  nilC : AllCertified []
  _∷C_ : {x : Σ Vertex Body} {xs : List (Σ Vertex Body)}
    → Certificate x → AllCertified xs → AllCertified (x ∷ xs)
infixr 5 _∷C_
append : {xs ys : List (Σ Vertex Body)} → AllCertified xs → AllCertified ys → AllCertified (xs ++ ys)
append nilC ys = ys
append (c ∷C cs) ys = c ∷C append cs ys
coreCertified : {m : Mode} {a b : F.Object} (t : F.Tree m a b) → CoreOrigins t → AllCertified (corePacket t)
coreCertified (F.cell f) c = endCertificate c ∷C nilC
coreCertified (F.unit a) c = endCertificate (Cell.identity-certificate a c) ∷C nilC
coreCertified (F.then r s) (cr , cs) = append (coreCertified r cr) (append (coreCertified s cs)
  (joinCertificate (coreCell r cr) (coreCell s cs) history
  ∷C joinCertificate (coreCell r cr) (coreCell s cs) bridge
  ∷C endCertificate (coreCell (F.then r s) (cr , cs)) ∷C nilC))
certified : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Origins t → AllCertified (packet t)
certified (M.old t) c = coreCertified t c
certified (M.join r s) (cr , cs) = append (certified r cr) (append (certified s cs)
  (joinCertificate (foldCell r cr) (foldCell s cs) history
  ∷C joinCertificate (foldCell r cr) (foldCell s cs) bridge
  ∷C endCertificate (foldCell (M.join r s) (cr , cs)) ∷C nilC))
certified (M.attach t o) c = append (certified t c)
  (attachCertificate (foldCell t c) o history ∷C attachCertificate (foldCell t c) o bridge
  ∷C endCertificate (foldCell (M.attach t o) c) ∷C nilC)
compileList : {xs : List (Σ Vertex Body)} → AllCertified xs → List Program
compileList nilC = []
compileList (c ∷C cs) = Certificate.producer c ∷ compileList cs
list-match : {xs : List (Σ Vertex Body)} (cs : AllCertified xs)
  → map native (compileList cs) ≡ map Native.closure xs
list-match nilC = refl
list-match (c ∷C cs) = cong₂ _∷_ (native-match c) (list-match cs)

-- Common-witness bundle: source evidence and old native history/recovery
-- evidence refer to the SAME unchanged tree. No bare Tree import is accepted.
record CertifiedTree {m : Mode} {a b : F.Object} (t : M.Tree m a b) : Type₁ where
  field
    origins : Origins t
    historyEvidence : H.Certificate t
    rootProducer : Certificate (fst b , H.root t)
    nodes : AllCertified (packet t)
assemble : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Origins t → CertifiedTree t
CertifiedTree.origins (assemble t o) = o
CertifiedTree.historyEvidence (assemble t o) = H.certify t
CertifiedTree.rootProducer (assemble t o) = root t o
CertifiedTree.nodes (assemble t o) = certified t o

-- Non-vacuous common-context instance: an imported core composition, a mixed
-- join and a derived attachment, using the ACTUAL named forward endpoints.
module Forward (d : Resolve Seeds (pointQ A)) (c0 : P.InitialCertificate A d) (o : Out C) where
  module D = P.Diagram d c0
  a b : F.Object
  a = C , D.D.source
  b = C , D.D.target
  f : F.Full stay a b
  f = F.from-generated stay D.D.source D.D.target D.D.sequential
  core : F.Tree stay a b
  core = F.then (F.cell f) (F.unit b)
  t : M.Tree stay a b
  t = M.join (M.old core) (M.old (F.unit b))
  origin : Origins t
  origin = (Cell.certify D.source-certificate D.target-certificate f , D.target-certificate)
    , D.target-certificate
  example : CertifiedTree (M.attach t o)
  example = assemble (M.attach t o) origin
  programs : List Program
  programs = compileList (CertifiedTree.nodes example)
  actual-packet-match : map native programs ≡ map Native.closure (packet (M.attach t o))
  actual-packet-match = list-match (CertifiedTree.nodes example)
