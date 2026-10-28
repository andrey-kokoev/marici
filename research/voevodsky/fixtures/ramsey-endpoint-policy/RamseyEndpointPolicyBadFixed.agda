{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEndpointPolicyBadFixed where
open import Cubical.Foundations.Prelude
open import RamseyEndpointPolicy
bad : turn left-selector ≡ left-selector
bad = refl
