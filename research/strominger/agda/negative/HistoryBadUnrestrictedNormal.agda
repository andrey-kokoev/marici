{-# OPTIONS --safe --cubical --guardedness #-}
module HistoryBadUnrestrictedNormal where
open import NativeExtensionFamilyAudit using (A; root)
import GeneratedReaderClassification as G
import MixedRootHistoryCoherence
bad : G.Normal G.hidden
bad = G.normal (G.start A (root A))
