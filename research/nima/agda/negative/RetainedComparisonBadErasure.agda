{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedComparisonBadErasure where
open import Cubical.Foundations.Prelude
open import RetainedComparisonStructure

-- Must reject: equal realized comparisons do not identify retained changes.
erased : change0 ≡ change1
erased = refl
