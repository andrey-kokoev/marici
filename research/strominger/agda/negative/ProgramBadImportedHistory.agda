{-# OPTIONS --safe --cubical --guardedness #-}
module ProgramBadImportedHistory where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
import GeneratedReaderClassification as Old
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
open import SourceCertifiedPrograms
bad : Resolve Seeds (pointQ A) → Program A
bad d = Old.start A d
