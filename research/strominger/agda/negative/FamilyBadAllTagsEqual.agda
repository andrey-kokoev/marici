{-# OPTIONS --safe --cubical --guardedness #-}
module FamilyBadAllTagsEqual where
open import Cubical.Foundations.Prelude
open import ContinuationPolicyFamily
bad : (k : Presentation) → target ≡ k
bad k = refl
