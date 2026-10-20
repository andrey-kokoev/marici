{-# OPTIONS --safe --cubical --guardedness #-}
module TreeBadHistoryCollapse where
open import Cubical.Foundations.Prelude
open import FiniteComparisonTrees
bad : (a : Object) → unit a ≡ then (unit a) (unit a)
bad a = refl
