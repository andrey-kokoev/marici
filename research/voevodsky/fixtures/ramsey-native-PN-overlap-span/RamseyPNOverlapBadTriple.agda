{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPNOverlapBadTriple where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
open import RamseyPNOverlapExamples
bad : S.Triple A B C
bad = c0 , (refl , (refl , refl))
