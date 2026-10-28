{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRequestedPortBadTotal where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import RamseySingleFrameFaces
open import RamseyRequestedPortExamples
bad : R.isAccepted (R.run q0 q6 c0 refl) ≡ true
bad = refl
