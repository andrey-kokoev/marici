{-# OPTIONS --safe --cubical --guardedness #-}
module TreeBadNativeComposition where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import NativeExtensionFamilyAudit using (Seeds)
open import InternalSourceComparisons using (package)
import GeneratedReaderClassification as G
open import FiniteComparisonTrees
import WholePackageSigmaPi as W
import WholePackageResolution as R
open W.Universe ℓ-zero
open R.Generators ℓ-zero
bad : (a : Object) → let q = package (G.body (snd a)) in
  Resolve Seeds (compose-comparisons q q q (idEquiv _) (idEquiv _) refl refl)
bad a = admitted (identity a)
