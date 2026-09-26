{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NewtonianBadReciprocal where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import NewtonianTidalKernel
open import NewtonianTidalFixture
-- EXPECTED FAILURE: 3^3 * 64 = 1728, not 1729.
bad : reciprocalCheck a ≡ pos 1729
bad = refl
