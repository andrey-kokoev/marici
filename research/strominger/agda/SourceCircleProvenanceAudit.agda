{-# OPTIONS --safe --cubical --guardedness #-}
module SourceCircleProvenanceAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit using (Unit; tt; isPropUnit)
open import Cubical.Relation.Nullary.Base using (¬_)
import Cubical.HITs.Pushout.Base as PO
open import Cubical.HITs.Susp.Base using (Susp; S¹≃SuspBool; Unit≃SuspUnit)
open import Cubical.HITs.Susp.Properties using (congSuspEquiv)
open import Cubical.HITs.S1.Base using (S¹; loop)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import ClosureGluingTreeRegression as Circle
open import ClosureDependentRefinementTrees using (Tree; leaf; glueNode)
import CoherentDependentExtensions as General
import GeneratedReaderClassification as G
import RetainedPackageFeedback as Feedback
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; AB; BC; CA; BA; AD; DB; pointQ; Seeds; root; sigma; isB)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set; outEquiv)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Reuse the actual predecessor span. The target is the constructed pushout,
-- not an independently supplied sphere; its local realization is identity.
RawCircle : Type
RawCircle = PO.Pushout Circle.f Circle.g
rawTree : Tree RawCircle 2
rawTree = glueNode Circle.f Circle.g (idEquiv RawCircle)
  leaf Circle.boundaryTree leaf

-- A precise obstruction to a carrier-EQUIVALENCE bridge, not to a new
-- topology-changing operation, a nonfaithful realization, or arbitrary WG.
no-full-circle-equivalence : {v : Vertex} (a : G.Fragment v)
  → ¬ (G.Carrier (G.body a) ≃ Circle.Full)
no-full-circle-equivalence a e = Circle.gluedLoopNotRefl
  (G.set-through-equiv (invEquiv e) (G.carrier-set (G.normal a)) _ _ Circle.gluedLoop refl)
no-raw-circle-equivalence : {v : Vertex} (a : G.Fragment v)
  → ¬ (G.Carrier (G.body a) ≃ RawCircle)
no-raw-circle-equivalence a e = no-full-circle-equivalence a
  (compEquiv (compEquiv e Circle.circleEquiv) (invEquiv Circle.unfolded))

-- Parameter-injection control. X is an EXPLICIT input already formed in the
-- ambient foundation. Native admission does not discover X from the seed.
module Envelope (S : Complete → Type₁) (q : Complete) (d : Resolve S q)
  (qSet : isSet (El (expression q))) (X : Type) (x : X) where
  branch : X → Complete
  branch _ = path-package (expression q) (value q) (value q) refl
  branch-derived : (z : X) → Resolve S (branch z)
  branch-derived z = apply (reflexivity-rule (expression q) (value q)) (λ _ → d)
  encoded : Complete
  encoded = E-package X branch x
  derived : Resolve S encoded
  derived = apply (E-rule X branch x) (λ { (lift z) → branch-derived z })
  contractible : (z : X) → isContr (El (retained (branch z)))
  contractible z = refl , (λ p → qSet _ _ refl p)
  module Projection = General.Projection X (λ z → El (retained (branch z)))
  projection : El (expression encoded) ≃ X
  projection = isoToEquiv (Projection.contractible-projection contractible)

module NativeCircle (v : Vertex) = Envelope Seeds (pointQ v) (root v)
  vertex-is-set RawCircle (PO.inl tt)
parent-retained : (v : Vertex)
  → Feedback.peel (Feedback.peel (NativeCircle.encoded v , NativeCircle.derived v))
    ≡ (pointQ v , root v)
parent-retained v = refl
not-a-fragment-presentation : (v : Vertex) {w : Vertex} (a : G.Fragment w)
  → ¬ (G.Carrier (G.body a) ≃ El (expression (NativeCircle.encoded v)))
not-a-fragment-presentation v a e = no-raw-circle-equivalence a
  (compEquiv e (NativeCircle.projection v))

-- A DECLARED replacement seed policy for an ablation, not a new member of
-- the original Seeds. The native twelve-rule signature is unchanged.
unitQ : Complete
unitQ = pack (atom Unit) tt
data UnitSeeds : Complete → Type₁ where
  suppliedUnit : UnitSeeds unitQ
module UnitCircle = Envelope UnitSeeds unitQ (seed suppliedUnit)
  (isProp→isSet isPropUnit) RawCircle (PO.inl tt)
seed-ablation : (v : Vertex)
  → El (expression (NativeCircle.encoded v)) ≃ El (expression UnitCircle.encoded)
seed-ablation v = compEquiv (NativeCircle.projection v) (invEquiv UnitCircle.projection)

-- A SOURCE-SENSITIVE CONTRAST, not the original Body.attach interpreter:
-- choose the uniform program Unit <- Out(v) -> Unit. Both endpoints, their
-- constant maps, and use of homotopy pushout are declared additional policy.
-- The boundary itself is read from the actual six-arrow source.
Boundary : Vertex → Type
Boundary A = Bool
Boundary B = Bool
Boundary C = Unit
Boundary D = Unit
encodeOut : (v : Vertex) → Out v → Boundary v
encodeOut _ (_ , AB) = false
encodeOut _ (_ , AD) = true
encodeOut _ (_ , BA) = false
encodeOut _ (_ , BC) = true
encodeOut _ (_ , CA) = tt
encodeOut _ (_ , DB) = tt
decodeOut : (v : Vertex) → Boundary v → Out v
decodeOut A false = B , AB
decodeOut A true = D , AD
decodeOut B false = A , BA
decodeOut B true = C , BC
decodeOut C tt = A , CA
decodeOut D tt = B , DB
out-section : (v : Vertex) (x : Boundary v) → encodeOut v (decodeOut v x) ≡ x
out-section A false = refl
out-section A true = refl
out-section B false = refl
out-section B true = refl
out-section C tt = refl
out-section D tt = refl
out-retraction : (v : Vertex) (o : Out v) → decodeOut v (encodeOut v o) ≡ o
out-retraction _ (_ , AB) = refl
out-retraction _ (_ , AD) = refl
out-retraction _ (_ , BA) = refl
out-retraction _ (_ , BC) = refl
out-retraction _ (_ , CA) = refl
out-retraction _ (_ , DB) = refl
out-boundary : (v : Vertex) → Out v ≃ Boundary v
out-boundary v = isoToEquiv (iso (encodeOut v) (decodeOut v) (out-section v) (out-retraction v))
SourceSuspension : Vertex → Type
SourceSuspension v = PO.PushoutSusp (Out v)
source-suspension-classification : (v : Vertex) → SourceSuspension v ≃ Susp (Boundary v)
source-suspension-classification v = compEquiv PO.PushoutSusp≃Susp (congSuspEquiv (out-boundary v))
at-A : SourceSuspension A ≃ S¹
at-A = compEquiv (source-suspension-classification A) (invEquiv S¹≃SuspBool)
at-B : SourceSuspension B ≃ S¹
at-B = compEquiv (source-suspension-classification B) (invEquiv S¹≃SuspBool)
at-C : SourceSuspension C ≃ Unit
at-C = compEquiv (source-suspension-classification C) (invEquiv Unit≃SuspUnit)
at-D : SourceSuspension D ≃ Unit
at-D = compEquiv (source-suspension-classification D) (invEquiv Unit≃SuspUnit)

A-not-C : ¬ (SourceSuspension A ≃ SourceSuspension C)
A-not-C e = Circle.circleLoopNotRefl
  (G.set-through-equiv (compEquiv (invEquiv at-A) (compEquiv e at-C))
    (isProp→isSet isPropUnit) _ _ loop refl)
source-covariance : (v : Vertex) → SourceSuspension v ≃ SourceSuspension (sigma v)
source-covariance v = compEquiv PO.PushoutSusp≃Susp
  (compEquiv (congSuspEquiv (outEquiv v)) (invEquiv PO.PushoutSusp≃Susp))

-- Both declared policies pass the one-step source-covariance requirement,
-- yet their interpreted outputs disagree at C. This is not a claim that
-- arbitrary all-dimensional action laws have been supplied here.
constant-covariance : (v : Vertex) → RawCircle ≃ RawCircle
constant-covariance v = idEquiv RawCircle
policies-differ-at-C : ¬ (RawCircle ≃ SourceSuspension C)
policies-differ-at-C e = Circle.circleLoopNotRefl
  (G.set-through-equiv (compEquiv (invEquiv Circle.circleEquiv) (compEquiv e at-C))
    (isProp→isSet isPropUnit) _ _ loop refl)

-- The original discrete vertex reader cannot descend while distinguishing
-- endpoints now connected by a newly adjoined path. Edge labels remain in
-- the construction; preserving them as discrete value observations is a
-- different requirement, which this new realization cannot silently inherit.
no-old-discrete-ports : (read : SourceSuspension A → Vertex)
  → read (PO.inl tt) ≡ A → ¬ (read (PO.inr tt) ≡ B)
no-old-discrete-ports read left right = false≢true
  (cong isB (sym left ∙ cong read (PO.push (B , AB)) ∙ right))

-- Same original native Seeds/rules admit this explicitly chosen parameter
-- program too. That extends the ADAPTER menu, not the native rule datatype.
module NativeSuspension (v : Vertex) = Envelope Seeds (pointQ v) (root v)
  vertex-is-set (SourceSuspension v) (PO.inl tt)
