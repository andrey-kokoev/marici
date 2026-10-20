{-# OPTIONS --safe --cubical --guardedness #-}
module PolicyBadPackageIdentification where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; AB; root; sigmaEquiv)
open import InternalSourceComparisons using (exchange; package)
import GeneratedReaderClassification as G
import ContinuationPolicyFamily as Policy
import CertifiedContinuationPolicies as C
module R = C.Model exchange (G.start A (root A)) (G.start B (root B))
  (sigmaEquiv , refl , (λ x → refl))
r = R.synchronize (B , AB)
bad : package (R.body r Policy.source C.output) ≡ package (R.body r Policy.target C.output)
bad = refl
