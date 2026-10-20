{-# OPTIONS --safe --cubical --guardedness #-}
module PolicyBadRoute where
open import Cubical.Foundations.Prelude
open import ContinuationSidePolicies
bad : Fixture.route z₀ ab ≡ bc
bad = route-ab
