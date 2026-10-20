{-# OPTIONS --safe --cubical --guardedness #-}
module PolicyBadSyncReflexivity where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Vertex)
open import InternalSourceComparisons using (Mode; act)
import GeneratedReaderClassification as G
import CertifiedContinuationPolicies as C
module Test (m : Mode) {v : Vertex} (a : G.Fragment v) (b : G.Fragment (act m v))
  (f : G.Comparisons.Filler m a b) where
  module R = C.Model m a b f
  bad : (r : R.Request) → R.synchronize (fst r) ≡ r
  bad r = refl
