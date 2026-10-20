{-# OPTIONS --safe --cubical --guardedness #-}
module HigherWitnessAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Foundations.HLevels using (isSetRetract; isSetΣ)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import NativeExtensionFamilyAudit as Native
import RepeatedInterchangeCoherence as R
import CoherentDependentExtensions as General
open import SourceIndexedExtensionFamilies using (vertex-is-set)
open import InternalSourceComparisons using (Body; package; derivation; attach; seedBody)
open import InternalComparisonInterchange using (graphIso)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero
open Native using (Seeds; Vertex; A; B)

-- A Boolean observation of Code is stable under its actual paths. Unlike
-- inspecting a fixed indexed seed proof, this invariant needs no axiom K.
atomicSpine : Code → Bool
atomicSpine (atom _) = true
atomicSpine (paths Q _ _) = atomicSpine Q
atomicSpine _ = false
seed-spine : {q : Complete} → Seeds q → atomicSpine (expression q) ≡ false
seed-spine (Native.source v) = refl
rule-spine : (r : Rule)
  → ((i : Arity r) → atomicSpine (expression (input r i)) ≡ false)
  → atomicSpine (expression (output r)) ≡ false
rule-spine (E-rule _ _ _) ds = refl
rule-spine (Pi-rule _ _) ds = refl
rule-spine (compare-rule _ _ _ _) ds = refl
rule-spine (identity-rule _) ds = refl
rule-spine (inverse-rule _ _ _ _) ds = refl
rule-spine (compose-rule _ _ _ _ _ _ _) ds = refl
rule-spine (higher-rule _ _ _ _ _ _) ds = ds (lift true)
rule-spine (reflexivity-rule _ _) ds = ds (lift tt)
rule-spine (path-lift-rule _ _ _ _ _) ds = refl
rule-spine (distribution-rule _ _ _ _) ds = refl
rule-spine (E-congruence-rule _ _ _ _ _ _) ds = refl
rule-spine (Pi-congruence-rule _ _ _ _ _) ds = refl
resolution-spine : {q : Complete} → Resolve Seeds q → atomicSpine (expression q) ≡ false
resolution-spine (seed s) = seed-spine s
resolution-spine (apply r ds) = rule-spine r (λ i → resolution-spine (ds i))

-- The EXACT formerly formed bare atomic path package is not reachable.
exact-atomic-path-not-admitted : ¬ (Resolve Seeds R.higher-package-formed)
exact-atomic-path-not-admitted d = false≢true (sym (resolution-spine d))

-- Existing reflexivity plus ordinary dependent transport already admits any
-- supplied path out of an ACTUALLY derived pointed package. No rule is added.
module PathAdmission (S : Complete → Type₁) where
  from-derived-point : (Q : Code) (x : El Q) → Resolve S (pack Q x)
    → {y : El Q} (p : x ≡ y) → Resolve S (path-package Q x y p)
  from-derived-point Q x d = J
    (λ y p → Resolve S (path-package Q x y p))
    (apply (reflexivity-rule Q x) (λ _ → d))

-- Each complete filler already gives an actual native comparison derivation.
-- Derive its reflexive witness, retaining its full comparison package in Code.
branch : R.CompleteFiller → Complete
branch f = path-package (expression (package (R.asBody f)))
  (value (package (R.asBody f))) (value (package (R.asBody f))) refl
branch-derived : (f : R.CompleteFiller) → Resolve Seeds (branch f)
branch-derived f = apply
  (reflexivity-rule (expression (package (R.asBody f))) (value (package (R.asBody f))))
  (λ _ → derivation (R.asBody f))

EnvelopeCode : Code
EnvelopeCode = E R.CompleteFiller (λ f → retained (branch f))
envelope : R.CompleteFiller → Complete
envelope f = E-package R.CompleteFiller branch f
envelope-derived : (f : R.CompleteFiller) → Resolve Seeds (envelope f)
envelope-derived f = apply (E-rule R.CompleteFiller branch f)
  (λ { (lift g) → branch-derived g })

-- Prove the envelope does not add independent value-level choices in THIS
-- diagram: each extra reflexive branch fiber is contractible.
firstSource-is-set : isSet (El (expression (package (attach (seedBody A) R.first))))
firstSource-is-set = isSetΣ (R.out-is-set A)
  (λ _ → isProp→isSet (vertex-is-set A A))
secondSource-is-set : isSet
  (El (expression (package (attach (attach (seedBody A) R.first) R.second))))
secondSource-is-set = isSetΣ (R.out-is-set B)
  (λ _ → isProp→isSet (firstSource-is-set _ _))
source-is-set : isSet (El (expression (package R.source)))
source-is-set = isSetRetract (Iso.fun (graphIso (R.Second.attachmentEquiv R.second)))
  (Iso.inv (graphIso (R.Second.attachmentEquiv R.second)))
  (Iso.leftInv (graphIso (R.Second.attachmentEquiv R.second))) secondSource-is-set
comparison-is-set : (f : R.CompleteFiller) → isSet (El (expression (package (R.asBody f))))
comparison-is-set f = isSetRetract (Iso.fun (graphIso (fst f)))
  (Iso.inv (graphIso (fst f))) (Iso.leftInv (graphIso (fst f))) source-is-set
branch-contractible : (f : R.CompleteFiller) → isContr (El (retained (branch f)))
branch-contractible f = refl , (λ p → comparison-is-set f _ _ refl p)
module Projection = General.Projection R.CompleteFiller (λ f → El (retained (branch f)))
envelopeEquiv : El EnvelopeCode ≃ R.CompleteFiller
envelopeEquiv = isoToEquiv (Projection.contractible-projection branch-contractible)

left right : El EnvelopeCode
left = value (envelope R.sequentialFiller)
right = value (envelope R.directFiller)
envelopePath : left ≡ right
envelopePath i = R.filler-coherence i , refl
path-recovery : cong fst envelopePath ≡ R.filler-coherence
path-recovery = refl
admittedPathPackage : Complete
admittedPathPackage = path-package EnvelopeCode left right envelopePath
module AdmitPath = PathAdmission Seeds
admitted-higher-witness : Resolve Seeds admittedPathPackage
admitted-higher-witness = AdmitPath.from-derived-point EnvelopeCode left
  (envelope-derived R.sequentialFiller) envelopePath

-- The same argument admits the target endpoint; both complete E inputs and
-- every comparison premise in the family use the unchanged source policy.
admitted-right : Resolve Seeds (envelope R.directFiller)
admitted-right = envelope-derived R.directFiller

-- An explicit subsequent higher-rule control: once both envelope path
-- packages are derived, their supplied right-unit coherence is admitted by
-- the UNCHANGED native higher schema. This is distinct from the original
-- repeated-interchange witness, already admitted above in its envelope.
normalizedPath : left ≡ right
normalizedPath = envelopePath ∙ refl
normalized-derived : Resolve Seeds (path-package EnvelopeCode left right normalizedPath)
normalized-derived = AdmitPath.from-derived-point EnvelopeCode left
  (envelope-derived R.sequentialFiller) normalizedPath
nextHigherPackage : Complete
nextHigherPackage = higher-package EnvelopeCode left right envelopePath normalizedPath (rUnit envelopePath)
next-higher-derived : Resolve Seeds nextHigherPackage
next-higher-derived = apply
  (higher-rule EnvelopeCode left right envelopePath normalizedPath (rUnit envelopePath))
  (λ { (lift true) → admitted-higher-witness ; (lift false) → normalized-derived })

record AdmissionCertificate : Type₁ where
  field
    original : R.Certificate
    leftDerivation : Resolve Seeds (envelope R.sequentialFiller)
    rightDerivation : Resolve Seeds (envelope R.directFiller)
    higherDerivation : Resolve Seeds admittedPathPackage
    nextHigherDerivation : Resolve Seeds nextHigherPackage
    recoveredHigher : cong fst (value admittedPathPackage) ≡ R.filler-coherence
certificate : AdmissionCertificate
AdmissionCertificate.original certificate = R.certificate
AdmissionCertificate.leftDerivation certificate = envelope-derived R.sequentialFiller
AdmissionCertificate.rightDerivation certificate = admitted-right
AdmissionCertificate.higherDerivation certificate = admitted-higher-witness
AdmissionCertificate.nextHigherDerivation certificate = next-higher-derived
AdmissionCertificate.recoveredHigher certificate = path-recovery
reified : Whole.Universe.Complete (ℓ-suc ℓ-zero)
reified = Whole.Universe.pack (Whole.Universe.atom AdmissionCertificate) certificate
recovery : Whole.Universe.value reified ≡ certificate
recovery = refl
