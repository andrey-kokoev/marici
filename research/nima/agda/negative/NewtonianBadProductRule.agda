{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NewtonianBadProductRule where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import NewtonianTidalKernel using (x; hessian)
open import NewtonianPotentialJet
-- EXPECTED FAILURE: omitting one product-rule cross term yields 1, not 2.
bad : hessian (multiply (coordinate x) (coordinate x)) x x ≡ pos 1
bad = refl
