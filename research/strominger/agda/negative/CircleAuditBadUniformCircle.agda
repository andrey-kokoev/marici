{-# OPTIONS --safe --cubical --guardedness #-}
module CircleAuditBadUniformCircle where
open import Cubical.Foundations.Equiv
open import Cubical.HITs.S1.Base using (S¹)
open import NativeExtensionFamilyAudit using (C)
import SourceCircleProvenanceAudit as Audit
bad : Audit.SourceSuspension C ≃ S¹
bad = Audit.at-A
