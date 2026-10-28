{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPassiveEPPortBadFace where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces
open import RamseyPassiveEPPortExamples
bad : R.isAccepted (R.run q7 q0 c0 refl) ≡ true
bad = refl
