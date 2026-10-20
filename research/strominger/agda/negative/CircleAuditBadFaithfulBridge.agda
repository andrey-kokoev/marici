{-# OPTIONS --safe --cubical --guardedness #-}
module CircleAuditBadFaithfulBridge where
open import Cubical.Foundations.Equiv
import GeneratedReaderClassification as G
import SourceCircleProvenanceAudit as Audit
bad : G.Carrier (G.body G.allA) ≃ Audit.RawCircle
bad = G.Normal.equivalence (G.normal G.allA)
