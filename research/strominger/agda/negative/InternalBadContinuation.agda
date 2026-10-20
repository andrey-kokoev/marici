{-# OPTIONS --safe --cubical --guardedness #-}
module InternalBadContinuation where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; D; AD)
open import InternalSourceComparisons using (Body; attach; nonidentity)

-- The internal A->B comparison has an explicitly target-side continuation.
-- AD is outgoing from its source side, not from the active B boundary.
bad : Body D
bad = attach (nonidentity A) (D , AD)
