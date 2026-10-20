{-# OPTIONS --safe --cubical --guardedness #-}
module TwoComparisonBadAtomicAdmission where
open import Cubical.Foundations.Prelude
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using (Seeds)
import TwoComparisonHigherAdmission as H
open Resolution.Generators ℓ-zero
bad : Resolve Seeds H.barePackage
bad = H.admitted-higher
