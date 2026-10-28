{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPassiveEPPortBadAdmission where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import Cubical.Data.Unit.Base using (tt)
open import RamseySingleFrameFaces
open import RamseyPassiveEPPortExamples
bad : A.Only.Good (A.context q0 m0 refl)
bad = λ _ → tt
