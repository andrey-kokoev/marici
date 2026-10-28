{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExternalPEBadErasure where
open import Cubical.Foundations.Prelude
open import RamseyExternalPEExamples
bad : left ≡ right
bad = refl
