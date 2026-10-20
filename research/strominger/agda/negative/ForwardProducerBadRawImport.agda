{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardProducerBadRawImport where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
open import ForwardCertifiedPrograms
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : Resolve Seeds (pointQ A) → Program A
bad d = initialP d
