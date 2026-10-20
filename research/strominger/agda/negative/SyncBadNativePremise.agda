{-# OPTIONS --safe --cubical --guardedness #-}
module SyncBadNativePremise where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Seeds)
open import SynchronizedContinuationAdapter
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : (r : Example.Request) → Resolve Seeds (Example.syncPackage r)
bad r = Example.S.sourceDerivation (fst r)
