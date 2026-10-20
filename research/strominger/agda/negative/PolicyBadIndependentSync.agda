{-# OPTIONS --safe --cubical --guardedness #-}
module PolicyBadIndependentSync where
open import Cubical.Foundations.Prelude
open import ContinuationSidePolicies
bad : Fixture.Independent z₀ → Fixture.Synchronized z₀
bad (s , t) = s , t , refl
