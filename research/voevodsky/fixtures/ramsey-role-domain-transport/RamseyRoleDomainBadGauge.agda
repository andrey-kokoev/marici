{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRoleDomainBadGauge where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
open import RamseyRoleDomainTransport
bad : M-role (swap-role m0) ≡ M-role m0
bad = refl
