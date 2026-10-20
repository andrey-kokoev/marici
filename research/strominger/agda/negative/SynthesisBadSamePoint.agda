{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisBadSamePoint where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool using (true)
open import CanonicalComparisonSynthesis
bad : SamePointMismatch.accepted SamePointMismatch.compile ≡ true
bad = refl
