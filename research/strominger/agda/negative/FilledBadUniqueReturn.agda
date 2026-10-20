{-# OPTIONS --safe --cubical --guardedness #-}
module FilledBadUniqueReturn where
open import Cubical.Foundations.Prelude
open import FilledSourceReturnClassification
open ExistingFilledCounterexample
bad : identity-return ≡ flip-return
bad = refl
