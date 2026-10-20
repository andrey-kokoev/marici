{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisBadSeedReset where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (B; root)
open import GeneratedReaderClassification using (start)
open import CanonicalComparisonSynthesis
bad : whole-next ≡ start B (root B)
bad = refl
