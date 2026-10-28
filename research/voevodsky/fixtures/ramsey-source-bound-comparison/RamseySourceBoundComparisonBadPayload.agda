{-# OPTIONS --safe --cubical --guardedness #-}
module RamseySourceBoundComparisonBadPayload where
open import Cubical.Foundations.Prelude
open import RamseySourceBoundComparison
bad : Valid (fst actual , "")
bad = refl
