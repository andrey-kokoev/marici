{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessGeneratorBadHiddenEquality where
open import Cubical.Foundations.Prelude
open import WitnessContinuationHistories
open State
open import WitnessHigherControls
bad : selected nativeId ≡ selected nativeSwap
bad = refl
