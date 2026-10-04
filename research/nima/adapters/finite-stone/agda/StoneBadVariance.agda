{-# OPTIONS --safe --cubical --guardedness #-}
module StoneBadVariance where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; not)
open import FiniteStoneDomain
f g : Bool → Bool
f _ = false
g = not
bad : pull (λ i → f (g i)) e₀ ≡ pull f (pull g e₀)
bad = refl
