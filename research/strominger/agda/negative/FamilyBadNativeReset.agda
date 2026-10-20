{-# OPTIONS --safe --cubical --guardedness #-}
module FamilyBadNativeReset where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; Seeds; sigmaEquiv)
open import InternalSourceComparisons
open import ContinuationPolicyFamily
import WholePackageResolution as R
open R.Generators ℓ-zero
module F = Family exchange (seedBody A) (seedBody B) sigmaEquiv refl (λ _ → refl)
bad : (r : F.S.Request) → Resolve Seeds (package (F.output r target))
bad r = derivation F.S.S.old
