{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedActionBadErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (snd)
import RetainedComparisonStructure as R
open import RetainedActionYoneda

-- Agreement in the realized action does not erase the regular action's value.
erased : snd (regular-value R.change0) ≡ snd (regular-value R.change1)
erased = refl
