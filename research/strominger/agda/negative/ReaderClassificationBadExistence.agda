{-# OPTIONS --safe --cubical --guardedness #-}
module ReaderClassificationBadExistence where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import NativeExtensionFamilyAudit using (Vertex)
open import GeneratedReaderClassification
bad : Mismatch.Filler
bad = idEquiv Vertex , refl , (λ x → refl)
