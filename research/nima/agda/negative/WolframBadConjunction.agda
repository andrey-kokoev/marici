{-# OPTIONS --safe --cubical --guardedness #-}
module negative.WolframBadConjunction where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
meet : Bool → Bool → Bool
meet false b = false
meet true b = b
-- EXPECTED FAILURE: conjunction is not a model of Wolfram's axiom.
bad : meet (meet (meet false false) true)
  (meet false (meet (meet false true) false)) ≡ true
bad = refl
