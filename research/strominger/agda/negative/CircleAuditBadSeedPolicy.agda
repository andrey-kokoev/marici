{-# OPTIONS --safe --cubical --guardedness #-}
module CircleAuditBadSeedPolicy where
open import Cubical.Foundations.Prelude
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using (Seeds)
import SourceCircleProvenanceAudit as Audit
open Resolution.Generators ℓ-zero
bad : Resolve Seeds Audit.unitQ
bad = seed Audit.suppliedUnit
