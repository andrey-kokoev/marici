{-# OPTIONS --safe --cubical --guardedness #-}
module NewtonianTidalRoutes where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Int.Base using (ℤ; pos; _·_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Sigma.Base using (_×_)
open import NewtonianTidalKernel
open import NewtonianTidalFixture
open import NewtonianPotentialJet
import NewtonianTidalCertificate as Prior
import WholePackageSigmaPi as Whole
import WholePackageResolution as RRC

-- Exhaustive entries of a second jet: value, three first derivatives,
-- and all nine second derivatives. No continuum differentiability claim.
entries : Jet → List ℤ
entries j = potential j ∷ gradient j x ∷ gradient j y ∷ gradient j z ∷
  hessian j x x ∷ hessian j x y ∷ hessian j x z ∷
  hessian j y x ∷ hessian j y y ∷ hessian j y z ∷
  hessian j z x ∷ hessian j z y ∷ hessian j z z ∷ []

normalizationA : entries (normalizationResidual (direction a)) ≡ entries (constant (pos 64))
normalizationA = refl
normalizationB : entries (normalizationResidual (direction b)) ≡ entries (constant (pos 64))
normalizationB = refl
positiveBranches : (potential (inverseRadius8 (direction a)) ≡ pos 8) ×
                   (potential (inverseRadius8 (direction b)) ≡ pos 8)
positiveBranches = refl , refl

-- Compare in the SAME denominator 8*1728. Integer tensor scaling is NOT
-- asserted to be an equivalence of all integer tensors.
geometric8 : Tensor
geometric8 i j = pos 8 · tidal a b i j
routeComponent : (i j : Axis) → potentialTotal8 a b i j ≡ geometric8 i j
routeComponent x x = refl
routeComponent x y = refl
routeComponent x z = refl
routeComponent y x = refl
routeComponent y y = refl
routeComponent y z = refl
routeComponent z x = refl
routeComponent z y = refl
routeComponent z z = refl
routeAgreement : potentialTotal8 a b ≡ geometric8
routeAgreement = funExt (λ i → funExt (routeComponent i))

open Whole.Universe ℓ-zero
open RRC.Generators ℓ-zero

-- Distinct retained presentations: polynomial jet vs direct geometry.
data Route : Type where
  differentiated-potential direct-geometry : Route
routeCode : Route → Code
routeCode r = retain (atom Route) r
  (retain (atom (Source × Source)) (a , b)
    (retain (atom ℤ) (pos 8 · denominator) (atom Tensor)))
adPackage directPackage : Complete
adPackage = pack (routeCode differentiated-potential) (potentialTotal8 a b)
directPackage = pack (routeCode direct-geometry) geometric8

record RouteEvidence : Type where
  constructor routeEvidence
  field
    priorEvidence : Prior.Evidence
    normalizedA : entries (normalizationResidual (direction a)) ≡ entries (constant (pos 64))
    normalizedB : entries (normalizationResidual (direction b)) ≡ entries (constant (pos 64))
    branches : (potential (inverseRadius8 (direction a)) ≡ pos 8) ×
               (potential (inverseRadius8 (direction b)) ≡ pos 8)
    agreement : potentialTotal8 a b ≡ geometric8

evidencePackage : Complete
evidencePackage = pack (atom RouteEvidence)
  (routeEvidence (value Prior.evidencePackage)
    normalizationA normalizationB positiveBranches routeAgreement)

data Seeds : Complete → Type₁ where
  ad-seed : Seeds adPackage
  direct-seed : Seeds directPackage
  evidence-seed : Seeds evidencePackage

comparisonRule : Rule
comparisonRule = compare-rule adPackage directPackage (idEquiv Tensor) routeAgreement
comparisonHistory : Resolve Seeds (output comparisonRule)
comparisonHistory = apply comparisonRule
  λ { (lift true) → seed ad-seed ; (lift false) → seed direct-seed }
family : Bool → Complete
family true = output comparisonRule
family false = evidencePackage
history : Resolve Seeds (Pi-package Bool family)
history = apply (Pi-rule Bool family)
  λ { (lift true) → comparisonHistory ; (lift false) → seed evidence-seed }
retainedHistory : Whole.Universe.Complete (ℓ-suc ℓ-zero)
retainedHistory = reify-history history
retains-history : snd (Whole.Universe.value retainedHistory) ≡ history
retains-history = refl
