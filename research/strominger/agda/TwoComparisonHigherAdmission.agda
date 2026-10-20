{-# OPTIONS --safe --cubical --guardedness #-}
module TwoComparisonHigherAdmission where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetRetract)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import TwoComparisonTwoAttachmentCoherence as T
import HigherWitnessAdmission as H
import CoherentDependentExtensions as General
open import NativeExtensionFamilyAudit using (Vertex; Seeds)
open import InternalSourceComparisons using (Body; package; derivation)
open import InternalComparisonInterchange using (graphEquiv)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

branch : T.CompleteFiller → Complete
branch f = path-package (expression (package (T.asBody f)))
  (value (package (T.asBody f))) (value (package (T.asBody f))) refl
branch-derived : (f : T.CompleteFiller) → Resolve Seeds (branch f)
branch-derived f = apply
  (reflexivity-rule (expression (package (T.asBody f))) (value (package (T.asBody f))))
  (λ _ → derivation (T.asBody f))
EnvelopeCode : Code
EnvelopeCode = E T.CompleteFiller (λ f → retained (branch f))
envelope : T.CompleteFiller → Complete
envelope f = E-package T.CompleteFiller branch f
envelope-derived : (f : T.CompleteFiller) → Resolve Seeds (envelope f)
envelope-derived f = apply (E-rule T.CompleteFiller branch f)
  (λ { (lift g) → branch-derived g })
abstract
  setViaEquiv : {X Y : Type} → X ≃ Y → isSet Y → isSet X
  setViaEquiv e = isSetRetract (equivFun e) (invEq e) (retEq e)
  source-is-set : isSet (El (expression (package T.source)))
  source-is-set = setViaEquiv T.direct T.target-is-set
  comparison-is-set : (f : T.CompleteFiller) → isSet (El (expression (package (T.asBody f))))
  comparison-is-set f = setViaEquiv (graphEquiv (fst f)) source-is-set
branch-contractible : (f : T.CompleteFiller) → isContr (El (retained (branch f)))
branch-contractible f = refl , (λ p → comparison-is-set f _ _ refl p)
module Projection = General.Projection T.CompleteFiller (λ f → El (retained (branch f)))
envelopeEquiv : El EnvelopeCode ≃ T.CompleteFiller
envelopeEquiv = isoToEquiv (Projection.contractible-projection branch-contractible)
left right : El EnvelopeCode
left = value (envelope T.sequentialFiller)
right = value (envelope T.directFiller)
envelopePath : left ≡ right
envelopePath i = T.filler-coherence i , refl
path-recovery : cong fst envelopePath ≡ T.filler-coherence
path-recovery = refl
admittedPathPackage : Complete
admittedPathPackage = path-package EnvelopeCode left right envelopePath
module Admit = H.PathAdmission Seeds
admitted-higher : Resolve Seeds admittedPathPackage
admitted-higher = Admit.from-derived-point EnvelopeCode left
  (envelope-derived T.sequentialFiller) envelopePath

-- The new filler likewise does not acquire literal atomic Code admission.
barePackage : Complete
barePackage = path-package (atom T.CompleteFiller) T.sequentialFiller T.directFiller T.filler-coherence
bare-not-admitted : ¬ (Resolve Seeds barePackage)
bare-not-admitted d = false≢true (sym (H.resolution-spine d))

nativeDiagram : List (Σ Vertex Body) → List (Closure Seeds)
nativeDiagram [] = []
nativeDiagram ((v , b) ∷ bs) = (package b , derivation b) ∷ nativeDiagram bs
-- The higher envelope's Code retains the full filler family, and its value
-- retains the higher path. Raw Bodies additionally preserve the port policy.
retainedClosures : List (Closure Seeds)
retainedClosures = (envelope T.sequentialFiller , envelope-derived T.sequentialFiller)
  ∷ (envelope T.directFiller , envelope-derived T.directFiller)
  ∷ (admittedPathPackage , admitted-higher) ∷ nativeDiagram T.diagram
Payload : Type₁
Payload = List (Σ Vertex Body) × List (Closure Seeds)
certificate : Payload
certificate = T.diagram , retainedClosures
reified : Whole.Universe.Complete (ℓ-suc ℓ-zero)
reified = Whole.Universe.pack (Whole.Universe.atom Payload) certificate
recovery : Whole.Universe.value reified ≡ certificate
recovery = refl
