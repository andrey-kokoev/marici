{-# OPTIONS --safe --cubical --guardedness #-}
-- EXPECTED FAILURE: this physical channel has square 8, not 9.
module negative.ScalarSixBadPropagator where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import ScalarSixKernel
open import ScalarSixFixture

bad-propagator : square (add (momenta l0) (add (momenta l1) (momenta l2))) ≡ pos 9
bad-propagator = refl
