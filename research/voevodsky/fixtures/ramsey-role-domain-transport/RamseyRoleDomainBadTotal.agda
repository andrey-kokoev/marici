{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRoleDomainBadTotal where
open import Cubical.Foundations.Prelude
open import RamseySingleFrameFaces
open import RamseyRoleDomainTransport
bad : TargetEligible c1
bad = refl
