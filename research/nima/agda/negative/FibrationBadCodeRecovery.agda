{-# OPTIONS --safe --cubical --guardedness #-}
module negative.FibrationBadCodeRecovery where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit)
import WholePackageSigmaPi as Old
open Old.Universe ℓ-zero
open import FibrationCodeInterpretation using (module LostMetadata)
open LostMetadata
-- EXPECTED FAILURE: identical pointed value tables do not identify codes.
bad : q-atom ≡ q-map
bad = refl
