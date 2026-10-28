{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPNOverlapBadEmptyPair where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
open import RamseyPNOverlapExamples
bad : S.Common C D
bad = c0 , (refl , refl)
