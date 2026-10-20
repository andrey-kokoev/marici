{-# OPTIONS --safe --cubical --guardedness #-}
module AdapterBadNativeComparison where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Seeds)
open import InternalSourceComparisons using (package)
open import ContinuationSidePolicies using (ab)
open import SourceIndexedContinuationAdapter
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : Resolve Seeds (package (Example.adapterComparison ab))
bad = Example.sourceDerivation ab
