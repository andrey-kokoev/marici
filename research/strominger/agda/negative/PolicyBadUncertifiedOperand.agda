{-# OPTIONS --safe --cubical --guardedness #-}
module PolicyBadUncertifiedOperand where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; AB)
open import InternalSourceComparisons using (stay)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
import ContinuationPolicyFamily as Policy
import CertifiedContinuationPolicies as C
bad : G.Fragment A → C.Program
bad a = C.policyP stay a (P.initialP (P.rootI A)) refl (B , AB) Policy.target C.output
