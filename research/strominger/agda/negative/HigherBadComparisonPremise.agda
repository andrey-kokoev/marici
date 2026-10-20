{-# OPTIONS --safe --cubical --guardedness #-}
module HigherBadComparisonPremise where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (rUnit)
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
open import NativeExtensionFamilyAudit using (Seeds)
open import InternalSourceComparisons using (derivation)
import RepeatedInterchangeCoherence as R
open import HigherWitnessAdmission using (EnvelopeCode; left; right; envelopePath; nextHigherPackage)

-- A native comparison derivation is not a derivation of a required path
-- package. Having the endpoints available does not fill this typed premise.
bad : Resolve Seeds nextHigherPackage
bad = apply (higher-rule EnvelopeCode left right envelopePath (envelopePath ∙ refl) (rUnit envelopePath))
  (λ _ → derivation (R.asBody R.sequentialFiller))
