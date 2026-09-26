{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NewtonianBadTensor where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (negsuc)
open import NewtonianTidalKernel
open import NewtonianTidalFixture
-- EXPECTED FAILURE: numerator is -229, not -230.
bad : tidal a b x x ≡ negsuc 229
bad = refl
