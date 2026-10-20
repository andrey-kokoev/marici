{-# OPTIONS --safe --cubical --guardedness #-}
module ReaderClassificationBadRawCollapse where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import NativeExtensionFamilyAudit using (A; Vertex)
open import InternalSourceComparisons using (stay; package)
open import GeneratedReaderClassification
identityComparison : Fragment A
identityComparison = compareF stay allA allA (idEquiv Vertex) refl (λ x → refl)
bad : package (body identityComparison) ≡ package (body allA)
bad = refl
