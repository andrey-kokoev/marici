{-# OPTIONS --safe --cubical --guardedness #-}
module FamilyBadSelectorBypass where
open import Cubical.Foundations.Prelude
open import ContinuationPolicyFamily
bad : Σ[ k ∈ Presentation ] k ≡ source
bad = target , refl
