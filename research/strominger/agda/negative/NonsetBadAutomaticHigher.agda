{-# OPTIONS --safe --cubical --guardedness #-}
module NonsetBadAutomaticHigher where
open import Cubical.Foundations.Prelude
open import NonsetWitnessEnvelopes
bad : (p q : x ≡ x) → p ≡ q
bad p q = refl
