{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPNOverlapBadLostPort where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
open import RamseyPNOverlapExamples
bad : S.Common A B
bad = c1 , (refl , refl)
