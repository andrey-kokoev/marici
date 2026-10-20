{-# OPTIONS --safe --cubical --guardedness #-}
module MixedBadNativeSubstitution where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Seeds)
import FiniteComparisonTrees as F
import NativeComposeHistoryBridge as H
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : (a : F.Object) → Resolve Seeds (H.Bridge.retainedPackage (F.identity a) (F.identity a))
bad a = F.admitted (F.compose (F.identity a) (F.identity a))
