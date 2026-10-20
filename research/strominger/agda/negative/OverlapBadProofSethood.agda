{-# OPTIONS --safe --cubical --guardedness #-}
module OverlapBadProofSethood where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
open import SourceIndexedExtensionFamilies using (vertex-is-set)
import WholePackageResolution as R
open R.Generators ℓ-zero
open import SourceInverseSquareCoherence
bad : isSet (Resolve Seeds (pointQ A))
bad = vertex-is-set
