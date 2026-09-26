{-# OPTIONS --safe --cubical --guardedness #-}
module negative.BoundaryBadWitnessCollapse where
open import Cubical.Foundations.Prelude
open import BoundaryGeneratedQuestions
-- EXPECTED FAILURE: common Boolean truth does not identify actual fillers.
bad : identity fourQ ≡ swap-filler
bad = refl
