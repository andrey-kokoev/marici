{-# OPTIONS --safe --cubical --guardedness #-}
module negative.FibrationBadMembership where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false)
open import TableFibrationCycle
-- EXPECTED FAILURE: an arbitrary row cannot be assigned to the false fiber.
bad : (b : Bool) → fibrate (λ x → x) false
bad b = b , refl
