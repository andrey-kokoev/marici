{-# OPTIONS --safe --cubical --guardedness #-}
module CliffordBadHistoryErasure where
open import Cubical.Foundations.Prelude
open import RetainedCliffordProfiles
bad : unit ≡ times e1 e1
bad = refl
