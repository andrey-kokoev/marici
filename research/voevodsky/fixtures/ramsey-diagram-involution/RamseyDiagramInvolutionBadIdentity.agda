{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDiagramInvolutionBadIdentity where
open import Cubical.Foundations.Prelude
open import RamseyDiagramInvolutionExamples
bad : input s01 ≡ input (swap s01)
bad = refl
