{-# OPTIONS --safe --cubical --guardedness #-}
module InterpretationComparisonBad where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
import InterpretationComparison
bad : InterpretationComparison.sign-diff ≡ (λ _ -> false)
bad = refl