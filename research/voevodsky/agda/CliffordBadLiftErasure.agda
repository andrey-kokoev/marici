{-# OPTIONS --safe --cubical --guardedness #-}
module CliffordBadLiftErasure where
open import Cubical.Foundations.Prelude
open import RetainedCliffordProfiles
bad : lift-reading LR ≡ lift-reading RL
bad = refl
