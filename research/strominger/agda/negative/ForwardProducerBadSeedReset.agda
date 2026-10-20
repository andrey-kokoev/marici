{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardProducerBadSeedReset where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
open import ForwardCertifiedPrograms
import GeneratedReaderClassification as G
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : (d : Resolve Seeds (pointQ A)) → Certificate (G.start A d)
bad d = certificate (initialP (rootI A)) refl
