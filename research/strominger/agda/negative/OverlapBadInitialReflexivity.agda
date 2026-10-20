{-# OPTIONS --safe --cubical --guardedness #-}
module OverlapBadInitialReflexivity where
open import Cubical.Foundations.Prelude
open import SourceInverseSquareCoherence
bad : InitialOverlapA
bad d = refl
