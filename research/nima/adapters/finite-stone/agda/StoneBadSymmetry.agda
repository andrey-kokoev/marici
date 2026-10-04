{-# OPTIONS --safe --cubical --guardedness #-}
module StoneBadSymmetry where
open import Cubical.Foundations.Prelude
open import FiniteStoneDomain
bad : swap e₀ ≡ e₀
bad = refl
