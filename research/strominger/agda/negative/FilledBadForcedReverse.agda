{-# OPTIONS --safe --cubical --guardedness #-}
module FilledBadForcedReverse where
open import Cubical.Foundations.Prelude
open import FilledSourceReturnClassification
import RetainedTetrahedralPackage as Retained
module Test {ℓ : Level} (X : Type ℓ) (full : Retained.Cells.Full X) where
  open At X full
  bad : (back : Return) → back ≡ reverse-choice
  bad back = refl
