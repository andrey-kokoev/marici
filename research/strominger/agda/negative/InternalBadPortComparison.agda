{-# OPTIONS --safe --cubical --guardedness #-}
module InternalBadPortComparison where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; tauEquiv)
open import InternalSourceComparisons using (Body; compare; exchange; seedBody)

-- Tau carries A to B, but does not implement the declared source comparison
-- on every port. Native point preservation alone cannot supply this witness.
bad : Body B
bad = compare exchange (seedBody A) (seedBody B) tauEquiv refl (λ x → refl)
