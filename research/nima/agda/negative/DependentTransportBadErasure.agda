{-# OPTIONS --safe --cubical --guardedness #-}
module DependentTransportBadErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true; false)
open import DependentTransportMachine
-- Same endpoint does not license replacing a turn by stay.
bad : run (carry turn (bit true)) ≡ true
bad = refl
