{-# OPTIONS --safe --cubical --guardedness #-}
module MixedBadBoundaryAfterComparison where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (D; CA)
open import MixedSourceAdmissionClosure using (Assembly; attach; certify; base)

-- Native comparison does not release the original source attachment constraint.
bad : Assembly D
bad = attach (certify base) (D , CA)
