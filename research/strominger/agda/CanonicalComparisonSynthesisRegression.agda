{-# OPTIONS --safe --cubical --guardedness #-}
module CanonicalComparisonSynthesisRegression where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (Bool; true; false)
open import NativeExtensionFamilyAudit using (A; B; C; D)
open import InternalSourceComparisons using (Mode; stay; exchange)
open import GeneratedReaderClassification using (Shape; whole; outgoing)
open import CanonicalComparisonSynthesis

-- An independent expected normal-form table. This does not assert every
-- shape pair admits operands at the required pair of selected vertices.
expected : Mode → Shape → Shape → Bool
expected stay whole whole = true
expected stay (outgoing A) (outgoing A) = true
expected stay (outgoing B) (outgoing B) = true
expected stay (outgoing C) (outgoing C) = true
expected stay (outgoing D) (outgoing D) = true
expected exchange whole whole = true
expected exchange (outgoing A) (outgoing B) = true
expected exchange (outgoing B) (outgoing A) = true
expected exchange (outgoing C) (outgoing D) = true
expected exchange (outgoing D) (outgoing C) = true
expected _ _ _ = false

finite-table-correct : (m : Mode) (s t : Shape) → shape-accepts m s t ≡ expected m s t
finite-table-correct stay whole whole = refl
finite-table-correct stay whole (outgoing A) = refl
finite-table-correct stay whole (outgoing B) = refl
finite-table-correct stay whole (outgoing C) = refl
finite-table-correct stay whole (outgoing D) = refl
finite-table-correct stay (outgoing A) whole = refl
finite-table-correct stay (outgoing A) (outgoing A) = refl
finite-table-correct stay (outgoing A) (outgoing B) = refl
finite-table-correct stay (outgoing A) (outgoing C) = refl
finite-table-correct stay (outgoing A) (outgoing D) = refl
finite-table-correct stay (outgoing B) whole = refl
finite-table-correct stay (outgoing B) (outgoing A) = refl
finite-table-correct stay (outgoing B) (outgoing B) = refl
finite-table-correct stay (outgoing B) (outgoing C) = refl
finite-table-correct stay (outgoing B) (outgoing D) = refl
finite-table-correct stay (outgoing C) whole = refl
finite-table-correct stay (outgoing C) (outgoing A) = refl
finite-table-correct stay (outgoing C) (outgoing B) = refl
finite-table-correct stay (outgoing C) (outgoing C) = refl
finite-table-correct stay (outgoing C) (outgoing D) = refl
finite-table-correct stay (outgoing D) whole = refl
finite-table-correct stay (outgoing D) (outgoing A) = refl
finite-table-correct stay (outgoing D) (outgoing B) = refl
finite-table-correct stay (outgoing D) (outgoing C) = refl
finite-table-correct stay (outgoing D) (outgoing D) = refl
finite-table-correct exchange whole whole = refl
finite-table-correct exchange whole (outgoing A) = refl
finite-table-correct exchange whole (outgoing B) = refl
finite-table-correct exchange whole (outgoing C) = refl
finite-table-correct exchange whole (outgoing D) = refl
finite-table-correct exchange (outgoing A) whole = refl
finite-table-correct exchange (outgoing A) (outgoing A) = refl
finite-table-correct exchange (outgoing A) (outgoing B) = refl
finite-table-correct exchange (outgoing A) (outgoing C) = refl
finite-table-correct exchange (outgoing A) (outgoing D) = refl
finite-table-correct exchange (outgoing B) whole = refl
finite-table-correct exchange (outgoing B) (outgoing A) = refl
finite-table-correct exchange (outgoing B) (outgoing B) = refl
finite-table-correct exchange (outgoing B) (outgoing C) = refl
finite-table-correct exchange (outgoing B) (outgoing D) = refl
finite-table-correct exchange (outgoing C) whole = refl
finite-table-correct exchange (outgoing C) (outgoing A) = refl
finite-table-correct exchange (outgoing C) (outgoing B) = refl
finite-table-correct exchange (outgoing C) (outgoing C) = refl
finite-table-correct exchange (outgoing C) (outgoing D) = refl
finite-table-correct exchange (outgoing D) whole = refl
finite-table-correct exchange (outgoing D) (outgoing A) = refl
finite-table-correct exchange (outgoing D) (outgoing B) = refl
finite-table-correct exchange (outgoing D) (outgoing C) = refl
finite-table-correct exchange (outgoing D) (outgoing D) = refl
