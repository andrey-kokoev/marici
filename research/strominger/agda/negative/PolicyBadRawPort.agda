{-# OPTIONS --safe --cubical --guardedness #-}
module PolicyBadRawPort where
open import Cubical.Foundations.Prelude
open import ContinuationSidePolicies
bad : Fixture.source z₀ ≡ Fixture.target z₀
bad = refl
